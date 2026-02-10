# Plan: Portar expo-flow a PyFlow

## Contexto

**expo-flow** es una app demo Java Vaadin 25 (Spring Boot) con 7 vistas, JPA/H2, Spring AI/OpenAI, y showcase de componentes. El objetivo es portarla a Python como `vaadin-pyflow/expo/`, demostrando que PyFlow puede ejecutar una app real.

**Decisiones del usuario:**
- Chart, Map, RichTextEditor: **OMITIR** (no existen en PyFlow ni en el bundle)
- Hilla/React view: **NO PORTAR**
- AI: **`openai`** Python library
- Base de datos: **SQLAlchemy + SQLite in-memory**

---

## Fase 0: Cambios mínimos al core de PyFlow

### 0a. `MessageList.set_markdown(enabled)` ← **ChatView necesita esto**
**Archivo:** `src/vaadin/flow/components/message_list.py`
- Añadir método `set_markdown(self, enabled: bool)` que haga `element.set_property("markdown", enabled)`
- Almacenar `self._markdown = enabled` y aplicar en `_attach`

### 0b. `TextField.set_clear_button_visible()` y `set_placeholder()`
**Archivo:** `src/vaadin/flow/components/text_field.py`
- `set_clear_button_visible(visible)` → `element.set_property("clearButtonVisible", visible)`
- `set_placeholder(text)` → `element.set_property("placeholder", text)`
- Patrón: guardar en `_pending_properties` si no attached

### 0c. `Header` y `Footer` HTML elements
**Archivo:** `src/vaadin/flow/components/html.py`
- Añadir `class Header(HtmlContainer)` con `_tag = "header"`
- Añadir `class Footer(HtmlContainer)` con `_tag = "footer"`
- Exportar en `components/__init__.py`

### 0d. `TextField.set_prefix_component(icon)` — slot-based child
**Archivo:** `src/vaadin/flow/components/text_field.py`
- Crear child element con `slot="prefix"`, patrón similar a tooltip en `component.py`
- El icon se añade como child del element con atributo `slot="prefix"`

---

## Fase 1: Backend (SQLAlchemy + servicios)

### 1a. Database setup — `expo/data/database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def init_db():
    Base.metadata.create_all(engine)
```

### 1b. Modelos — `expo/data/models.py`
**Person:** id (UUID), first_name, last_name, email, date_of_birth
**TShirtOrder:** id (auto-increment), name, email, shirt_size
- Ambos extienden `Base`
- `to_dict()` method para convertir a dict para Grid

### 1c. Data generator — `expo/data/generator.py`
- Usar `faker` para generar 100 personas
- Se ejecuta al iniciar la app (idempotente)

### 1d. PersonService — `expo/services/person_service.py`
- `find_all() → list[dict]`
- `find_page(offset, limit) → (list[dict], total_count)` para Grid lazy loading
- Singleton: `person_service = PersonService()`

### 1e. TShirtService — `expo/services/tshirt_service.py`
- `get_sizes() → list[str]` = ["Small", "Medium", "Large", "Extra Large", "XXL"]
- `place_order(order)` → save to DB
- `find_all() → list[dict]`
- `delete(id)` → eliminar pedido
- Singleton: `tshirt_service = TShirtService()`

---

## Fase 2: Estructura base de la app

### 2a. `expo/__init__.py` — vacío
### 2b. `expo/__main__.py`
```python
from vaadin.flow import FlowApp
FlowApp(port=8889).run()
```
Puerto **8889** para no colisionar con demo (8088) ni Java (8080).

### 2c. `expo/views/__init__.py` — vacío (FlowApp auto-descubre @Route)

### 2d. MainLayout — `expo/views/main_layout.py`
**Fuente Java:** MainLayout.java (73 líneas)
- `AppLayout` con `DrawerToggle` + `H1` en navbar
- `SideNav` poblado desde `get_menu_entries()`
- `Checkbox` "Dark theme" con `execute_js` para toggle
- `Scroller` en drawer
- `Header` con `H1("Vaadin }>")` y `Footer` vacío (usar Div si Header/Footer no ready)
- `@StyleSheet("lumo/lumo.css", "styles/styles.css")`
- **Workaround SvgIcon:** Usar `Icon("vaadin:xxx")` en lugar de SvgIcon con line-awesome
- **Sin AfterNavigationObserver:** No actualizar título dinámicamente (simplificación)

---

## Fase 3: Vistas (7 vistas)

### 3a. PlaygroundView — `expo/views/playground.py` (la más simple)
**Fuente Java:** PlaygroundView.java (34 líneas)
- `@Route("playground")`, `@Menu(title="Python Playground", order=6, icon="vaadin:code")`
- TextField + Button("Say hello") con `add_click_shortcut(Key.ENTER)` ← ya existe en PyFlow
- Cada click añade un `Paragraph(f"Hello {name}")`

### 3b. FormView — `expo/views/form.py`
**Fuente Java:** FormView.java (72 líneas)
- `@Route("form")`, `@Menu(title="Form", order=2, icon="vaadin:pencil")`
- Campos: TextField(firstName), TextField(lastName), EmailField, DatePicker
- Binder con `bind_instance_fields(self)` → mapea por nombre de atributo
- Save/Cancel buttons, Notification al guardar
- **Bean:** dataclass `PersonFormBean(first_name, last_name, email, date_of_birth)`

### 3c. GridView — `expo/views/grid.py`
**Fuente Java:** GridView.java (31 líneas)
- `@Route("grid")`, `@Menu(title="Grid", order=3, icon="vaadin:table")`
- Grid con lazy data provider desde PersonService
- Columna "Name" computada: `fullName = f"{firstName} {lastName}"` en el callback
- Columnas: Name (auto_width), Date Of Birth, Email

### 3d. TShirtView — `expo/views/tshirt.py`
**Fuente Java:** TShirtView.java (94 líneas)
- `@Route("tshirt")`, `@Menu(title="Order T-shirt", order=5, icon="vaadin:user")`
- H1, TextField(name), TextField(email), ComboBox(shirtSize) con set_items(*sizes)
- Binder con `bind_instance_fields(self)`
- Button "Place order" con `add_click_shortcut(Key.ENTER)`
- Notification al pedir, reset form

### 3e. ListOrdersView — `expo/views/orders.py`
**Fuente Java:** ListOrdersView.java (95 líneas)
- `@Route("listorders")`
- Grid con set_columns("name", "email", "shirtSize")
- `ComponentRenderer` para botón de borrar por fila
- Button refresh, RouterLink a /tshirt
- **Export:** Botón que genera CSV via `execute_js` (blob download client-side, sin REST endpoint)

### 3f. ComponentsView — `expo/views/components.py` (la más grande)
**Fuente Java:** ComponentsView.java (295 líneas)
- `@Route("components")`, `@Route("")` como landing page
- Grid CSS layout con `addClassName("components-view")`
- Helper `_add_to_grid(component, *class_names)` → Div wrapper con class "component"
- **Componentes incluidos (12 de 15, sin Chart/Map/RTE):**
  1. Buttons (Save primary + Cancel) en HorizontalLayout
  2. RadioButtonGroup (vertical, 3 opciones, pre-selección)
  3. LoginForm
  4. DateTimePicker (valor actual)
  5. CheckboxGroup (vertical, 3 opciones, pre-selección)
  6. Grid multi-select con datos de PersonService (4 columnas)
  7. ComboBox con personas (item_label_generator)
  8. MessageList + MessageInput (mensajes estáticos de ejemplo)
  9. TextField con búsqueda (clearButton, placeholder, ~~prefix icon~~)
  10. Upload
  11. MultiSelectComboBox con personas
  12. Tabs (Details, Payment, Shipping)

### 3g. ChatView — `expo/views/chat.py`
**Fuente Java:** ChatView.java (59 líneas)
- `@Route("chat")`, `@Menu(title="Chat", order=4, icon="vaadin:comments")`
- MessageList con `set_markdown(True)` + MessageInput
- **OpenAI integration (síncrono, sin streaming):** PyFlow no tiene Push/WebSocket
  - `openai.OpenAI().chat.completions.create()` — respuesta completa, no token a token
  - Historial de mensajes para contexto conversacional
  - Si no hay API key → mensaje de error
- Items: MessageListItem con user_color_index (4=user, 1=AI)

---

## Fase 4: CSS

### `expo/styles/styles.css`
Combina styles.css + components-view.css + main-layout.css del Java:
- Drawer styling (background gradient, padding)
- Button borders (1px)
- LoginForm background removal
- Input field borders
- Dark theme colors (teal primary)
- MessageList scroll-snap
- `.components-view` CSS Grid (auto-fit, 240px min columns)
- `.component` cards (200px, shadow, overflow hidden)
- `.component.tall` (400px, grid-row span 2)
- `.component.col-span-2/3` (grid-column span)

---

## Fase 5: Dependencias

```bash
pip install sqlalchemy faker openai
```
- `sqlalchemy` — ORM (JPA equivalent)
- `faker` — Generación de datos demo
- `openai` — API de OpenAI (requiere `OPENAI_API_KEY` env var)

---

## Fase 6: Actualizar STATUS.md

Añadir sección en `vaadin-pyflow/STATUS.md`:

```markdown
### Expo Demo App (port of Java expo-flow)
- [x] SQLAlchemy + SQLite in-memory (Person, TShirtOrder)
- [x] Faker data generation (100 people)
- [x] 7 vistas portadas
- [x] MainLayout (AppLayout + SideNav + dark toggle)
- [x] OpenAI chat integration (síncrono)
- [ ] Chart, Map, RichTextEditor (omitidos — no disponibles en bundle)
- [ ] Streaming AI (requiere Push/WebSocket)
```

Añadir a sección "Missing/Pending":
```markdown
### Components not yet in bundle
- Chart (Vaadin Charts Pro — Highcharts)
- Map (Vaadin Map — OpenLayers)
- RichTextEditor
```

---

## Fase 7: Verificación

### 7a. Arrancar la app
```bash
cd vaadin-pyflow && source .venv/bin/activate
pip install sqlalchemy faker openai
python -m expo
# → http://localhost:8889
```

### 7b. Tests con Playwright
1. `browser_navigate` → http://localhost:8889
2. Verificar MainLayout: drawer, sidenav, título
3. Navegar a cada vista y verificar renderizado
4. ComponentsView: grid CSS layout con cards de componentes
5. FormView: llenar form → Save → Notification
6. GridView: scroll con lazy loading
7. TShirtView: llenar form → Place order → Notification
8. ListOrdersView: ver pedidos, borrar, export
9. PlaygroundView: escribir nombre → Say hello → ver Paragraph
10. ChatView: enviar mensaje → respuesta AI (si OPENAI_API_KEY)
11. Dark theme toggle en drawer

### 7c. Tests unitarios
```bash
pytest tests/ -v  # Los 1245 tests existentes deben seguir pasando
```

---

## Archivos a crear/modificar

### Modificar (PyFlow core — 4 archivos):
1. `src/vaadin/flow/components/message_list.py` — set_markdown()
2. `src/vaadin/flow/components/text_field.py` — set_clear_button_visible(), set_placeholder(), set_prefix_component()
3. `src/vaadin/flow/components/html.py` — Header, Footer classes
4. `src/vaadin/flow/components/__init__.py` — exportar Header, Footer

### Crear (expo app — ~18 archivos):
```
expo/__init__.py
expo/__main__.py
expo/data/__init__.py
expo/data/database.py
expo/data/models.py
expo/data/generator.py
expo/services/__init__.py
expo/services/person_service.py
expo/services/tshirt_service.py
expo/views/__init__.py
expo/views/main_layout.py
expo/views/components.py
expo/views/form.py
expo/views/grid.py
expo/views/tshirt.py
expo/views/orders.py
expo/views/chat.py
expo/views/playground.py
expo/styles/styles.css
```

### Actualizar:
- `vaadin-pyflow/STATUS.md` — Sección Expo Demo App

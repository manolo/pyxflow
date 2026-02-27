# PyFlow Landing Website — Asset Sources & Regeneration Guide

**Content source of truth**: `INDEX.md` — section-by-section content for regenerating `index.html`.
**Design specs**: `SPECS.md` — colors, typography, animations, responsive rules.

Single-page marketing landing for Vaadin PyFlow. Zero external dependencies (no CDN, no fonts, no JS libs, no build tools).

## Cómo se generó

Se generó con Claude Code en varias sesiones iterativas. El proceso fue:

1. Se describió el concepto general ("landing page para PyFlow, estilo dark, como las de frameworks modernos")
2. Se capturaron screenshots de la app demo de PyFlow corriendo en local
3. Se iteró sección por sección: hero con typing animation, feature cards, architecture, code showcase, gallery, quick start
4. Se refinaron textos, snippets de código, y detalles visuales a lo largo de varias sesiones

## Fuentes de los assets

### Screenshots (`screenshots/`)

Capturas de la **app demo de PyFlow** corriendo en localhost con **Lumo Dark theme**, usando Playwright MCP:

| Archivo | Qué muestra | Cómo se capturó |
|---------|-------------|-----------------|
| `screenshot-hello.png` | Vista HelloWorld simple | Navegador a la ruta /hello de la demo |
| `screenshot-grid.png` | Grid con datos tabulares | Vista con Grid y columnas |
| `screenshot-master-detail.png` | CRUD master-detail con SplitLayout | Clic en una fila (Barry Rodriquez), clic en icono datepicker, captura con calendario abierto (Jun 2015). Ventana 870x512 |
| `screenshot-components.png` | Galería de componentes (LoginForm, ListBox, ProgressBar, Avatar, Tabs, MenuBar) | Vista de componentes de la demo |
| `screenshot-file-explorer.png` | File explorer con TreeGrid | Vista file explorer de la demo |
| `screenshot-stopwatch.png` | Cronómetro con Push en tiempo real | Vista stopwatch de la demo |
| `architecture.png` | Ilustración conceptual server-browser | **Generada con IA** (imagen de concepto mostrando arquitectura server-side) |

### Logos

| Archivo | Origen |
|---------|--------|
| `logo.png` | PNG del logo de PyFlow (serpiente Python + motivo flow, gradiente azul/cyan) |

### Código fuente de referencia

Los snippets de código en la página deben coincidir con la API real de PyFlow. Referencia: `pyflow` repo (`https://github.com/manolo/pyflow`).

Patrones clave de la API:
- `@Route("path")`, `@Menu("Title", icon="vaadin:icon")`, `@Push`, `@AppShell`
- Vistas son clases que extienden layouts (`VerticalLayout`, `HorizontalLayout`, `SplitLayout`)
- `Button("text", callback)` — detección automática de parámetros, sin `on_click=`
- `Grid`, `TreeGrid`, `Binder`, `Notification.show()`
- `from pyflow import ...` y `from pyflow.components import *`

## Prompt de regeneración

Para generar una página similar desde cero, usar un prompt como:

---

> Crea una landing page single-page para **Vaadin PyFlow**, un framework Python para construir web apps con componentes Vaadin. La página debe:
>
> **Requisitos técnicos:**
> - Un solo archivo HTML con CSS y JS embebidos (sin dependencias externas, sin CDN, sin fonts remotas)
> - Tema oscuro (fondo `#1a1a2e`, code blocks `#0d1117`, accent azul `#1676f3`, cyan `#00d2ff`)
> - Responsive (2 columnas en desktop, 1 en móvil <768px)
> - Syntax highlighting manual con clases CSS (`.kw` keywords rojo, `.fn` funciones violeta, `.str` strings azul, `.cls` clases verde, `.dec` decoradores naranja)
>
> **Secciones (en orden):**
> 1. **Nav fija** — Logo + links a secciones, efecto frosted glass con backdrop-filter
> 2. **Hero** (full viewport) — Título "Build Web Apps in Pure Python", animación de typing character-by-character en un bloque de código hello world, botones CTA
> 3. **Why PyFlow** — 4 cards: Pure Python, 49+ Components, Real-time Push, Hot Reload. Con iconos SVG inline
> 4. **Architecture** — Diagrama animado Server ↔ WebSocket ↔ Browser (thin client), con items positivos en server y negativos con escudos en browser. Subtítulo: "Your code runs on the server. The browser is just a Thin-Client." + 3 benefit cards (Zero Attack Surface, Server-side State, Minimal Bandwidth)
> 5. **Code Showcase** — 3 ejemplos side-by-side (código + screenshot): Hello World, Data Grid, Master-Detail CRUD. Layout alternado
> 6. **Component Gallery** — Screenshots de componentes (galería, file explorer, stopwatch)
> 7. **Quick Start** — Terminal con comandos pip install + estructura de archivos mínima
> 8. **Footer** — Links a GitHub, Issues, Apache 2.0
>
> **Animaciones:**
> - Typing animation en hero (JS, 35-60ms por carácter, cursor parpadeante)
> - Fade-in on scroll con IntersectionObserver
> - Hover lift en cards y botones
> - Pulso animado en el cable WebSocket del diagrama de arquitectura
>
> Los screenshots están en `screenshots/` y el logo en `logo.png`.

---

## Estructura del directorio

```
web/
├── index.html              # La página (HTML + CSS + JS, todo en uno)
├── logo.png                # Logo PNG
├── screenshots/            # Capturas de la demo (Lumo Dark)
│   ├── screenshot-hello.png
│   ├── screenshot-grid.png
│   ├── screenshot-master-detail.png
│   ├── screenshot-components.png
│   ├── screenshot-file-explorer.png
│   ├── screenshot-stopwatch.png
│   └── architecture.png    # Imagen IA de arquitectura
├── SPECS.md                # Especificaciones detalladas de diseño
├── CLAUDE.md               # Instrucciones para modificar con Claude Code
└── README.md               # Este archivo
```
## Generar logos con Geminy o grok

Haz una imagen: cambia el logo de python para que una de las serpientes parezca una curly bracket right y la otra un greater than no quiero que ponga nada, solo los dibujos, y solo 2 serpientes (2 cabezas y ojos)

o

hazme un logo modificado de vaadin que es }> para que parezcan dos serpientes, quiero que cada letra sean una serpiente, no extra serpientes, tiene que quedar que parezca el logo de vaadin pero cada simbolo del logo sea una serpiente con esa forma, es decir una serpiente es una llave en esta posicion } y la otra un mayor-que > separados por un espacio pequeño, no añadas mas elelementos a la escena, es muy importante que el logo parezca el original en forma que se puedan superponer y solo cambie que uno esta hecho con serpientes, cada parte tiene que tener cabeza y cola, es decir dos serpientes. Tiene que ser tipo dibujo, no realistico. Usa colores Azul: #3776AB Amarillo: #FFD43B


## Verificación

```bash
python -m http.server 8000
# Abrir http://localhost:8000
```

Checklist:
- Todas las imágenes cargan (7 screenshots + logo)
- Animación de typing funciona en el hero
- Syntax highlighting en snippets de código
- Scroll suave entre secciones desde el nav
- Fade-in al hacer scroll
- Layout responsive en ventana estrecha (<768px)

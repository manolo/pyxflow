# PyFlow Implementation Status

## Current State: MVP + Routing + Grid (Advanced) + Renderers + Full UIDL Compatibility

**Vaadin version:** 25.0.4
**Lines of code:** ~3,400
**Tests:** 798 passing
**Last updated:** 2026-02-08

---

## Implemented

### Core
- [x] StateTree - Node management, change tracking
- [x] StateNode - Features, attach/put/splice
- [x] Element - Properties, attributes, styles, events
- [x] Component - Base class with element attachment

### UIDL Protocol Compatibility (Java Flow)
- [x] **Event hashes** - Hardcoded Java Flow hashes for exact compatibility
  - Click: `F8oCtNArLiI=`
  - Change: `Fg73o1qebBo=`
  - Keydown: `OSoHnU3SjNg=`
  - Opened-changed: `t7mULTj4JVU=`
  - Checked-changed: `azhwx/bqd+0=`
  - Notification closed: `vIpODLLAUDo=`
  - Notification opened-changed: `uqvzCy8jAQc=`
- [x] **UI navigation hashes** - For client-side routing
  - ui-navigate: `msDV4SvCysE=`
  - ui-leave-navigation: `i2nDWhpwLZE=`
  - ui-refresh: `18ACma10cDE=`
- [x] **contextRootUrl** - Uses `"./"` matching Java Flow
- [x] **Execute commands** - document.title, invalid property, serverConnected, component-queued (`queue_execute`)
- [x] **FlowComponentHost** - Virtual children renderer for Dialog/Overlay components
- [x] **publishedEventHandler** - Client-callable methods via Feature 19 (`CLIENT_DELEGATE_HANDLERS`)
- [x] **Server-client state sync** - `_pending_server_change` flag absorbs echoes from server-initiated property changes
- [x] **Grid connector protocol** - `gridConnector.initLazy`, `$connector.set/updateSize/confirm`, `setHeaderRenderer`
- [x] **Select connector protocol** - `selectConnector.initLazy`, `requestContentUpdate`
- [x] **ComboBox connector protocol** - `comboBoxConnector.initLazy`, `$connector.set/updateSize/confirm`, filtering
- [x] **DatePicker connector protocol** - `datepickerConnector.initLazy`
- [x] **TimePicker connector protocol** - `timepickerConnector.initLazy`
- [x] **MenuBar connector protocol** - `menubarConnector.initLazy`, `contextMenuConnector.generateItemsTree`

### Components
- [x] Button - Text, click listener
- [x] Checkbox - Label, checked, indeterminate, value change
- [x] IntegerField - Integer input with min/max/step
- [x] NumberField - Numeric input with min/max/step
- [x] TextArea - Multi-line text input with placeholder
- [x] TextField - Label, value, change event, mSync
- [x] Span - Text content
- [x] Div - Simple `<div>` with text content
- [x] VerticalLayout - Theme, add children, padding/spacing/margin, expand, horizontal component alignment
- [x] HorizontalLayout - Theme, add children, margin/spacing, expand, vertical component alignment
- [x] FlexLayout - Pure CSS Flexbox `<div>`: flex-direction, flex-wrap, justify-content, align-items/self/content, flex-grow/shrink/basis, order, expand
- [x] Dialog - Header title, modal, draggable, resizable, FlowComponentHost renderer, publishedEventHandler close
- [x] Notification - Position, duration, theme variants, open/close, static show(), body attachment
- [x] PasswordField - Password input with reveal button
- [x] EmailField - Email input with validation
- [x] ProgressBar - Determinate/indeterminate progress
- [x] Select - Dropdown single selection, `selectConnector.initLazy` overlay renderer
- [x] RadioButtonGroup - Radio button selection
- [x] CheckboxGroup - Multiple checkbox selection
- [x] FormLayout - Responsive steps, colspan, FormItem (label slot), FormRow, auto-responsive, CSS custom properties
- [x] Grid - Columns (path, header, width, flexGrow, autoWidth, resizable, sortable), in-memory data push, single/multi selection, sorting, lazy loading/DataProvider, column reordering, LitRenderer, ComponentRenderer
- [x] ConfirmDialog - Confirm/cancel/reject actions, header/message/button text, theme, cancelable/rejectable
- [x] ComboBox - Filtered dropdown, data push protocol, item label generator, custom value support
- [x] DatePicker - Date selection with calendar overlay, min/max, connector init
- [x] TimePicker - Time selection with dropdown, step, min/max, connector init
- [x] Tabs - Tab container with selected index, orientation, selection change events
- [x] Tab - Individual tab with label text
- [x] TabSheet - Tabs + content panels with slot-based association
- [x] MenuBar - Hierarchical menus with connector protocol, submenu support, click listeners
- [x] Upload - File upload via multipart HTTP POST, receiver callback, file reject/success/error events, max files/size, accepted types, auto-upload, drop zone

### Component Base Features
- [x] `setVisible()` / `isVisible()` - Show/hide components
- [x] `setEnabled()` / `isEnabled()` - Enable/disable components
- [x] `addClassName()` / `removeClassName()` - CSS class management
- [x] `setId()` / `getId()` - Component id attribute
- [x] `focus()` / `blur()` - Focus management via execute commands
- [x] `setHelperText()` / `getHelperText()` - Helper text below fields
- [x] `setTooltipText()` / `getTooltipText()` - Tooltips via `<vaadin-tooltip>` child
- [x] `addClickShortcut(Key)` - Keyboard shortcuts (keydown→click dispatch)

### Data Binding
- [x] Binder - Fluent API (`for_field().with_validator().with_converter().bind()`), `read_bean`, `write_bean`, `set_bean` (auto two-way sync), `is_dirty()` dirty tracking
- [x] Validators - `required`, `min_length`, `max_length`, `pattern`, `value_range`, `positive`, `email`
- [x] Converters - `string_to_int`, `string_to_float`, custom `Converter(to_model, to_presentation)`
- [x] ValidationError - Raised by `write_bean()` with error results
- [x] Bean-level validators - Cross-field validation via `binder.with_validator(predicate, message)`
- [x] Field error display - Sets `invalid`/`errorMessage` properties on Vaadin web components

### Server
- [x] HTTP Server (aiohttp) - Sessions, static files
- [x] UIDL Handler - Init, navigation, events, mSync
- [x] Page reload support - State reset on init
- [x] Serves index.html from bundle (Vaadin-generated)
- [x] Lumo theme CSS loading - Extracted from JAR, served at `/lumo/*`, injected in index.html

### Protocol
- [x] Init response - appConfig, CSRF, constants (Java-compatible hashes)
- [x] UIDL response - syncId, changes, execute
- [x] RPC: event - click, change, ui-navigate, keydown
- [x] RPC: mSync - Property sync from client
- [x] RPC: publishedEventHandler - Generic dispatch to any component method (Dialog close, Grid select/deselect)
- [x] **UIDL compatibility verified** - Matches Java Flow exactly:
  - Same constants keys (Base64 hashes)
  - Same execute commands format
  - Same number of changes (27 for HelloWorldView)
  - Same change types (5 attach, 17 put, 1 clear, 4 splice)

### Routing
- [x] `@Route` decorator - Path registration
- [x] Multiple views - HelloWorldView, AboutView
- [x] Page title - Explicit or auto-generated from class name
- [x] Route parameters (`/users/:id`) - Required and optional (`:param?`) syntax
- [x] Re-navigation - Navigate between views without page reload
- [x] Navigation guards - `before_leave()`, `before_enter(params)`, `after_navigation()`
- [x] RouterLink component - `<a>` tag with `router-link` attribute for client-side navigation
- [x] `@PageTitle` decorator - Alternative to `page_title` param, supports `get_page_title()` for dynamic titles

---

## Not Implemented

### Component Inventory (Vaadin 25 — 20 missing components)

Vaadin 25 has 72 npm packages. Filtering out infrastructure/themes/internals, there are **20 real UI components** not yet implemented in PyFlow, organized by implementation phase.

Full analysis with complexity, connectors, and dependencies: **`../specs/COMPONENTS.md`**

### Phase 8 — AppLayout & Prerequisites (enables real app layouts)

| Component | Tag | Complexity | Notes |
|---|---|---|---|
| [ ] **Icon** | `vaadin-icon` | Trivial | Properties: `icon`, `svg`. Required by AppLayout, SideNav, MenuBar icons |
| [ ] **App Layout** | `vaadin-app-layout` | Medium-High | Slots: drawer, navbar, content. RouterLayout interface. DrawerToggle |
| [ ] **DrawerToggle** | `vaadin-drawer-toggle` | Trivial | Hamburger button for AppLayout drawer |
| [ ] **SideNav / SideNavItem** | `vaadin-side-nav` | Medium | Navigation items with path, nested items, path matching |
| [ ] **RouterLayout interface** | (infrastructure) | Medium | `show_router_layout_content()`, `@Route(layout=...)`, layout chain in navigation |
| [ ] **`@ParentLayout` / `@RoutePrefix`** | (infrastructure) | Low | Nested layout hierarchies, path prefix from parent layouts |

### Phase 9 — Menu System + Simple High-Value Components

| Component | Tag | Complexity | Notes |
|---|---|---|---|
| [ ] **`@Menu` decorator** | (infrastructure) | Low | `@Menu(title, order, icon)`, stores metadata on view class |
| [ ] **`MenuConfiguration`** | (infrastructure) | Low | `get_menu_entries()` — collects `@Menu` routes, filters, sorts |
| [ ] **Details** | `vaadin-details` | Low | Collapsible panel. Property `opened`, slot `summary` |
| [ ] **Accordion** | `vaadin-accordion` | Medium | AccordionPanel children, `opened-changed` event |
| [ ] **Context Menu** | `vaadin-context-menu` | Medium-High | Reuses `contextMenuConnector` (already implemented for MenuBar!) |
| [ ] **DateTimePicker** | `vaadin-date-time-picker` | Medium | Composition of DatePicker + TimePicker (both already implemented) |
| [ ] **Markdown** | `vaadin-markdown` | Low | Property `content`. **New in v25**, useful for AI apps |

### Phase 10 — Visual & Layout Components

| Component | Tag | Complexity | Notes |
|---|---|---|---|
| [ ] **Avatar** | `vaadin-avatar` | Low | Properties: `name`, `abbr`, `img` |
| [ ] **Avatar Group** | `vaadin-avatar-group` | Low | Property `items` (JSON array), max visible |
| [ ] **Card** | `vaadin-card` | Low | Container with slots. **New in v25** |
| [ ] **Split Layout** | `vaadin-split-layout` | Medium | Property `splitterPosition`, orientation, resize event |
| [ ] **Scroller** | `vaadin-scroller` | Low | Scrollable container. Property `scrollDirection` |
| [ ] **Popover** | `vaadin-popover` | Medium | Overlay component. Target, trigger, position. Similar to Dialog |
| [ ] **Master Detail Layout** | `vaadin-master-detail-layout` | Medium | Layout with slots. **New in v25** |

### Phase 11 — Data & Specialized Components

| Component | Tag | Complexity | Notes |
|---|---|---|---|
| [ ] **List Box** | `vaadin-list-box` | Medium | Selection with items. Similar to RadioButtonGroup |
| [ ] **Multi Select Combo Box** | `vaadin-multi-select-combo-box` | High | Extends ComboBox: multi-select, chips, data provider |
| [ ] **Virtual List** | `vaadin-virtual-list` | High | Data provider integration (like Grid but simpler), renderer |
| [ ] **Message Input** | `vaadin-message-input` | Low | Text input with submit button |
| [ ] **Message List** | `vaadin-message-list` | Medium | Property `items` (JSON), timestamp formatting |
| [ ] **Login Form / Login Overlay** | `vaadin-login-form` | Medium | Form with `login` and `forgot-password` events |
| [ ] **Custom Field** | `vaadin-custom-field` | Medium-Low | Composite field wrapper, combines children as value |

### Protocol / Security
- [ ] CSRF token validation (actual check)
- [ ] ClientId validation (duplicate detection)
- [ ] SyncId validation (out-of-sync detection)
- [ ] Resynchronize flag support
- [ ] `@ClientCallable` methods
- [x] Return channels

### Theme
- [ ] Aura theme support (alternative to Lumo)
- [ ] Theme switching at runtime

### Server Infrastructure
- [ ] Session timeout / cleanup
- [ ] Error handling
- [ ] Push / WebSocket
- [ ] Hot reload

---

## Suggested Implementation Order

1. ~~**More basic components** - Checkbox, TextArea, NumberField~~ ✓ DONE
2. ~~**Component features** - setVisible, setEnabled, addClassName~~ ✓ DONE
3. ~~**Routing** - @Route decorator, multiple views~~ ✓ DONE
4. ~~**Feedback components** - Dialog, Notification~~ ✓ DONE
5. ~~**Lumo theme loading** - Extract and serve theme CSS~~ ✓ DONE
6. ~~**Grid** - Complex but essential for data apps~~ ✓ DONE
7. ~~**Grid advanced** - Lazy loading, sorting, multi-select, renderers~~ ✓ DONE
8. **AppLayout & Prerequisites** - Icon, AppLayout, DrawerToggle, SideNav, RouterLayout interface, `@Route(layout=...)`, layout chain
9. **Menu System + High-Value Components** - `@Menu`, MenuConfiguration, Details, Accordion, ContextMenu, DateTimePicker, Markdown
10. **Visual & Layout Components** - Avatar, Card, SplitLayout, Scroller, Popover, MasterDetailLayout
11. **Data & Specialized Components** - ListBox, MultiSelectComboBox, VirtualList, MessageInput/List, Login, CustomField

---

## Running the MVP

```bash
cd /Users/manolo/Github/platform/python/vaadin-pyflow
source .venv/bin/activate
python run.py
# Open http://localhost:8088
```

## Running Tests

```bash
pytest tests/ -v
```

---

## Architecture Reference

See parent directory:
- `/Users/manolo/Github/platform/python/CLAUDE.md` - Development guide
- `/Users/manolo/Github/platform/python/specs/PROTOCOL.md` - Protocol specs

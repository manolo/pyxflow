# PyFlow Implementation Status

## Current State: All 49 Components + WebSocket Push + Multi-UI Sessions + Full UIDL Compatibility

**Vaadin version:** 25.0.4
**Components:** 49 implemented (all Vaadin 25 UI components)
**Lines of code:** ~17,800 (core src/), ~53,400 (total with demo + tests)
**Test structure:** `tests/unit/` (2380 unit tests, default `pytest`) + `tests/ui/` (423 Playwright, run explicitly)
**Tests:** 2380 unit + 423 UI (Playwright)
**Last updated:** 2026-02-20

---

## Implemented

### Core
- [x] StateTree - Node management, change tracking
- [x] StateNode - Features, attach/put/splice
- [x] Element - Properties, attributes, styles (set/get/remove), events
- [x] Component - Base class with element attachment, `_BufferedStyle`, deferred execute_js

### UIDL Protocol Compatibility (Java Flow)
- [x] **Event hashes** - Dynamically computed via `compute_event_hash(config)` using `base64(sha256(BOM + json.encode('utf-16-be'))[:8])` for exact Java Flow compatibility
- [x] **contextRootUrl** - Uses `"./"` matching Java Flow
- [x] **Execute commands** - document.title, invalid property, serverConnected, component-queued (`queue_execute`)
- [x] **FlowComponentHost** - Virtual children renderer for Dialog/Overlay components
- [x] **publishedEventHandler** - Client-callable methods via Feature 19 (`CLIENT_DELEGATE_HANDLERS`)
- [x] **Server-client state sync** - `_pending_server_change` flag absorbs echoes from server-initiated property changes
- [x] **Client-side validation** - Field components use native web component validation (pattern, allowedCharPattern, required); `manualValidation` removed
- [x] **Grid connector protocol** - `gridConnector.initLazy`, `$connector.set/updateSize/confirm`, `setHeaderRenderer`, `setFooterRenderer`
- [x] **Grid header rows** - `prepend_header_row()`, `HeaderRow.join()` creates `<vaadin-grid-column-group>` for spanning headers
- [x] **Grid column footers** - `Column.set_footer_text()` renders footer via `setFooterRenderer`
- [x] **TreeGrid** - Hierarchical Grid with expand/collapse, inline treeGridConnector overrides (no bundle rebuild)
- [x] **Select connector protocol** - `selectConnector.initLazy`, `requestContentUpdate`
- [x] **ComboBox connector protocol** - `comboBoxConnector.initLazy`, `$connector.set/updateSize/confirm`, filtering
- [x] **MultiSelectComboBox connector** - Reuses `comboBoxConnector.initLazy`, multi-select with `selectedItems` array
- [x] **VirtualList connector protocol** - `virtualListConnector.initLazy`, `$connector.set/updateSize`, LitRenderer/ComponentRenderer
- [x] **DatePicker connector protocol** - `datepickerConnector.initLazy`
- [x] **TimePicker connector protocol** - `timepickerConnector.initLazy`
- [x] **MenuBar connector protocol** - `menubarConnector.initLazy`, `contextMenuConnector.generateItemsTree`
- [x] **ContextMenu connector protocol** - `contextMenuConnector.initLazy`, `$connector.generateItems`

### Components
- [x] Button - Text, click listener, icon (prefix slot), `set_disable_on_click`
- [x] Checkbox - Label, checked, indeterminate, value change
- [x] IntegerField - Integer input with min/max/step
- [x] NumberField - Numeric input with min/max/step, ValueChangeMode
- [x] TextArea - Multi-line text input with placeholder, ValueChangeMode
- [x] TextField - Label, value, change event, mSync, clearButtonVisible, placeholder, prefix component slot, errorMessage, pattern, allowedCharPattern, ValueChangeMode
- [x] Span - Text content
- [x] Div - Simple `<div>` with text content (extends HtmlContainer)
- [x] Header - HTML `<header>` container (extends HtmlContainer)
- [x] Footer - HTML `<footer>` container (extends HtmlContainer)
- [x] VerticalLayout - Theme, add/remove/remove_all children, padding/spacing/margin, expand, horizontal component alignment, get_flex_grow, add_and_expand
- [x] HorizontalLayout - Theme, add/remove/remove_all children, margin/spacing, expand, vertical component alignment, get_flex_grow, add_and_expand, set_wrap
- [x] FlexLayout - Pure CSS Flexbox `<div>`: flex-direction, flex-wrap, justify-content, align-items/self/content, flex-grow/shrink/basis, order, expand, remove_all
- [x] SplitLayout - Horizontal/vertical split with primary/secondary slots, splitter position, orientation
- [x] Dialog - Header title, modal, draggable, resizable, FlowComponentHost renderer, publishedEventHandler close, `get_header()`/`get_footer()` sections, set_top/set_left positioning, resize/dragged listeners
- [x] Notification - Position, duration, theme variants, open/close, static show(), body attachment
- [x] PasswordField - Password input with reveal button, ValueChangeMode
- [x] EmailField - Email input with validation, ValueChangeMode
- [x] ProgressBar - Determinate/indeterminate progress
- [x] Select - Dropdown single selection, `selectConnector.initLazy` overlay renderer, empty selection allowed
- [x] RadioButtonGroup - Radio button selection
- [x] CheckboxGroup - Multiple checkbox selection
- [x] FormLayout - Responsive steps, colspan, FormItem (label slot), FormRow, auto-responsive, CSS custom properties
- [x] Grid - Columns (path, header, width, flexGrow, autoWidth, resizable, sortable, textAlign), in-memory data push, single/multi selection, sorting, lazy loading/DataProvider, column reordering, LitRenderer, ComponentRenderer, header rows (column groups), column footers, item click listeners, scroll_to_item, remove_column, set_rows_draggable, set_drop_mode, set_empty_state_text, set_details_visible_on_click
- [x] ConfirmDialog - Confirm/cancel/reject actions, header/message/button text, theme, cancelable/rejectable
- [x] ComboBox - Filtered dropdown, data push protocol, item label generator, custom value support, class name generator, prefix component, overlay width
- [x] DatePicker - Date selection with calendar overlay, min/max, connector init, i18n, week numbers, initial position, open/close, opened-change listener
- [x] TimePicker - Time selection with dropdown, step, min/max, connector init, i18n
- [x] Tabs - Tab container with selected index, orientation, selection change events
- [x] Tab - Individual tab with label text
- [x] TabSheet - Tabs + content panels with slot-based association
- [x] MenuBar - Hierarchical menus with connector protocol, submenu support, click listeners, keep-open, disable-on-click, aria-label, separator, submenu remove/remove_all
- [x] Upload - File upload via multipart HTTP POST, receiver callback, file reject/success/error events, max files/size, accepted types, auto-upload, drop zone, i18n
- [x] Icon - `vaadin-icon`, auto-prefix `vaadin:`, color (CSS fill), size
- [x] DrawerToggle - Hamburger button for AppLayout drawer, extends Button
- [x] SideNav / SideNavItem - Navigation items with path, prefix icon slot, nested items via children slot, collapsible, label span
- [x] AppLayout - Navbar/drawer/content slots, drawerOpened, primarySection, RouterLayout interface
- [x] Details - Expandable panel, summary (text or Component), opened-changed sync
- [x] Accordion / AccordionPanel - Vertically stacked expandable panels, single-open, opened index sync
- [x] ContextMenu - Right-click/long-press menu, contextMenuConnector, hierarchical items, separators
- [x] DateTimePicker - Combined date+time, datepickerConnector + timepickerConnector, min/max/step, i18n
- [x] Markdown - Renders markdown as HTML, `content` property, new in Vaadin 25
- [x] Avatar - Name, abbreviation, image, color index
- [x] AvatarGroup - Item list (JSON property), max items visible
- [x] Scroller - Scrollable container, scroll direction (vertical/horizontal/both/none)
- [x] Card - Multi-slot container (title, subtitle, media, header-prefix/suffix, footer, content). New in v25
- [x] Popover - Overlay anchored to target, FlowComponentHost renderer, position, trigger config, open/close/modal
- [x] MasterDetailLayout - Master/detail slots, size property. New in v25
- [x] MessageInput - Submit event with message text, i18n
- [x] MessageList - Items JSON property (text, time, userName, userAbbr, userImg, userColorIndex), markdown rendering
- [x] ListBox - Items as `vaadin-item` children, selected index, value change
- [x] MultiSelectListBox - Items as children, selectedValues array, multi-select
- [x] CustomField - Composite field wrapper, children contribute to combined value
- [x] LoginForm - Login event (username/password), forgot-password event, error property, i18n
- [x] LoginOverlay - Login form in overlay, opened/title/description properties, i18n
- [x] MultiSelectComboBox - Multi-select with chips, comboBoxConnector, data provider, filtering, auto-expand, selected-items-on-top, keep-filter
- [x] VirtualList - Scrollable list, virtualListConnector, LitRenderer/ComponentRenderer support

### Component Base Features
- [x] `setVisible()` / `isVisible()` - Show/hide components
- [x] `setEnabled()` / `isEnabled()` - Enable/disable components
- [x] `addClassName()` / `removeClassName()` - CSS class management
- [x] `setId()` / `getId()` - Component id attribute
- [x] `focus()` / `blur()` - Focus management via execute commands
- [x] `setHelperText()` / `getHelperText()` - Helper text below fields
- [x] `setTooltipText()` / `getTooltipText()` - Tooltips via `<vaadin-tooltip>` child
- [x] `addClickShortcut(Key)` - Keyboard shortcuts (keydown→click dispatch)
- [x] `get_style()` - Returns `_BufferedStyle` that works before and after attach (set/get/remove buffered pre-attach, delegates to real `Style` post-attach)
- [x] `set_aria_label()` / `get_aria_label()` - ARIA label (HasAriaLabel)
- [x] `set_aria_labelled_by()` / `get_aria_labelled_by()` - ARIA labelled-by reference
- [x] `add_focus_listener()` / `add_blur_listener()` - Focus/blur events (FocusNotifier/BlurNotifier)
- [x] `ValueChangeMode` - Controls when text fields sync to server (EAGER/LAZY/TIMEOUT/ON_BLUR/ON_CHANGE). Applied to TextField, TextArea, EmailField, PasswordField, NumberField
- [x] `set_i18n(dict)` / `get_i18n()` - Localization via dict-based approach on 7 components (Upload, DatePicker, TimePicker, DateTimePicker, LoginForm, LoginOverlay, MessageInput)

### Constants & Enums
- [x] `components/constants.py` - Central enum file with all 34 theme variant enums, layout enums, field enums, GridDropMode, AutoExpandMode
- [x] Theme variant enums — `add_theme_variants()` / `remove_theme_variants()` on 34 components (Button, Grid, TextField, Dialog, etc.)
- [x] `ColumnTextAlign` — START/CENTER/END enum for Grid column text alignment
- [x] `Autocomplete` — ~50 HTML autocomplete values for TextField, PasswordField, EmailField
- [x] `Key` — Keyboard constants (ENTER, ESCAPE, TAB, Arrow keys, F1-F12) re-exported from `core/`, `components/`
- [x] All enums importable from `components/` package and from `components/constants` module

### Field Mixins
- [x] `HasReadOnly` mixin - `set_read_only()`, `is_read_only()` on all 16 field components + Checkbox + ListBox + MultiSelectListBox (18 total)
- [x] `HasValidation` mixin - `set_invalid()`, `is_invalid()`, `set_error_message()`, `get_error_message()` on all 14 field components + CustomField
- [x] `HasRequired` mixin - `set_required_indicator_visible()`, `is_required_indicator_visible()` on all 14 field components + CustomField + Checkbox
- [x] Deferred buffering - Values set before attach are buffered in `_pending_properties` and flushed on attach
- [x] `set_value()` fires change listeners — All 18 field components fire `{"value": ..., "from_client": False}` on server-side value changes, matching Java Flow's `AbstractFieldSupport.setValue()` behavior

### Data Binding
- [x] Binder - Fluent API (`for_field().with_validator().with_converter().bind()`), `read_bean`, `write_bean`, `set_bean` (auto two-way sync), `is_dirty()` dirty tracking with mSync-safe Select handling
- [x] Validators - `required`, `min_length`, `max_length`, `pattern`, `value_range`, `positive`, `email`
- [x] Converters - `string_to_int`, `string_to_float`, custom `Converter(to_model, to_presentation)`
- [x] ValidationError - Raised by `write_bean()` with error results
- [x] Bean-level validators - Cross-field validation via `binder.with_validator(predicate, message)`
- [x] Field error display - Sets `invalid`/`errorMessage` properties on Vaadin web components

### Server
- [x] HTTP Server (aiohttp) - Sessions, static files
- [x] UIDL Handler - Init, navigation, events, mSync (two-pass: mSync before events, matching Java Flow)
- [x] Page reload support - State reset on init
- [x] Multiple UIs per session - Each browser tab gets independent StateTree/UidlHandler keyed by `v-uiId`, shared CSRF token per session
- [x] UI singleton per tab - UI instance persists across navigations (like Java Flow), preserving theme state and other UI-level settings
- [x] Serves index.html from bundle (Vaadin-generated)
- [x] Lumo/Aura theme CSS - Extracted from JARs, served at `/lumo/*` and `/aura/*`, loaded via `@StyleSheet` on layout
- [x] `@StyleSheet` decorator - Load custom CSS via UIDL EAGER dependencies, served from app's `styles/` directory
- [x] Dev mode (`--dev`) - Auto-reload on Python file changes via watchfiles, socket-in-parent architecture (no EADDRINUSE on reload), file change logging, mtime-based dedup (ignores macOS metadata-only events)
- [x] WebSocket Push - Atmosphere protocol, `GET /VAADIN/push` endpoint, push sender coroutine, `UI.access()` / `UI.push()` API, reconnect resilience (pending message buffer)
- [x] Heartbeat handler (`v-r=heartbeat`) — keeps session alive, prevents 403 after idle
- [x] Session timeout / cleanup (30min idle, background sweep every 60s)
- [x] Error handling — Per-RPC try/except, error Notification to user, navigation error feedback, push sender broad catch
- [x] Missing bundle file logging — `[404] /VAADIN/{path}` printed to server console for easier debugging

### Protocol / Security
- [x] CSRF token validation (actual check) — validated in `http_server.py`
- [x] ClientId validation (duplicate detection, replays last response)
- [x] SyncId validation (out-of-sync detection)
- [x] Resynchronize flag support
- [x] Return channels — used by Grid and VirtualList ComponentRenderer
- [x] Multi-UI session routing — `v-uiId` query param routes UIDL/push to correct UI; invalid UI returns session-expired

### Theme
- [x] Lumo/Aura theme support — `@StyleSheet("lumo/lumo.css")` or `@StyleSheet("aura/aura.css")` on layout
- [x] Runtime theme switching — `UI.set_theme(theme, variant)` / `UI.get_theme()` / `UI.get_theme_variant()` — full get/set API
- [x] Theme-agnostic CSS — Demo styles use `--vaadin-*` base properties with `--lumo-*` fallbacks
- [x] `@ColorScheme` decorator — Set initial color scheme on `@AppShell` (dark/light/system), modifies `<html>` attributes at bootstrap (no flash)
- [x] `UI.set_color_scheme(value)` — Runtime color scheme switching (dark/light/system/normal)

### Protocol
- [x] Init response - appConfig, pushScript, CSRF, constants (Java-compatible hashes)
- [x] UIDL response - syncId, changes, execute
- [x] Push response - `meta.async`, Atmosphere length-prefix format
- [x] RPC: event - click, change, input, blur, ui-navigate, keydown
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
- [x] Wildcard route parameters (`:path*`) - Match 0+ remaining segments, `RouteParameters.get_wildcard()`
- [x] Mid-position optional params (`user/:id?/contact`) - Optional segments anywhere in path
- [x] Query parameters - `QueryParameters` class, parsed from URL via `BeforeEnterEvent.location.query_parameters`
- [x] `BeforeEnterEvent` - Full navigation context (location, route params, query params), dict-compatible for backward compat
- [x] Navigation data classes - `QueryParameters`, `RouteParameters`, `Location`, `BeforeEnterEvent`
- [x] Re-navigation - Navigate between views without page reload
- [x] Navigation guards - `before_leave()`, `before_enter(event)`, `after_navigation()`
- [x] RouterLink component - `<a>` tag with `router-link` attribute for client-side navigation
- [x] `@PageTitle` decorator - Alternative to `page_title` param, supports `get_page_title()` for dynamic titles
- [x] `@Route(layout=...)` - RouterLayout support, layout chain in navigation, layout reuse on same-layout routes
- [x] `@Menu(title, order, icon)` - Decorator for automatic menu generation
- [x] `get_menu_entries()` - Collects @Menu routes, filters required params, sorts by order/path
- [x] `@AppShell` - Global app configuration class (single place for @Push, @StyleSheet)
- [x] `@Push` - Opt-in WebSocket push (conditional pushScript, push nodes in init)
- [x] `@ColorScheme` - Initial color scheme (dark/light/system) applied to `<html>` at bootstrap
- [x] AppShell `@StyleSheet` - Stylesheets loaded in init response (before any navigation)
- [x] Route not found - Shows "Could not navigate to '...'" view for unregistered routes
- [x] Dev mode route list - In `--dev` mode, not-found view shows clickable RouterLinks to all registered routes

---

## What's Missing

> **For the detailed per-component API inventory (every method, [x]/[ ]), see `STATUS.API.md`.**
>
> API coverage: **~470 methods implemented, ~40 missing** (~92% complete).

### Unimplemented Features

| Feature | Priority | Description |
|---------|----------|-------------|
| `@PWA` annotation | Medium | Activate `sw.js` from bundle, serve `manifest.json` with configurable app name/icons |
| Security (`--secure`) | Medium | Login screen from local config, restrict interfaces (localhost vs 0.0.0.0), HTTPS/TLS |
| Grid Editor API | Low | Inline row editing (`get_editor`, bind fields to columns, save/cancel) |
| `HasErrorParameter` error views | Medium | Navigate to error view on unhandled exceptions (Java's `DefaultErrorHandler` + `ErrorHandlerUtil`). Currently shows Notification instead. |
| Grid Drag/Drop listeners | Low | Drag start/end/drop event listeners (rows draggable & drop mode already implemented) |
| Grid item details renderer | Low | Expandable row details via `set_item_details_renderer` (set_details_visible_on_click already implemented) |
| Specialized renderers | Low | NumberRenderer, LocalDateRenderer, LocalDateTimeRenderer, NativeButtonRenderer, IconRenderer |
| ConfigurableFilterDataProvider | Low | Advanced filtering for DataProvider |

### Missing API Methods — Summary by Component

| Component | Missing Methods | Priority |
|-----------|----------------|----------|
| **Grid** | `add_component_column`, `set_item_details_renderer`, Editor API, Drag/Drop listeners | Medium |
| **ComboBox** | `set_renderer` | Low |
| **MultiSelectComboBox** | `set_renderer` | Low |
| **MenuBar** | `add_item(Component)`, `close` | Low |
| **DatePicker** | `set_locale` | Low |
| **FlexLayout** | `replace`/`add_component_at_index` | Low |
| **Select** | `set_renderer`, `set_item_enabled_provider` | Low |
| **CheckboxGroup/RadioButtonGroup** | `set_item_enabled_provider`, `set_renderer` | Low |
| **ListBox/MultiSelectListBox** | `set_renderer`, `add_components` (dividers) | Low |
| **Button** | `click` (server-side) | Low |
| **Other** | Various minor methods across Tabs, Details, ContextMenu, Upload, LoginOverlay, Popover, etc. | Low |

### Missing Tests

| Category | Coverage | Details |
|----------|----------|---------|
| **Unit tests** | 2314 passing | Good coverage of all 49 components + core + data layer. Located in `tests/unit/` |
| **UI tests** | 423 passed | All 31 test views (in `tests/views/`) with shared SideNav layout and single browser session. UI tests in `tests/ui/`. |

---

## Completed Phases

All 12 implementation phases are complete:

1. ~~Core + basic components~~ ✓
2. ~~Component features (setVisible, setEnabled, addClassName)~~ ✓
3. ~~Routing (@Route, multiple views, parameters)~~ ✓
4. ~~Feedback (Dialog, Notification)~~ ✓
5. ~~Lumo/Aura theme loading~~ ✓
6. ~~Grid (basic)~~ ✓
7. ~~Grid (advanced: lazy loading, sorting, multi-select, renderers)~~ ✓
8. ~~AppLayout & Prerequisites (Icon, DrawerToggle, SideNav, RouterLayout)~~ ✓
9. ~~Menu System + High-Value Components (@Menu, Details, Accordion, ContextMenu, DateTimePicker, Markdown)~~ ✓
10. ~~Visual & Layout Components (Avatar, Card, Scroller, Popover, MasterDetailLayout)~~ ✓
11. ~~Data & Specialized Components (ListBox, MultiSelectComboBox, VirtualList, MessageInput/List, Login, CustomField)~~ ✓
12. ~~WebSocket Push (Atmosphere protocol, UI.access, push sender)~~ ✓

Plus: `@ClientCallable`, `@ColorScheme`, runtime theme switching, field mixins, Binder, `vaadin --bundle`.

### Packaging & Bundle
- [x] PyPI-ready wheel — `pip install vaadin-pyflow`
- [x] Bundle inside package — `src/vaadin/flow/bundle/` ships in wheel (1.5 MB compressed)
- [x] CLI entry point — `vaadin [app_module] [--dev] [--debug] [--port N]`
- [x] `vaadin --bundle` — Auto-generate bundle from `_v_fqcn` component registry
- [x] `vaadin <app> --bundle` — User projects can generate their own bundle
- [x] Bundle discovery priority — app-dir bundle > package-internal > cwd fallback
- [x] Apache 2.0 LICENSE file

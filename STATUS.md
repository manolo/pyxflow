# PyFlow Implementation Status

## Current State: MVP + Routing + Full UIDL Compatibility

**Vaadin version:** 25.0.4
**Lines of code:** ~2,500
**Tests:** 302 passing
**Last updated:** 2026-02-06

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
- [x] **Execute commands** - document.title, invalid property, serverConnected
- [x] **FlowComponentHost** - Virtual children renderer for Dialog/Overlay components
- [x] **publishedEventHandler** - Client-callable methods via Feature 19 (`CLIENT_DELEGATE_HANDLERS`)
- [x] **Server-client state sync** - `_pending_server_change` flag absorbs echoes from server-initiated property changes

### Components
- [x] Button - Text, click listener
- [x] Checkbox - Label, checked, indeterminate, value change
- [x] IntegerField - Integer input with min/max/step
- [x] NumberField - Numeric input with min/max/step
- [x] TextArea - Multi-line text input with placeholder
- [x] TextField - Label, value, change event, mSync
- [x] Span - Text content
- [x] VerticalLayout - Theme, add children, padding/spacing
- [x] HorizontalLayout - Theme, add children, margin/spacing, vertical alignment
- [x] Dialog - Header title, modal, draggable, resizable, FlowComponentHost renderer, publishedEventHandler close
- [x] Notification - Position, duration, theme variants, open/close, static show(), body attachment
- [x] PasswordField - Password input with reveal button
- [x] EmailField - Email input with validation
- [x] ProgressBar - Determinate/indeterminate progress
- [x] Select - Dropdown single selection
- [x] RadioButtonGroup - Radio button selection
- [x] CheckboxGroup - Multiple checkbox selection

### Component Base Features
- [x] `setVisible()` / `isVisible()` - Show/hide components
- [x] `setEnabled()` / `isEnabled()` - Enable/disable components
- [x] `addClassName()` / `removeClassName()` - CSS class management

### Server
- [x] HTTP Server (aiohttp) - Sessions, static files
- [x] UIDL Handler - Init, navigation, events, mSync
- [x] Page reload support - State reset on init
- [x] Serves index.html from bundle (Vaadin-generated)
- [x] Lumo theme CSS loading - Extracted from JAR, served at `/lumo/*`, injected in index.html

### Bundle Generator
- [x] Minimal Maven project (`bundle-generator/`)
- [x] Uses `vaadin-core` (no Spring)
- [x] Lumo theme via `@StyleSheet(Lumo.STYLESHEET)`
- [x] `AllComponentsView.java` mirrors Python `ComponentsDemoView` (identical content/structure)
- [x] Build: `./mvnw package` (Vaadin 25 builds production bundle by default)
- [x] `generate-bundle.sh` extracts Lumo CSS from nested JAR (version-independent)

### Protocol
- [x] Init response - appConfig, CSRF, constants (Java-compatible hashes)
- [x] UIDL response - syncId, changes, execute
- [x] RPC: event - click, change, ui-navigate, keydown
- [x] RPC: mSync - Property sync from client
- [x] RPC: publishedEventHandler - Client-callable methods (Dialog close)
- [x] **UIDL compatibility verified** - Matches Java Flow exactly:
  - Same constants keys (Base64 hashes)
  - Same execute commands format
  - Same number of changes (27 for HelloWorldView)
  - Same change types (5 attach, 17 put, 1 clear, 4 splice)

### Routing
- [x] `@Route` decorator - Path registration
- [x] Multiple views - HelloWorldView, AboutView
- [x] Page title - Explicit or auto-generated from class name

---

## Not Implemented

### Components (Priority: High)
- [ ] ComboBox (with filtering)
- [ ] DatePicker / TimePicker

### Components (Priority: Medium)
- [ ] Grid (complex)
- [ ] MenuBar
- [ ] Tabs / TabSheet
- [ ] FormLayout
- [ ] Upload

### Component Features
- [ ] `setId()` / `getId()`
- [ ] `focus()` / `blur()`
- [ ] Keyboard shortcuts (`addClickShortcut(Key.ENTER)`)
- [ ] Tooltips
- [ ] Helper text

### Routing (Advanced)
- [ ] Route parameters (`/users/:id`)
- [ ] Navigation guards (BeforeEnter/Leave)
- [ ] RouterLink component
- [ ] `@PageTitle` decorator (alternative to page_title param)

### Data Binding
- [ ] Binder
- [ ] Validators
- [ ] Converters
- [ ] DataProvider

### Protocol / Security
- [ ] CSRF token validation (actual check)
- [ ] ClientId validation (duplicate detection)
- [ ] SyncId validation (out-of-sync detection)
- [ ] Resynchronize flag support
- [ ] `@ClientCallable` methods
- [ ] Return channels

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
6. **Grid** - Complex but essential for data apps

---

## Running the MVP

```bash
cd /Users/manolo/Github/platform/python/vaadin-pyflow
source .venv/bin/activate
python run.py
# Open http://localhost:8080
```

## Running Tests

```bash
pytest tests/ -v
```

---

## Architecture Reference

See parent directory:
- `/Users/manolo/Github/platform/python/CLAUDE.md` - Development guide
- `/Users/manolo/Github/platform/python/SPECS.md` - Protocol specs

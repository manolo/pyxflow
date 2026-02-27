# Vaadin Frontend Bundle

PyFlow reuses Vaadin's frontend infrastructure (FlowClient, web components, Lumo theme) by serving a pre-built JavaScript bundle.

## What's in the Bundle

The bundle lives inside the Python package at `src/pyflow/bundle/` so it ships with the wheel.

```
src/pyflow/bundle/
├── index.html                     # Entry point HTML
├── VAADIN/build/
│   ├── indexhtml-*.js              # Entry point, initializes FlowClient
│   ├── FlowClient-*.js             # UIDL protocol handler
│   ├── FlowBootstrap-*.js          # Bootstrap utilities
│   ├── generated-flow-imports-*.js # ALL web components (~3.7MB)
│   ├── commonjsHelpers-*.js        # CommonJS compatibility
│   └── *.br                        # Brotli-compressed versions
├── lumo/                           # Lumo theme CSS (from vaadin-lumo-theme JAR)
│   ├── lumo.css                    # Main theme (224KB) - colors, typography, icons
│   ├── utility.css                 # Utility classes (34KB, optional)
│   └── presets/
│       └── compact.css             # Compact preset (566B, optional)
└── aura/                           # Aura theme CSS
    ├── aura.css                    # Aura theme styles
    └── fonts/                      # Aura fonts (InstrumentSans)
```

### Theme CSS

The `lumo/` directory contains the Lumo theme CSS extracted from `vaadin-lumo-theme-25.0.6.jar`.
**Without this CSS, components render with browser defaults** (no Lumo styling).
The server injects `<link rel="stylesheet" href="lumo/lumo.css">` into the HTML at serve time.

The bundle includes **all Vaadin components**:
- Basic: Button, TextField, TextArea, Checkbox, NumberField, etc.
- Layout: VerticalLayout, HorizontalLayout, FormLayout, etc.
- Data: Grid, ComboBox, Select, DatePicker, etc.
- Feedback: Dialog, Notification, ProgressBar, etc.
- Navigation: Tabs, MenuBar, SideNav, etc.

## Bundle Source

The bundle comes from **vaadin-prod-bundle** on Maven Central:

```
https://repo1.maven.org/maven2/com/vaadin/vaadin-prod-bundle/25.0.6/vaadin-prod-bundle-25.0.6.jar
```

We use the **unoptimized** version (single file, no code splitting) for simplicity.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                         Browser                                  │
├─────────────────────────────────────────────────────────────────┤
│  1. Load index.html                                             │
│  2. Load indexhtml-*.js  ──────────────────────┐                │
│  3. FlowClient initializes                     │                │
│  4. GET /?v-r=init (get appConfig)             │   From         │
│  5. POST /?v-r=uidl (navigation)               │   bundle/      │
│  6. FlowClient applies changes to DOM          │                │
│  7. Web components render UI                   │                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       PyFlow Server                              │
├─────────────────────────────────────────────────────────────────┤
│  - Generates index.html                                         │
│  - Serves VAADIN/* static files from package bundle              │
│  - Handles UIDL protocol (init, events, sync)                   │
│  - Manages StateTree (server-side component state)              │
└─────────────────────────────────────────────────────────────────┘
```

## Updating the Bundle

### Using `pyflow bundle` (recommended)

```bash
# Copy bundle from Maven JARs (auto-downloads from Maven Central if missing)
pyflow bundle

# Pin a specific version
pyflow bundle --vaadin-version 25.1.0

# Use the optimized (code-split) bundle (larger on disk, lazy-loaded chunks)
pyflow bundle --optimized
```

The command extracts the bundle from 4 Maven JARs (prod-bundle, flow-push, lumo-theme, aura-theme). If any JAR is not in `~/.m2/repository/`, it is automatically downloaded from Maven Central.

### Verify

```bash
ls src/pyflow/bundle/VAADIN/build/
# Should show: FlowClient-*.js, indexhtml-*.js, generated-flow-imports-*.js, etc.
```

## Bundle Versions

The Vaadin version is configured in `pyproject.toml`:

```toml
[tool.pyflow]
vaadin-version = "25.0.6"
flow-version = "25.0.7"
```

| PyFlow Version | Vaadin Bundle Version | Notes |
|----------------|----------------------|-------|
| Current        | 25.0.6               | All components included |

### Upgrading Vaadin Version

1. Update `vaadin-version` (and `flow-version` if needed) in `pyproject.toml`
2. Run `pyflow bundle` (auto-downloads new JARs)
3. Test that PyFlow still works
4. Update this table

## Optimized vs Unoptimized Bundle

The `vaadin-prod-bundle` JAR contains two variants:

| | Unoptimized (default) | Optimized (`--optimized`) |
|---|---|---|
| JAR path | `vaadin-prod-bundle-unoptimized/webapp/` | `vaadin-prod-bundle/webapp/` |
| JS files | 6 (single `generated-flow-imports.js`) | 28 (~10 chunks x 3 browser variants) |
| JS on disk | 4.07 MB | 11.17 MB |
| Brotli on disk | 0.91 MB | 2.61 MB |
| JS per browser | 4.07 MB (all upfront) | ~3.9 MB (lazy-loaded chunks) |
| Other files | 34 (icons, sw.js) - 728 KB | 34 (identical) - 728 KB |
| **Total on disk** | **5.69 MB (47 files)** | **14.49 MB (91 files)** |

The **optimized** bundle is code-split into lazy chunks, but each chunk ships in 3 variants
(ES2020/ES2022/ESNext) for different browser targets -- so the on-disk size is ~3x larger.
The browser only downloads one variant per chunk, so the actual network transfer is slightly
smaller (~3.9 MB vs 4.07 MB before compression).

The default is **unoptimized** because:
- Much smaller on disk (5.7 MB vs 14.5 MB) -- matters for wheel/package size
- Simpler (one JS file, no chunk loading logic)
- Easier to debug
- PyFlow loads all components anyway, so lazy loading has little benefit
- Network difference is negligible with Brotli compression (~0.9 MB either way)

Use `pyflow bundle --optimized` to switch to the code-split version if lazy chunk loading is desired.

The `--optimized` flag works with both modes:
- **Copy mode** (`pyflow bundle --optimized`): extracts from `vaadin-prod-bundle/webapp/`
  instead of `vaadin-prod-bundle-unoptimized/webapp/`.
- **Build mode** (`pyflow bundle --build --optimized`): sets `<optimizeBundle>true</optimizeBundle>`
  in the Maven plugin config so Vite produces code-split chunks. Without it, `<optimizeBundle>false</optimizeBundle>`
  generates a single monolithic JS file.

Note: `--build` defaults to `--optimized` being off (single JS file), matching the copy mode default.

## Troubleshooting

### "Component not rendering"

All components are included in the bundle. If a component doesn't render:
1. Check that PyFlow has the component class implemented
2. Verify the tag name matches (`vaadin-checkbox`, `vaadin-grid`, etc.)
3. Check browser console for errors

### "FlowClient error"

The UIDL protocol might have changed between Vaadin versions:
1. Check the Vaadin version in the bundle
2. Compare UIDL responses with a Java Vaadin app of the same version
3. Adjust `uidl_handler.py` as needed

### "Old bundle cached"

Clear the browser cache or use incognito mode to ensure the latest bundle is loaded.

## File Sizes (v25.0.6, unoptimized -- default)

| File | Original | Brotli |
|------|----------|--------|
| generated-flow-imports-*.js | 3,668 KB | 807 KB |
| indexhtml-*.js | 331 KB | 92 KB |
| FlowClient-*.js | 145 KB | 41 KB |
| FlowBootstrap-*.js | 3 KB | 0.9 KB |
| **Total JS** | **4.07 MB** | **~942 KB** |

With Brotli compression (enabled by default in browsers), the JS download is under 1 MB.

# Vaadin Frontend Bundle

PyFlow reuses Vaadin's frontend infrastructure (FlowClient, web components, Lumo theme) by serving a pre-built JavaScript bundle.

## What's in the Bundle

The bundle lives inside the Python package at `src/vaadin/flow/bundle/` so it ships with the wheel.

```
src/vaadin/flow/bundle/
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

The `lumo/` directory contains the Lumo theme CSS extracted from `vaadin-lumo-theme-25.0.4.jar`.
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
https://repo1.maven.org/maven2/com/vaadin/vaadin-prod-bundle/25.0.4/vaadin-prod-bundle-25.0.4.jar
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

### Download from Maven Central

```bash
cd /tmp

# Download the JAR
curl -LO "https://repo1.maven.org/maven2/com/vaadin/vaadin-prod-bundle/25.0.4/vaadin-prod-bundle-25.0.4.jar"

# Extract the unoptimized bundle
unzip -o vaadin-prod-bundle-25.0.4.jar "vaadin-prod-bundle-unoptimized/webapp/VAADIN/build/*" -d extracted

# Copy to PyFlow (bundle lives inside the package)
cd /path/to/vaadin-pyflow
rm -rf src/vaadin/flow/bundle/VAADIN/build/*
cp /tmp/extracted/vaadin-prod-bundle-unoptimized/webapp/VAADIN/build/* src/vaadin/flow/bundle/VAADIN/build/
```

### Verify

```bash
ls src/vaadin/flow/bundle/VAADIN/build/
# Should show: FlowClient-*.js, indexhtml-*.js, generated-flow-imports-*.js, etc.
```

## Bundle Versions

| PyFlow Version | Vaadin Bundle Version | Notes |
|----------------|----------------------|-------|
| Current        | 25.0.4               | All components included |

### Upgrading Vaadin Version

1. Find the new version on Maven Central
2. Download and extract as shown above
3. Test that PyFlow still works
4. Update this table

## Optimized vs Unoptimized Bundle

The JAR contains two versions:

| Version | Path | Size | Structure |
|---------|------|------|-----------|
| Optimized | `vaadin-prod-bundle/webapp/` | ~4MB | Multiple chunks (code splitting) |
| Unoptimized | `vaadin-prod-bundle-unoptimized/webapp/` | ~5MB | Single `generated-flow-imports.js` |

We use **unoptimized** because:
- Simpler (one file for all components)
- No chunk loading logic needed
- Easier to debug
- Size difference is minimal with compression

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

## File Sizes (v25.0.4)

| File | Original | Brotli |
|------|----------|--------|
| generated-flow-imports-*.js | 3.7 MB | 807 KB |
| indexhtml-*.js | 329 KB | 92 KB |
| FlowClient-*.js | 145 KB | 41 KB |
| FlowBootstrap-*.js | 2.7 KB | 0.9 KB |
| **Total** | **~4.2 MB** | **~942 KB** |

With Brotli compression (enabled by default in browsers), the download is under 1MB.

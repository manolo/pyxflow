# Vaadin Frontend Bundle

PyFlow reuses Vaadin's frontend infrastructure (FlowClient, web components, Lumo theme) by serving a pre-built JavaScript bundle.

## What's in the Bundle

```
bundle/VAADIN/build/
├── indexhtml-*.js           # Entry point, initializes FlowClient
├── FlowClient-*.js          # UIDL protocol handler
├── FlowBootstrap-*.js       # Bootstrap utilities
├── generated-flow-imports-*.js  # Web components (Button, TextField, etc.)
├── commonjsHelpers-*.js     # CommonJS compatibility
└── *.br                     # Brotli-compressed versions
```

These files handle:
- **FlowClient**: Communication with the server via UIDL protocol
- **Web Components**: `<vaadin-button>`, `<vaadin-text-field>`, layouts, etc.
- **Lumo Theme**: Default Vaadin styling

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
│  - Serves bundle/VAADIN/* static files                          │
│  - Handles UIDL protocol (init, events, sync)                   │
│  - Manages StateTree (server-side component state)              │
└─────────────────────────────────────────────────────────────────┘
```

## Generating the Bundle

The bundle is generated from a reference Java Vaadin application. Currently we use `my-hello` as the reference.

### Prerequisites

- Java 21+
- Maven

### Steps

1. **Build the reference application**

   ```bash
   cd /Users/manolo/Github/platform/python/my-hello
   ./mvnw package
   ```

   This creates a production bundle in:
   ```
   target/classes/META-INF/VAADIN/webapp/VAADIN/build/
   ```

2. **Copy the bundle to PyFlow**

   ```bash
   cd /Users/manolo/Github/platform/python/vaadin-pyflow

   # Remove old bundle
   rm -rf bundle/VAADIN/build/*

   # Copy new bundle
   cp -r ../my-hello/target/classes/META-INF/VAADIN/webapp/VAADIN/build/* bundle/VAADIN/build/
   ```

3. **Verify**

   ```bash
   ls bundle/VAADIN/build/
   # Should show: FlowClient-*.js, indexhtml-*.js, etc.
   ```

### What Components Are Included

The bundle includes web components based on what's imported in the reference app. The `my-hello` app includes:

- `vaadin-button`
- `vaadin-text-field`
- `vaadin-horizontal-layout`
- `vaadin-vertical-layout`
- Lumo theme

To add more components (e.g., `vaadin-checkbox`, `vaadin-grid`), add them to the reference app's Java code and rebuild.

## Reference Application (my-hello)

Location: `/Users/manolo/Github/platform/python/my-hello`

This is a minimal Vaadin 25 application that:
1. Imports the components we need
2. Generates the production frontend bundle
3. Serves as a reference for UIDL protocol behavior

### Adding New Components

1. Add the component to `my-hello/pom.xml` (if not already included)
2. Use the component in Java code (to trigger inclusion in bundle)
3. Rebuild: `./mvnw package`
4. Copy the new bundle to PyFlow

Example - to add Checkbox:
```java
// In my-hello's MainView.java
import com.vaadin.flow.component.checkbox.Checkbox;

// Use it somewhere to ensure it's bundled
Checkbox cb = new Checkbox("Example");
```

## Bundle Version

The bundle is tied to a specific Vaadin version. Current: **Vaadin 25.x**

When upgrading Vaadin:
1. Update `my-hello/pom.xml` with new Vaadin version
2. Rebuild and copy the bundle
3. Test that PyFlow still works with the new FlowClient

## Troubleshooting

### "Component not rendering"

The web component might not be in the bundle. Check:
```bash
grep "vaadin-checkbox" bundle/VAADIN/build/generated-flow-imports-*.js
```

If not found, add it to the reference app and rebuild.

### "FlowClient error"

The UIDL protocol might have changed. Compare:
1. Capture UIDL from Java app (browser DevTools → Network)
2. Compare with PyFlow's UIDL responses
3. Adjust `uidl_handler.py` as needed

### "Styles not applied"

Lumo theme is included in the bundle. If custom styles are needed:
1. Add them to the reference app's theme
2. Rebuild the bundle

# Theming

PyXFlow uses Vaadin's Lumo theme system with support for dark/light mode,
custom stylesheets, component theme variants, and CSS custom properties.

## Theme Setup

Every PyXFlow app should configure its theme in the `@AppShell` class:

```python
# views/layout.py
from pyxflow import AppShell, ColorScheme, StyleSheet
from pyxflow.components import AppLayout, DrawerToggle, H2, SideNav, SideNavItem, Icon
from pyxflow.menu import get_menu_entries

@AppShell
@ColorScheme("dark")                           # "dark" or "light"
@StyleSheet("lumo/lumo.css", "styles/app.css") # Lumo base + custom CSS
class MainLayout(AppLayout):
    def __init__(self):
        self.add_to_navbar(DrawerToggle(), H2("My App"))
        nav = SideNav()
        for entry in get_menu_entries():
            icon = Icon(entry.icon) if entry.icon else None
            nav.add_item(SideNavItem(entry.title, entry.path, icon))
        self.add_to_drawer(nav)
```

### Decorator order

Decorators are read bottom-up. `@AppShell` must be outermost (first line):

```python
@AppShell                    # 1. marks this as the app shell
@ColorScheme("dark")         # 2. sets initial color scheme
@StyleSheet("lumo/lumo.css", "styles/app.css")  # 3. loads stylesheets
class MainLayout(AppLayout):
    ...
```

### @StyleSheet paths

- `"lumo/lumo.css"` -- **always include this** as the first stylesheet; it loads Lumo utility CSS
- Additional paths are relative to `<app_dir>/static/` and served automatically
- Multiple stylesheets: `@StyleSheet("lumo/lumo.css", "styles/app.css", "styles/grid.css")`

## Starter CSS Template

Create `static/styles/app.css` with this base:

```css
/* ── Lumo variable overrides ── */
/* Uncomment to customize the default Lumo theme */

/* html {
  --lumo-primary-color: hsl(220, 90%, 52%);
  --lumo-primary-text-color: hsl(220, 90%, 52%);
  --lumo-primary-color-50pct: hsla(220, 90%, 52%, 0.5);
  --lumo-primary-color-10pct: hsla(220, 90%, 52%, 0.1);
  --lumo-border-radius-m: 8px;
  --lumo-font-family: "Inter", var(--lumo-font-family);
} */

/* ── Full-height app layout ── */
html, body {
  height: 100%;
  margin: 0;
}

/* ── View padding ── */
/* Views inside AppLayout get consistent padding */
.view-padding {
  padding: var(--lumo-space-l);
}

/* ── Master-Detail pattern ── */
.master-detail-view {
  display: flex;
  flex-direction: column;
}

.master-detail-view vaadin-split-layout {
  flex: 1;
  min-height: 0;
}

.master-detail-view .editor-layout {
  display: flex;
  flex-direction: column;
  width: 400px;
}

.master-detail-view .editor {
  flex-grow: 1;
  padding: var(--lumo-space-l);
  overflow-y: auto;
}

.master-detail-view .button-layout {
  width: 100%;
  flex-wrap: wrap;
  background-color: var(--lumo-contrast-5pct);
  padding: var(--lumo-space-s) var(--lumo-space-l);
}
```

## File Structure

```
my-app/
  views/
    layout.py          # @AppShell + @ColorScheme + @StyleSheet
    home.py
  static/
    styles/
      app.css          # Custom styles (referenced in @StyleSheet)
    images/
      logo.png         # Static assets
  app.py               # FlowApp("views")
```

## Color Scheme

```python
@ColorScheme("dark")   # Dark mode (Lumo Dark)
@ColorScheme("light")  # Light mode (Lumo Light, default)
```

The color scheme sets the `theme` attribute on `<html>`: `theme="dark"` or nothing for light.

## Custom Stylesheets

```python
@StyleSheet("lumo/lumo.css", "styles/custom.css")
```

CSS files go in `<app_dir>/static/` and are served automatically.
Always include `"lumo/lumo.css"` first to load the Lumo utility layer.

## Theme Variants

Components have variant enums for quick styling:

```python
from pyxflow.components import Button, ButtonVariant

btn = Button("Save")
btn.add_theme_variants(ButtonVariant.LUMO_PRIMARY)
btn.add_theme_variants(ButtonVariant.LUMO_SMALL)

# Or use theme name strings directly
btn.add_theme_name("primary", "small")
```

## Common Variants

```python
# Button
ButtonVariant.LUMO_PRIMARY, LUMO_TERTIARY, LUMO_ERROR, LUMO_SUCCESS, LUMO_SMALL, LUMO_ICON

# Grid
GridVariant.LUMO_NO_BORDER, LUMO_ROW_STRIPES, LUMO_COMPACT, LUMO_COLUMN_BORDERS

# TextField (and similar fields)
TextFieldVariant.LUMO_SMALL, LUMO_ALIGN_RIGHT, LUMO_HELPER_ABOVE_FIELD

# Notification
NotificationVariant.LUMO_SUCCESS, LUMO_ERROR, LUMO_WARNING, LUMO_PRIMARY

# Dialog
DialogVariant.LUMO_NO_PADDING
```

## Inline Styles

```python
component.get_style().set("color", "red")
component.get_style().set("padding", "var(--lumo-space-m)")
component.get_style().set("background", "var(--lumo-contrast-5pct)")
```

## CSS Class Names

```python
component.add_class_name("my-custom-class")
component.remove_class_name("my-custom-class")
```

## Lumo CSS Variables Reference

### Spacing
```css
var(--lumo-space-xs)   /* 0.25rem */
var(--lumo-space-s)    /* 0.5rem */
var(--lumo-space-m)    /* 1rem */
var(--lumo-space-l)    /* 1.5rem */
var(--lumo-space-xl)   /* 2.5rem */
```

### Colors
```css
var(--lumo-primary-color)            /* Primary brand color */
var(--lumo-primary-text-color)       /* Primary color for text */
var(--lumo-primary-color-50pct)      /* Primary at 50% opacity */
var(--lumo-primary-color-10pct)      /* Primary at 10% opacity */
var(--lumo-error-color)              /* Error/danger color */
var(--lumo-error-text-color)         /* Error color for text */
var(--lumo-success-color)            /* Success color */
var(--lumo-success-text-color)       /* Success color for text */
var(--lumo-contrast-5pct)            /* Subtle background */
var(--lumo-contrast-10pct)           /* Borders, separators */
var(--lumo-contrast-20pct)           /* Stronger borders */
var(--lumo-contrast-50pct)           /* Disabled text */
var(--lumo-contrast-60pct)           /* Secondary text */
var(--lumo-contrast-80pct)           /* Body text */
var(--lumo-contrast-90pct)           /* Heading text */
var(--lumo-base-color)               /* Surface/card background */
var(--lumo-body-text-color)          /* Default text color */
var(--lumo-secondary-text-color)     /* Muted text */
var(--lumo-header-text-color)        /* Header text */
```

### Typography
```css
var(--lumo-font-size-xxs)   /* 0.75rem */
var(--lumo-font-size-xs)    /* 0.8125rem */
var(--lumo-font-size-s)     /* 0.875rem */
var(--lumo-font-size-m)     /* 1rem */
var(--lumo-font-size-l)     /* 1.125rem */
var(--lumo-font-size-xl)    /* 1.375rem */
var(--lumo-font-size-xxl)   /* 1.75rem */
var(--lumo-font-size-xxxl)  /* 2.5rem */
var(--lumo-line-height-xs)  /* 1.25 */
var(--lumo-line-height-s)   /* 1.375 */
var(--lumo-line-height-m)   /* 1.625 */
var(--lumo-font-family)     /* Default font stack */
```

### Border Radius
```css
var(--lumo-border-radius-s)  /* 0.25em */
var(--lumo-border-radius-m)  /* 0.5em - default for most components */
var(--lumo-border-radius-l)  /* 1em */
```

### Shadows
```css
var(--lumo-box-shadow-xs)    /* Subtle shadow */
var(--lumo-box-shadow-s)     /* Card shadow */
var(--lumo-box-shadow-m)     /* Dropdown shadow */
var(--lumo-box-shadow-l)     /* Dialog shadow */
var(--lumo-box-shadow-xl)    /* Overlay shadow */
```

## Size Utilities

```python
component.set_width("100%")
component.set_height("400px")
component.set_size_full()       # width=100%, height=100%
component.set_width_full()      # width=100%
component.set_height_full()     # height=100%
component.set_min_width("200px")
component.set_max_width("800px")
```

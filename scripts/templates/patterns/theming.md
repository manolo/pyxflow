# Theming

PyXFlow uses Vaadin's Lumo theme system with support for dark mode,
custom stylesheets, and component theme variants.

## Color Scheme

```python
from pyxflow import AppShell, ColorScheme

@AppShell
@ColorScheme("dark")  # "dark" or "light"
class MainLayout(AppLayout):
    pass
```

## Custom Stylesheets

```python
from pyxflow import StyleSheet

@AppShell
@StyleSheet("lumo/lumo.css", "styles/custom.css")
class MainLayout(AppLayout):
    pass
```

CSS files go in `<app_dir>/static/` and are served automatically.

## Theme Variants

Every component has a Variant enum:

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

## Lumo CSS Variables

Common Lumo tokens:

```css
/* Spacing */
var(--lumo-space-xs)   /* 0.25rem */
var(--lumo-space-s)    /* 0.5rem */
var(--lumo-space-m)    /* 1rem */
var(--lumo-space-l)    /* 1.5rem */
var(--lumo-space-xl)   /* 2.5rem */

/* Colors */
var(--lumo-primary-color)
var(--lumo-error-color)
var(--lumo-success-color)
var(--lumo-contrast-5pct)

/* Typography */
var(--lumo-font-size-s)
var(--lumo-font-size-m)
var(--lumo-font-size-l)
```

## Size Utilities

```python
component.set_width("100%")
component.set_height("400px")
component.set_size_full()       # width=100%, height=100%
component.set_width_full()      # width=100%
component.set_height_full()     # height=100%
```

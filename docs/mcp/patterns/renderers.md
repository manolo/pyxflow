# Renderers

Renderers customize how Grid cells, ComboBox items, and other components display data.

## LitRenderer (Recommended)

HTML templates with data binding using Lit syntax:

```python
from pyxflow.components import Grid, LitRenderer

grid = Grid()

# Simple property rendering
grid.add_column("name", header="Name")

# Custom template
grid.add_column(
    LitRenderer('<span style="font-weight:bold">${item.name}</span>'),
    header="Name"
).set_auto_width(True)

# Multi-property template
grid.add_column(
    LitRenderer('''
        <div>
            <strong>${item.firstName} ${item.lastName}</strong>
            <br><small>${item.email}</small>
        </div>
    '''),
    header="Contact"
)
```

## LitRenderer with Events

```python
# Button in grid cell
grid.add_column(
    LitRenderer(
        '<vaadin-button @click="${handleClick}">Edit</vaadin-button>',
        handle_click=lambda item: edit_person(item)
    ),
    header="Actions"
)

# Multiple handlers
grid.add_column(
    LitRenderer(
        '''<vaadin-button @click="${handleEdit}">Edit</vaadin-button>
           <vaadin-button theme="error" @click="${handleDelete}">Delete</vaadin-button>''',
        handle_edit=lambda item: edit(item),
        handle_delete=lambda item: delete(item),
    ),
    header="Actions"
)
```

## TextRenderer

Simple text transformation:

```python
from pyxflow.components import TextRenderer

grid.add_column(
    TextRenderer(lambda item: f"{item['firstName']} {item['lastName']}"),
    header="Full Name"
)

grid.add_column(
    TextRenderer(lambda item: "Yes" if item.get("active") else "No"),
    header="Active"
)
```

## ComponentRenderer

Server-side components in grid cells:

```python
from pyxflow.components import ComponentRenderer, Button, Icon

grid.add_column(
    ComponentRenderer(lambda item: Button(
        Icon("vaadin:edit"),
        lambda e: edit_item(item)
    )),
    header="Actions"
)
```

## ComboBox Renderer

```python
combo = ComboBox("Country")
combo.set_items("US", "CA", "UK")
combo.set_renderer(
    LitRenderer('<span>${item.label} (${item.value})</span>')
)
```

## Grid Column with Auto Properties

```python
# Automatic: uses item["name"] or item.name
grid.add_column("name", header="Name")

# Equivalent to:
grid.add_column(
    TextRenderer(lambda item: str(item.get("name", ""))),
    header="Name"
)
```

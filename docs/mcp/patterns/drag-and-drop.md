# Drag and Drop

HTML5 Drag and Drop via `DragSource` and `DropTarget` mixins.
Works on any component -- configure via static factory or mixin inheritance.

## DragSource - Make a Component Draggable

```python
from pyxflow.components import Span, Div, DragSource, EffectAllowed

item = Span("Drag me")
DragSource.configure(item)
item.set_drag_data({"id": 42, "label": "Item A"})
item.set_effect_allowed(EffectAllowed.MOVE)

item.add_drag_start_listener(lambda e: print("Drag started"))
item.add_drag_end_listener(lambda e: print(f"Success: {e.is_successful()}"))
```

## DropTarget - Make a Component Accept Drops

```python
from pyxflow.components import VerticalLayout, DropTarget, DropEffect

drop_zone = VerticalLayout()
DropTarget.configure(drop_zone)
drop_zone.set_drop_effect(DropEffect.MOVE)

def on_drop(event):
    data = event.get_drag_data()           # Server-side drag data
    source = event.get_drag_source_component()  # The dragged component
    print(f"Dropped: {data}")

drop_zone.add_drop_listener(on_drop)
```

## Custom Drag Image (Ghost)

Each draggable can use a custom element as the drag ghost.
The image element must be in the DOM (even if positioned off-screen).

```python
# Create the ghost element (hidden off-screen)
ghost = Span("EMOJI")
ghost.add_class_name("my-drag-ghost")  # position: fixed; top: -100px;

# Each draggable item gets its own ghost
item.set_drag_image(ghost, 20, 20)  # element, offsetX, offsetY
```

**Important:** The drag ghost is captured as a bitmap snapshot by the browser
at the instant the drag starts. Any server-side updates to the ghost element
(e.g., changing its text in a `drag_start_listener`) arrive too late --
the browser already took the snapshot. Use one ghost per item with pre-set content.

## Complete Example - Two Baskets

```python
from pyxflow.components import (
    HorizontalLayout, VerticalLayout, Div, Span, NativeLabel,
    DragSource, DropTarget, DropEffect,
)

@Route("dnd")
class DndView(VerticalLayout):
    def __init__(self):
        self.left = ["Apple", "Banana"]
        self.right = ["Mango"]

        self.left_box = VerticalLayout()
        self.right_box = VerticalLayout()
        for box in (self.left_box, self.right_box):
            DropTarget.configure(box)
            box.set_drop_effect(DropEffect.MOVE)
            box.add_drop_listener(self.on_drop)

        # Hidden container for drag ghost images
        self.ghosts = Div()
        self.ghosts.add_class_name("offscreen")

        self.rebuild()
        self.add(HorizontalLayout(self.ghosts, self.left_box, self.right_box))

    def make_item(self, fruit):
        item = Span(fruit)
        DragSource.configure(item)
        item.set_drag_data(fruit)
        # Per-item ghost (content set at creation, not on drag)
        ghost = Span(fruit)
        self.ghosts.add(ghost)
        item.set_drag_image(ghost, 10, 10)
        return item

    def rebuild(self):
        for box, items in ((self.left_box, self.left), (self.right_box, self.right)):
            box.remove_all()
            for fruit in items:
                box.add(self.make_item(fruit))

    def on_drop(self, event):
        fruit = event.get_drag_data()
        target = event.get_component()
        if fruit in self.left and target is self.right_box:
            self.left.remove(fruit)
            self.right.append(fruit)
        elif fruit in self.right and target is self.left_box:
            self.right.remove(fruit)
            self.left.append(fruit)
        self.rebuild()
```

## As Mixin (Alternative)

```python
from pyxflow.components import Div, DragSource, DropTarget

class DraggableCard(Div, DragSource):
    def __init__(self, label):
        super().__init__(label)
        self.set_draggable(True)
        self.set_drag_data(label)

class DropZone(VerticalLayout, DropTarget):
    def __init__(self):
        super().__init__()
        self.set_active(True)
        self.set_drop_effect(DropEffect.MOVE)
```

## API Reference

### DragSource
| Method | Description |
|--------|-------------|
| `DragSource.configure(component, draggable=True)` | Static factory -- adds drag methods to any component |
| `set_draggable(bool)` | Enable/disable dragging |
| `set_drag_data(data)` | Server-side data carried during drag (not sent to client) |
| `set_effect_allowed(EffectAllowed)` | MOVE, COPY, LINK, ALL, etc. |
| `set_drag_image(component, x, y)` | Custom drag ghost element |
| `add_drag_start_listener(fn)` | Called when drag begins |
| `add_drag_end_listener(fn)` | Called when drag ends (`event.is_successful()`) |

### DropTarget
| Method | Description |
|--------|-------------|
| `DropTarget.configure(component, active=True)` | Static factory -- adds drop methods to any component |
| `set_active(bool)` | Enable/disable drop acceptance |
| `set_drop_effect(DropEffect)` | MOVE, COPY, LINK, NONE |
| `add_drop_listener(fn)` | Called on drop (`event.get_drag_data()`, `event.get_drag_source_component()`) |

### Enums
```python
from pyxflow.components import EffectAllowed, DropEffect

EffectAllowed.MOVE / COPY / LINK / ALL / COPY_MOVE / ...
DropEffect.MOVE / COPY / LINK / NONE
```

## Pitfalls

1. **Ghost element must be in DOM** -- `set_drag_image` requires the element to be
   attached (even if hidden). Add it to a container before calling `set_drag_image`.
2. **Attach order matters** -- If the ghost attaches after the drag source in the
   tree, use the framework's deferred flush (automatic since v0.5.4).
3. **No dynamic ghost text** -- Don't update ghost content in `drag_start_listener`;
   the browser captures the snapshot before the server response arrives.
4. **Drag data is server-side only** -- `set_drag_data()` stores data in Python memory,
   not in the browser's `dataTransfer`. It's retrieved via `event.get_drag_data()` on drop.

# Data Binding with Binder

Binder connects form fields to a data model with validation.

## Basic Usage

```python
from pyxflow.components import TextField, EmailField, Checkbox
from pyxflow.data import Binder, ValidationError

class Person:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.active = False

# Create fields
name_field = TextField("Name")
email_field = EmailField("Email")
active_field = Checkbox("Active")

# Create binder and bind fields
binder = Binder(Person)
binder.for_field(name_field).as_required("Name is required").bind(
    lambda p: p.name, lambda p, v: setattr(p, "name", v))
binder.for_field(email_field).as_required("Email is required").bind(
    lambda p: p.email, lambda p, v: setattr(p, "email", v))
binder.for_field(active_field).bind(
    lambda p: p.active, lambda p, v: setattr(p, "active", v))

# Read from model to fields
person = Person()
person.name = "Alice"
binder.read_bean(person)

# Write from fields to model (validates first)
try:
    binder.write_bean(person)
except ValidationError:
    print("Validation failed")
```

## Validators

```python
from pyxflow.data import Binder

binder.for_field(email_field) \
    .as_required("Email required") \
    .with_validator(lambda v: "@" in v, "Must be valid email") \
    .bind(lambda p: p.email, lambda p, v: setattr(p, "email", v))

binder.for_field(age_field) \
    .with_validator(lambda v: v >= 0, "Age must be positive") \
    .with_validator(lambda v: v <= 150, "Age must be <= 150") \
    .bind(lambda p: p.age, lambda p, v: setattr(p, "age", v))
```

## Built-in Validators

```python
from pyxflow.data import required, min_length, max_length, email, pattern, positive, value_range

binder.for_field(field).with_validator(required("Required")).bind(...)
binder.for_field(field).with_validator(min_length(3, "Min 3 chars")).bind(...)
binder.for_field(field).with_validator(email("Invalid email")).bind(...)
binder.for_field(field).with_validator(value_range(1, 100, "1-100")).bind(...)
```

## Converters

```python
from pyxflow.data import Binder, string_to_int

binder.for_field(number_field) \
    .with_converter(string_to_int) \
    .bind(lambda p: p.count, lambda p, v: setattr(p, "count", v))
```

## Status Change Listener

```python
# Monitor dirty state (e.g. to enable/disable save button)
def on_status_change():
    save_btn.set_enabled(binder.is_dirty())

binder.add_status_change_listener(on_status_change)
```

## Clear Form

```python
binder.read_bean(None)  # Clears all fields
```

## Grid Editor with Binder

```python
editor = grid.get_editor()
editor.set_binder(binder)
editor.set_buffered(True)  # Save/Cancel buttons

grid.add_item_double_click_listener(lambda e: editor.edit_item(e["item"]))
editor.add_save_listener(lambda e: Notification.show(f"Saved {e.item['name']}"))
```

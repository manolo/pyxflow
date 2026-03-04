# Field Validation

PyXFlow fields support both client-side and server-side validation.

## Required Fields

```python
from pyxflow.components import TextField

name = TextField("Name")
name.set_required_indicator_visible(True)  # Shows * indicator

# With Binder (recommended)
binder.for_field(name).as_required("Name is required").bind(...)
```

## Error Messages

```python
field = TextField("Email")
field.set_error_message("Please enter a valid email")
field.set_invalid(True)  # Shows error state + message
```

## Pattern Validation (Client-Side)

```python
# Regex pattern validation
email = TextField("Email")
email.set_pattern(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

# Restrict allowed characters (blocks invalid input)
phone = TextField("Phone")
phone.set_allowed_char_pattern(r"[0-9+\-() ]")
```

## Server-Side Validation with Binder

```python
from pyxflow.data import Binder

binder = Binder(Person)

# Single validator
binder.for_field(name_field) \
    .as_required("Required") \
    .with_validator(lambda v: len(v) >= 2, "Min 2 characters") \
    .bind(lambda p: p.name, lambda p, v: setattr(p, "name", v))

# Multiple validators (chained)
binder.for_field(age_field) \
    .with_validator(lambda v: v is not None, "Required") \
    .with_validator(lambda v: v >= 0, "Must be positive") \
    .with_validator(lambda v: v <= 150, "Must be <= 150") \
    .bind(lambda p: p.age, lambda p, v: setattr(p, "age", v))
```

## Built-In Validators

```python
from pyxflow.data import required, min_length, max_length, email, pattern, positive, value_range

binder.for_field(f).with_validator(required("Required"))
binder.for_field(f).with_validator(min_length(3, "Too short"))
binder.for_field(f).with_validator(max_length(100, "Too long"))
binder.for_field(f).with_validator(email("Invalid email"))
binder.for_field(f).with_validator(positive("Must be positive"))
binder.for_field(f).with_validator(value_range(1, 100, "Out of range"))
binder.for_field(f).with_validator(pattern(r"\d{5}", "Must be 5 digits"))
```

## Read-Only Fields

```python
field.set_read_only(True)  # Non-editable but visible
```

## Field Mixins

All input components inherit from these mixins:

- **HasReadOnly** (18 components): `set_read_only()`, `is_read_only()`
- **HasValidation** (15 components): `set_invalid()`, `is_invalid()`, `set_error_message()`, `get_error_message()`
- **HasRequired** (16 components): `set_required_indicator_visible()`, `is_required_indicator_visible()`

## Max/Min Length

```python
name = TextField("Name")
name.set_max_length(50)
name.set_min_length(2)
```

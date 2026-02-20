"""Binder — connects form fields to data objects."""

from __future__ import annotations

from typing import Callable, Generic, TypeVar

from vaadin.flow.data.converter import Converter
from vaadin.flow.data.result import Result, ValidationResult

T = TypeVar("T")  # Bean type


class ValidationError(Exception):
    """Raised when write_bean fails validation."""

    def __init__(self, results: list[ValidationResult]):
        self.results = results
        messages = [r.message for r in results if r.is_error]
        super().__init__("; ".join(messages))


class Binding:
    """A single field-to-property binding."""

    def __init__(self, field, getter: Callable, setter: Callable | None,
                 pre_validators: list[Callable], post_validators: list[Callable],
                 converter: Converter | None, required_validator: Callable | None):
        self._field = field
        self._getter = getter
        self._setter = setter
        self._pre_validators = pre_validators
        self._post_validators = post_validators
        self._converter = converter
        self._required_validator = required_validator

    @property
    def field(self):
        return self._field

    def clear(self):
        """Reset the field to its empty/default value."""
        field = self._field
        value = field.get_value()
        if isinstance(value, bool):
            field.set_value(False)
        elif isinstance(value, (int, float)):
            field.set_value(0)
        else:
            field.set_value("")

    def read(self, bean):
        """Read value from bean into field."""
        model_value = self._getter(bean)
        if self._converter:
            presentation_value = self._converter.to_presentation(model_value)
        else:
            presentation_value = model_value
        self._field.set_value(presentation_value)

    def validate(self) -> list[ValidationResult]:
        """Validate the current field value. Sets invalid/errorMessage on field."""
        results = []
        presentation_value = self._field.get_value()

        # Required validator first
        if self._required_validator:
            result = self._required_validator(presentation_value)
            if result.is_error:
                results.append(result)
                self._set_field_error(result.message)
                return results

        # Pre-conversion validators
        for validator in self._pre_validators:
            result = validator(presentation_value)
            if result.is_error:
                results.append(result)
                self._set_field_error(result.message)
                return results

        # Converter
        if self._converter:
            conv_result = self._converter.to_model(presentation_value)
            if conv_result.is_error:
                results.append(ValidationResult.error(conv_result.message))
                self._set_field_error(conv_result.message)
                return results
            model_value = conv_result.value
        else:
            model_value = presentation_value

        # Post-conversion validators
        for validator in self._post_validators:
            result = validator(model_value)
            if result.is_error:
                results.append(result)
                self._set_field_error(result.message)
                return results

        self._clear_field_error()
        return results

    def write(self, bean) -> list[ValidationResult]:
        """Validate and write field value to bean. Returns error results."""
        results = self.validate()
        if results:
            return results

        if self._setter is None:
            return []

        presentation_value = self._field.get_value()
        if self._converter:
            conv_result = self._converter.to_model(presentation_value)
            model_value = conv_result.value
        else:
            model_value = presentation_value

        self._setter(bean, model_value)
        return []

    def _set_field_error(self, message: str):
        """Set invalid state on the field."""
        if self._field._element:
            self._field.element.set_property("invalid", True)
            self._field.element.set_property("errorMessage", message)

    def _clear_field_error(self):
        """Clear invalid state on the field."""
        if self._field._element:
            self._field.element.set_property("invalid", False)
            self._field.element.set_property("errorMessage", "")


class BindingBuilder:
    """Fluent builder for creating a Binding."""

    def __init__(self, binder: Binder, field):
        self._binder = binder
        self._field = field
        self._pre_validators: list[Callable] = []
        self._post_validators: list[Callable] = []
        self._converter: Converter | None = None
        self._required_validator: Callable | None = None

    def as_required(self, message: str = "This field is required") -> BindingBuilder:
        """Mark this binding as required."""
        from vaadin.flow.data.validator import required
        self._required_validator = required(message)
        if hasattr(self._field, "set_required_indicator_visible"):
            self._field.set_required_indicator_visible(True)
        return self

    def with_validator(self, validator_or_predicate, message: str | None = None) -> BindingBuilder:
        """Add a validator.

        Can be called with:
        - A Validator (callable returning ValidationResult)
        - A predicate + message (callable returning bool + error message)
        """
        if message is not None:
            # predicate + message form
            predicate = validator_or_predicate
            def validator(value) -> ValidationResult:
                if not predicate(value):
                    return ValidationResult.error(message)
                return ValidationResult.ok()
        else:
            validator = validator_or_predicate

        if self._converter is None:
            self._pre_validators.append(validator)
        else:
            self._post_validators.append(validator)
        return self

    def with_converter(self, converter: Converter) -> BindingBuilder:
        """Set the converter for this binding."""
        self._converter = converter
        return self

    def bind(self, getter: Callable, setter: Callable | None = None) -> Binding:
        """Finalize the binding with getter and optional setter.

        Args:
            getter: Callable that takes a bean and returns the property value.
            setter: Callable that takes (bean, value) and sets the property.
                    If None, the binding is read-only.
        """
        binding = Binding(
            self._field, getter, setter,
            self._pre_validators, self._post_validators,
            self._converter, self._required_validator,
        )
        self._binder._add_binding(binding)
        return binding


class Binder(Generic[T]):
    """Binds form fields to a data object (bean)."""

    def __init__(self, bean_type: type[T] | None = None):
        self._bean_type = bean_type
        self._bindings: list[Binding] = []
        self._bean: T | None = None
        self._bean_validators: list[Callable] = []
        self._status_listeners: list[Callable] = []
        self._change_registrations: list = []
        self._snapshot: dict | None = None

    def for_field(self, field) -> BindingBuilder:
        """Start building a binding for the given field."""
        return BindingBuilder(self, field)

    def _add_binding(self, binding: Binding):
        """Register a binding (called by BindingBuilder.bind)."""
        self._bindings.append(binding)
        # If a bean is set, populate the field
        if self._bean is not None:
            binding.read(self._bean)
        # Register value change listener for auto-write and status notification
        binding.field.add_value_change_listener(
            lambda e: self._on_field_change(binding)
        )

    def _on_field_change(self, binding: Binding):
        """Handle field value change."""
        # Auto-write if bean is set
        if self._bean is not None:
            binding.write(self._bean)
        # Notify status listeners
        for listener in self._status_listeners:
            listener()

    def read_bean(self, bean: T | None):
        """Populate all fields from the bean, or clear them if None."""
        if bean is None:
            for binding in self._bindings:
                binding.clear()
        else:
            for binding in self._bindings:
                binding.read(bean)
        self._take_snapshot()

    def write_bean(self, bean: T):
        """Write all field values to the bean. Raises ValidationError on failure."""
        all_errors = []
        for binding in self._bindings:
            errors = binding.validate()
            all_errors.extend(errors)

        if all_errors:
            raise ValidationError(all_errors)

        # Field-level validation passed — write values to bean
        for binding in self._bindings:
            binding.write(bean)

        # Bean-level validators (run after writing so bean has current values)
        bean_errors = []
        for validator in self._bean_validators:
            result = validator(bean, self)
            if result.is_error:
                bean_errors.append(result)

        if bean_errors:
            raise ValidationError(bean_errors)

    def write_bean_if_valid(self, bean: T) -> bool:
        """Write all field values to the bean if valid. Returns True on success."""
        try:
            self.write_bean(bean)
            return True
        except ValidationError:
            return False

    def set_bean(self, bean: T | None):
        """Set the bean for automatic two-way binding.

        Populates fields immediately and auto-writes on changes.
        """
        self._bean = bean
        if bean is not None:
            self.read_bean(bean)
        else:
            self._snapshot = None

    def get_bean(self) -> T | None:
        """Get the currently bound bean."""
        return self._bean

    def _take_snapshot(self):
        """Capture current field values for dirty comparison."""
        self._snapshot = {i: b.field.get_value() for i, b in enumerate(self._bindings)}

    def is_dirty(self) -> bool:
        """Check if any field value differs from the last read_bean snapshot."""
        if self._snapshot is None:
            return False
        for i, binding in enumerate(self._bindings):
            if i in self._snapshot and binding.field.get_value() != self._snapshot[i]:
                return True
        return False

    def validate(self) -> list[ValidationResult]:
        """Validate all bindings. Returns list of error results."""
        all_errors = []
        for binding in self._bindings:
            errors = binding.validate()
            all_errors.extend(errors)
        return all_errors

    def is_valid(self) -> bool:
        """Check if all bindings are currently valid."""
        return len(self.validate()) == 0

    def with_validator(self, predicate: Callable, message: str) -> Binder:
        """Add a bean-level (cross-field) validator.

        The predicate receives (bean, binder) and should return True if valid.
        """
        def validator(bean, binder) -> ValidationResult:
            if not predicate(bean, binder):
                return ValidationResult.error(message)
            return ValidationResult.ok()
        self._bean_validators.append(validator)
        return self

    def bind_instance_fields(self, owner):
        """Automatically bind fields of the owner to bean properties by name.

        Matches owner instance attributes that are form fields (have set_value/
        get_value) to bean properties with the same name — like Java's
        ``binder.bindInstanceFields(this)``.
        """
        if self._bean_type is None:
            raise ValueError("bean_type required for bind_instance_fields")

        # Get bean property names
        dc_fields = getattr(self._bean_type, "__dataclass_fields__", None)
        if dc_fields is not None:
            bean_props = set(dc_fields.keys())
        elif hasattr(self._bean_type, "__annotations__"):
            bean_props = set(self._bean_type.__annotations__.keys())
        else:
            bean_props = set()

        for attr_name in list(vars(owner)):
            if attr_name.startswith("_") or attr_name not in bean_props:
                continue
            field = getattr(owner, attr_name)
            if hasattr(field, "set_value") and hasattr(field, "get_value"):
                name = attr_name
                self.for_field(field).bind(
                    lambda bean, n=name: getattr(bean, n),
                    lambda bean, value, n=name: setattr(bean, n, value),
                )

    def remove_binding(self, binding_or_field) -> None:
        """Remove a binding by Binding instance or by field.

        Args:
            binding_or_field: A Binding instance, or a field whose binding to remove.
        """
        if isinstance(binding_or_field, Binding):
            binding = binding_or_field
        else:
            binding = None
            for b in self._bindings:
                if b.field is binding_or_field:
                    binding = b
                    break
        if binding and binding in self._bindings:
            self._bindings.remove(binding)

    def remove_bean(self) -> None:
        """Remove the currently set bean (equivalent to set_bean(None))."""
        self.set_bean(None)

    def add_status_change_listener(self, listener: Callable):
        """Add a listener notified when any field value changes."""
        self._status_listeners.append(listener)

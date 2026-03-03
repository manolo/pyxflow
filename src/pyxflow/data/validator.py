"""Validators for data binding."""

from __future__ import annotations

import re
from typing import Callable, TypeVar

from pyxflow.data.result import ValidationResult

T = TypeVar("T")

# Validator is a callable that takes a value and returns a ValidationResult
Validator = Callable[[T], ValidationResult]


def required(message: str = "This field is required") -> Validator:
    """Validator that rejects empty/None values."""
    def validate(value) -> ValidationResult:
        if value is None or (isinstance(value, str) and not value.strip()):
            return ValidationResult.error(message)
        return ValidationResult.ok()
    return validate


def min_length(length: int, message: str | None = None) -> Validator:
    """Validator that requires a minimum string length."""
    msg = message or f"Must be at least {length} characters"
    def validate(value) -> ValidationResult:
        if isinstance(value, str) and len(value) < length:
            return ValidationResult.error(msg)
        return ValidationResult.ok()
    return validate


def max_length(length: int, message: str | None = None) -> Validator:
    """Validator that enforces a maximum string length."""
    msg = message or f"Must be at most {length} characters"
    def validate(value) -> ValidationResult:
        if isinstance(value, str) and len(value) > length:
            return ValidationResult.error(msg)
        return ValidationResult.ok()
    return validate


def pattern(regex: str, message: str = "Invalid format") -> Validator:
    """Validator that checks a value against a regex pattern."""
    compiled = re.compile(regex)
    def validate(value) -> ValidationResult:
        if isinstance(value, str) and not compiled.fullmatch(value):
            return ValidationResult.error(message)
        return ValidationResult.ok()
    return validate


def value_range(min_val: float | None = None, max_val: float | None = None,
                message: str | None = None) -> Validator:
    """Validator that checks a numeric value is within a range."""
    def validate(value) -> ValidationResult:
        if value is None:
            return ValidationResult.ok()
        if min_val is not None and value < min_val:
            msg = message or f"Must be at least {min_val}"
            return ValidationResult.error(msg)
        if max_val is not None and value > max_val:
            msg = message or f"Must be at most {max_val}"
            return ValidationResult.error(msg)
        return ValidationResult.ok()
    return validate


def positive(message: str = "Must be positive") -> Validator:
    """Validator that checks a numeric value is positive (> 0)."""
    def validate(value) -> ValidationResult:
        if value is not None and value <= 0:
            return ValidationResult.error(message)
        return ValidationResult.ok()
    return validate


_EMAIL_RE = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")


def email(message: str = "Invalid email address") -> Validator:
    """Validator that checks for a valid email format."""
    def validate(value) -> ValidationResult:
        if isinstance(value, str) and value and not _EMAIL_RE.fullmatch(value):
            return ValidationResult.error(message)
        return ValidationResult.ok()
    return validate

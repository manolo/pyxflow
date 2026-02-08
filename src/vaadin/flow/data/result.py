"""Result types for validation and conversion."""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Result(Generic[T]):
    """Result of a conversion: either ok(value) or error(message)."""

    __slots__ = ("_value", "_message", "_ok")

    def __init__(self, value: T | None, message: str | None, ok: bool):
        self._value = value
        self._message = message
        self._ok = ok

    @staticmethod
    def ok(value: T) -> Result[T]:
        return Result(value, None, True)

    @staticmethod
    def error(message: str) -> Result:
        return Result(None, message, False)

    @property
    def is_ok(self) -> bool:
        return self._ok

    @property
    def is_error(self) -> bool:
        return not self._ok

    @property
    def value(self) -> T:
        if not self._ok:
            raise ValueError("Cannot get value from error result")
        return self._value

    @property
    def message(self) -> str:
        if self._ok:
            raise ValueError("Cannot get message from ok result")
        return self._message


class ValidationResult:
    """Result of a validation: either ok() or error(message)."""

    __slots__ = ("_message", "_ok")

    def __init__(self, message: str | None, ok: bool):
        self._message = message
        self._ok = ok

    @staticmethod
    def ok() -> ValidationResult:
        return ValidationResult(None, True)

    @staticmethod
    def error(message: str) -> ValidationResult:
        return ValidationResult(message, False)

    @property
    def is_ok(self) -> bool:
        return self._ok

    @property
    def is_error(self) -> bool:
        return not self._ok

    @property
    def message(self) -> str:
        if self._ok:
            raise ValueError("Cannot get message from ok result")
        return self._message

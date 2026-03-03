"""Converters for data binding."""

from __future__ import annotations

from typing import Callable, Generic, TypeVar

from pyxflow.data.result import Result

P = TypeVar("P")  # Presentation type
M = TypeVar("M")  # Model type


class Converter(Generic[P, M]):
    """Converts between presentation type P and model type M."""

    def __init__(self, to_model: Callable[[P], Result[M]],
                 to_presentation: Callable[[M], P]):
        self._to_model = to_model
        self._to_presentation = to_presentation

    def to_model(self, value: P) -> Result[M]:
        return self._to_model(value)

    def to_presentation(self, value: M) -> P:
        return self._to_presentation(value)


def string_to_int(error_message: str = "Not a valid integer") -> Converter[str, int]:
    """Converter from string to int."""
    def to_model(value: str) -> Result[int]:
        if value is None or (isinstance(value, str) and not value.strip()):
            return Result.ok(0)
        try:
            return Result.ok(int(value))
        except (ValueError, TypeError):
            return Result.error(error_message)

    return Converter(to_model, lambda v: str(v) if v is not None else "")


def string_to_float(error_message: str = "Not a valid number") -> Converter[str, float]:
    """Converter from string to float."""
    def to_model(value: str) -> Result[float]:
        if value is None or (isinstance(value, str) and not value.strip()):
            return Result.ok(0.0)
        try:
            return Result.ok(float(value))
        except (ValueError, TypeError):
            return Result.error(error_message)

    return Converter(to_model, lambda v: str(v) if v is not None else "")

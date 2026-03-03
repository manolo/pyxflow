"""ProgressBar component."""

from pyxflow.core.component import Component
from pyxflow.components.constants import ProgressBarVariant


class ProgressBar(Component):
    """A progress bar component.

    Shows the amount of completion of a task or process.
    The progress can be determinate or indeterminate.
    """

    _v_fqcn = "com.vaadin.flow.component.progressbar.ProgressBar"
    _tag = "vaadin-progress-bar"

    def __init__(self):
        super().__init__()
        self._value = 0.0
        self._min = 0.0
        self._max = 1.0
        self._indeterminate = False

    def _attach(self, tree):
        super()._attach(tree)
        self.element.set_property("min", self._min)
        self.element.set_property("max", self._max)
        self.element.set_property("value", self._value)
        if self._indeterminate:
            self.element.set_property("indeterminate", True)

    def get_value(self) -> float:
        """Get the current value."""
        return self._value

    def set_value(self, value: float):
        """Set the value (between min and max)."""
        self._value = value
        if self._element:
            self.element.set_property("value", value)

    def get_min(self) -> float:
        """Get the minimum value."""
        return self._min

    def set_min(self, min_value: float):
        """Set the minimum value."""
        self._min = min_value
        if self._element:
            self.element.set_property("min", min_value)

    def get_max(self) -> float:
        """Get the maximum value."""
        return self._max

    def set_max(self, max_value: float):
        """Set the maximum value."""
        self._max = max_value
        if self._element:
            self.element.set_property("max", max_value)

    def is_indeterminate(self) -> bool:
        """Check if the progress bar is indeterminate."""
        return self._indeterminate

    def set_indeterminate(self, indeterminate: bool):
        """Set whether the progress bar is indeterminate.

        An indeterminate progress bar shows that progress is ongoing
        but can't be computed.
        """
        self._indeterminate = indeterminate
        if self._element:
            self.element.set_property("indeterminate", indeterminate)

    def add_theme_variants(self, *variants: ProgressBarVariant):
        """Add theme variants to the progress bar."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: ProgressBarVariant):
        """Remove theme variants from the progress bar."""
        self.remove_theme_name(*variants)

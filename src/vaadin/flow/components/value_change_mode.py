"""ValueChangeMode enum for text field components."""

from enum import Enum


class ValueChangeMode(Enum):
    """Controls when a text field syncs its value to the server.

    EAGER — fires on every keystroke ("input" event)
    LAZY — fires after a debounce timeout ("input" event, behaves like EAGER for now)
    TIMEOUT — fires after a timeout ("input" event, behaves like EAGER for now)
    ON_BLUR — fires when the field loses focus ("blur" event)
    ON_CHANGE — fires on change event (default, "change" event)
    """
    EAGER = "eager"
    LAZY = "lazy"
    TIMEOUT = "timeout"
    ON_BLUR = "on_blur"
    ON_CHANGE = "on_change"

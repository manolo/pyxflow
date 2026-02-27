"""Tests for 7 bug fixes found during UI testing.

Each test verifies a specific bug that was discovered via Playwright UI tests
and fixed in the Python port. The tests ensure these regressions don't recur.
"""

from pyflow.core.state_tree import StateTree
from pyflow.core.state_node import Feature
from pyflow.core.component import UI


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_tree():
    """Create a StateTree and UI for attaching components."""
    tree = StateTree()
    ui = UI(tree)
    return tree, ui


def attach(component, tree, ui):
    """Attach a component to the tree with a UI reference."""
    component._ui = ui
    component._attach(tree)
    return component


# ---------------------------------------------------------------------------
# 1. Span.set_text() lazy creation
# ---------------------------------------------------------------------------

class TestSpanSetTextLazyCreation:
    """Span("") with empty text, then set_text("hello") after attach
    should create a text node lazily.

    Before fix, set_text() was a no-op when initialized with empty string
    because _text_node was None and _element was None during __init__,
    and after attach _text_node was still None (empty text skips creation).
    """

    def test_empty_span_then_set_text_after_attach(self):
        """set_text() after attach creates text node lazily."""
        from pyflow.components import Span

        tree, ui = make_tree()
        span = Span("")
        attach(span, tree, ui)

        # Clear initial changes (tag, etc.)
        tree.collect_changes()

        span.set_text("hello")
        changes = tree.collect_changes()

        # Should have a text node with "hello"
        text_change = next(
            (c for c in changes if c.get("feat") == Feature.TEXT_NODE and c.get("key") == "text"),
            None
        )
        assert text_change is not None, "set_text() after attach should create a text node"
        assert text_change["value"] == "hello"

    def test_empty_span_default_no_text_node(self):
        """Span("") should NOT create a text node on attach (no content)."""
        from pyflow.components import Span

        tree, ui = make_tree()
        span = Span("")
        attach(span, tree, ui)
        changes = tree.collect_changes()

        text_change = next(
            (c for c in changes if c.get("feat") == Feature.TEXT_NODE),
            None
        )
        assert text_change is None, "Empty span should not create text node on attach"

    def test_span_with_initial_text_creates_node_on_attach(self):
        """Span("hi") should create text node on attach normally."""
        from pyflow.components import Span

        tree, ui = make_tree()
        span = Span("hi")
        attach(span, tree, ui)
        changes = tree.collect_changes()

        text_change = next(
            (c for c in changes if c.get("feat") == Feature.TEXT_NODE and c.get("key") == "text"),
            None
        )
        assert text_change is not None
        assert text_change["value"] == "hi"

    def test_set_text_updates_existing_node(self):
        """set_text() on a span with existing text node should update it."""
        from pyflow.components import Span

        tree, ui = make_tree()
        span = Span("first")
        attach(span, tree, ui)
        tree.collect_changes()

        span.set_text("second")
        changes = tree.collect_changes()

        text_change = next(
            (c for c in changes if c.get("feat") == Feature.TEXT_NODE and c.get("key") == "text"),
            None
        )
        assert text_change is not None
        assert text_change["value"] == "second"

    def test_get_text_reflects_set_text(self):
        """get_text() should return the value set by set_text()."""
        from pyflow.components import Span

        tree, ui = make_tree()
        span = Span("")
        attach(span, tree, ui)
        span.set_text("hello")

        assert span.get_text() == "hello"


# ---------------------------------------------------------------------------
# 2. set_enabled(False) flush on attach
# ---------------------------------------------------------------------------

class TestSetEnabledFlushOnAttach:
    """Calling button.set_enabled(False) before attach, then attaching
    should produce a "disabled" attribute change.

    Before fix, the disabled attribute was never set because set_enabled()
    checked self._element (which is None before attach) and _attach() did
    not flush the pending enabled state.
    """

    def test_disabled_before_attach_produces_attribute(self):
        """set_enabled(False) before attach should set disabled attribute on attach."""
        from pyflow.components import Button

        tree, ui = make_tree()
        button = Button("Save")
        button.set_enabled(False)
        attach(button, tree, ui)
        changes = tree.collect_changes()

        disabled = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "disabled"),
            None
        )
        assert disabled is not None, "Disabled attribute should be set on attach"
        assert disabled["value"] == ""

    def test_enabled_before_attach_no_disabled_attribute(self):
        """A normally enabled button should NOT have a disabled attribute."""
        from pyflow.components import Button

        tree, ui = make_tree()
        button = Button("Save")
        # Default is enabled
        attach(button, tree, ui)
        changes = tree.collect_changes()

        disabled = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "disabled"),
            None
        )
        assert disabled is None, "Enabled button should not have disabled attribute"

    def test_enabled_state_tracked_internally(self):
        """is_enabled() should return False after set_enabled(False)."""
        from pyflow.components import Button

        button = Button("Save")
        button.set_enabled(False)
        assert button.is_enabled() is False

    def test_disabled_span_before_attach(self):
        """set_enabled(False) works on non-button components too."""
        from pyflow.components import Span

        tree, ui = make_tree()
        span = Span("text")
        span.set_enabled(False)
        attach(span, tree, ui)
        changes = tree.collect_changes()

        disabled = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "disabled"),
            None
        )
        assert disabled is not None, "Disabled attribute should be set on attach for Span too"


# ---------------------------------------------------------------------------
# 3. Button icon-only theme
# ---------------------------------------------------------------------------

class TestButtonIconOnlyTheme:
    """Button(icon=Icon("lumo:plus")) with no text should auto-add
    theme="icon" on attach.

    Before fix, no theme was set for icon-only buttons.
    """

    def test_icon_only_button_has_icon_theme(self):
        """Icon-only button should have theme='icon'."""
        from pyflow.components import Button, Icon

        tree, ui = make_tree()
        icon = Icon("lumo:plus")
        button = Button(icon=icon)
        attach(button, tree, ui)
        changes = tree.collect_changes()

        theme = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "theme"),
            None
        )
        assert theme is not None, "Icon-only button should have theme attribute"
        assert "icon" in theme["value"]

    def test_button_with_text_and_icon_no_icon_theme(self):
        """Button with both text and icon should NOT have theme='icon'."""
        from pyflow.components import Button, Icon

        tree, ui = make_tree()
        icon = Icon("lumo:plus")
        button = Button("Add", icon=icon)
        attach(button, tree, ui)
        changes = tree.collect_changes()

        theme = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "theme"),
            None
        )
        # Should either have no theme or not include "icon"
        if theme is not None:
            assert "icon" not in theme["value"]

    def test_icon_only_button_has_icon_element(self):
        """Icon-only button should have an icon child element."""
        from pyflow.components import Button, Icon

        tree, ui = make_tree()
        icon = Icon("lumo:plus")
        button = Button(icon=icon)
        attach(button, tree, ui)
        changes = tree.collect_changes()

        # Should have vaadin-icon tag
        icon_tag = next(
            (c for c in changes
             if c.get("key") == "tag" and c.get("value") == "vaadin-icon"),
            None
        )
        assert icon_tag is not None, "Icon element should be attached"


# ---------------------------------------------------------------------------
# 4. Button disableOnClick server-side disable
# ---------------------------------------------------------------------------

class TestButtonDisableOnClick:
    """When set_disable_on_click(True) is set and _handle_click({}) is called,
    the button should become disabled (_enabled = False and disabled attribute set).

    Before fix, the server never disabled the button on click.
    """

    def test_disable_on_click_disables_on_handle_click(self):
        """_handle_click should disable button when disableOnClick is True."""
        from pyflow.components import Button

        tree, ui = make_tree()
        button = Button("Submit")
        button.set_disable_on_click(True)
        attach(button, tree, ui)
        tree.collect_changes()  # Clear initial changes

        button._handle_click({})

        assert button.is_enabled() is False, "Button should be disabled after click"

        changes = tree.collect_changes()
        disabled = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "disabled"),
            None
        )
        assert disabled is not None, "Disabled attribute should be set after click"

    def test_disable_on_click_still_fires_listeners(self):
        """Click listeners should still fire even when disableOnClick is True."""
        from pyflow.components import Button

        tree, ui = make_tree()
        clicks = []
        button = Button("Submit", on_click=lambda e: clicks.append(e))
        button.set_disable_on_click(True)
        attach(button, tree, ui)

        button._handle_click({})

        assert len(clicks) == 1, "Click listener should have fired"
        assert button.is_enabled() is False

    def test_no_disable_without_flag(self):
        """Without disableOnClick, button should stay enabled after click."""
        from pyflow.components import Button

        tree, ui = make_tree()
        button = Button("Normal")
        attach(button, tree, ui)

        button._handle_click({})

        assert button.is_enabled() is True

    def test_programmatic_click_also_disables(self):
        """button.click() (programmatic) should also trigger disableOnClick."""
        from pyflow.components import Button

        tree, ui = make_tree()
        button = Button("Submit")
        button.set_disable_on_click(True)
        attach(button, tree, ui)

        button.click()

        assert button.is_enabled() is False


# ---------------------------------------------------------------------------
# 5. TextField maxlength flush on attach
# ---------------------------------------------------------------------------

class TestTextFieldMaxLengthFlush:
    """tf.set_max_length(5) before attach, then attaching should set
    the "maxlength" property to 5.

    Before fix, the property was lost because set_max_length() checked
    self._element (None before attach) and _attach() did not flush it.
    """

    def test_maxlength_set_before_attach(self):
        """set_max_length() before attach should be flushed on attach."""
        from pyflow.components import TextField

        tree, ui = make_tree()
        tf = TextField("Name")
        tf.set_max_length(5)
        attach(tf, tree, ui)
        changes = tree.collect_changes()

        maxlength = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP
             and c.get("key") == "maxlength"),
            None
        )
        assert maxlength is not None, "maxlength property should be set on attach"
        assert maxlength["value"] == 5

    def test_maxlength_set_after_attach(self):
        """set_max_length() after attach should also work."""
        from pyflow.components import TextField

        tree, ui = make_tree()
        tf = TextField("Name")
        attach(tf, tree, ui)
        tree.collect_changes()

        tf.set_max_length(10)
        changes = tree.collect_changes()

        maxlength = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_PROPERTY_MAP
             and c.get("key") == "maxlength"),
            None
        )
        assert maxlength is not None
        assert maxlength["value"] == 10

    def test_get_max_length(self):
        """get_max_length() should return the set value."""
        from pyflow.components import TextField

        tf = TextField("Name")
        tf.set_max_length(5)
        assert tf.get_max_length() == 5


# ---------------------------------------------------------------------------
# 6. TextField suffix flush on attach
# ---------------------------------------------------------------------------

class TestTextFieldSuffixFlush:
    """tf.set_suffix_component(Span("kg")) before attach, then attaching
    should add the suffix as a child with slot="suffix".

    Before fix, suffix was ignored on attach because _attach() did not
    flush the pending suffix component.
    """

    def test_suffix_set_before_attach(self):
        """set_suffix_component() before attach should be flushed on attach."""
        from pyflow.components import TextField, Span

        tree, ui = make_tree()
        tf = TextField("Weight")
        suffix = Span("kg")
        tf.set_suffix_component(suffix)
        attach(tf, tree, ui)
        changes = tree.collect_changes()

        # The suffix span should exist in changes with tag="span"
        span_tag = next(
            (c for c in changes
             if c.get("key") == "tag" and c.get("value") == "span"),
            None
        )
        assert span_tag is not None, "Suffix span should be attached"

        # The suffix should have slot="suffix" attribute
        suffix_slot = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "slot"
             and c.get("value") == "suffix"),
            None
        )
        assert suffix_slot is not None, "Suffix should have slot='suffix' attribute"

    def test_suffix_set_after_attach(self):
        """set_suffix_component() after attach should work immediately."""
        from pyflow.components import TextField, Span

        tree, ui = make_tree()
        tf = TextField("Weight")
        attach(tf, tree, ui)
        tree.collect_changes()

        suffix = Span("kg")
        tf.set_suffix_component(suffix)
        changes = tree.collect_changes()

        span_tag = next(
            (c for c in changes
             if c.get("key") == "tag" and c.get("value") == "span"),
            None
        )
        assert span_tag is not None

        suffix_slot = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "slot"
             and c.get("value") == "suffix"),
            None
        )
        assert suffix_slot is not None

    def test_prefix_set_before_attach(self):
        """set_prefix_component() before attach should also be flushed."""
        from pyflow.components import TextField
        from pyflow.components.icon import Icon

        tree, ui = make_tree()
        tf = TextField("Search")
        prefix = Icon("vaadin:search")
        tf.set_prefix_component(prefix)
        attach(tf, tree, ui)
        changes = tree.collect_changes()

        prefix_slot = next(
            (c for c in changes
             if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "slot"
             and c.get("value") == "prefix"),
            None
        )
        assert prefix_slot is not None, "Prefix should have slot='prefix' attribute"


# ---------------------------------------------------------------------------
# 7. _handle_change event_data includes value
# ---------------------------------------------------------------------------

class TestHandleChangeEventData:
    """When TextField._handle_change is called (simulating a change event
    from client), the listener should receive {"value": ..., "from_client": True}
    not raw empty event_data.

    Before fix, listeners got empty dict because _handle_change passed through
    the raw event_data without constructing a proper event object.
    """

    def test_handle_change_passes_value_to_listener(self):
        """_handle_change should pass {value, from_client} to listeners."""
        from pyflow.components import TextField

        tree, ui = make_tree()
        tf = TextField("Name")
        attach(tf, tree, ui)

        events = []
        tf.add_value_change_listener(lambda e: events.append(e))

        tf._handle_change({"value": "typed"})

        assert len(events) == 1
        assert events[0]["value"] == "typed"
        assert events[0]["from_client"] is True

    def test_handle_change_updates_internal_value(self):
        """_handle_change should update the internal _value."""
        from pyflow.components import TextField

        tree, ui = make_tree()
        tf = TextField("Name")
        attach(tf, tree, ui)

        tf._handle_change({"value": "new"})

        assert tf.get_value() == "new"

    def test_handle_change_with_empty_event_data(self):
        """_handle_change with empty dict should keep current value."""
        from pyflow.components import TextField

        tree, ui = make_tree()
        tf = TextField("Name")
        attach(tf, tree, ui)
        tf.set_value("initial")

        events = []
        tf.add_value_change_listener(lambda e: events.append(e))
        tf._handle_change({})

        # Should still fire listener with current value
        assert len(events) == 1
        assert events[0]["value"] == "initial"
        assert events[0]["from_client"] is True

    def test_handle_change_multiple_listeners(self):
        """All listeners should receive the proper event object."""
        from pyflow.components import TextField

        tree, ui = make_tree()
        tf = TextField("Name")
        attach(tf, tree, ui)

        events1, events2 = [], []
        tf.add_value_change_listener(lambda e: events1.append(e))
        tf.add_value_change_listener(lambda e: events2.append(e))

        tf._handle_change({"value": "hello"})

        assert len(events1) == 1
        assert len(events2) == 1
        assert events1[0]["from_client"] is True
        assert events2[0]["from_client"] is True

"""Core Component Tests."""

import pytest

from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


class TestVerticalLayout:
    """Test VerticalLayout component."""

    @pytest.fixture
    def attached_layout(self):
        """Create and attach a VerticalLayout."""
        from vaadin.flow.components import VerticalLayout
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        layout = VerticalLayout()
        layout._ui = ui
        layout._attach(tree)
        return layout, tree

    def test_tag_is_vertical_layout(self, attached_layout):
        layout, tree = attached_layout
        changes = tree.collect_changes()
        tag = next((c for c in changes if c.get("key") == "tag"), None)
        assert tag["value"] == "vaadin-vertical-layout"

    def test_default_width_100_percent(self, attached_layout):
        layout, tree = attached_layout
        changes = tree.collect_changes()
        width = next(
            (c for c in changes if c.get("feat") == Feature.INLINE_STYLE_PROPERTY_MAP and c.get("key") == "width"),
            None
        )
        assert width is not None
        assert width["value"] == "100%"

    def test_default_theme_padding_spacing(self, attached_layout):
        layout, tree = attached_layout
        changes = tree.collect_changes()
        theme = next(
            (c for c in changes if c.get("key") == "theme" and c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP),
            None
        )
        assert theme is not None
        assert "padding" in theme["value"]
        assert "spacing" in theme["value"]

    def test_add_child_creates_splice(self, attached_layout):
        from vaadin.flow.components import Span

        layout, tree = attached_layout
        tree.collect_changes()  # Clear initial changes

        span = Span("test")
        layout.add(span)

        changes = tree.collect_changes()
        splice = next((c for c in changes if c.get("type") == "splice"), None)
        assert splice is not None
        assert splice["feat"] == Feature.ELEMENT_CHILDREN_LIST


class TestHorizontalLayout:
    """Test HorizontalLayout component."""

    @pytest.fixture
    def attached_layout(self):
        from vaadin.flow.components import HorizontalLayout
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        layout = HorizontalLayout()
        layout._ui = ui
        layout._attach(tree)
        return layout, tree

    def test_tag_is_horizontal_layout(self, attached_layout):
        layout, tree = attached_layout
        changes = tree.collect_changes()
        tag = next((c for c in changes if c.get("key") == "tag"), None)
        assert tag["value"] == "vaadin-horizontal-layout"

    def test_set_margin_updates_theme(self, attached_layout):
        layout, tree = attached_layout
        tree.collect_changes()  # Clear

        layout.set_margin(True)

        changes = tree.collect_changes()
        theme = next((c for c in changes if c.get("key") == "theme"), None)
        assert theme is not None
        assert "margin" in theme["value"]


class TestTextField:
    """Test TextField component."""

    @pytest.fixture
    def attached_field(self):
        from vaadin.flow.components import TextField
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        field = TextField("Your name")
        field._ui = ui
        field._attach(tree)
        return field, tree

    def test_tag_is_text_field(self, attached_field):
        field, tree = attached_field
        changes = tree.collect_changes()
        tag = next((c for c in changes if c.get("key") == "tag"), None)
        assert tag["value"] == "vaadin-text-field"

    def test_has_label_property(self, attached_field):
        field, tree = attached_field
        changes = tree.collect_changes()
        label = next(
            (c for c in changes if c.get("key") == "label" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP),
            None
        )
        assert label is not None
        assert label["value"] == "Your name"

    def test_has_change_listener(self, attached_field):
        field, tree = attached_field
        changes = tree.collect_changes()
        listener = next(
            (c for c in changes if c.get("key") == "change" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None
        )
        assert listener is not None


class TestButton:
    """Test Button component."""

    @pytest.fixture
    def attached_button(self):
        from vaadin.flow.components import Button
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        button = Button("Say hello")
        button._ui = ui
        button._attach(tree)
        return button, tree

    def test_tag_is_button(self, attached_button):
        button, tree = attached_button
        changes = tree.collect_changes()
        tag = next((c for c in changes if c.get("key") == "tag"), None)
        assert tag["value"] == "vaadin-button"

    def test_has_click_listener(self, attached_button):
        button, tree = attached_button
        changes = tree.collect_changes()
        listener = next(
            (c for c in changes if c.get("key") == "click" and c.get("feat") == Feature.ELEMENT_LISTENER_MAP),
            None
        )
        assert listener is not None

    def test_has_text_node_child(self, attached_button):
        button, tree = attached_button
        changes = tree.collect_changes()
        text_node = next(
            (c for c in changes if c.get("feat") == Feature.TEXT_NODE and c.get("key") == "text"),
            None
        )
        assert text_node is not None
        assert text_node["value"] == "Say hello"


    def test_button_with_icon_has_both_children(self):
        """Button(text, icon) should have both text node and icon element."""
        from vaadin.flow.components import Button, Icon
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        icon = Icon("vaadin:plus")
        button = Button("Add", icon=icon)
        button._ui = ui
        button._attach(tree)
        changes = tree.collect_changes()

        # Text node exists
        text_node = next(
            (c for c in changes if c.get("feat") == Feature.TEXT_NODE and c.get("key") == "text"),
            None
        )
        assert text_node is not None
        assert text_node["value"] == "Add"

        # Icon has slot="prefix"
        icon_slot = next(
            (c for c in changes if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "slot" and c.get("value") == "prefix"),
            None
        )
        assert icon_slot is not None

    def test_button_icon_after_text(self):
        """set_icon_after_text(True) should set slot='suffix' on icon."""
        from vaadin.flow.components import Button, Icon
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        icon = Icon("vaadin:arrow-right")
        button = Button("Next", icon=icon)
        button.set_icon_after_text(True)
        button._ui = ui
        button._attach(tree)
        changes = tree.collect_changes()

        icon_slot = next(
            (c for c in changes if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "slot" and c.get("value") == "suffix"),
            None
        )
        assert icon_slot is not None

    def test_button_icon_after_text_toggle(self):
        """Toggling icon_after_text on attached button updates slot attribute."""
        from vaadin.flow.components import Button, Icon
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        icon = Icon("vaadin:plus")
        button = Button("Add", icon=icon)
        button._ui = ui
        button._attach(tree)
        tree.collect_changes()  # flush

        button.set_icon_after_text(True)
        changes = tree.collect_changes()
        slot_change = next(
            (c for c in changes if c.get("key") == "slot" and c.get("value") == "suffix"),
            None
        )
        assert slot_change is not None

        button.set_icon_after_text(False)
        changes = tree.collect_changes()
        slot_change = next(
            (c for c in changes if c.get("key") == "slot" and c.get("value") == "prefix"),
            None
        )
        assert slot_change is not None

    def test_button_on_click_constructor(self):
        """Button(on_click=fn) should register the click listener."""
        from vaadin.flow.components import Button
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        clicked = []
        button = Button("Click me", on_click=lambda e: clicked.append(True))
        button._ui = ui
        button._attach(tree)

        button._handle_click({})
        assert len(clicked) == 1

    def test_button_icon_as_second_positional(self):
        """Button("text", Icon(...)) should detect Icon and not treat it as on_click."""
        from vaadin.flow.components import Button, Icon
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        button = Button("Add", Icon("vaadin:plus"))
        button._ui = ui
        button._attach(tree)
        changes = tree.collect_changes()

        # Icon should be attached with slot="prefix"
        icon_slot = next(
            (c for c in changes if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "slot" and c.get("value") == "prefix"),
            None
        )
        assert icon_slot is not None
        # No click listeners (Icon was not mistaken for on_click)
        assert len(button._click_listeners) == 0

    def test_button_icon_as_first_positional(self):
        """Button(Icon(...)) should detect Icon as first arg."""
        from vaadin.flow.components import Button, Icon
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        button = Button(Icon("vaadin:trash"))
        button._ui = ui
        button._attach(tree)
        changes = tree.collect_changes()

        assert button._text == ""
        icon_slot = next(
            (c for c in changes if c.get("feat") == Feature.ELEMENT_ATTRIBUTE_MAP
             and c.get("key") == "slot" and c.get("value") == "prefix"),
            None
        )
        assert icon_slot is not None

    def test_button_icon_first_with_click(self):
        """Button(Icon(...), lambda e: ...) should detect both."""
        from vaadin.flow.components import Button, Icon
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        clicked = []
        button = Button(Icon("vaadin:trash"), lambda e: clicked.append(True))
        button._ui = ui
        button._attach(tree)

        assert button._text == ""
        assert len(button._click_listeners) == 1
        button._handle_click({})
        assert len(clicked) == 1


class TestSpan:
    """Test Span component."""

    @pytest.fixture
    def attached_span(self):
        from vaadin.flow.components import Span
        from vaadin.flow.core.component import UI

        tree = StateTree()
        ui = UI(tree)
        span = Span("Hello World")
        span._ui = ui
        span._attach(tree)
        return span, tree

    def test_tag_is_span(self, attached_span):
        span, tree = attached_span
        changes = tree.collect_changes()
        tag = next((c for c in changes if c.get("key") == "tag"), None)
        assert tag["value"] == "span"

    def test_has_text_node_child(self, attached_span):
        span, tree = attached_span
        changes = tree.collect_changes()
        text_node = next(
            (c for c in changes if c.get("feat") == Feature.TEXT_NODE and c.get("key") == "text"),
            None
        )
        assert text_node is not None
        assert text_node["value"] == "Hello World"

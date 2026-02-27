"""Tests for Component visibility, enabled, and className features."""

import pytest

from pyflow.components import Button, TextField
from pyflow.core.state_tree import StateTree


class TestComponentVisibility:
    """Test component visibility methods."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_component_visible_by_default(self):
        """Components are visible by default."""
        button = Button("Click me")
        assert button.is_visible() is True

    def test_set_visible_false(self, tree):
        """set_visible(False) hides the component."""
        button = Button("Click me")
        button._attach(tree)

        button.set_visible(False)
        assert button.is_visible() is False

    def test_set_visible_true(self, tree):
        """set_visible(True) shows the component."""
        button = Button("Click me")
        button._attach(tree)

        button.set_visible(False)
        button.set_visible(True)
        assert button.is_visible() is True

    def test_set_visible_updates_style(self, tree):
        """set_visible updates display style."""
        button = Button("Click me")
        button._attach(tree)
        tree.collect_changes()  # Clear initial changes

        button.set_visible(False)
        changes = tree.collect_changes()

        # Find the style change for display
        style_change = next(
            (c for c in changes if c.get("key") == "display"),
            None
        )
        assert style_change is not None
        assert style_change["value"] == "none"


class TestComponentEnabled:
    """Test component enabled methods."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_component_enabled_by_default(self):
        """Components are enabled by default."""
        button = Button("Click me")
        assert button.is_enabled() is True

    def test_set_enabled_false(self, tree):
        """set_enabled(False) disables the component."""
        button = Button("Click me")
        button._attach(tree)

        button.set_enabled(False)
        assert button.is_enabled() is False

    def test_set_enabled_true(self, tree):
        """set_enabled(True) enables the component."""
        button = Button("Click me")
        button._attach(tree)

        button.set_enabled(False)
        button.set_enabled(True)
        assert button.is_enabled() is True

    def test_set_enabled_false_sets_attribute(self, tree):
        """set_enabled(False) sets disabled attribute."""
        button = Button("Click me")
        button._attach(tree)
        tree.collect_changes()  # Clear initial changes

        button.set_enabled(False)
        changes = tree.collect_changes()

        # Find the disabled attribute change
        disabled_change = next(
            (c for c in changes if c.get("key") == "disabled"),
            None
        )
        assert disabled_change is not None

    def test_set_enabled_true_removes_attribute(self, tree):
        """set_enabled(True) removes disabled attribute."""
        button = Button("Click me")
        button._attach(tree)
        button.set_enabled(False)
        tree.collect_changes()  # Clear changes

        button.set_enabled(True)
        changes = tree.collect_changes()

        # Find the remove change for disabled
        remove_change = next(
            (c for c in changes if c.get("key") == "disabled" and c.get("type") == "remove"),
            None
        )
        assert remove_change is not None


class TestComponentClassName:
    """Test component className methods."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_no_class_names_by_default(self):
        """Components have no class names by default."""
        button = Button("Click me")
        assert len(button.get_class_names()) == 0

    def test_add_class_name(self, tree):
        """add_class_name adds a CSS class."""
        button = Button("Click me")
        button._attach(tree)

        button.add_class_name("my-button")
        assert button.has_class_name("my-button")
        assert "my-button" in button.get_class_names()

    def test_add_multiple_class_names(self, tree):
        """add_class_name can add multiple classes at once."""
        button = Button("Click me")
        button._attach(tree)

        button.add_class_name("class-a", "class-b", "class-c")
        assert button.has_class_name("class-a")
        assert button.has_class_name("class-b")
        assert button.has_class_name("class-c")

    def test_remove_class_name(self, tree):
        """remove_class_name removes a CSS class."""
        button = Button("Click me")
        button._attach(tree)

        button.add_class_name("my-button", "other-class")
        button.remove_class_name("my-button")

        assert not button.has_class_name("my-button")
        assert button.has_class_name("other-class")

    def test_remove_nonexistent_class_name(self, tree):
        """Removing nonexistent class is a no-op."""
        button = Button("Click me")
        button._attach(tree)

        # Should not raise
        button.remove_class_name("nonexistent")
        assert len(button.get_class_names()) == 0

    def test_set_class_name_add(self, tree):
        """set_class_name with add=True adds the class."""
        button = Button("Click me")
        button._attach(tree)

        button.set_class_name("my-class", add=True)
        assert button.has_class_name("my-class")

    def test_set_class_name_remove(self, tree):
        """set_class_name with add=False removes the class."""
        button = Button("Click me")
        button._attach(tree)

        button.add_class_name("my-class")
        button.set_class_name("my-class", add=False)
        assert not button.has_class_name("my-class")

    def test_class_attribute_updated(self, tree):
        """Class attribute is updated on the element."""
        button = Button("Click me")
        button._attach(tree)
        tree.collect_changes()  # Clear initial changes

        button.add_class_name("class-a", "class-b")
        changes = tree.collect_changes()

        # Find the class attribute change
        class_change = next(
            (c for c in changes if c.get("key") == "class"),
            None
        )
        assert class_change is not None
        # Classes are sorted
        assert class_change["value"] == "class-a class-b"

    def test_class_attribute_removed_when_empty(self, tree):
        """Class attribute is removed when no classes remain."""
        button = Button("Click me")
        button._attach(tree)
        button.add_class_name("my-class")
        tree.collect_changes()  # Clear changes

        button.remove_class_name("my-class")
        changes = tree.collect_changes()

        # Find the remove change for class
        remove_change = next(
            (c for c in changes if c.get("key") == "class" and c.get("type") == "remove"),
            None
        )
        assert remove_change is not None

    def test_get_class_names_returns_copy(self, tree):
        """get_class_names returns a copy, not the internal set."""
        button = Button("Click me")
        button._attach(tree)

        button.add_class_name("my-class")
        class_names = button.get_class_names()
        class_names.add("other-class")

        # Original should not be modified
        assert not button.has_class_name("other-class")


class TestComponentExecuteJs:
    """Test Component.execute_js with buffering."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_execute_js_when_attached(self, tree):
        """execute_js delegates to element when attached."""
        button = Button("Click me")
        button._attach(tree)
        tree.collect_execute()  # Clear initial execute commands

        button.execute_js("this.focus()")
        cmds = tree.collect_execute()

        assert len(cmds) == 1
        cmd = cmds[0]
        assert "this.focus()" in cmd[-1]  # Script is wrapped in try/catch
        assert cmd[0] == {"@v-node": button.element.node_id}  # Element ref is first

    def test_execute_js_with_args_when_attached(self, tree):
        """execute_js passes arguments to element."""
        button = Button("Click me")
        button._attach(tree)
        tree.collect_execute()

        button.execute_js("this.style.color = $0", "red")
        cmds = tree.collect_execute()

        assert len(cmds) == 1
        cmd = cmds[0]
        assert "this.style.color = $0" in cmd[-1]  # Script is wrapped in try/catch
        assert cmd[0] == {"@v-node": button.element.node_id}
        assert cmd[1] == "red"  # First arg

    def test_execute_js_buffered_before_attach(self, tree):
        """execute_js buffers calls when not yet attached."""
        button = Button("Click me")
        # Not attached yet — should not raise
        button.execute_js("this.focus()")

        # Now attach — buffered JS should be flushed
        button._attach(tree)
        cmds = tree.collect_execute()

        focus_cmds = [c for c in cmds if "this.focus()" in c[-1]]
        assert len(focus_cmds) == 1

    def test_execute_js_buffered_multiple(self, tree):
        """Multiple buffered execute_js calls are all flushed in order."""
        button = Button("Click me")
        button.execute_js("console.log($0)", "first")
        button.execute_js("console.log($0)", "second")

        button._attach(tree)
        cmds = tree.collect_execute()

        log_cmds = [c for c in cmds if "console.log($0)" in c[-1]]
        assert len(log_cmds) == 2
        assert log_cmds[0][1] == "first"
        assert log_cmds[1][1] == "second"

    def test_execute_js_buffer_cleared_after_attach(self, tree):
        """Buffered JS list is cleaned up after attach."""
        button = Button("Click me")
        button.execute_js("this.focus()")

        button._attach(tree)
        assert not hasattr(button, "_pending_execute_js")

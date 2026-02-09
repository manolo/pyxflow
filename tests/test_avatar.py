"""Tests for Avatar and AvatarGroup components."""

import pytest
from vaadin.flow.components import Avatar, AvatarGroup, AvatarGroupItem
from vaadin.flow.core.state_tree import StateTree
from vaadin.flow.core.state_node import Feature


@pytest.fixture
def tree():
    return StateTree()


class TestAvatar:
    def test_tag(self, tree):
        a = Avatar()
        a._attach(tree)
        assert a.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-avatar"

    def test_default_empty(self):
        a = Avatar()
        assert a.get_name() == ""
        assert a.get_abbreviation() == ""
        assert a.get_image() == ""
        assert a.get_color_index() is None

    def test_constructor_name(self, tree):
        a = Avatar("Sophia Williams")
        a._attach(tree)
        assert a.get_name() == "Sophia Williams"
        assert a.element.get_property("name") == "Sophia Williams"

    def test_constructor_abbr(self, tree):
        a = Avatar(abbr="SW")
        a._attach(tree)
        assert a.get_abbreviation() == "SW"
        assert a.element.get_property("abbr") == "SW"

    def test_constructor_img(self, tree):
        a = Avatar(img="https://example.com/photo.jpg")
        a._attach(tree)
        assert a.get_image() == "https://example.com/photo.jpg"
        assert a.element.get_property("img") == "https://example.com/photo.jpg"

    def test_set_name_after_attach(self, tree):
        a = Avatar()
        a._attach(tree)
        a.set_name("Hugo Santos")
        assert a.get_name() == "Hugo Santos"
        assert a.element.get_property("name") == "Hugo Santos"

    def test_set_abbreviation_after_attach(self, tree):
        a = Avatar()
        a._attach(tree)
        a.set_abbreviation("HS")
        assert a.get_abbreviation() == "HS"
        assert a.element.get_property("abbr") == "HS"

    def test_set_image_after_attach(self, tree):
        a = Avatar()
        a._attach(tree)
        a.set_image("https://example.com/img.png")
        assert a.get_image() == "https://example.com/img.png"
        assert a.element.get_property("img") == "https://example.com/img.png"

    def test_set_color_index(self, tree):
        a = Avatar("Test")
        a.set_color_index(3)
        a._attach(tree)
        assert a.get_color_index() == 3
        assert a.element.get_property("colorIndex") == 3

    def test_set_color_index_after_attach(self, tree):
        a = Avatar()
        a._attach(tree)
        a.set_color_index(5)
        assert a.get_color_index() == 5
        assert a.element.get_property("colorIndex") == 5

    def test_all_constructor_args(self, tree):
        a = Avatar(name="Full Name", abbr="FN", img="https://example.com/x.png")
        a._attach(tree)
        assert a.element.get_property("name") == "Full Name"
        assert a.element.get_property("abbr") == "FN"
        assert a.element.get_property("img") == "https://example.com/x.png"

    def test_empty_constructor_no_properties(self, tree):
        a = Avatar()
        a._attach(tree)
        changes = tree.collect_changes()
        # Should not have name/abbr/img properties set
        prop_keys = [c.get("key") for c in changes if c.get("type") == "put" and c.get("feat") == Feature.ELEMENT_PROPERTY_MAP]
        assert "name" not in prop_keys
        assert "abbr" not in prop_keys
        assert "img" not in prop_keys


class TestAvatarGroupItem:
    def test_to_dict_full(self):
        item = AvatarGroupItem(name="Test", abbr="T", img="http://x.com/y.png", color_index=2)
        d = item.to_dict()
        assert d == {"name": "Test", "abbr": "T", "img": "http://x.com/y.png", "colorIndex": 2}

    def test_to_dict_partial(self):
        item = AvatarGroupItem(name="Only Name")
        d = item.to_dict()
        assert d == {"name": "Only Name"}

    def test_to_dict_empty(self):
        item = AvatarGroupItem()
        d = item.to_dict()
        assert d == {}


class TestAvatarGroup:
    def test_tag(self, tree):
        g = AvatarGroup()
        g._attach(tree)
        assert g.element.node.get(Feature.ELEMENT_DATA, "tag") == "vaadin-avatar-group"

    def test_add_items(self, tree):
        g = AvatarGroup()
        g.add(AvatarGroupItem("Alice"), AvatarGroupItem("Bob"))
        g._attach(tree)
        assert len(g.get_items()) == 2
        items_prop = g.element.get_property("items")
        assert len(items_prop) == 2
        assert items_prop[0] == {"name": "Alice"}
        assert items_prop[1] == {"name": "Bob"}

    def test_add_items_after_attach(self, tree):
        g = AvatarGroup()
        g._attach(tree)
        g.add(AvatarGroupItem("Alice"))
        items_prop = g.element.get_property("items")
        assert len(items_prop) == 1

    def test_set_items(self, tree):
        g = AvatarGroup()
        g.add(AvatarGroupItem("Old"))
        g._attach(tree)
        g.set_items([AvatarGroupItem("New1"), AvatarGroupItem("New2")])
        assert len(g.get_items()) == 2
        items_prop = g.element.get_property("items")
        assert len(items_prop) == 2
        assert items_prop[0] == {"name": "New1"}

    def test_max_items_visible(self, tree):
        g = AvatarGroup()
        g.set_max_items_visible(3)
        g._attach(tree)
        assert g.get_max_items_visible() == 3
        assert g.element.get_property("maxItemsVisible") == 3

    def test_max_items_visible_after_attach(self, tree):
        g = AvatarGroup()
        g._attach(tree)
        g.set_max_items_visible(2)
        assert g.element.get_property("maxItemsVisible") == 2

    def test_items_with_color_index(self, tree):
        g = AvatarGroup()
        g.add(AvatarGroupItem("X", color_index=4))
        g._attach(tree)
        items_prop = g.element.get_property("items")
        assert items_prop[0] == {"name": "X", "colorIndex": 4}

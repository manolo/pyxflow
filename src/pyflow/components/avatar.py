"""Avatar and AvatarGroup components."""

from typing import TYPE_CHECKING

from pyflow.core.component import Component
from pyflow.components.constants import AvatarVariant, AvatarGroupVariant

if TYPE_CHECKING:
    from pyflow.core.state_tree import StateTree


class Avatar(Component):
    """An avatar component showing a user's image, initials, or icon.

    Usage::

        avatar = Avatar("Sophia Williams")
        avatar = Avatar(name="Hugo", abbr="HS", img="https://...")
    """

    _v_fqcn = "com.vaadin.flow.component.avatar.Avatar"
    _tag = "vaadin-avatar"

    def __init__(self, name: str = "", abbr: str = "", img: str = ""):
        self._name = name
        self._abbr = abbr
        self._img = img
        self._color_index: int | None = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        if self._name:
            self.element.set_property("name", self._name)
        if self._abbr:
            self.element.set_property("abbr", self._abbr)
        if self._img:
            self.element.set_property("img", self._img)
        if self._color_index is not None:
            self.element.set_property("colorIndex", self._color_index)

    def set_name(self, name: str):
        """Set the name displayed as tooltip and used for initials."""
        self._name = name
        if self._element:
            self.element.set_property("name", name)

    def get_name(self) -> str:
        return self._name

    def set_abbreviation(self, abbr: str):
        """Set the abbreviation (initials) shown in the avatar."""
        self._abbr = abbr
        if self._element:
            self.element.set_property("abbr", abbr)

    def get_abbreviation(self) -> str:
        return self._abbr

    def set_image(self, img: str):
        """Set the image URL for the avatar."""
        self._img = img
        if self._element:
            self.element.set_property("img", img)

    def get_image(self) -> str:
        return self._img

    def set_color_index(self, index: int):
        """Set the color index (0-6) for the avatar background."""
        self._color_index = index
        if self._element:
            self.element.set_property("colorIndex", index)

    def get_color_index(self) -> int | None:
        return self._color_index

    def add_theme_variants(self, *variants: AvatarVariant):
        """Add theme variants to the avatar."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: AvatarVariant):
        """Remove theme variants from the avatar."""
        self.remove_theme_name(*variants)


class AvatarGroupItem:
    """Data class for AvatarGroup items."""

    def __init__(self, name: str = "", abbr: str = "", img: str = "",
                 color_index: int | None = None):
        self.name = name
        self.abbr = abbr
        self.img = img
        self.color_index = color_index

    def to_dict(self) -> dict:
        d = {}
        if self.name:
            d["name"] = self.name
        if self.abbr:
            d["abbr"] = self.abbr
        if self.img:
            d["img"] = self.img
        if self.color_index is not None:
            d["colorIndex"] = self.color_index
        return d


class AvatarGroup(Component):
    """A group of avatars with overflow handling.

    Usage::

        group = AvatarGroup()
        group.add(AvatarGroupItem("Sophia"), AvatarGroupItem("Hugo"))
        group.set_max_items_visible(3)
    """

    _v_fqcn = "com.vaadin.flow.component.avatar.AvatarGroup"
    _tag = "vaadin-avatar-group"

    def __init__(self):
        self._items: list[AvatarGroupItem] = []
        self._max_items_visible: int | None = None

    def _attach(self, tree: "StateTree"):
        super()._attach(tree)
        self._push_items()
        if self._max_items_visible is not None:
            self.element.set_property("maxItemsVisible", self._max_items_visible)

    def _push_items(self):
        """Push the items list as a JSON property."""
        if self._element:
            items_json = [item.to_dict() for item in self._items]
            self.element.set_property("items", items_json)

    def add(self, *items: AvatarGroupItem):
        """Add items to the group."""
        self._items.extend(items)
        self._push_items()

    def set_items(self, items: list[AvatarGroupItem]):
        """Replace all items."""
        self._items = list(items)
        self._push_items()

    def get_items(self) -> list[AvatarGroupItem]:
        return list(self._items)

    def set_max_items_visible(self, max_visible: int):
        """Set the maximum number of avatars visible before overflow."""
        self._max_items_visible = max_visible
        if self._element:
            self.element.set_property("maxItemsVisible", max_visible)

    def get_max_items_visible(self) -> int | None:
        return self._max_items_visible

    def add_theme_variants(self, *variants: AvatarGroupVariant):
        """Add theme variants to the avatar group."""
        self.add_theme_name(*variants)

    def remove_theme_variants(self, *variants: AvatarGroupVariant):
        """Remove theme variants from the avatar group."""
        self.remove_theme_name(*variants)

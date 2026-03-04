"""FlexLayout component — a div with display:flex and full Flexbox API."""

from pyxflow.core.component import Component
from pyxflow.components.constants import (
    FlexDirection, FlexWrap, JustifyContentMode, ContentAlignment, Alignment,
)


class FlexLayout(Component):
    """A layout component that implements CSS Flexbox.

    Uses a plain <div> with display:flex. No predetermined width or height.
    """

    _v_fqcn = "com.vaadin.flow.component.orderedlayout.FlexLayout"
    _tag = "div"

    FlexDirection = FlexDirection
    FlexWrap = FlexWrap
    JustifyContentMode = JustifyContentMode
    ContentAlignment = ContentAlignment
    Alignment = Alignment

    def __init__(self, *children: Component):
        super().__init__()
        self._children: list[Component] = list(children)

    def _attach(self, tree):
        super()._attach(tree)
        self.element.get_style().set("display", "flex")
        for child in self._children:
            child._ui = self._ui
            child._parent = self
            child._attach(tree)
        if self._children:
            self.element.add_children([child.element for child in self._children])

    def add(self, *components: Component):
        """Add components to the layout."""
        for component in components:
            self._children.append(component)
            component._parent = self
            component._ui = self._ui
            if self._element:
                if not component._element:
                    component._attach(self._element._tree)
                self.element.add_child(component.element)

    def remove(self, *components: Component):
        """Remove components from the layout."""
        for component in components:
            if component in self._children:
                self._children.remove(component)
                component._parent = None
                if self._element:
                    self.element.remove_child(component.element)

    def remove_all(self):
        """Remove all child components."""
        for child in list(self._children):
            self.remove(child)

    # --- Flex direction ---

    def set_flex_direction(self, direction: FlexDirection | None):
        """Set the flex-direction CSS property."""
        if direction is None:
            self.get_style().set("flex-direction", "")
        else:
            self.get_style().set("flex-direction", direction.value)

    def get_flex_direction(self) -> FlexDirection:
        """Get the flex-direction. Default is ROW."""
        val = self.get_style().get("flex-direction")
        if val:
            for d in FlexDirection:
                if d.value == val:
                    return d
        return FlexDirection.ROW

    # --- Flex wrap ---

    def set_flex_wrap(self, wrap: FlexWrap):
        """Set the flex-wrap CSS property."""
        self.get_style().set("flex-wrap", wrap.value)

    def get_flex_wrap(self) -> FlexWrap:
        """Get the flex-wrap. Default is NOWRAP."""
        val = self.get_style().get("flex-wrap")
        if val:
            for w in FlexWrap:
                if w.value == val:
                    return w
        return FlexWrap.NOWRAP

    # --- Justify content ---

    def set_justify_content_mode(self, mode: JustifyContentMode):
        """Set the justify-content CSS property."""
        self.get_style().set("justify-content", mode.value)

    def get_justify_content_mode(self) -> JustifyContentMode:
        """Get the justify-content mode. Default is START."""
        val = self.get_style().get("justify-content")
        if val:
            for m in JustifyContentMode:
                if m.value == val:
                    return m
        return JustifyContentMode.START

    # --- Align items ---

    def set_align_items(self, alignment: Alignment | None):
        """Set the align-items CSS property (cross-axis alignment for all children)."""
        if alignment is None:
            self.get_style().set("align-items", "")
        else:
            self.get_style().set("align-items", alignment.value)

    def get_align_items(self) -> Alignment:
        """Get the align-items value. Default is STRETCH."""
        val = self.get_style().get("align-items")
        if val:
            for a in Alignment:
                if a.value == val:
                    return a
        return Alignment.STRETCH

    # --- Align self (per-component) ---

    def set_align_self(self, alignment: Alignment | None, *components: Component):
        """Set align-self on individual components."""
        for component in components:
            if alignment is None:
                component.get_style().remove("align-self")
            else:
                component.get_style().set("align-self", alignment.value)

    def get_align_self(self, component: Component) -> Alignment:
        """Get align-self for a component. Default is AUTO."""
        val = component.get_style().get("align-self")
        if val:
            for a in Alignment:
                if a.value == val:
                    return a
        return Alignment.AUTO

    # --- Align content ---

    def set_align_content(self, alignment: ContentAlignment | None):
        """Set the align-content CSS property (multi-line cross-axis alignment)."""
        if alignment is None:
            self.get_style().set("align-content", "")
        else:
            self.get_style().set("align-content", alignment.value)

    def get_align_content(self) -> ContentAlignment:
        """Get the align-content value. Default is STRETCH."""
        val = self.get_style().get("align-content")
        if val:
            for a in ContentAlignment:
                if a.value == val:
                    return a
        return ContentAlignment.STRETCH

    # --- Flex grow ---

    def set_flex_grow(self, flex_grow: float, *components: Component):
        """Set flex-grow on components."""
        for component in components:
            component.get_style().set("flex-grow", str(flex_grow))

    def get_flex_grow(self, component: Component) -> float:
        """Get flex-grow for a component. Default is 0."""
        val = component.get_style().get("flex-grow")
        if val:
            return float(val)
        return 0.0

    def expand(self, *components: Component):
        """Set flex-grow to 1 on the given components."""
        self.set_flex_grow(1, *components)

    # --- Flex shrink ---

    def set_flex_shrink(self, flex_shrink: float, *components: Component):
        """Set flex-shrink on components."""
        for component in components:
            component.get_style().set("flex-shrink", str(flex_shrink))

    def get_flex_shrink(self, component: Component) -> float:
        """Get flex-shrink for a component. Default is 1."""
        val = component.get_style().get("flex-shrink")
        if val:
            return float(val)
        return 1.0

    # --- Flex basis ---

    def set_flex_basis(self, width: str | None, *components: Component):
        """Set flex-basis on components."""
        for component in components:
            if width is None:
                component.get_style().remove("flex-basis")
            else:
                component.get_style().set("flex-basis", width)

    def get_flex_basis(self, component: Component) -> str | None:
        """Get flex-basis for a component."""
        val = component.get_style().get("flex-basis")
        return val or None

    # --- Order ---

    def set_order(self, order: int, component: Component):
        """Set the order CSS property on a component."""
        if order == 0:
            component.get_style().remove("order")
        else:
            component.get_style().set("order", str(order))

    def get_order(self, component: Component) -> int:
        """Get the order for a component. Default is 0."""
        val = component.get_style().get("order")
        if val:
            return int(val)
        return 0

    def replace(self, old_component: Component, new_component: Component):
        """Replace an existing component with a new one."""
        idx = self._children.index(old_component)
        self.remove(old_component)
        self.add_component_at_index(idx, new_component)

    def add_component_at_index(self, index: int, component: Component):
        """Add a component at a specific index."""
        self._children.insert(index, component)
        component._parent = self
        component._ui = self._ui
        if self._element:
            component._attach(self._element._tree)
            self.element.add_child(component.element, index)

"""FlexLayout component — a div with display:flex and full Flexbox API."""

from enum import Enum

from vaadin.flow.core.component import Component


class FlexDirection(Enum):
    """Flex direction values (flex-direction CSS property)."""
    ROW = "row"
    ROW_REVERSE = "row-reverse"
    COLUMN = "column"
    COLUMN_REVERSE = "column-reverse"


class FlexWrap(Enum):
    """Flex wrap values (flex-wrap CSS property)."""
    NOWRAP = "nowrap"
    WRAP = "wrap"
    WRAP_REVERSE = "wrap-reverse"


class JustifyContentMode(Enum):
    """Justify content values (justify-content CSS property)."""
    START = "flex-start"
    END = "flex-end"
    CENTER = "center"
    BETWEEN = "space-between"
    AROUND = "space-around"
    EVENLY = "space-evenly"


class ContentAlignment(Enum):
    """Content alignment values (align-content CSS property)."""
    START = "flex-start"
    END = "flex-end"
    CENTER = "center"
    STRETCH = "stretch"
    SPACE_BETWEEN = "space-between"
    SPACE_AROUND = "space-around"


class Alignment(Enum):
    """Item alignment values (align-items / align-self CSS property)."""
    START = "flex-start"
    END = "flex-end"
    CENTER = "center"
    STRETCH = "stretch"
    BASELINE = "baseline"
    AUTO = "auto"


class FlexLayout(Component):
    """A layout component that implements CSS Flexbox.

    Uses a plain <div> with display:flex. No predetermined width or height.
    """

    _tag = "div"

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

    # --- Flex direction ---

    def set_flex_direction(self, direction: FlexDirection | None):
        """Set the flex-direction CSS property."""
        if direction is None:
            self._set_style("flex-direction", "")
        else:
            self._set_style("flex-direction", direction.value)

    def get_flex_direction(self) -> FlexDirection:
        """Get the flex-direction. Default is ROW."""
        val = self._get_style("flex-direction")
        if val:
            for d in FlexDirection:
                if d.value == val:
                    return d
        return FlexDirection.ROW

    # --- Flex wrap ---

    def set_flex_wrap(self, wrap: FlexWrap):
        """Set the flex-wrap CSS property."""
        self._set_style("flex-wrap", wrap.value)

    def get_flex_wrap(self) -> FlexWrap:
        """Get the flex-wrap. Default is NOWRAP."""
        val = self._get_style("flex-wrap")
        if val:
            for w in FlexWrap:
                if w.value == val:
                    return w
        return FlexWrap.NOWRAP

    # --- Justify content ---

    def set_justify_content_mode(self, mode: JustifyContentMode):
        """Set the justify-content CSS property."""
        self._set_style("justify-content", mode.value)

    def get_justify_content_mode(self) -> JustifyContentMode:
        """Get the justify-content mode. Default is START."""
        val = self._get_style("justify-content")
        if val:
            for m in JustifyContentMode:
                if m.value == val:
                    return m
        return JustifyContentMode.START

    # --- Align items ---

    def set_align_items(self, alignment: Alignment | None):
        """Set the align-items CSS property (cross-axis alignment for all children)."""
        if alignment is None:
            self._set_style("align-items", "")
        else:
            self._set_style("align-items", alignment.value)

    def get_align_items(self) -> Alignment:
        """Get the align-items value. Default is STRETCH."""
        val = self._get_style("align-items")
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
                if component._element:
                    component.element.get_style().set("align-self", "")
                else:
                    component._pending_styles.pop("align-self", None)
            else:
                if component._element:
                    component.element.get_style().set("align-self", alignment.value)
                else:
                    component._pending_styles["align-self"] = alignment.value

    def get_align_self(self, component: Component) -> Alignment:
        """Get align-self for a component. Default is AUTO."""
        if component._element:
            val = component.element.get_style().get("align-self")
        else:
            val = component._pending_styles.get("align-self")
        if val:
            for a in Alignment:
                if a.value == val:
                    return a
        return Alignment.AUTO

    # --- Align content ---

    def set_align_content(self, alignment: ContentAlignment | None):
        """Set the align-content CSS property (multi-line cross-axis alignment)."""
        if alignment is None:
            self._set_style("align-content", "")
        else:
            self._set_style("align-content", alignment.value)

    def get_align_content(self) -> ContentAlignment:
        """Get the align-content value. Default is STRETCH."""
        val = self._get_style("align-content")
        if val:
            for a in ContentAlignment:
                if a.value == val:
                    return a
        return ContentAlignment.STRETCH

    # --- Flex grow ---

    def set_flex_grow(self, flex_grow: float, *components: Component):
        """Set flex-grow on components."""
        for component in components:
            if component._element:
                component.element.get_style().set("flex-grow", str(flex_grow))
            else:
                component._pending_styles["flex-grow"] = str(flex_grow)

    def get_flex_grow(self, component: Component) -> float:
        """Get flex-grow for a component. Default is 0."""
        if component._element:
            val = component.element.get_style().get("flex-grow")
        else:
            val = component._pending_styles.get("flex-grow")
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
            if component._element:
                component.element.get_style().set("flex-shrink", str(flex_shrink))
            else:
                component._pending_styles["flex-shrink"] = str(flex_shrink)

    def get_flex_shrink(self, component: Component) -> float:
        """Get flex-shrink for a component. Default is 1."""
        if component._element:
            val = component.element.get_style().get("flex-shrink")
        else:
            val = component._pending_styles.get("flex-shrink")
        if val:
            return float(val)
        return 1.0

    # --- Flex basis ---

    def set_flex_basis(self, width: str | None, *components: Component):
        """Set flex-basis on components."""
        for component in components:
            if width is None:
                if component._element:
                    component.element.get_style().set("flex-basis", "")
                else:
                    component._pending_styles.pop("flex-basis", None)
            else:
                if component._element:
                    component.element.get_style().set("flex-basis", width)
                else:
                    component._pending_styles["flex-basis"] = width

    def get_flex_basis(self, component: Component) -> str | None:
        """Get flex-basis for a component."""
        if component._element:
            val = component.element.get_style().get("flex-basis")
        else:
            val = component._pending_styles.get("flex-basis")
        return val or None

    # --- Order ---

    def set_order(self, order: int, component: Component):
        """Set the order CSS property on a component."""
        if component._element:
            if order == 0:
                component.element.get_style().set("order", "")
            else:
                component.element.get_style().set("order", str(order))
        else:
            if order == 0:
                component._pending_styles.pop("order", None)
            else:
                component._pending_styles["order"] = str(order)

    def get_order(self, component: Component) -> int:
        """Get the order for a component. Default is 0."""
        if component._element:
            val = component.element.get_style().get("order")
        else:
            val = component._pending_styles.get("order")
        if val:
            return int(val)
        return 0

"""@Menu decorator and MenuConfiguration for automatic menu generation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from vaadin.flow.core.component import Component


def Menu(title: str | None = None, order: int = 0, icon: str | None = None, exclude: bool = False):
    """Decorator to mark a view as a menu entry.

    Usage:
        @Route("")
        @Menu(title="Home", order=0, icon="vaadin:home")
        class HomeView(VerticalLayout):
            pass

    Args:
        title: Menu entry title. Defaults to the class name derived title.
        order: Sort order (lower = first). Default 0.
        icon: Icon name (e.g. "vaadin:home"). Optional.
        exclude: If True, the view is excluded from menu generation.
    """
    def decorator(cls: Type["Component"]) -> Type["Component"]:
        setattr(cls, '_menu_title', title)
        setattr(cls, '_menu_order', order)
        setattr(cls, '_menu_icon', icon)
        setattr(cls, '_menu_exclude', exclude)
        return cls
    return decorator


@dataclass
class MenuEntry:
    """A menu entry generated from @Menu-annotated routes."""
    path: str
    title: str
    order: int
    icon: str | None


def get_menu_entries() -> list[MenuEntry]:
    """Collect menu entries from all @Menu-annotated routes.

    Filters out:
    - Routes without @Menu
    - Routes with @Menu(exclude=True)
    - Routes with required parameters (contain ':' without '?')

    Returns entries sorted by (order, path).
    """
    from vaadin.flow.router import _routes

    entries = []
    for path, (cls, page_title, param_names, regex, layout_cls) in _routes.items():
        # Skip alias routes (only primary @Route appears in menu)
        if path in getattr(cls, '_route_aliases', []):
            continue

        # Skip if no @Menu decorator
        if not hasattr(cls, '_menu_order'):
            continue

        # Skip if explicitly excluded
        if getattr(cls, '_menu_exclude', False):
            continue

        # Skip routes with required parameters
        has_required_params = any(
            not p.endswith('?')
            for p in path.split('/')
            if p.startswith(':')
        )
        if has_required_params:
            continue

        title = getattr(cls, '_menu_title', None) or page_title or _derive_title(cls)
        order = getattr(cls, '_menu_order', 0)
        icon = getattr(cls, '_menu_icon', None)

        entries.append(MenuEntry(
            path="/" + path if path else "/",
            title=title,
            order=order,
            icon=icon,
        ))

    entries.sort(key=lambda e: (e.order, e.path))
    return entries


def get_page_header(view: "Component") -> str | None:
    """Get the page header/title for the given view.

    Resolution order (matches Java's MenuConfiguration.getPageHeader):
    1. view.get_page_title() — dynamic title (HasDynamicTitle pattern)
    2. @PageTitle annotation value (cls._page_title)
    3. Auto-derived from class name (e.g. "MyDashboardView" → "My Dashboard")

    Args:
        view: The current view component instance.

    Returns:
        The resolved title string, or None if view is None.
    """
    if view is None:
        return None
    from vaadin.flow.router import _resolve_title
    return _resolve_title(type(view), view)


def _derive_title(cls) -> str:
    """Derive a title from the class name."""
    import re
    name = cls.__name__
    if name.endswith("View"):
        name = name[:-4]
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', name)

"""Vaadin Flow for Python - Server-side UI framework."""

__version__ = "0.1.0"

from vaadin.flow.core.component import Component
from vaadin.flow.core.element import Element
from vaadin.flow.router import Route, PageTitle, discover_views
from vaadin.flow.menu import Menu, MenuEntry, get_menu_entries

__all__ = ["Component", "Element", "Menu", "MenuEntry", "PageTitle", "Route", "discover_views", "get_menu_entries", "__version__"]

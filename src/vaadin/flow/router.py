"""Router - URL routing with @Route decorator."""

from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from vaadin.flow.core.component import Component


# Global route registry: path -> (view_class, page_title)
_routes: dict[str, tuple[Type["Component"], str | None]] = {}


def Route(path: str = "", page_title: str | None = None):
    """Decorator to register a view class for a route.

    Usage:
        @Route("")
        class MainView(VerticalLayout):
            pass

        @Route("about")
        class AboutView(VerticalLayout):
            pass

        @Route("users", page_title="Users List")
        class UsersView(VerticalLayout):
            pass
    """
    def decorator(cls: Type["Component"]) -> Type["Component"]:
        # Normalize path (remove leading/trailing slashes)
        normalized_path = path.strip("/")
        _routes[normalized_path] = (cls, page_title)
        # Store route info on the class for introspection
        cls._route_path = normalized_path
        cls._page_title = page_title
        return cls
    return decorator


def get_view_class(path: str) -> Type["Component"] | None:
    """Get the view class for a given path.

    Args:
        path: The URL path (e.g., "", "about", "users/123")

    Returns:
        The view class or None if no route matches.
    """
    # Normalize path
    normalized_path = path.strip("/")

    # Exact match first
    if normalized_path in _routes:
        return _routes[normalized_path][0]

    # TODO: Add parameter matching (e.g., "users/:id")

    return None


def get_page_title(path: str) -> str | None:
    """Get the page title for a given path.

    Args:
        path: The URL path

    Returns:
        The page title or None.
    """
    normalized_path = path.strip("/")
    if normalized_path in _routes:
        view_class, title = _routes[normalized_path]
        # Use explicit title or class name
        if title:
            return title
        # Convert class name to title (e.g., HelloWorldView -> Hello World)
        name = view_class.__name__
        if name.endswith("View"):
            name = name[:-4]
        # Add spaces before capitals
        import re
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', name)
    return None


def get_all_routes() -> dict[str, Type["Component"]]:
    """Get all registered routes.

    Returns:
        Dict of path -> view_class
    """
    return {path: cls for path, (cls, _) in _routes.items()}


def clear_routes():
    """Clear all registered routes. Useful for testing."""
    _routes.clear()

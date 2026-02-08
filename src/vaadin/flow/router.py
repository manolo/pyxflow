"""Router - URL routing with @Route decorator."""

import re
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from vaadin.flow.core.component import Component


# Route entry: (view_class, explicit_page_title, param_names, compiled_regex)
_RouteEntry = tuple[Type["Component"], str | None, list[str], re.Pattern | None]

# Global route registry: normalized_path -> route entry
_routes: dict[str, _RouteEntry] = {}


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

        @Route("user/:id")
        class UserView(VerticalLayout):
            def set_parameter(self, params):
                user_id = params["id"]

        @Route("search/:q?")
        class SearchView(VerticalLayout):
            def set_parameter(self, params):
                query = params.get("q", "")
    """
    def decorator(cls: Type["Component"]) -> Type["Component"]:
        # Normalize path (remove leading/trailing slashes)
        normalized_path = path.strip("/")

        # Parse route parameters
        param_names, regex = _compile_route(normalized_path)

        _routes[normalized_path] = (cls, page_title, param_names, regex)

        # Store route info on the class for introspection
        cls._route_path = normalized_path
        # Only set _page_title from @Route if explicitly provided
        if page_title is not None:
            cls._page_title = page_title
        elif not hasattr(cls, '_page_title'):
            cls._page_title = None
        return cls
    return decorator


def PageTitle(title: str):
    """Decorator to set the page title for a view.

    Can be used alongside @Route. Takes priority over @Route's page_title param.

    Usage:
        @Route("about")
        @PageTitle("About Us")
        class AboutView(VerticalLayout):
            pass
    """
    def decorator(cls: Type["Component"]) -> Type["Component"]:
        cls._page_title = title
        return cls
    return decorator


def _compile_route(path: str) -> tuple[list[str], re.Pattern | None]:
    """Compile a route path into param names and regex pattern.

    Returns (param_names, regex) where regex is None for static routes.
    Supports :param (required) and :param? (optional) syntax.
    """
    if ':' not in path:
        return [], None

    param_names = []
    parts = path.split('/')
    regex_parts = []

    for part in parts:
        if part.startswith(':'):
            if part.endswith('?'):
                name = part[1:-1]
                param_names.append(name)
                regex_parts.append('(?:([^/]+))?')
            else:
                name = part[1:]
                param_names.append(name)
                regex_parts.append('([^/]+)')
        else:
            regex_parts.append(re.escape(part))

    pattern = '^' + '/'.join(regex_parts) + '$'
    # Also match without trailing optional segments
    # e.g., "search/:q?" should match both "search/foo" and "search"
    if any(p.endswith('?') for p in parts if p.startswith(':')):
        # Build alternative pattern without trailing optional segments
        alt_parts = []
        for part in parts:
            if part.startswith(':') and part.endswith('?'):
                break
            elif part.startswith(':'):
                alt_parts.append('([^/]+)')
            else:
                alt_parts.append(re.escape(part))
        alt_pattern = '^' + '/'.join(alt_parts) + '$'
        pattern = f'(?:{pattern}|{alt_pattern})'

    return param_names, re.compile(pattern)


def match_route(path: str) -> tuple[Type["Component"], str | None, dict[str, str]] | None:
    """Match a path against registered routes, returning view class, title, and params.

    Static routes have priority over parameterized routes.

    Returns:
        (view_class, page_title, params_dict) or None if no route matches.
    """
    normalized_path = path.strip("/")

    # Static routes first (exact match)
    for route_path, (cls, title, param_names, regex) in _routes.items():
        if regex is None and route_path == normalized_path:
            resolved_title = _resolve_title(cls)
            return cls, resolved_title, {}

    # Parameterized routes
    for route_path, (cls, title, param_names, regex) in _routes.items():
        if regex is not None:
            m = regex.match(normalized_path)
            if m:
                groups = m.groups()
                params = {}
                for i, name in enumerate(param_names):
                    if i < len(groups) and groups[i] is not None:
                        params[name] = groups[i]
                resolved_title = _resolve_title(cls)
                return cls, resolved_title, params

    return None


def get_view_class(path: str) -> Type["Component"] | None:
    """Get the view class for a given path.

    Args:
        path: The URL path (e.g., "", "about", "users/123")

    Returns:
        The view class or None if no route matches.
    """
    result = match_route(path)
    if result:
        return result[0]
    return None


def get_page_title(path: str) -> str | None:
    """Get the page title for a given path.

    Args:
        path: The URL path

    Returns:
        The page title or None.
    """
    result = match_route(path)
    if result:
        return result[1]
    return None


def _resolve_title(view_class: Type["Component"], view_instance=None) -> str | None:
    """Resolve the page title for a view.

    Priority:
    1. view_instance.get_page_title() (dynamic title - HasDynamicTitle)
    2. cls._page_title (from @PageTitle or @Route page_title param)
    3. Auto-derived from class name
    """
    # Dynamic title from instance
    if view_instance is not None and hasattr(view_instance, 'get_page_title'):
        return view_instance.get_page_title()

    # Explicit title from decorator
    title = getattr(view_class, '_page_title', None)
    if title:
        return title

    # Auto-derive from class name
    name = view_class.__name__
    if name.endswith("View"):
        name = name[:-4]
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', name)


def get_all_routes() -> dict[str, Type["Component"]]:
    """Get all registered routes.

    Returns:
        Dict of path -> view_class
    """
    return {path: cls for path, (cls, _, _, _) in _routes.items()}


def clear_routes():
    """Clear all registered routes. Useful for testing."""
    _routes.clear()

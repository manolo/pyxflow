"""Router - URL routing with @Route decorator."""

import re
from itertools import product
from typing import Type, TYPE_CHECKING
from urllib.parse import parse_qs

if TYPE_CHECKING:
    from vaadin.flow.core.component import Component


# ---------------------------------------------------------------------------
# Data classes for navigation context
# ---------------------------------------------------------------------------

class QueryParameters:
    """Immutable multidict for URL query parameters (?key=val&key=val2)."""

    __slots__ = ("_params",)

    def __init__(self, params: dict[str, list[str]] | None = None):
        self._params: dict[str, list[str]] = dict(params) if params else {}

    @staticmethod
    def from_string(query_string: str) -> "QueryParameters":
        """Parse a raw query string (without leading '?')."""
        if not query_string:
            return QueryParameters()
        return QueryParameters(parse_qs(query_string, keep_blank_values=True))

    @staticmethod
    def empty() -> "QueryParameters":
        return QueryParameters()

    def get_parameters(self, key: str) -> list[str]:
        """Return all values for *key*, or empty list."""
        return list(self._params.get(key, []))

    def get_single_parameter(self, key: str) -> str | None:
        """Return the first value for *key*, or None."""
        vals = self._params.get(key)
        return vals[0] if vals else None

    def get_parameter_names(self) -> set[str]:
        return set(self._params.keys())

    def __bool__(self) -> bool:
        return bool(self._params)

    def __repr__(self) -> str:
        return f"QueryParameters({self._params!r})"

    def __eq__(self, other):
        if isinstance(other, QueryParameters):
            return self._params == other._params
        return NotImplemented


class RouteParameters:
    """Immutable wrapper around path parameters with typed access."""

    __slots__ = ("_params",)

    def __init__(self, params: dict[str, str] | None = None):
        self._params: dict[str, str] = dict(params) if params else {}

    def get(self, name: str) -> str | None:
        """Return value of path parameter *name*, or None."""
        return self._params.get(name)

    def get_integer(self, name: str) -> int | None:
        """Return int value of *name*, or None if missing / not an int."""
        val = self._params.get(name)
        if val is None:
            return None
        try:
            return int(val)
        except (ValueError, TypeError):
            return None

    def get_wildcard(self, name: str) -> list[str]:
        """Split a wildcard param value by '/' and return segments."""
        val = self._params.get(name)
        if not val:
            return []
        return [s for s in val.split("/") if s]

    def get_parameter_names(self) -> set[str]:
        return set(self._params.keys())

    # --- dict-like read access (for backward compat) ---
    def __getitem__(self, key: str) -> str:
        return self._params[key]

    def __contains__(self, key: str) -> bool:
        return key in self._params

    def keys(self):
        return self._params.keys()

    def values(self):
        return self._params.values()

    def items(self):
        return self._params.items()

    def __bool__(self) -> bool:
        return bool(self._params)

    def __repr__(self) -> str:
        return f"RouteParameters({self._params!r})"

    def __eq__(self, other):
        if isinstance(other, RouteParameters):
            return self._params == other._params
        return NotImplemented


class Location:
    """Represents a navigation location (path + query parameters)."""

    __slots__ = ("_path", "_query_parameters")

    def __init__(self, path: str, query_parameters: QueryParameters | None = None):
        self._path = path.strip("/")
        self._query_parameters = query_parameters or QueryParameters.empty()

    @property
    def path(self) -> str:
        return self._path

    @property
    def segments(self) -> list[str]:
        if not self._path:
            return []
        return self._path.split("/")

    @property
    def query_parameters(self) -> QueryParameters:
        return self._query_parameters

    @property
    def first_segment(self) -> str:
        segs = self.segments
        return segs[0] if segs else ""

    def __repr__(self) -> str:
        return f"Location({self._path!r}, {self._query_parameters!r})"

    def __eq__(self, other):
        if isinstance(other, Location):
            return self._path == other._path and self._query_parameters == other._query_parameters
        return NotImplemented


class BeforeEnterEvent:
    """Full navigation context passed to view.before_enter().

    Dict-compatible so existing ``before_enter(params)`` code that does
    ``params["id"]`` or ``params.get("q")`` keeps working unchanged.
    """

    __slots__ = ("_location", "_route_parameters", "_navigation_target", "_ui", "_trigger")

    def __init__(
        self,
        location: Location,
        route_parameters: RouteParameters,
        navigation_target: type | None = None,
        ui: object | None = None,
        trigger: str = "router",
    ):
        self._location = location
        self._route_parameters = route_parameters
        self._navigation_target = navigation_target
        self._ui = ui
        self._trigger = trigger

    @property
    def location(self) -> Location:
        return self._location

    @property
    def route_parameters(self) -> RouteParameters:
        return self._route_parameters

    @property
    def navigation_target(self) -> type | None:
        return self._navigation_target

    @property
    def ui(self) -> object | None:
        return self._ui

    @property
    def trigger(self) -> str:
        return self._trigger

    # --- dict-like API delegating to route_parameters (backward compat) ---
    def get(self, key: str, default=None):
        val = self._route_parameters.get(key)
        return val if val is not None else default

    def __getitem__(self, key: str) -> str:
        return self._route_parameters[key]

    def __contains__(self, key: str) -> bool:
        return key in self._route_parameters

    def keys(self):
        return self._route_parameters.keys()

    def values(self):
        return self._route_parameters.values()

    def items(self):
        return self._route_parameters.items()

    def __bool__(self) -> bool:
        return True  # event is always truthy

    def __repr__(self) -> str:
        return f"BeforeEnterEvent(location={self._location!r}, route_parameters={self._route_parameters!r})"


# ---------------------------------------------------------------------------
# Route registry
# ---------------------------------------------------------------------------

# Route entry: (view_class, explicit_page_title, param_names, compiled_regexes, layout_class)
# compiled_regexes is None for static routes, or a list of regex patterns to try in order
_RouteEntry = tuple[Type["Component"], str | None, list[str], list[re.Pattern] | None, Type["Component"] | None]

# Global route registry: normalized_path -> route entry
_routes: dict[str, _RouteEntry] = {}

# Global AppShell class (set by @AppShell decorator)
_app_shell: type | None = None

# Sentinel for distinguishing "layout not specified" from "layout=None"
_SENTINEL = object()


def Route(path: str = "", page_title: str | None = None, layout: Type["Component"] | None = None):
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

        @Route("", layout=MainLayout)
        class HomeView(VerticalLayout):
            pass
    """
    def decorator(cls: Type["Component"]) -> Type["Component"]:
        # Normalize path (remove leading/trailing slashes)
        normalized_path = path.strip("/")

        # Parse route parameters
        param_names, regex = _compile_route(normalized_path)

        _routes[normalized_path] = (cls, page_title, param_names, regex, layout)

        # Store route info on the class for introspection
        setattr(cls, '_route_path', normalized_path)
        setattr(cls, '_route_layout', layout)
        # Only set _page_title from @Route if explicitly provided
        if page_title is not None:
            setattr(cls, '_page_title', page_title)
        elif not hasattr(cls, '_page_title'):
            setattr(cls, '_page_title', None)

        # Flush pending aliases (decorators run bottom-to-top, so aliases
        # are registered before @Route; now we can resolve inherited layouts)
        for alias_path, alias_layout_val in getattr(cls, '_pending_route_aliases', []):
            alias_pnames, alias_regex = _compile_route(alias_path)
            resolved_layout = alias_layout_val if alias_layout_val is not _SENTINEL else layout
            resolved_title = page_title or getattr(cls, '_page_title', None)
            _routes[alias_path] = (cls, resolved_title, alias_pnames, alias_regex, resolved_layout)
        if hasattr(cls, '_pending_route_aliases'):
            del cls._pending_route_aliases

        return cls
    return decorator


def RouteAlias(path: str, layout: Type["Component"] | None = _SENTINEL):
    """Decorator to register an additional path for a view.

    The view must also have a @Route. Aliases share the same page title.
    Each alias can optionally specify a different layout.

    Repeatable — multiple @RouteAlias can be stacked on the same class.

    Usage:
        @Route("dashboard", layout=AdminLayout)
        @RouteAlias("admin-dashboard")
        @RouteAlias("public-dash", layout=PublicLayout)
        class DashboardView(VerticalLayout):
            pass
    """
    def decorator(cls: Type["Component"]) -> Type["Component"]:
        normalized = path.strip("/")

        # Track aliases on class for introspection
        if not hasattr(cls, '_route_aliases'):
            cls._route_aliases = []
        cls._route_aliases.append(normalized)

        # If @Route already ran (cls has _route_path), register immediately.
        # Otherwise, store as pending — @Route will flush them.
        if hasattr(cls, '_route_path'):
            param_names, regex = _compile_route(normalized)
            alias_layout = layout if layout is not _SENTINEL else getattr(cls, '_route_layout', None)
            page_title = getattr(cls, '_page_title', None)
            _routes[normalized] = (cls, page_title, param_names, regex, alias_layout)
        else:
            if not hasattr(cls, '_pending_route_aliases'):
                cls._pending_route_aliases = []
            cls._pending_route_aliases.append((normalized, layout))

        return cls
    return decorator



def StyleSheet(*urls: str):
    """Decorator to load CSS stylesheets for a view.

    Usage:
        @Route("myview")
        @StyleSheet("styles/my-styles.css")
        class MyView(VerticalLayout):
            pass

    Multiple stylesheets can be specified:
        @StyleSheet("styles/base.css", "styles/theme.css")
    """
    def decorator(cls):
        existing = getattr(cls, '_stylesheets', [])
        setattr(cls, '_stylesheets', list(urls) + existing)
        return cls
    return decorator


def AppShell(cls):
    """Decorator to mark a class as the global app configuration.

    Only one class can be decorated with @AppShell per application.
    Use alongside @Push and @StyleSheet for global config.

    Usage:
        @AppShell
        @Push
        @StyleSheet("styles/styles.css")
        class MyAppShell:
            pass
    """
    global _app_shell
    _app_shell = cls
    return cls


def Push(cls):
    """Decorator to enable WebSocket push on the AppShell.

    Without @Push, push is disabled (no pushScript sent, no WS connection).

    Usage:
        @AppShell
        @Push
        class MyAppShell:
            pass
    """
    cls._push_enabled = True
    return cls


def ColorScheme(value: str):
    """Set the initial color scheme on the AppShell.

    Modifies <html> attributes at bootstrap time so the page loads
    with the correct theme immediately (no flash).

    Values: "dark", "light", "light dark", "dark light", "system", "normal".
    "system" is an alias for "light dark".

    Usage:
        @AppShell
        @ColorScheme("dark")
        class MyAppShell:
            pass
    """
    resolved = "light dark" if value == "system" else value
    def decorator(cls):
        cls._color_scheme = resolved
        return cls
    return decorator


def get_app_shell() -> type | None:
    """Get the registered AppShell class, or None."""
    return _app_shell


def clear_app_shell():
    """Clear the registered AppShell. Useful for testing."""
    global _app_shell
    _app_shell = None


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
        setattr(cls, '_page_title', title)
        return cls
    return decorator


def _compile_route(path: str) -> tuple[list[str], list[re.Pattern] | None]:
    """Compile a route path into param names and regex patterns.

    Returns (param_names, regexes) where regexes is None for static routes,
    or a list of compiled patterns to try in order.

    Supported syntax:
        :param   -- required segment
        :param?  -- optional segment (can appear mid-path or trailing)
        :param*  -- wildcard (0+ remaining segments, must be last)
    """
    if ':' not in path:
        return [], None

    param_names: list[str] = []
    parts = path.split('/')

    # Classify each part
    segments: list[tuple[str, str]] = []  # (kind, name_or_literal)
    for part in parts:
        if part.startswith(':') and part.endswith('*'):
            name = part[1:-1]
            param_names.append(name)
            segments.append(('wildcard', name))
        elif part.startswith(':') and part.endswith('?'):
            name = part[1:-1]
            param_names.append(name)
            segments.append(('optional', name))
        elif part.startswith(':'):
            name = part[1:]
            param_names.append(name)
            segments.append(('required', name))
        else:
            segments.append(('literal', part))

    # Validate: wildcard must be last
    for i, (kind, _) in enumerate(segments):
        if kind == 'wildcard' and i != len(segments) - 1:
            raise ValueError(f"Wildcard parameter must be the last segment in route: {path}")

    optional_indices = [i for i, (kind, _) in enumerate(segments) if kind == 'optional']

    if len(optional_indices) > 4:
        raise ValueError(f"Max 4 optional parameters supported, got {len(optional_indices)} in: {path}")

    if not optional_indices:
        # No optionals -- single pattern
        return param_names, [re.compile(_build_pattern(segments))]

    # Generate alternative patterns for each combination of present/absent optionals.
    # Each alternative is compiled separately (Python re doesn't allow
    # duplicate named groups across alternatives in a single pattern).
    regexes: list[re.Pattern] = []
    for combo in product([True, False], repeat=len(optional_indices)):
        # combo[j] = True means optional_indices[j] is present
        opt_set = {optional_indices[j] for j, present in enumerate(combo) if not present}
        filtered = [seg for i, seg in enumerate(segments) if i not in opt_set]
        regexes.append(re.compile(_build_pattern(filtered)))

    return param_names, regexes


def _build_pattern(segments: list[tuple[str, str]]) -> str:
    """Build a single regex pattern string from classified segments."""
    parts: list[str] = []
    for kind, name in segments:
        if kind == 'literal':
            parts.append(re.escape(name))
        elif kind in ('required', 'optional'):
            parts.append(f'(?P<{name}>[^/]+)')
        elif kind == 'wildcard':
            # Match 0 or more remaining path segments
            parts.append(f'(?:/(?P<{name}>.*))?')

    # Wildcard segment already includes its leading slash, so join
    # only the non-wildcard parts with '/'
    result_parts: list[str] = []
    for i, (kind, _) in enumerate(segments):
        if kind == 'wildcard':
            # Don't put '/' before the wildcard group -- it's built in
            result_parts.append(parts[i])
        else:
            result_parts.append(parts[i])

    pattern = '/'.join(p for i, p in enumerate(result_parts) if segments[i][0] != 'wildcard')
    # Append wildcard part (if any) at the end
    for i, (kind, _) in enumerate(segments):
        if kind == 'wildcard':
            pattern += result_parts[i]

    return f'^{pattern}$'


def match_route(path: str) -> tuple[Type["Component"], str | None, dict[str, str], Type["Component"] | None] | None:
    """Match a path against registered routes, returning view class, title, params, and layout.

    Static routes have priority over parameterized routes.

    Returns:
        (view_class, page_title, params_dict, layout_class) or None if no route matches.
    """
    normalized_path = path.strip("/")

    # Static routes first (exact match)
    for route_path, (cls, title, param_names, regex, layout_cls) in _routes.items():
        if regex is None and route_path == normalized_path:
            resolved_title = _resolve_title(cls)
            return cls, resolved_title, {}, layout_cls

    # Parameterized routes (uses named groups)
    for route_path, (cls, title, param_names, regexes, layout_cls) in _routes.items():
        if regexes is not None:
            for regex in regexes:
                m = regex.match(normalized_path)
                if m:
                    params = {k: v for k, v in m.groupdict().items() if v is not None}
                    resolved_title = _resolve_title(cls)
                    return cls, resolved_title, params, layout_cls

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
    return {path: cls for path, (cls, _, _, _, _) in _routes.items()}


def clear_routes():
    """Clear all registered routes. Useful for testing."""
    _routes.clear()


def discover_views(package: str) -> list[str]:
    """Import all modules in a package to trigger @Route registration.

    If a module is already imported (e.g. after clear_routes() in tests),
    it will be reloaded to re-execute the @Route decorators.

    Args:
        package: Dotted package name (e.g. "demo.views").

    Returns:
        List of fully qualified module names that were imported.
    """
    import importlib
    import pkgutil
    import sys

    pkg = importlib.import_module(package)
    imported = []
    for _finder, name, _is_pkg in pkgutil.iter_modules(pkg.__path__):
        full_name = f"{package}.{name}"
        if full_name in sys.modules:
            importlib.reload(sys.modules[full_name])
        else:
            importlib.import_module(full_name)
        imported.append(full_name)
    return imported

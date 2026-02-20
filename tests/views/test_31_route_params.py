"""Test View 31: Enhanced Route Parameters -- /test/route-params"""

from vaadin.flow import Route, BeforeEnterEvent
from vaadin.flow.components import Span, VerticalLayout
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


# --- V31.01: Wildcard route ---

@Route("test/files/:path*", page_title="Test: Wildcard")
class TestWildcardView(VerticalLayout):
    def __init__(self):
        self._path = Span("")
        self._path.set_id("wildcard-path")
        self._segments = Span("")
        self._segments.set_id("wildcard-segments")
        self.add(self._path, self._segments)

    def set_parameter(self, params):
        raw = params.get("path", "")
        self._path.set_text(raw)

    def before_enter(self, event):
        segs = event.route_parameters.get_wildcard("path")
        self._segments.set_text(",".join(segs))


# --- V31.02: Mid-position optional ---

@Route("test/user/:id?/profile", page_title="Test: Mid Optional")
class TestMidOptionalView(VerticalLayout):
    def __init__(self):
        self._user_id = Span("")
        self._user_id.set_id("mid-opt-id")
        self._has_id = Span("")
        self._has_id.set_id("mid-opt-has-id")
        self.add(self._user_id, self._has_id)

    def before_enter(self, event):
        uid = event.get("id", "")
        self._user_id.set_text(uid)
        self._has_id.set_text("yes" if "id" in event else "no")


# --- V31.03: BeforeEnterEvent with query params ---

@Route("test/search-params", page_title="Test: Search Params")
class TestSearchParamsView(VerticalLayout):
    def __init__(self):
        self._query = Span("")
        self._query.set_id("search-q")
        self._sort = Span("")
        self._sort.set_id("search-sort")
        self._path = Span("")
        self._path.set_id("search-path")
        self.add(self._query, self._sort, self._path)

    def before_enter(self, event):
        qp = event.location.query_parameters
        self._query.set_text(qp.get_single_parameter("q") or "")
        self._sort.set_text(qp.get_single_parameter("sort") or "")
        self._path.set_text(event.location.path)


# --- V31.04: BeforeEnterEvent dict-compat with route params ---

@Route("test/event-compat/:id", page_title="Test: Event Compat")
class TestEventCompatView(VerticalLayout):
    def __init__(self):
        self._param_id = Span("")
        self._param_id.set_id("compat-id")
        self._has_event = Span("")
        self._has_event.set_id("compat-has-event")
        self._int_id = Span("")
        self._int_id.set_id("compat-int-id")
        self.add(self._param_id, self._has_event, self._int_id)

    def before_enter(self, event):
        # Dict-like access (backward compat)
        self._param_id.set_text(event["id"])
        # Verify it's a BeforeEnterEvent
        self._has_event.set_text("yes" if isinstance(event, BeforeEnterEvent) else "no")
        # Typed access
        self._int_id.set_text(str(event.route_parameters.get_integer("id") or ""))


# --- V31.05: Hub view for navigation (linked from menu) ---

@Route("test/route-params", page_title="Test: Route Params", layout=TestMainLayout)
@Menu(title="31 Route Params", order=31)
class TestRouteParamsView(VerticalLayout):
    def __init__(self):
        self.add(Span("Route params test hub"))

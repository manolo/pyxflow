"""Test View 23: Navigation — /test/navigation"""

from vaadin.flow import Route
from vaadin.flow.components import (
    RouterLink, Span, VerticalLayout,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/navigation", page_title="Test: Navigation", layout=TestMainLayout)
@Menu(title="Navigation", order=20)
class TestNavigationView(VerticalLayout):
    def __init__(self):
        title_span = Span("Navigation view")
        title_span.set_id("nav-title")

        # --- RouterLink ---
        link1 = RouterLink("Go to param view", "test/nav-param/42")
        link1.set_id("link-param")

        link2 = RouterLink("Go to opt param", "test/nav-opt")
        link2.set_id("link-opt")

        link3 = RouterLink("Go to opt param with value", "test/nav-opt/search")
        link3.set_id("link-opt-val")

        self.add(title_span, link1, link2, link3)


@Route("test/nav-param/:id", page_title="Test: Nav Param")
class TestNavParamView(VerticalLayout):
    def __init__(self):
        self._param = Span("")
        self._param.set_id("param")
        self.add(self._param)
        nav_link = RouterLink("Back to nav", "test/navigation")
        nav_link.set_id("nav-back")
        self.add(nav_link)

    def set_parameter(self, params):
        self._param.set_text(params.get("id", ""))


@Route("test/nav-opt/:q?", page_title="Test: Nav Opt")
class TestNavOptView(VerticalLayout):
    def __init__(self):
        self._opt = Span("")
        self._opt.set_id("opt")
        self.add(self._opt)
        nav_link = RouterLink("Back to nav", "test/navigation")
        nav_link.set_id("nav-back")
        self.add(nav_link)

    def set_parameter(self, params):
        self._opt.set_text(params.get("q", ""))

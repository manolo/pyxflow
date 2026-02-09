import logging

from vaadin.flow import Menu, Route

log = logging.getLogger("vaadin.flow")
from demo.services import people_service
from demo.views.main_layout import MainLayout
from vaadin.flow.components import (
    Grid,
    H2,
    H3,
    SortDirection,
    Span,
    VerticalLayout,
)


# Pre-load for lazy data provider
_ALL_PEOPLE = [p.to_dict() for p in people_service.find_all()]


@Route("grid", page_title="Grid Demo", layout=MainLayout)
@Menu(title="Grid", order=3, icon="vaadin:table")
class GridDemoView(VerticalLayout):
    def __init__(self):
        self.set_height_full()

        self.add(H2("Grid Advanced Features Demo"))

        # --- Lazy Loading Grid ---
        self.add(H3("Lazy Loading (200 rows, page size 20)"))
        self.add(Span("Data is fetched on demand as you scroll. Check server logs for fetch calls."))

        self.grid = Grid()
        self.grid.add_column("name", header="Name").set_auto_width(True).set_sortable(True)
        self.grid.add_column("email", header="Email").set_auto_width(True).set_sortable(True)
        self.grid.add_column("role", header="Role").set_sortable(True).set_resizable(True)
        self.grid.add_column("city", header="City").set_auto_width(True).set_sortable(True)
        self.grid.add_column("department", header="Department").set_sortable(True).set_resizable(True)
        self.grid.set_column_reordering_allowed(True)
        self.grid.set_page_size(20)

        self.fetch_count = 0
        self._selected_name = "(none)"
        self.grid.set_data_provider(self._lazy_fetch)

        self.lazy_status = Span("Fetches: 0 | Selected: (none)")
        self.grid.add_selection_listener(self._on_lazy_select)

        self.add(self.grid)
        self.expand(self.grid)
        self.add(self.lazy_status)

    def _lazy_fetch(self, offset, limit, sort_orders):
        self.fetch_count += 1

        items = _ALL_PEOPLE[:]

        # Apply sorting
        for order in reversed(sort_orders):
            prop = order.column.property_name
            rev = order.direction == SortDirection.DESCENDING
            items = sorted(items, key=lambda x, p=prop: x.get(p, ""), reverse=rev)

        page = items[offset:offset + limit]
        log.debug("Lazy fetch #%d: offset=%d, limit=%d, sorts=%d, returning %d of %d",
                  self.fetch_count, offset, limit, len(sort_orders), len(page), len(items))

        self._update_status()
        return page, len(items)

    def _update_status(self):
        self.lazy_status.set_text(f"Fetches: {self.fetch_count} | Selected: {self._selected_name}")

    def _on_lazy_select(self, event):
        item = event.get("item")
        self._selected_name = item["name"] if item else "(none)"
        self._update_status()

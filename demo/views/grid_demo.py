"""Grid demo view showcasing advanced grid features."""

from vaadin.flow import Menu, Route
from demo.services import people_service
from demo.main_layout import MainLayout
from vaadin.flow.components import (
    Button,
    Grid,
    GridSortOrder,
    H2,
    H3,
    HorizontalLayout,
    SelectionMode,
    SortDirection,
    Span,
    VerticalLayout,
)


# Pre-load for lazy data provider
_ALL_PEOPLE = [p.to_dict() for p in people_service.find_all()]


@Route("grid", page_title="Grid Demo", layout=MainLayout)
@Menu(title="Grid", order=3, icon="vaadin:table")
class GridDemoView(VerticalLayout):
    """View demonstrating advanced Grid features: lazy loading, sorting, multi-select."""

    def __init__(self):
        super().__init__()
        self.set_height_full()

        self.add(H2("Grid Advanced Features Demo"))

        # --- Lazy Loading Grid ---
        self.add(H3("Lazy Loading (200 rows, page size 20)"))
        self.add(Span("Data is fetched on demand as you scroll. Check server logs for fetch calls."))

        self.lazy_grid = Grid()
        self.lazy_grid.add_column("name", header="Name").set_auto_width(True).set_sortable(True)
        self.lazy_grid.add_column("email", header="Email").set_auto_width(True).set_sortable(True)
        self.lazy_grid.add_column("role", header="Role").set_sortable(True).set_resizable(True)
        self.lazy_grid.add_column("city", header="City").set_auto_width(True).set_sortable(True)
        self.lazy_grid.add_column("department", header="Department").set_sortable(True).set_resizable(True)
        self.lazy_grid.set_column_reordering_allowed(True)
        self.lazy_grid.set_page_size(20)

        self.fetch_count = 0
        self._selected_name = "(none)"
        self.lazy_grid.set_data_provider(self._lazy_fetch)

        self.lazy_status = Span("Fetches: 0 | Selected: (none)")
        self.lazy_grid.add_selection_listener(self._on_lazy_select)

        self.add(self.lazy_grid)
        self.add(self.lazy_status)

    def _lazy_fetch(self, offset, limit, sort_orders):
        """Lazy data provider - fetches a page of data."""
        self.fetch_count += 1

        items = _ALL_PEOPLE[:]

        # Apply sorting
        for order in reversed(sort_orders):
            prop = order.column.property_name
            rev = order.direction == SortDirection.DESCENDING
            items = sorted(items, key=lambda x, p=prop: x.get(p, ""), reverse=rev)

        page = items[offset:offset + limit]
        print(f"  [GridDemo] Lazy fetch #{self.fetch_count}: offset={offset}, limit={limit}, sorts={len(sort_orders)}, returning {len(page)} of {len(items)}")

        self._update_status()
        return page, len(items)

    def _update_status(self):
        self.lazy_status.set_text(f"Fetches: {self.fetch_count} | Selected: {self._selected_name}")

    def _on_lazy_select(self, event):
        item = event.get("item")
        self._selected_name = item["name"] if item else "(none)"
        self._update_status()

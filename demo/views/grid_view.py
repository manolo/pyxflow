import logging

from pyxflow import Menu, Route

log = logging.getLogger("pyxflow")
from demo.services import people_service
from demo.views.main_layout import MainLayout
from pyxflow.components import *
from pyxflow.data.binder import Binder


# Pre-load for lazy data provider
_ALL_PEOPLE = [p.to_dict() for p in people_service.find_all()]


@Route("grid", page_title="Grid Demo", layout=MainLayout)
@Menu(title="Grid", order=3, icon="vaadin:table")
class GridDemoView(VerticalLayout):
    def __init__(self):
        self.set_height_full()

        hint = Div()
        hint.add_class_name("demo-hint")
        hint.add(Icon("vaadin:info-circle"), Span(
            "Lazy data provider \u2014 rows are fetched on demand as you scroll, "
            "with server-side sorting and single-row selection."))
        self.add(hint)

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


@Route("grid-editor", page_title="Grid Editor Demo", layout=MainLayout)
@Menu(title="Grid Editor", order=4, icon="vaadin:edit")
class GridEditorDemoView(VerticalLayout):
    def __init__(self):
        self.set_height_full()
        self.set_spacing(False)
        self.get_style().set("padding", "0")

        items = [dict(p.to_dict()) for p in people_service.find_all()]

        grid = Grid()
        name_col = grid.add_column("name", header="Name").set_auto_width(True)
        email_col = grid.add_column("email", header="Email").set_auto_width(True)
        role_col = grid.add_column("role", header="Role").set_auto_width(True)
        grid.add_column("city", header="City").set_auto_width(True)
        grid.add_column("department", header="Department").set_auto_width(True)

        # Editor fields
        name_field = TextField()
        email_field = TextField()
        role_field = TextField()

        name_col.set_editor_component(name_field)
        email_col.set_editor_component(email_field)
        role_col.set_editor_component(role_field)

        # Binder
        binder = Binder()
        binder.for_field(name_field).bind(
            lambda item: item.get("name", ""),
            lambda item, val: item.__setitem__("name", val),
        )
        binder.for_field(email_field).bind(
            lambda item: item.get("email", ""),
            lambda item, val: item.__setitem__("email", val),
        )
        binder.for_field(role_field).bind(
            lambda item: item.get("role", ""),
            lambda item, val: item.__setitem__("role", val),
        )

        editor = grid.get_editor()
        editor.set_binder(binder)
        editor.set_buffered(True)

        # Save / Cancel buttons -- start disabled
        btn_save = Button("Save")
        btn_save.add_theme_variants(ButtonVariant.LUMO_PRIMARY)
        btn_save.set_enabled(False)
        btn_cancel = Button("Cancel")
        btn_cancel.set_enabled(False)
        btn_cancel.set_id("editor-cancel-btn")

        # Confirm dialog for cancel
        confirm_dlg = ConfirmDialog(
            "Discard changes?",
            "Unsaved changes will be lost.",
            "Discard",
        )
        confirm_dlg.set_cancel_button_theme("primary")
        confirm_dlg.set_confirm_button_theme("error")
        confirm_dlg.set_cancelable(True)
        confirm_dlg.add_confirm_listener(lambda e: (
            editor.cancel(),
            _update_buttons(),
            Notification.show("Edit cancelled", duration=2000),
        ))

        def _update_buttons():
            is_open = editor.is_open()
            dirty = is_open and binder.is_dirty()
            btn_save.set_enabled(dirty)
            btn_cancel.set_enabled(is_open)
            if dirty:
                btn_save.add_theme_variants(ButtonVariant.LUMO_PRIMARY)
            else:
                btn_save.remove_theme_variants(ButtonVariant.LUMO_PRIMARY)

        binder.add_status_change_listener(_update_buttons)

        # Open on double-click
        def _on_dblclick(e):
            editor.edit_item(e["item"])
            _update_buttons()

        grid.add_item_double_click_listener(_on_dblclick)

        def _on_save(e):
            editor.save()
            _update_buttons()

        def _on_cancel(e):
            if binder.is_dirty():
                confirm_dlg.open()
            else:
                editor.cancel()
                _update_buttons()

        btn_save.add_click_listener(_on_save)
        btn_cancel.add_click_listener(_on_cancel)

        # Escape key on grid triggers cancel (client-side JS -- grid stops
        # propagation of keydown so server-side listeners never fire)
        grid.execute_js("""
            $0.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    var btn = document.getElementById('editor-cancel-btn');
                    if (btn && !btn.disabled) btn.click();
                }
            });
        """)

        editor.add_save_listener(
            lambda e: Notification.show(
                f"Saved: {e.item.get('name', '')}", duration=3000)
        )

        grid.set_items(items)

        # Footer bar with buttons
        footer = HorizontalLayout(btn_save, btn_cancel)
        footer.set_spacing(True)
        footer.get_style().set("padding", "var(--lumo-space-s) var(--lumo-space-m)")
        footer.set_width_full()

        self.add(grid, footer)
        self.expand(grid)

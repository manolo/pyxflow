import os
import pathlib
import subprocess
import sys

from vaadin.flow import Menu, Route
from vaadin.flow.components import *
from vaadin.flow.core.component import ClientCallable
from demo.views.main_layout import MainLayout

_DEMO_ROOT = pathlib.Path(__file__).resolve().parent.parent

def _format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes >= 512 * 1024:
        value = size_bytes / (1024 * 1024)
        return f"{value:,.2f} MB".replace(",", "X").replace(".", ",").replace("X", ".")
    value = size_bytes / 1024
    return f"{value:,.2f} KB".replace(",", "X").replace(".", ",").replace("X", ".")


def _scan_dir(path: pathlib.Path) -> list[dict]:
    try:
        entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        return []
    items = []
    for entry in entries:
        if entry.name.startswith(".") or entry.name == "__pycache__":
            continue
        items.append({
            "name": entry.name,
            "size": _format_size(entry.stat().st_size) if entry.is_file() else "",
            "type": "Folder" if entry.is_dir() else entry.suffix or "file",
            "_path": str(entry),
        })
    return items


def _get_children(item: dict) -> list[dict]:
    p = pathlib.Path(item["_path"])
    if not p.is_dir():
        return []
    depth = len(p.relative_to(_DEMO_ROOT).parts)
    return _scan_dir(p)


@Route("file-explorer", page_title="File Explorer", layout=MainLayout)
@Menu(title="File Explorer", order=11, icon="vaadin:folder-open")
class FileExplorerView(VerticalLayout):
    def __init__(self):
        self.set_height_full()

        hint = Div()
        hint.add_class_name("demo-hint")
        hint.add(Icon("vaadin:info-circle"), Span(
            "@ClientCallable \u2014 TreeGrid with hierarchical browsing; "
            "double-click calls a server method directly from the browser."))
        self.add(hint)

        self.tree_grid = TreeGrid()
        self._name_col = self.tree_grid.add_hierarchy_column(
            lambda item: item.get("name", ""), header="Name",
        )
        self.tree_grid.add_column("size", header="Size").set_auto_width(True).set_text_align("end")
        self.tree_grid.add_column("type", header="Type").set_auto_width(True)

        # Extra header row spanning all columns
        header_row = self.tree_grid.prepend_header_row()
        header_row.join(*self.tree_grid.columns).set_text("Browsing: demo/")

        self._load_data()

        refresh_btn = Button("Refresh")
        refresh_btn.add_click_listener(lambda e: self._load_data())

        self.add(refresh_btn, self.tree_grid)
        self.expand(self.tree_grid)

    def _attach(self, tree):
        super()._attach(tree)
        # Register dblclick → $server.open(key) after grid is attached
        view_ref = {"@v-node": self.element.node_id}
        grid_ref = {"@v-node": self.tree_grid.element.node_id}
        tree.queue_execute([
            view_ref, grid_ref,
            "return (function() {"
            "  $1.addEventListener('dblclick', function(e) {"
            "    var ctx = $1.getEventContext(e);"
            "    if (ctx && ctx.item) { $0.$server.open(ctx.item.key); }"
            "  });"
            "}).apply(null)",
        ])

    @ClientCallable
    def open(self, key):
        item = self.tree_grid._key_to_item.get(str(key))
        if not item:
            return
        path = item.get("_path", "")
        print(f"opening {os.path.relpath(path)}")
        if sys.platform == "darwin":
            subprocess.Popen(["open", path])
        elif sys.platform == "win32":
            os.startfile(path)
        else:
            subprocess.Popen(["xdg-open", path])

    def _load_data(self):
        root_items = _scan_dir(_DEMO_ROOT)
        self.tree_grid.set_items(root_items, children_provider=_get_children)
        self._name_col.set_footer_text(f"{len(root_items)} entries")

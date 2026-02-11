import pathlib

from vaadin.flow import Menu, Route
from vaadin.flow.components import Button, TreeGrid, VerticalLayout
from demo.views.main_layout import MainLayout


_DEMO_ROOT = pathlib.Path(__file__).resolve().parent.parent
_MAX_DEPTH = 3


def _scan_dir(path: pathlib.Path) -> list[dict]:
    """Scan a directory and return sorted entries (dirs first, then files)."""
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
            "size": entry.stat().st_size if entry.is_file() else "",
            "type": "Folder" if entry.is_dir() else entry.suffix or "file",
            "_path": str(entry),
        })
    return items


def _get_children(item: dict) -> list[dict]:
    """Children provider: returns directory contents up to MAX_DEPTH."""
    p = pathlib.Path(item["_path"])
    if not p.is_dir():
        return []
    depth = len(p.relative_to(_DEMO_ROOT).parts)
    if depth >= _MAX_DEPTH:
        return []
    return _scan_dir(p)


@Route("file-explorer", page_title="File Explorer", layout=MainLayout)
@Menu(title="File Explorer", order=11, icon="vaadin:folder-open")
class FileExplorerView(VerticalLayout):
    def __init__(self):
        self.set_height_full()

        self.tree_grid = TreeGrid()
        self._name_col = self.tree_grid.add_hierarchy_column(
            lambda item: item.get("name", ""), header="Name",
        )
        self.tree_grid.add_column("size", header="Size").set_auto_width(True)
        self.tree_grid.add_column("type", header="Type").set_auto_width(True)

        # Extra header row spanning all columns
        header_row = self.tree_grid.prepend_header_row()
        header_row.join(*self.tree_grid.columns).set_text("Browsing: demo/")

        self._load_data()

        refresh_btn = Button("Refresh")
        refresh_btn.add_click_listener(lambda e: self._load_data())

        self.add(refresh_btn, self.tree_grid)
        self.expand(self.tree_grid)

    def _load_data(self):
        root_items = _scan_dir(_DEMO_ROOT)
        self.tree_grid.set_items(root_items, children_provider=_get_children)
        self._name_col.set_footer_text(f"{len(root_items)} entries")

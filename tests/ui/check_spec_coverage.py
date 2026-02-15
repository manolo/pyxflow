#!/usr/bin/env python3
"""Check UI spec coverage: compare SPECS.md scenario IDs against @pytest.mark.spec markers.

Usage:
    python tests/ui/check_spec_coverage.py              # full report
    python tests/ui/check_spec_coverage.py --missing     # only missing (actionable) specs
    python tests/ui/check_spec_coverage.py V08           # filter by view
    python tests/ui/check_spec_coverage.py --json        # machine-readable output

Specs in SPECS.md can be tagged with [skip:reason] to mark them as non-critical:
    Scenario: V07.18 — DatePicker value survives mSync+change cycle [skip:unit]

Recognized skip reasons:
    [skip:unit]   — covered by unit tests, UI test adds little value
    [skip:flaky]  — unreliable in Playwright (timing, overlays, complex interaction)
    [skip:minor]  — low-value edge case
"""

import ast
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPECS_FILE = HERE / "SPECS.md"
TEST_GLOB = "test_*.py"

# View number → route name (for display)
VIEW_NAMES = {
    1: "buttons-icons", 2: "text-inputs", 3: "number-inputs",
    4: "checkbox-radio", 5: "select-listbox", 6: "combo-box",
    7: "date-time", 8: "grid-basic", 9: "grid-features",
    10: "tree-grid", 11: "dialog", 12: "notification-popover",
    13: "tabs-accordion", 14: "menu", 15: "layouts",
    16: "card-scroller", 17: "upload", 18: "display",
    19: "html-elements", 20: "component-api", 21: "field-mixins",
    22: "binder", 23: "navigation", 24: "push",
    25: "theme", 26: "client-callable", 27: "custom-field",
    28: "virtual-list", 29: "login", 30: "server-errors",
}

SKIP_RE = re.compile(r"\[skip:(\w+)\]")


def parse_specs():
    """Parse SPECS.md → dict of {spec_id: (name, skip_reason|None)}."""
    specs = {}
    text = SPECS_FILE.read_text()
    for m in re.finditer(r"Scenario: (V\d{2}\.\d{2}) — (.+)", text):
        raw_name = m.group(2).strip()
        skip_match = SKIP_RE.search(raw_name)
        if skip_match:
            skip_reason = skip_match.group(1)
            name = SKIP_RE.sub("", raw_name).strip()
        else:
            skip_reason = None
            name = raw_name
        specs[m.group(1)] = (name, skip_reason)
    return specs


def parse_tests():
    """Parse all test files → dict of {spec_id: (file, class, method)}."""
    markers = {}
    for test_file in sorted(HERE.glob(TEST_GLOB)):
        try:
            tree = ast.parse(test_file.read_text(), filename=str(test_file))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        for dec in item.decorator_list:
                            ids = _extract_spec_ids(dec)
                            for sid in ids:
                                markers[sid] = (
                                    test_file.name,
                                    class_name,
                                    item.name,
                                )
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Top-level test functions (not in a class)
                if node.name.startswith("test_"):
                    for dec in node.decorator_list:
                        ids = _extract_spec_ids(dec)
                        for sid in ids:
                            markers[sid] = (test_file.name, None, node.name)
    return markers


def _extract_spec_ids(decorator):
    """Extract spec IDs from a @pytest.mark.spec(...) decorator AST node."""
    # Match: pytest.mark.spec("V01.01") or pytest.mark.spec("V01.01", "V01.02")
    if isinstance(decorator, ast.Call):
        func = decorator.func
        if (
            isinstance(func, ast.Attribute)
            and func.attr == "spec"
            and isinstance(func.value, ast.Attribute)
            and func.value.attr == "mark"
        ):
            return [
                arg.value
                for arg in decorator.args
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str)
            ]
    return []


def view_of(spec_id):
    """V01.05 → 1"""
    return int(spec_id[1:3])


def main():
    args = sys.argv[1:]
    show_missing_only = "--missing" in args
    json_mode = "--json" in args
    view_filter = None
    for a in args:
        if re.match(r"V\d{2}$", a):
            view_filter = int(a[1:])

    specs = parse_specs()
    markers = parse_tests()

    # Group by view
    views = {}
    for sid in sorted(specs):
        v = view_of(sid)
        views.setdefault(v, []).append(sid)

    if json_mode:
        import json
        result = {}
        for v in sorted(views):
            if view_filter and v != view_filter:
                continue
            sids = views[v]
            implemented = [s for s in sids if s in markers]
            skipped = [s for s in sids if s not in markers and specs[s][1]]
            missing = [s for s in sids if s not in markers and not specs[s][1]]
            result[f"V{v:02d}"] = {
                "name": VIEW_NAMES.get(v, "?"),
                "total": len(sids),
                "implemented": implemented,
                "skipped": skipped,
                "missing": missing,
            }
        total = sum(len(v["implemented"]) + len(v["missing"]) + len(v["skipped"]) for v in result.values())
        impl = sum(len(v["implemented"]) for v in result.values())
        skip = sum(len(v["skipped"]) for v in result.values())
        actionable = total - skip
        print(json.dumps({
            "total": total, "implemented": impl, "skipped": skip,
            "actionable": actionable, "views": result,
        }, indent=2))
        return

    total_specs = 0
    total_impl = 0
    total_skip = 0

    for v in sorted(views):
        if view_filter and v != view_filter:
            continue
        sids = views[v]
        implemented = [s for s in sids if s in markers]
        skipped = [s for s in sids if s not in markers and specs[s][1]]
        missing = [s for s in sids if s not in markers and not specs[s][1]]
        n_total = len(sids)
        n_impl = len(implemented)
        n_skip = len(skipped)
        n_actionable = n_total - n_skip
        total_specs += n_total
        total_impl += n_impl
        total_skip += n_skip

        if show_missing_only and not missing:
            continue

        pct = n_impl / n_actionable * 100 if n_actionable else 100
        bar_len = 20
        filled = int(bar_len * n_impl / n_actionable) if n_actionable else bar_len
        bar = "=" * filled + "-" * (bar_len - filled)
        vname = VIEW_NAMES.get(v, "?")

        summary = f"View {v:2d} ({vname:20s}): {n_impl:3d}/{n_actionable:3d}"
        if n_skip:
            summary += f" (+{n_skip} skip)"
        summary += f"  [{bar}]  {pct:.0f}%"
        if missing:
            summary += f"  Missing: {', '.join(missing)}"
        print(summary)

        if not show_missing_only:
            for sid in sids:
                name, skip_reason = specs[sid]
                if sid in markers:
                    f, cls, method = markers[sid]
                    loc = f"  → {f}::{cls}::{method}" if cls else f"  → {f}::{method}"
                    print(f"    [x] {sid} — {name}{loc}")
                elif skip_reason:
                    print(f"    [-] {sid} — {name}  [skip:{skip_reason}]")
                else:
                    print(f"    [ ] {sid} — {name}")

    print()
    actionable = total_specs - total_skip
    pct = total_impl / actionable * 100 if actionable else 100
    print(f"Total: {total_impl}/{actionable} actionable ({pct:.1f}%)", end="")
    if total_skip:
        print(f"  — {total_skip} skipped")
    else:
        print()


if __name__ == "__main__":
    main()

"""Root test configuration — shared across unit and UI tests."""

from pathlib import Path


def pytest_addoption(parser):
    parser.addoption(
        "--all",
        action="store_true",
        default=False,
        help="Run all tests including UI tests (unit + UI).",
    )


def pytest_configure(config):
    if config.getoption("--all", default=False):
        ui_dir = str(Path(__file__).parent / "ui")
        # Append tests/ui/ to the collection paths so both unit and UI run
        if ui_dir not in config.args:
            config.args.append(ui_dir)

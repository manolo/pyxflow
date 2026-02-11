# vaadin-pyflow

Python implementation of Vaadin Flow - Server-side UI framework for Python.

Uses Vaadin's existing frontend (web components + FlowClient.js) with a Python server implementing the UIDL protocol. All 49 Vaadin 25 UI components are supported.

## Installation

```bash
# From PyPI (when published)
pip install vaadin-pyflow

# From GitHub
pip install git+https://github.com/manolo/vaadin-pyflow.git

# Development mode
pip install -e ".[dev]"
```

## Quick Start

Create a project with a `views` module:

```
myapp/
  __init__.py
  __main__.py
  views/
    __init__.py
    hello.py
```

```python
# myapp/views/hello.py
from vaadin.flow.components import Button, TextField, VerticalLayout, Span
from vaadin.flow.router import Route

@Route("")
class HelloWorldView(VerticalLayout):
    def __init__(self):
        super().__init__()
        self.text_field = TextField("Your name")
        self.button = Button("Say hello")
        self.button.add_click_listener(
            lambda e: self.add(Span(f"Hello {self.text_field.value}"))
        )
        self.add(self.text_field, self.button)
```

```python
# myapp/__main__.py
from vaadin.flow import FlowApp

FlowApp(port=8080).run()
```

```bash
python -m myapp
# Open http://localhost:8080
```

Or use the CLI:

```bash
vaadin myapp.views --port 8080
vaadin myapp.views --port 8080 --dev   # Auto-reload on changes
```

## Demos

```bash
# Clone and run the built-in demo
git clone https://github.com/manolo/vaadin-pyflow.git
cd vaadin-pyflow
pip install -e .
python -m demo
# http://localhost:8088
```

See [demo/](demo/) for the demo views.

## Features

- **49 components** - Button, TextField, Grid, Dialog, ComboBox, DatePicker, AppLayout, and more
- **Server-side routing** - `@Route`, `@Route(layout=...)`, navigation guards
- **Data binding** - `Binder` with validators, converters, dirty tracking
- **WebSocket Push** - Real-time updates via `UI.access()`
- **Dev mode** - Auto-reload on Python file changes (`--dev`)
- **Lumo & Aura themes** - Runtime theme switching with dark mode

## Running Tests

```bash
pip install -e ".[dev]"
pytest
```

## License

Apache License 2.0

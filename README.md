# vaadin-pyflow

Python implementation of Vaadin Flow - Server-side UI framework for Python.

## Installation

```bash
pip install vaadin-pyflow
```

## Quick Start

```python
from vaadin.flow.components import Button, TextField, VerticalLayout, Span
from vaadin.flow.server import run_server

class HelloWorldView(VerticalLayout):
    def __init__(self):
        super().__init__()
        self.text_field = TextField("Your name")
        self.button = Button("Say hello")
        self.button.add_click_listener(
            lambda e: self.add(Span(f"Hello {self.text_field.value}"))
        )
        self.add(self.text_field, self.button)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_server(HelloWorldView, port=8080))
```

## Demos

```bash
python -m demo
# http://localhost:8088
```

See [demo/](demo/) for the demo views.

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## License

Apache License 2.0

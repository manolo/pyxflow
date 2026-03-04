# @ClientCallable

Allows client-side JavaScript to call Python methods on the server.

## Basic Usage

```python
from pyxflow import Route
from pyxflow.components import VerticalLayout, Div, ClientCallable

@Route("custom")
class CustomView(VerticalLayout):
    def __init__(self):
        self.result = Div()
        self.add(self.result)
        # Call from JS: this.$server.greet("World")
        self.execute_js('this.$server.greet("World")')

    @ClientCallable
    def greet(self, name: str):
        self.result.set_text(f"Hello, {name}!")
```

## With Return Values

```python
@ClientCallable
def calculate(self, a: float, b: float) -> float:
    return a + b
```

The return value is delivered as a resolved Promise on the client:

```javascript
const result = await this.$server.calculate(2, 3);
console.log(result); // 5.0
```

## execute_js to Invoke

```python
# Call server method from component JS
self.execute_js('this.$server.methodName(arg1, arg2)')

# Or with element reference
self.execute_js('$0.querySelector("input").value', some_element)
```

## Key Points

- Methods decorated with `@ClientCallable` are automatically registered
- The decorator scans the class MRO during `_attach()`
- Client calls arrive as RPCs and are processed server-side
- Return values are sent back as resolved promises
- Use `self.execute_js()` (not `self.element.execute_js()`) to safely buffer before attach

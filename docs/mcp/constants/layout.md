# Layout Constants

## Alignment

Item alignment values (align-items / align-self CSS property).

```python
from pyxflow.components import Alignment
```

| Name | Value |
|------|-------|
| `Alignment.START` | `"flex-start"` |
| `Alignment.END` | `"flex-end"` |
| `Alignment.CENTER` | `"center"` |
| `Alignment.STRETCH` | `"stretch"` |
| `Alignment.BASELINE` | `"baseline"` |
| `Alignment.AUTO` | `"auto"` |

## AppLayoutSection

Sections that can be used as primary in AppLayout.

NAVBAR — navbar takes full width, drawer below (default).
DRAWER — drawer takes full height, navbar beside it.

```python
from pyxflow.components import AppLayoutSection
```

| Name | Value |
|------|-------|
| `AppLayoutSection.NAVBAR` | `"navbar"` |
| `AppLayoutSection.DRAWER` | `"drawer"` |

## ContentAlignment

Content alignment values (align-content CSS property).

```python
from pyxflow.components import ContentAlignment
```

| Name | Value |
|------|-------|
| `ContentAlignment.START` | `"flex-start"` |
| `ContentAlignment.END` | `"flex-end"` |
| `ContentAlignment.CENTER` | `"center"` |
| `ContentAlignment.STRETCH` | `"stretch"` |
| `ContentAlignment.SPACE_BETWEEN` | `"space-between"` |
| `ContentAlignment.SPACE_AROUND` | `"space-around"` |

## FlexDirection

Flex direction values (flex-direction CSS property).

```python
from pyxflow.components import FlexDirection
```

| Name | Value |
|------|-------|
| `FlexDirection.ROW` | `"row"` |
| `FlexDirection.ROW_REVERSE` | `"row-reverse"` |
| `FlexDirection.COLUMN` | `"column"` |
| `FlexDirection.COLUMN_REVERSE` | `"column-reverse"` |

## FlexWrap

Flex wrap values (flex-wrap CSS property).

```python
from pyxflow.components import FlexWrap
```

| Name | Value |
|------|-------|
| `FlexWrap.NOWRAP` | `"nowrap"` |
| `FlexWrap.WRAP` | `"wrap"` |
| `FlexWrap.WRAP_REVERSE` | `"wrap-reverse"` |

## JustifyContentMode

Justify content values (justify-content CSS property).

```python
from pyxflow.components import JustifyContentMode
```

| Name | Value |
|------|-------|
| `JustifyContentMode.START` | `"flex-start"` |
| `JustifyContentMode.END` | `"flex-end"` |
| `JustifyContentMode.CENTER` | `"center"` |
| `JustifyContentMode.BETWEEN` | `"space-between"` |
| `JustifyContentMode.AROUND` | `"space-around"` |
| `JustifyContentMode.EVENLY` | `"space-evenly"` |

## Orientation

Orientation for SplitLayout and similar components.

```python
from pyxflow.components import Orientation
```

| Name | Value |
|------|-------|
| `Orientation.HORIZONTAL` | `"horizontal"` |
| `Orientation.VERTICAL` | `"vertical"` |

## PopoverPosition

Position for Popover.

```python
from pyxflow.components import PopoverPosition
```

| Name | Value |
|------|-------|
| `PopoverPosition.BOTTOM` | `"bottom"` |
| `PopoverPosition.BOTTOM_START` | `"bottom-start"` |
| `PopoverPosition.BOTTOM_END` | `"bottom-end"` |
| `PopoverPosition.TOP` | `"top"` |
| `PopoverPosition.TOP_START` | `"top-start"` |
| `PopoverPosition.TOP_END` | `"top-end"` |
| `PopoverPosition.START` | `"start"` |
| `PopoverPosition.START_TOP` | `"start-top"` |
| `PopoverPosition.START_BOTTOM` | `"start-bottom"` |
| `PopoverPosition.END` | `"end"` |
| `PopoverPosition.END_TOP` | `"end-top"` |
| `PopoverPosition.END_BOTTOM` | `"end-bottom"` |

## ScrollDirection

Scroll direction for Scroller.

```python
from pyxflow.components import ScrollDirection
```

| Name | Value |
|------|-------|
| `ScrollDirection.VERTICAL` | `"vertical"` |
| `ScrollDirection.HORIZONTAL` | `"horizontal"` |
| `ScrollDirection.BOTH` | `"both"` |
| `ScrollDirection.NONE` | `"none"` |

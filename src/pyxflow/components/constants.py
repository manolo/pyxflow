"""Consolidated constants (enums) for Vaadin Flow components.

All enums used by components live here. Component files re-export
for backward compatibility.

Convention: all enums inherit from (str, Enum) so that str(member) == member.value.
Theme variant enums use LUMO_/AURA_ prefixed names matching Java exactly.
"""

from enum import Enum


# ---------------------------------------------------------------------------
#  Layout enums (from flex_layout / horizontal_layout)
# ---------------------------------------------------------------------------

class FlexDirection(str, Enum):
    """Flex direction values (flex-direction CSS property)."""
    ROW = "row"
    ROW_REVERSE = "row-reverse"
    COLUMN = "column"
    COLUMN_REVERSE = "column-reverse"


class FlexWrap(str, Enum):
    """Flex wrap values (flex-wrap CSS property)."""
    NOWRAP = "nowrap"
    WRAP = "wrap"
    WRAP_REVERSE = "wrap-reverse"


class JustifyContentMode(str, Enum):
    """Justify content values (justify-content CSS property)."""
    START = "flex-start"
    END = "flex-end"
    CENTER = "center"
    BETWEEN = "space-between"
    AROUND = "space-around"
    EVENLY = "space-evenly"


class ContentAlignment(str, Enum):
    """Content alignment values (align-content CSS property)."""
    START = "flex-start"
    END = "flex-end"
    CENTER = "center"
    STRETCH = "stretch"
    SPACE_BETWEEN = "space-between"
    SPACE_AROUND = "space-around"


class Alignment(str, Enum):
    """Item alignment values (align-items / align-self CSS property)."""
    START = "flex-start"
    END = "flex-end"
    CENTER = "center"
    STRETCH = "stretch"
    BASELINE = "baseline"
    AUTO = "auto"


class Orientation(str, Enum):
    """Orientation for SplitLayout and similar components."""
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


# ---------------------------------------------------------------------------
#  Scroll / Popover position enums
# ---------------------------------------------------------------------------

class ScrollDirection(str, Enum):
    """Scroll direction for Scroller."""
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
    BOTH = "both"
    NONE = "none"


class PopoverPosition(str, Enum):
    """Position for Popover."""
    BOTTOM = "bottom"
    BOTTOM_START = "bottom-start"
    BOTTOM_END = "bottom-end"
    TOP = "top"
    TOP_START = "top-start"
    TOP_END = "top-end"
    START = "start"
    START_TOP = "start-top"
    START_BOTTOM = "start-bottom"
    END = "end"
    END_TOP = "end-top"
    END_BOTTOM = "end-bottom"


# ---------------------------------------------------------------------------
#  Grid enums
# ---------------------------------------------------------------------------

class SortDirection(str, Enum):
    """Sort direction for grid columns."""
    ASCENDING = "asc"
    DESCENDING = "desc"


class GridDropMode(str, Enum):
    """Grid drop mode for drag-and-drop."""
    BETWEEN = "between"
    ON_TOP = "on-top"
    ON_TOP_OR_BETWEEN = "on-top-or-between"
    ON_GRID = "on-grid"


class AutoExpandMode(str, Enum):
    """MultiSelectComboBox auto-expand mode."""
    NONE = "none"
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
    BOTH = "both"


class SelectionMode(str, Enum):
    """Grid selection mode."""
    SINGLE = "SINGLE"
    MULTI = "MULTI"
    NONE = "NONE"


class ColumnTextAlign(str, Enum):
    """Text alignment for grid columns."""
    START = "start"
    CENTER = "center"
    END = "end"


# ---------------------------------------------------------------------------
#  ValueChangeMode
# ---------------------------------------------------------------------------

class ValueChangeMode(str, Enum):
    """Controls when a text field syncs its value to the server.

    EAGER — fires on every keystroke ("input" event)
    LAZY — fires after a debounce timeout ("input" event, behaves like EAGER for now)
    TIMEOUT — fires after a timeout ("input" event, behaves like EAGER for now)
    ON_BLUR — fires when the field loses focus ("blur" event)
    ON_CHANGE — fires on change event (default, "change" event)
    """
    EAGER = "eager"
    LAZY = "lazy"
    TIMEOUT = "timeout"
    ON_BLUR = "on_blur"
    ON_CHANGE = "on_change"


# ---------------------------------------------------------------------------
#  Autocomplete (HTML autocomplete attribute values)
# ---------------------------------------------------------------------------

class Autocomplete(str, Enum):
    """HTML autocomplete attribute values."""
    OFF = "off"
    ON = "on"
    NAME = "name"
    HONORIFIC_PREFIX = "honorific-prefix"
    GIVEN_NAME = "given-name"
    ADDITIONAL_NAME = "additional-name"
    FAMILY_NAME = "family-name"
    HONORIFIC_SUFFIX = "honorific-suffix"
    NICKNAME = "nickname"
    EMAIL = "email"
    USERNAME = "username"
    NEW_PASSWORD = "new-password"
    CURRENT_PASSWORD = "current-password"
    ORGANIZATION_TITLE = "organization-title"
    ORGANIZATION = "organization"
    STREET_ADDRESS = "street-address"
    ADDRESS_LINE1 = "address-line1"
    ADDRESS_LINE2 = "address-line2"
    ADDRESS_LINE3 = "address-line3"
    ADDRESS_LEVEL1 = "address-level1"
    ADDRESS_LEVEL2 = "address-level2"
    ADDRESS_LEVEL3 = "address-level3"
    ADDRESS_LEVEL4 = "address-level4"
    COUNTRY = "country"
    COUNTRY_NAME = "country-name"
    POSTAL_CODE = "postal-code"
    CC_NAME = "cc-name"
    CC_GIVEN_NAME = "cc-given-name"
    CC_ADDITIONAL_NAME = "cc-additional-name"
    CC_FAMILY_NAME = "cc-family-name"
    CC_NUMBER = "cc-number"
    CC_EXP = "cc-exp"
    CC_EXP_MONTH = "cc-exp-month"
    CC_EXP_YEAR = "cc-exp-year"
    CC_CSC = "cc-csc"
    CC_TYPE = "cc-type"
    TRANSACTION_CURRENCY = "transaction-currency"
    TRANSACTION_AMOUNT = "transaction-amount"
    LANGUAGE = "language"
    BDAY = "bday"
    BDAY_DAY = "bday-day"
    BDAY_MONTH = "bday-month"
    BDAY_YEAR = "bday-year"
    SEX = "sex"
    TEL = "tel"
    TEL_COUNTRY_CODE = "tel-country-code"
    TEL_NATIONAL = "tel-national"
    TEL_AREA_CODE = "tel-area-code"
    TEL_LOCAL = "tel-local"
    TEL_LOCAL_PREFIX = "tel-local-prefix"
    TEL_LOCAL_SUFFIX = "tel-local-suffix"
    TEL_EXTENSION = "tel-extension"
    URL = "url"
    PHOTO = "photo"


# ===========================================================================
#  Theme Variant enums — one per component, matching Java exactly
# ===========================================================================

class NotificationVariant(str, Enum):
    """Theme variants for Notification."""
    LUMO_PRIMARY = "primary"
    LUMO_CONTRAST = "contrast"
    LUMO_SUCCESS = "success"
    LUMO_ERROR = "error"
    LUMO_WARNING = "warning"


class ButtonVariant(str, Enum):
    """Theme variants for Button."""
    LUMO_SMALL = "small"
    LUMO_LARGE = "large"
    LUMO_TERTIARY = "tertiary"
    LUMO_TERTIARY_INLINE = "tertiary-inline"
    LUMO_PRIMARY = "primary"
    LUMO_SUCCESS = "success"
    LUMO_WARNING = "warning"
    LUMO_ERROR = "error"
    LUMO_CONTRAST = "contrast"
    LUMO_ICON = "icon"
    AURA_PRIMARY = "primary"
    AURA_TERTIARY = "tertiary"
    AURA_DANGER = "danger"


class GridVariant(str, Enum):
    """Theme variants for Grid."""
    LUMO_NO_BORDER = "no-border"
    LUMO_NO_ROW_BORDERS = "no-row-borders"
    LUMO_COLUMN_BORDERS = "column-borders"
    LUMO_ROW_STRIPES = "row-stripes"
    LUMO_COMPACT = "compact"
    LUMO_WRAP_CELL_CONTENT = "wrap-cell-content"
    AURA_NO_BORDER = "no-border"
    AURA_NO_ROW_BORDERS = "no-row-borders"
    AURA_COLUMN_BORDERS = "column-borders"
    AURA_ROW_STRIPES = "row-stripes"
    AURA_WRAP_CELL_CONTENT = "wrap-cell-content"


class TextFieldVariant(str, Enum):
    """Theme variants for TextField."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class TextAreaVariant(str, Enum):
    """Theme variants for TextArea."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class ComboBoxVariant(str, Enum):
    """Theme variants for ComboBox."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_LEFT = "align-left"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class MultiSelectComboBoxVariant(str, Enum):
    """Theme variants for MultiSelectComboBox."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_LEFT = "align-left"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class SelectVariant(str, Enum):
    """Theme variants for Select."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_LEFT = "align-left"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class DatePickerVariant(str, Enum):
    """Theme variants for DatePicker."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_LEFT = "align-left"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class TimePickerVariant(str, Enum):
    """Theme variants for TimePicker."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_LEFT = "align-left"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class DateTimePickerVariant(str, Enum):
    """Theme variants for DateTimePicker."""
    LUMO_SMALL = "small"
    LUMO_ALIGN_LEFT = "align-left"
    LUMO_ALIGN_CENTER = "align-center"
    LUMO_ALIGN_RIGHT = "align-right"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_ALIGN_LEFT = "align-left"
    AURA_ALIGN_CENTER = "align-center"
    AURA_ALIGN_RIGHT = "align-right"
    AURA_ALIGN_START = "align-start"
    AURA_ALIGN_END = "align-end"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class CheckboxVariant(str, Enum):
    """Theme variants for Checkbox."""
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class CheckboxGroupVariant(str, Enum):
    """Theme variants for CheckboxGroup."""
    LUMO_VERTICAL = "vertical"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_HORIZONTAL = "horizontal"


class RadioGroupVariant(str, Enum):
    """Theme variants for RadioButtonGroup."""
    LUMO_VERTICAL = "vertical"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"
    AURA_HORIZONTAL = "horizontal"


class AvatarVariant(str, Enum):
    """Theme variants for Avatar."""
    LUMO_XLARGE = "xlarge"
    LUMO_LARGE = "large"
    LUMO_SMALL = "small"
    LUMO_XSMALL = "xsmall"
    AURA_FILLED = "filled"


class AvatarGroupVariant(str, Enum):
    """Theme variants for AvatarGroup."""
    LUMO_XLARGE = "xlarge"
    LUMO_LARGE = "large"
    LUMO_SMALL = "small"
    LUMO_XSMALL = "xsmall"
    LUMO_REVERSE = "reverse"
    AURA_FILLED = "filled"
    AURA_REVERSE = "reverse"


class DialogVariant(str, Enum):
    """Theme variants for Dialog."""
    LUMO_NO_PADDING = "no-padding"
    AURA_NO_PADDING = "no-padding"


class MenuBarVariant(str, Enum):
    """Theme variants for MenuBar."""
    LUMO_SMALL = "small"
    LUMO_LARGE = "large"
    LUMO_TERTIARY = "tertiary"
    LUMO_TERTIARY_INLINE = "tertiary-inline"
    LUMO_PRIMARY = "primary"
    LUMO_CONTRAST = "contrast"
    LUMO_ICON = "icon"
    LUMO_END_ALIGNED = "end-aligned"
    LUMO_DROPDOWN_INDICATORS = "dropdown-indicators"
    AURA_END_ALIGNED = "end-aligned"
    AURA_PRIMARY = "primary"
    AURA_TERTIARY = "tertiary"


class TabsVariant(str, Enum):
    """Theme variants for Tabs."""
    LUMO_CENTERED = "centered"
    LUMO_SMALL = "small"
    LUMO_MINIMAL = "minimal"
    LUMO_HIDE_SCROLL_BUTTONS = "hide-scroll-buttons"
    LUMO_EQUAL_WIDTH_TABS = "equal-width-tabs"
    LUMO_SHOW_SCROLL_BUTTONS = "show-scroll-buttons"
    AURA_HIDE_SCROLL_BUTTONS = "hide-scroll-buttons"
    AURA_SHOW_SCROLL_BUTTONS = "show-scroll-buttons"
    AURA_FILLED = "filled"


class TabVariant(str, Enum):
    """Theme variants for Tab."""
    LUMO_ICON_ON_TOP = "icon-on-top"


class TabSheetVariant(str, Enum):
    """Theme variants for TabSheet."""
    LUMO_TABS_CENTERED = "centered"
    LUMO_TABS_SMALL = "small"
    LUMO_TABS_MINIMAL = "minimal"
    LUMO_TABS_HIDE_SCROLL_BUTTONS = "hide-scroll-buttons"
    LUMO_TABS_EQUAL_WIDTH_TABS = "equal-width-tabs"
    LUMO_BORDERED = "bordered"
    LUMO_NO_PADDING = "no-padding"
    LUMO_TABS_SHOW_SCROLL_BUTTONS = "show-scroll-buttons"
    AURA_TABS_HIDE_SCROLL_BUTTONS = "hide-scroll-buttons"
    AURA_TABS_SHOW_SCROLL_BUTTONS = "show-scroll-buttons"
    AURA_NO_PADDING = "no-padding"
    AURA_NO_BORDER = "no-border"
    AURA_TABS_FILLED = "filled"


class DetailsVariant(str, Enum):
    """Theme variants for Details."""
    LUMO_FILLED = "filled"
    AURA_FILLED = "filled"
    LUMO_REVERSE = "reverse"
    AURA_REVERSE = "reverse"
    LUMO_SMALL = "small"
    AURA_SMALL = "small"
    AURA_NO_PADDING = "no-padding"


class UploadVariant(str, Enum):
    """Theme variants for Upload."""
    AURA_NO_BORDER = "no-border"


class ProgressBarVariant(str, Enum):
    """Theme variants for ProgressBar."""
    LUMO_CONTRAST = "contrast"
    LUMO_ERROR = "error"
    LUMO_SUCCESS = "success"


class PopoverVariant(str, Enum):
    """Theme variants for Popover."""
    LUMO_NO_PADDING = "no-padding"
    LUMO_ARROW = "arrow"
    AURA_NO_PADDING = "no-padding"
    AURA_ARROW = "arrow"


class ScrollerVariant(str, Enum):
    """Theme variants for Scroller."""
    LUMO_OVERFLOW_INDICATORS = "overflow-indicators"
    LUMO_OVERFLOW_INDICATOR_TOP = "overflow-indicator-top"
    LUMO_OVERFLOW_INDICATOR_BOTTOM = "overflow-indicator-bottom"
    AURA_OVERFLOW_INDICATORS = "overflow-indicators"
    AURA_OVERFLOW_INDICATOR_TOP = "overflow-indicator-top"
    AURA_OVERFLOW_INDICATOR_BOTTOM = "overflow-indicator-bottom"


class VerticalLayoutVariant(str, Enum):
    """Theme variants for VerticalLayout."""
    LUMO_MARGIN = "margin"
    LUMO_PADDING = "padding"
    LUMO_SPACING_XS = "spacing-xs"
    LUMO_SPACING_S = "spacing-s"
    LUMO_SPACING = "spacing"
    LUMO_SPACING_L = "spacing-l"
    LUMO_SPACING_XL = "spacing-xl"
    LUMO_WRAP = "wrap"
    AURA_MARGIN = "margin"
    AURA_PADDING = "padding"
    AURA_SPACING = "spacing"
    AURA_WRAP = "wrap"


class HorizontalLayoutVariant(str, Enum):
    """Theme variants for HorizontalLayout."""
    LUMO_MARGIN = "margin"
    LUMO_PADDING = "padding"
    LUMO_SPACING_XS = "spacing-xs"
    LUMO_SPACING_S = "spacing-s"
    LUMO_SPACING = "spacing"
    LUMO_SPACING_L = "spacing-l"
    LUMO_SPACING_XL = "spacing-xl"
    LUMO_WRAP = "wrap"
    AURA_MARGIN = "margin"
    AURA_PADDING = "padding"
    AURA_SPACING = "spacing"
    AURA_WRAP = "wrap"


class MessageInputVariant(str, Enum):
    """Theme variants for MessageInput."""
    AURA_ICON_BUTTON = "icon-button"


class CustomFieldVariant(str, Enum):
    """Theme variants for CustomField."""
    LUMO_SMALL = "small"
    LUMO_HELPER_ABOVE_FIELD = "helper-above-field"
    LUMO_WHITESPACE = "whitespace"
    AURA_HELPER_ABOVE_FIELD = "helper-above-field"


class SideNavVariant(str, Enum):
    """Theme variants for SideNav."""
    AURA_FILLED = "filled"


class SplitLayoutVariant(str, Enum):
    """Theme variants for SplitLayout."""
    LUMO_SMALL = "small"
    LUMO_MINIMAL = "minimal"
    AURA_SMALL = "small"


class MasterDetailLayoutVariant(str, Enum):
    """Theme variants for MasterDetailLayout."""
    AURA_INSET_DRAWER = "inset-drawer"


class CardVariant(str, Enum):
    """Theme variants for Card."""
    LUMO_ELEVATED = "elevated"
    LUMO_OUTLINED = "outlined"
    LUMO_HORIZONTAL = "horizontal"
    LUMO_STRETCH_MEDIA = "stretch-media"
    LUMO_COVER_MEDIA = "cover-media"
    AURA_ELEVATED = "elevated"
    AURA_OUTLINED = "outlined"
    AURA_HORIZONTAL = "horizontal"
    AURA_STRETCH_MEDIA = "stretch-media"
    AURA_COVER_MEDIA = "cover-media"


class VirtualListVariant(str, Enum):
    """Theme variants for VirtualList."""
    LUMO_OVERFLOW_INDICATORS = "overflow-indicators"
    LUMO_OVERFLOW_INDICATOR_TOP = "overflow-indicator-top"
    LUMO_OVERFLOW_INDICATOR_BOTTOM = "overflow-indicator-bottom"
    AURA_OVERFLOW_INDICATORS = "overflow-indicators"
    AURA_OVERFLOW_INDICATOR_TOP = "overflow-indicator-top"
    AURA_OVERFLOW_INDICATOR_BOTTOM = "overflow-indicator-bottom"


# ---------------------------------------------------------------------------
#  AppLayout enums
# ---------------------------------------------------------------------------

class AppLayoutSection(str, Enum):
    """Sections that can be used as primary in AppLayout.

    NAVBAR -- navbar takes full width, drawer below (default).
    DRAWER -- drawer takes full height, navbar beside it.
    """
    NAVBAR = "navbar"
    DRAWER = "drawer"


# ---------------------------------------------------------------------------
#  Drag and Drop enums
# ---------------------------------------------------------------------------

class EffectAllowed(str, Enum):
    """Allowed effects for drag-and-drop operations.

    Controls what operations (move, copy, link) are allowed on a drag source.
    """
    MOVE = "move"
    COPY = "copy"
    LINK = "link"
    COPY_MOVE = "copyMove"
    COPY_LINK = "copyLink"
    MOVE_LINK = "moveLink"
    ALL = "all"
    NONE = "none"
    UNINITIALIZED = "uninitialized"


class DropEffect(str, Enum):
    """Drop effect for drag-and-drop operations.

    Controls how the drop target processes the dropped data.
    """
    MOVE = "move"
    COPY = "copy"
    LINK = "link"
    NONE = "none"

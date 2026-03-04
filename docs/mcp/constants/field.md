# Field Constants

## Autocomplete

HTML autocomplete attribute values.

```python
from pyxflow.components import Autocomplete
```

| Name | Value |
|------|-------|
| `Autocomplete.OFF` | `"off"` |
| `Autocomplete.ON` | `"on"` |
| `Autocomplete.NAME` | `"name"` |
| `Autocomplete.HONORIFIC_PREFIX` | `"honorific-prefix"` |
| `Autocomplete.GIVEN_NAME` | `"given-name"` |
| `Autocomplete.ADDITIONAL_NAME` | `"additional-name"` |
| `Autocomplete.FAMILY_NAME` | `"family-name"` |
| `Autocomplete.HONORIFIC_SUFFIX` | `"honorific-suffix"` |
| `Autocomplete.NICKNAME` | `"nickname"` |
| `Autocomplete.EMAIL` | `"email"` |
| `Autocomplete.USERNAME` | `"username"` |
| `Autocomplete.NEW_PASSWORD` | `"new-password"` |
| `Autocomplete.CURRENT_PASSWORD` | `"current-password"` |
| `Autocomplete.ORGANIZATION_TITLE` | `"organization-title"` |
| `Autocomplete.ORGANIZATION` | `"organization"` |
| `Autocomplete.STREET_ADDRESS` | `"street-address"` |
| `Autocomplete.ADDRESS_LINE1` | `"address-line1"` |
| `Autocomplete.ADDRESS_LINE2` | `"address-line2"` |
| `Autocomplete.ADDRESS_LINE3` | `"address-line3"` |
| `Autocomplete.ADDRESS_LEVEL1` | `"address-level1"` |
| `Autocomplete.ADDRESS_LEVEL2` | `"address-level2"` |
| `Autocomplete.ADDRESS_LEVEL3` | `"address-level3"` |
| `Autocomplete.ADDRESS_LEVEL4` | `"address-level4"` |
| `Autocomplete.COUNTRY` | `"country"` |
| `Autocomplete.COUNTRY_NAME` | `"country-name"` |
| `Autocomplete.POSTAL_CODE` | `"postal-code"` |
| `Autocomplete.CC_NAME` | `"cc-name"` |
| `Autocomplete.CC_GIVEN_NAME` | `"cc-given-name"` |
| `Autocomplete.CC_ADDITIONAL_NAME` | `"cc-additional-name"` |
| `Autocomplete.CC_FAMILY_NAME` | `"cc-family-name"` |
| `Autocomplete.CC_NUMBER` | `"cc-number"` |
| `Autocomplete.CC_EXP` | `"cc-exp"` |
| `Autocomplete.CC_EXP_MONTH` | `"cc-exp-month"` |
| `Autocomplete.CC_EXP_YEAR` | `"cc-exp-year"` |
| `Autocomplete.CC_CSC` | `"cc-csc"` |
| `Autocomplete.CC_TYPE` | `"cc-type"` |
| `Autocomplete.TRANSACTION_CURRENCY` | `"transaction-currency"` |
| `Autocomplete.TRANSACTION_AMOUNT` | `"transaction-amount"` |
| `Autocomplete.LANGUAGE` | `"language"` |
| `Autocomplete.BDAY` | `"bday"` |
| `Autocomplete.BDAY_DAY` | `"bday-day"` |
| `Autocomplete.BDAY_MONTH` | `"bday-month"` |
| `Autocomplete.BDAY_YEAR` | `"bday-year"` |
| `Autocomplete.SEX` | `"sex"` |
| `Autocomplete.TEL` | `"tel"` |
| `Autocomplete.TEL_COUNTRY_CODE` | `"tel-country-code"` |
| `Autocomplete.TEL_NATIONAL` | `"tel-national"` |
| `Autocomplete.TEL_AREA_CODE` | `"tel-area-code"` |
| `Autocomplete.TEL_LOCAL` | `"tel-local"` |
| `Autocomplete.TEL_LOCAL_PREFIX` | `"tel-local-prefix"` |
| `Autocomplete.TEL_LOCAL_SUFFIX` | `"tel-local-suffix"` |
| `Autocomplete.TEL_EXTENSION` | `"tel-extension"` |
| `Autocomplete.URL` | `"url"` |
| `Autocomplete.PHOTO` | `"photo"` |

## ValueChangeMode

Controls when a text field syncs its value to the server.

EAGER — fires on every keystroke ("input" event)
LAZY — fires after a debounce timeout ("input" event, behaves like EAGER for now)
TIMEOUT — fires after a timeout ("input" event, behaves like EAGER for now)
ON_BLUR — fires when the field loses focus ("blur" event)
ON_CHANGE — fires on change event (default, "change" event)

```python
from pyxflow.components import ValueChangeMode
```

| Name | Value |
|------|-------|
| `ValueChangeMode.EAGER` | `"eager"` |
| `ValueChangeMode.LAZY` | `"lazy"` |
| `ValueChangeMode.TIMEOUT` | `"timeout"` |
| `ValueChangeMode.ON_BLUR` | `"on_blur"` |
| `ValueChangeMode.ON_CHANGE` | `"on_change"` |

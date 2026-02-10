"""Theme switching — Lumo / Aura, light / dark."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vaadin.flow.core.component import UI


class Theme:
    """Utility for switching themes and color variants at runtime.

    Themes:
        Theme.LUMO — Vaadin's default theme
        Theme.AURA — Alternative Vaadin theme

    Variants:
        Theme.LIGHT — Light color scheme (default)
        Theme.DARK  — Dark color scheme

    Usage from any component with access to UI:
        Theme.set(self._ui, Theme.AURA)
        Theme.set(self._ui, Theme.LUMO, Theme.DARK)
        Theme.set_variant(self._ui, Theme.DARK)
    """

    LUMO = "lumo"
    AURA = "aura"
    LIGHT = "light"
    DARK = "dark"

    _THEMES = {LUMO: "lumo/lumo.css", AURA: "aura/aura.css"}

    @staticmethod
    def set(ui: UI, theme: str, variant: str = LIGHT) -> None:
        """Switch theme and variant.

        Replaces the current theme stylesheet and sets the color variant.

        Args:
            ui: The UI instance (available as self._ui in components).
            theme: Theme.LUMO or Theme.AURA.
            variant: Theme.LIGHT or Theme.DARK.
        """
        new_href = Theme._THEMES[theme]
        other_href = Theme._THEMES[Theme.AURA if theme == Theme.LUMO else Theme.LUMO]
        theme_attr = variant if variant == Theme.DARK else ""

        js = (
            "return (async function() {"
            "  var old = document.querySelector("
            "    'link[rel=stylesheet][href*=\"' + $0 + '\"]'"
            "  );"
            "  if (old) old.href = $1;"
            "  else {"
            "    var l = document.createElement('link');"
            "    l.rel = 'stylesheet'; l.href = $1;"
            "    document.head.appendChild(l);"
            "  }"
            "  if ($2) document.documentElement.setAttribute('theme', $2);"
            "  else document.documentElement.removeAttribute('theme');"
            "})()"
        )
        ui._tree.queue_execute([other_href, new_href, theme_attr, js])

    @staticmethod
    def set_variant(ui: UI, variant: str) -> None:
        """Switch only the color variant (light / dark) without changing the theme.

        Args:
            ui: The UI instance.
            variant: Theme.LIGHT or Theme.DARK.
        """
        theme_attr = variant if variant == Theme.DARK else ""
        js = (
            "return (async function() {"
            "  if ($0) document.documentElement.setAttribute('theme', $0);"
            "  else document.documentElement.removeAttribute('theme');"
            "})()"
        )
        ui._tree.queue_execute([theme_attr, js])

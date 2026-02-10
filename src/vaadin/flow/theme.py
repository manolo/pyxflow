"""Theme constants — Lumo / Aura, light / dark."""


class Theme:
    """Theme and variant constants.

    Themes:
        Theme.LUMO — Vaadin's default theme
        Theme.AURA — Alternative Vaadin theme

    Variants:
        Theme.LIGHT — Light color scheme (default)
        Theme.DARK  — Dark color scheme

    Usage from any component:
        self._ui.set_theme(Theme.AURA, Theme.DARK)
        self._ui.set_theme_variant(Theme.DARK)
    """

    LUMO = "lumo"
    AURA = "aura"
    LIGHT = "light"
    DARK = "dark"

    THEMES = {LUMO: "lumo/lumo.css", AURA: "aura/aura.css"}

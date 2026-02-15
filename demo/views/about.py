from vaadin.flow import Menu, Route, StyleSheet
from vaadin.flow.components import Div, H1, Image, Paragraph
from demo.views.main_layout import MainLayout


@Route("", page_title="About", layout=MainLayout)
@Menu(title="About", order=0, icon="vaadin:info-circle")
@StyleSheet("styles/about.css")
class AboutView(Div):
    def __init__(self):
        self.add_class_name("about-view")

        # ── Hero ──────────────────────────────────────────────
        hero = Div()
        hero.add_class_name("about-hero")

        logo = Image("images/logo2.png", "PyFlow")
        logo.add_class_name("about-logo")

        title = H1("Build Web Apps in Pure Python")
        title.add_class_name("about-title")

        subtitle = Paragraph(
            "No JavaScript. No HTML templates. Just Python. "
            "Enterprise-grade Vaadin components, powered by Python."
        )
        subtitle.add_class_name("about-subtitle")

        arch_img = Image("images/architecture.png", "Architecture diagram")
        arch_img.add_class_name("about-arch-img")

        hero.add(logo, title, subtitle, arch_img)

        self.add(hero)

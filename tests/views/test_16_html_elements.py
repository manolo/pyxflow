"""Test View 19: HTML Elements — /test/html-elements"""

from vaadin.flow import Route
from vaadin.flow.components import (
    Anchor, Div, H1, H2, H3, H4, H5, H6, Hr, IFrame, Image, NativeLabel,
    Paragraph, Pre, Span, VerticalLayout,
    Header, Footer, Section, Nav, Main,
)
from vaadin.flow.menu import Menu
from tests.views.test_main_layout import TestMainLayout


@Route("test/html-elements", page_title="Test: HTML Elements", layout=TestMainLayout)
@Menu(title="16 HTML Elements", order=16)
class TestHtmlElementsView(VerticalLayout):
    def __init__(self):
        h1 = H1("Title")
        h1.set_id("h1")

        h2 = H2("Subtitle")
        h2.set_id("h2")

        h3 = H3("H3")
        h3.set_id("h3")

        h4 = H4("H4")
        h4.set_id("h4")

        h5 = H5("H5")
        h5.set_id("h5")

        h6 = H6("H6")
        h6.set_id("h6")

        p1 = Paragraph("Lorem ipsum")
        p1.set_id("p1")

        sp1 = Span("inline")
        sp1.set_id("sp1")

        div1 = Div()
        div1.set_id("div1")
        div1.add(Span("child1"), Span("child2"))

        div_text = Div("text content")
        div_text.set_id("div-text")

        a1 = Anchor("https://example.com", "Link")
        a1.set_id("a1")

        a_target = Anchor("https://example.com", "Blank")
        a_target.set_id("a-target")
        a_target.set_target("_blank")

        iframe1 = IFrame("about:blank")
        iframe1.set_id("iframe1")

        hr1 = Hr()
        hr1.set_id("hr1")

        pre1 = Pre("code block")
        pre1.set_id("pre1")

        img1 = Image("data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==", "Logo")
        img1.set_id("img1")

        lbl1 = NativeLabel("Field label")
        lbl1.set_id("lbl1")

        header1 = Header("header")
        header1.set_id("header1")

        footer1 = Footer("footer")
        footer1.set_id("footer1")

        section1 = Section("section")
        section1.set_id("section1")

        nav1 = Nav("nav")
        nav1.set_id("nav1")

        main1 = Main("main")
        main1.set_id("main1")

        self.add(
            h1, h2, h3, h4, h5, h6,
            p1, sp1,
            div1, div_text,
            a1, a_target,
            iframe1,
            hr1,
            pre1,
            img1,
            lbl1,
            header1, footer1, section1, nav1, main1,
        )

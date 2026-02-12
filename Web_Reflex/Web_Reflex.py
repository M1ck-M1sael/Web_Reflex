import reflex as rx
from Web_Reflex.components.navbar import navbar
from Web_Reflex.views.header.header import header_component as header
from Web_Reflex.styles import TYPEWRITER_ANIMATION
from .state import State

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        rx.el.style(TYPEWRITER_ANIMATION),
    )

app = rx.App()
app.add_page(index)
import reflex as rx
from Web_Reflex.components.navbar import navbar
from Web_Reflex.views.header.header import header_component as header
from Web_Reflex.styles import TYPEWRITER_ANIMATION
from .state import State
from Web_Reflex.components.background import animated_background
from Web_Reflex.views.links.links import links

def index() -> rx.Component:
    return rx.box(
        # Fondo animado
        animated_background(),
        # Contenido principal
        rx.vstack(
            navbar(),
            header(),
            links(),
            rx.el.style(TYPEWRITER_ANIMATION),
            spacing="0", #ajusta el espacio entre componentes si es necesario
            width="100%",
        ),

        # Estilos de contenedor principal
        width="100%",
        min_height="100vh",
        position="relative",
    )

app = rx.App()
app.add_page(index)
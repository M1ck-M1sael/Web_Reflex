import reflex as rx
from Web_Reflex.state import State
from Web_Reflex.styles import typewriter_style

def navbar() -> rx.Component:
    return rx.hstack(
        # Lado izquierdo: Logo + Nombre
        rx.hstack(
            rx.avatar(
                src="/MickRM_Logo2.png", #logo
                fallback="MR",          #por si no carga la imagen
                size="5",
                border_radius="full",
            ),
            rx.text(
                "MickRM",
                style=typewriter_style, #anmación
                font_weight="bold",
                font_family="JetBrains Mono", #estilo de letra
                size="4",
            ),
            align="center",
            spacing="2",
        ),

        #empuja cualquier otra cosa a la derecha
        rx.spacer(),

        #botón de idioma
        rx.button(
            rx.cond(State.idioma_ingles, "ES", "EN"), #dependiendo el idioma muestra las siglas del idioma contrario
            on_click=State.cambiar_idioma, #cambia el idioma al hacer click
            variant="ghost", 
            size="2",
        ),

        #cambio de tema claro/oscuro
        rx.color_mode.button(),

        width="100%",
        padding_x="2em",
        padding_y="1em",
        border_bottom="rgb(74, 78, 82) 1px solid", # Una línea sutil divisoria
        align="center",
    )
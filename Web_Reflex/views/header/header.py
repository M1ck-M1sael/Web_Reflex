import reflex as rx
from Web_Reflex.state import State

def header_component() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            #cambié el avatar por una imágen
            rx.image(
                src="/Eseman.jpg",
                width="600px",
                heigth="auto",
                border_radius="15%",
                object_fit="cover"
                ), 
            
            #textos
            rx.text(
                rx.cond(
                    State.idioma_ingles,
                    "Hello there! My name es Misael",
                    "¡Hola! Mi nombre es Misael"
                ),
                font_weight="bold",
                size="7"
            ),
            #rx.text("@M1ck-M1sael", color_scheme="gray"),
            #No creo usar esto, pero lo comento por si acaso

            #cuadro de texto
            rx.card(
                rx.text(
                    rx.cond(
                        State.idioma_ingles, 
                        "Systems Administrator | Computer Systems Engineering Studen (TecNM) | Aspiring DevOps | AWS Cloud Practitioner (in progress)",
                        "Systems Administrator | Estudiante de Ing. Sistemas Computacionales | DevOps en formación | AWS Cloud Practitioner en proceso"
                    ),
                    text_align="center",
                    size="7"
                ),
                max_width="970px",
                variant="classic",
            ),

            spacing="4",
            align="center",
        ),
        width="100%",
        justify="center",
        align="center",
        padding_y="2em",
    )
import reflex as rx
from Web_Reflex.state import State

def header_component() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            # Avatar
            rx.avatar(src="/El bigote.jpg", size="9"), #cambié el tamaño de 8 a 9
            
            # Textos
            rx.text(
                rx.cond(
                    State.idioma_ingles,
                    "Hey!👊 My Name is Misael López",
                    "¡Hola!👊 Mi nombre es Misael López"
                ),
                font_weight="bold",
            ),
            rx.text("@M1ck-M1sael", color_scheme="gray"),

            # Cuadro de texto (Asegúrate de que el paréntesis cierre DESPUÉS de las propiedades)
            rx.card(
                rx.text(
                    rx.cond(
                        State.idioma_ingles, 
                        "Systems Engineer student at Tecnologico Nacional de México. Passionate about DevOps and AWS. Always eager to learn and grow in the tech world.",
                        "Estudiante de Ingeniería en Sistemas Computacionales en el Tecnológico Nacional de México. Apasionado por DevOps y AWS. Siempre dispuesto a aprender y crecer en el mundo tecnológico."
                    ),
                    text_align="left",
                ),
                max_width="670px", # Esto va ADENTRO del card
                variant="classic", # Esto también va ADENTRO del card
            ),

            spacing="4",
            align="center",
        ),
        width="100%",
        justify="center",
        align="center",
        padding_y="2em",
    )
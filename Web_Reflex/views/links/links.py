import reflex as rx

def link_button(text: str, url: str, icon_tag: str):
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag=icon_tag),
                rx.text(text),
                align="center",
                spacing="2",
            ),
            color_scheme="gray",
            varaint="soft",
        ),
        href=url,
        is_external=True, #esto hace que el enlace se abra en una nueva pestaña
    )

def links():
    return rx.hstack(
        link_button("LinkedIn", "www.linkedin.com/in/misael-lópez-franco-409566209", "linkedin"),
        link_button("GitHub", "https://github.com/M1ck-M1sael", "github"),
        spacing="3",
        justify="center",
        width="100%",
        padding_top="1em",
    )
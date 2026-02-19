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
        link_button("LinkedIn", "https://www.linkedin.com/in/misael-lópez-franco-409566209", "linkedin"),
        link_button("GitHub", "https://github.com/M1ck-M1sael", "github"),
        link_button("Spotify", "https://open.spotify.com/user/udsaws99krcqg1hxz618s3cgj?si=13a9ed0c5fd94a26", "music"),
        spacing="3",
        justify="center",
        width="100%",
        padding_top="1em",
    )
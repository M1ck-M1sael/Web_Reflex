#Modulo para el backgrouna animado del app.
#Falta resolver que en Opera GX y Edge el vídeo se queda estático, pero en Chrome si funciona.

import reflex as rx

def animated_background():
    return rx.html(
        """
        <video 
            autoplay 
            loop 
            muted 
            playsinline 
            preload="auto"
            style="
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                z-index: -1;
                object-fit: cover;
                filter: brightness(0.6);
                background-color: black;
                transform: translateZ(0); /* Fuerza aceleración 3D en Opera */
            ">
            <source src="/background_loop-vid.mp4" type="video/mp4">
        </video>
        """
    )
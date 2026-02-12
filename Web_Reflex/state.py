#Para manejar correctamente las llamadas a State

import reflex as rx

class State(rx.State):
    #Por defecto el español
    idioma_ingles: bool = False

    def cambiar_idioma(self):
        #Invierte el valor del selector de idioma
        self.idioma_ingles = not self.idioma_ingles
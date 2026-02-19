# Keyframes para la animación
TYPEWRITER_ANIMATION = """
@keyframes typing { 
    from { width: 0 } 
    to { width: 100% } 
}
@keyframes blink-caret { 
    from, to { border_color: transparent } 
    50% { border_color: white; } /* Cambia 'white' por el color que quieras */
}
"""

# Diccionario de estilo de texto que se usará para el efecto de máquina de escribir
typewriter_style = {
    "overflow": "hidden",
    "white_space": "nowrap",
    "border_right": "3px solid", 
    "margin": "0 auto",
    "width": "0", # se empieza con el ancho en 0 para la animación
    "animation": (
        "typing 3s steps(6, end) forwards, " # mantiene el texto visible después de la animación
        "blink-caret 0.75s step-end infinite"  # animación del cursor parpadeante
    ),
}
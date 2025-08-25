from src.lesson import Lesson

lesson = Lesson(
    title="Flujo de control y estructuras condicionales",
    content=(
        "<b>¿Qué es el flujo de control?</b>\n"
        "Es el orden en el que se ejecutan las instrucciones de un programa. Por defecto, el flujo es <b>secuencial</b>, es decir, las sentencias se ejecutan una detrás de otra, de arriba a abajo.\n\n"

        "<b>Estructura secuencial:</b>\n"
        "Las instrucciones se ejecutan en el orden en el que aparecen. Es el tipo más básico de flujo.\n\n"

        "<b>Estructura condicional:</b>\n"
        "Permite tomar decisiones. Según se cumpla una condición, se ejecutan unas instrucciones u otras.\n\n"

        "<b>Tipos de estructuras condicionales:</b>\n"
        "• <b>Simple</b>: Se ejecuta un bloque solo si la condición se cumple.\n"
        "• <b>Doble</b>: Se elige entre dos bloques, uno si se cumple la condición, y otro si no.\n"
        "• <b>Múltiple</b>: Se elige entre varios bloques posibles, según el valor de una expresión.\n"
    )
)

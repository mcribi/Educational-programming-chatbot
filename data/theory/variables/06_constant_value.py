
from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es una constante?",
    content=(
        "Una <b>constante</b> es como una variable, pero su valor no puede cambiar.\n"
        "Se usa la palabra clave <code>const</code>:\n"
        "<code>const double PI = 3.1416;</code>\n\n"
        "Intentar cambiar su valor da error:\n"
        "<code>PI = 3.15;</code>  // ❌ Error\n\n"
        "<b>Ventajas:</b>\n"
        "• Ayudan a evitar errores.\n"
        "• Mejoran la legibilidad del código."
    )
)
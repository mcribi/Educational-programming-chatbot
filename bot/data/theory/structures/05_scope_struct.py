from src.lesson import Lesson

lesson = Lesson(
    title="Ámbito de un struct",
    content=(
        "Los <code>struct</code> se comportan como cualquier otra variable en cuanto a ámbito:\n\n"
        "• Pueden ser <b>globales</b> (no recomendado en este curso).\n"
        "• Pueden ser <b>locales</b> dentro de una función.\n"
        "• Pueden declararse dentro de un <b>bloque</b> y solo existir ahí.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>while (hay_datos) {\n"
        "    Punto2D p; // Se crea uno nuevo en cada iteración\n"
        "}</code></pre>\n\n"
        "👉 El struct <code>p</code> existe solo dentro del bucle."
    )
)

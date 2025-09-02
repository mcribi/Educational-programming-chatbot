from src.lesson import Lesson

lesson = Lesson(
    title="Vectores y memoria",
    content=(
        "Las posiciones de un vector se guardan en memoria de forma <b>contigua</b>.\n"
        "👉 El índice es una forma de calcular el desplazamiento desde el inicio.\n\n"
        "<b>Ejemplo:</b>\n"
        "Si <code>double notas[3]</code> ocupa direcciones a partir de 1000:\n"
        "• notas[0] está en 1000\n"
        "• notas[1] en 1008 (si double ocupa 8 bytes)\n"
        "• notas[2] en 1016\n\n"
        "👉 Por eso acceder fuera de rango pisa memoria indebida."
    )
)

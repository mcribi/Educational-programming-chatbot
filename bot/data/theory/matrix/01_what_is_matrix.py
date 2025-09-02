from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es una matriz?",
    content=(
        "Una <b>matriz</b> es como un vector de dos dimensiones: una tabla de filas y columnas.\n\n"
        "👉 Permite guardar datos del mismo tipo organizados en posiciones con dos índices: [fila][columna].\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>double notas[2][3];\n"
        "notas[0][0] = 7.5;\n"
        "notas[0][1] = 8.0;\n"
        "notas[1][2] = 9.2;</code></pre>\n\n"
        "👉 Aquí tenemos una tabla de 2 filas × 3 columnas."
    )
)

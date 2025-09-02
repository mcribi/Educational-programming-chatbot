from src.lesson import Lesson

lesson = Lesson(
    title="Matrices de más dimensiones",
    content=(
        "En C++ podemos declarar matrices con 3 o más dimensiones.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>const int X = 2, Y = 3, Z = 5;\n"
        "double datos[X][Y][Z];\n"
        "datos[1][2][0] = 4.5;</code></pre>\n\n"
        "👉 Aquí tenemos un cubo de 2 × 3 × 5 = 30 elementos."
    )
)

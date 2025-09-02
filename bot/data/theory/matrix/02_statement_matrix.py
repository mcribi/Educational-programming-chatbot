from src.lesson import Lesson

lesson = Lesson(
    title="Declaración de matrices",
    content=(
        "La forma general de declarar una matriz en C++ es:\n\n"
        "<pre><code>&lt;tipo&gt; &lt;nombre&gt;[&lt;filas&gt;][&lt;columnas&gt;];</code></pre>\n\n"
        "• <b>tipo</b>: el tipo de dato de todos los elementos (int, double, char...)\n"
        "• <b>nombre</b>: identificador de la matriz\n"
        "• <b>filas, columnas</b>: número fijo de elementos en cada dimensión\n\n"
        "<b>Ejemplo:</b>\n"
        "<code>int tablero[3][3];</code>  // Matriz de 3x3 enteros"
    )
)

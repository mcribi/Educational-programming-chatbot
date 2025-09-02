from src.lesson import Lesson

lesson = Lesson(
    title="Declaración de vectores",
    content=(
        "La forma general de declarar un vector en C++ es:\n\n"
        "<pre><code>&lt;tipo&gt; &lt;nombre&gt;[&lt;tamaño&gt;];</code></pre>\n\n"
        "• <b>tipo</b>: el tipo de dato de todos los elementos (int, double, char...)\n"
        "• <b>nombre</b>: identificador del vector\n"
        "• <b>tamaño</b>: número fijo de elementos que puede almacenar\n\n"
        "<b>Ejemplo:</b>\n"
        "<code>int edades[5];</code>  // Guarda 5 enteros (edades[0]...edades[4])"
    )
)

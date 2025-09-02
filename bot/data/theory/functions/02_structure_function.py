from src.lesson import Lesson

lesson = Lesson(
    title="Estructura de una función",
    content=(
        "La definición de una función en C++ tiene esta forma:\n\n"
        "<pre><code>&lt;tipo&gt; &lt;nombre&gt;(&lt;parámetros&gt;) {\n"
        "    &lt;sentencias&gt;\n"
        "    return &lt;valor&gt;;\n"
        "}</code></pre>\n\n"
        "• <b>Tipo</b>: el tipo de dato que devuelve (ej. int, double, bool). Si no devuelve nada se usa <code>void</code>.\n"
        "• <b>Nombre</b>: identificador de la función.\n"
        "• <b>Parámetros</b>: datos de entrada que recibe.\n"
        "• <b>return</b>: valor que devuelve (excepto en funciones void).\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int Suma(int a, int b) {\n"
        "    return a + b;\n"
        "}</code></pre>"
    )
)

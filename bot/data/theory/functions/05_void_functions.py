from src.lesson import Lesson

lesson = Lesson(
    title="Funciones void",
    content=(
        "Las funciones <code>void</code> no devuelven ningún valor. Se usan para realizar una acción.\n\n"
        "<b>Estructura:</b>\n"
        "<pre><code>void Presentacion(int lineas) {\n"
        "    for (int i = 0; i &lt; lineas; i++)\n"
        "        cout &lt;&lt; \"**********\" &lt;&lt; endl;\n"
        "    cout &lt;&lt; \"Bienvenido al programa\";\n"
        "}</code></pre>\n\n"
        "👉 Para llamarla simplemente escribimos su nombre con los parámetros:\n"
        "<code>Presentacion(3);</code>"
    )
)

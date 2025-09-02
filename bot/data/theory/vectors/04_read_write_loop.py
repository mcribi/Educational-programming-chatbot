from src.lesson import Lesson

lesson = Lesson(
    title="Lectura y escritura con bucles",
    content=(
        "Los vectores suelen manejarse con bucles <code>for</code> para recorrer sus elementos.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>const int N = 3;\n"
        "double notas[N];\n\n"
        "for (int i = 0; i &lt; N; i++) {\n"
        "    cout &lt;&lt; \"Introduce nota \" &lt;&lt; i &lt;&lt; \": \";\n"
        "    cin &gt;&gt; notas[i];\n"
        "}\n\n"
        "for (int i = 0; i &lt; N; i++) {\n"
        "    cout &lt;&lt; \"Nota \" &lt;&lt; i &lt;&lt; \": \" &lt;&lt; notas[i] &lt;&lt; endl;\n"
        "}</code></pre>"
    )
)

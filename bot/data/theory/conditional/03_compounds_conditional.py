from src.lesson import Lesson

lesson = Lesson(
    title="Condiciones compuestas",
    content=(
        "Podemos usar operadores lógicos para combinar varias condiciones:\n\n"

        "• <code>&amp;&amp;</code> → y lógico (ambas condiciones deben cumplirse)\n"
        "• <code>||</code> → o lógico (basta con que una se cumpla)\n"
        "• <code>!</code> → negación (invierte el valor lógico)\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>double dato, inferior = 0, superior = 10;\n"
        "cin &gt;&gt; dato;\n"
        "if (dato &gt;= inferior &amp;&amp; dato &lt;= superior) {\n"
        "   cout &lt;&lt; \"El valor está en el intervalo\";\n"
        "}</code></pre>\n\n"

        "En este ejemplo, la condición se cumple solo si <code>dato</code> está dentro del intervalo [0, 10]."
    )
)

from src.lesson import Lesson

lesson = Lesson(
    title="Bucles con condiciones compuestas",
    content=(
        "Podemos combinar condiciones usando operadores lógicos dentro de un bucle:\n\n"
        "• <code>&amp;&amp;</code> → Y lógico (ambas condiciones verdaderas)\n"
        "• <code>||</code> → O lógico (al menos una verdadera)\n"
        "• <code>!</code> → Negación\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>while (x &gt; 0 &amp;&amp; x &lt;= 100) {\n    // instrucciones\n}</code></pre>\n"
        "👉 El bucle solo se ejecuta si <code>x</code> está entre 1 y 100."
    )
)

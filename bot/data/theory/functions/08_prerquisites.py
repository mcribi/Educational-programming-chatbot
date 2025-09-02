from src.lesson import Lesson

lesson = Lesson(
    title="Precondiciones y buenas prácticas",
    content=(
        "A veces una función solo tiene sentido si se cumplen ciertas condiciones en los parámetros.\n"
        "A eso se le llama <b>precondición</b>.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>// Prec: 0 &lt;= n &amp;&amp; n &lt;= 20\n"
        "long long Factorial(int n) {\n"
        "    long long f = 1;\n"
        "    for (int i = 2; i &lt;= n; i++)\n"
        "        f *= i;\n"
        "    return f;\n"
        "}</code></pre>\n\n"
        "👉 Documenta tus funciones y mantenlas simples. Si una función es demasiado larga o hace demasiadas cosas, divídela en varias."
    )
)

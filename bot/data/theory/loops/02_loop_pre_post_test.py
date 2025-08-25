from src.lesson import Lesson

lesson = Lesson(
    title="Bucles pre-test y post-test",
    content=(
        "🔍 Según cuándo se evalúe la condición, hay dos tipos de bucles:\n\n"
        "🔹 <b>Pre-test</b>: evalúan la condición <b>antes</b> de ejecutar el cuerpo (ej. <code>while</code>, <code>for</code>).\n"
        "🔹 <b>Post-test</b>: evalúan la condición <b>después</b> de ejecutar el cuerpo (ej. <code>do-while</code>).\n\n"
        "<b>Ejemplo pre-test:</b>\n"
        "<pre><code>int i = 1;\nwhile (i &lt;= 3) {\n    cout &lt;&lt; i &lt;&lt; \" \";\n    i++;\n}</code></pre>\n"
        "👉 Imprime: <code>1 2 3</code>\n\n"
        "<b>Ejemplo post-test:</b>\n"
        "<pre><code>int x = 10;\ndo {\n    cout &lt;&lt; x;\n} while (x &lt; 5);</code></pre>\n"
        "👉 Aunque <code>x &lt; 5</code> es falso, se ejecuta una vez."
    )
)

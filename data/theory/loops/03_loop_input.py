from src.lesson import Lesson

lesson = Lesson(
    title="Bucles con lectura de datos",
    content=(
        "Muchos programas necesitan leer datos hasta que se cumpla cierta condición (como introducir un número positivo).\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int numero;\ndo {\n    cout &lt;&lt; \"Introduce un número positivo: \";\n    cin &gt;&gt; numero;\n} while (numero &lt;= 0);</code></pre>\n"
        "👉 El programa seguirá pidiendo números hasta que se introduzca uno mayor que 0.\n\n"
        "✅ Esto es útil cuando no sabes cuántas veces necesitarás leer datos."
    )
)

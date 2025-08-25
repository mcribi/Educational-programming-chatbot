from src.lesson import Lesson

lesson = Lesson(
    title="Bucles anidados",
    content=(
        "Un <b>bucle anidado</b> es un bucle dentro de otro. Se usa por ejemplo para recorrer filas y columnas.\n\n"
        "<b>Ejemplo: Tabla de multiplicar</b>\n"
        "<pre><code>for (int i = 1; i &lt;= 3; i++) {\n    for (int j = 1; j &lt;= 3; j++) {\n        cout &lt;&lt; i * j &lt;&lt; \" \";\n    }\n    cout &lt;&lt; endl;\n}</code></pre>\n"
        "👉 Imprime una tabla de 3x3 con productos."
    )
)

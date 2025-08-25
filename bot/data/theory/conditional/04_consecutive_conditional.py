from src.lesson import Lesson

lesson = Lesson(
    title="Condicionales consecutivos",
    content=(
        "A veces queremos comprobar varias condiciones de forma independiente, una tras otra. Para eso, escribimos varios <code>if</code> seguidos.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>int nota = 7;\n"
        "if (nota &gt;= 5) {\n"
        "   cout &lt;&lt; \"Has aprobado.\";\n"
        "}\n"
        "if (nota &gt;= 9) {\n"
        "   cout &lt;&lt; \"¡Sobresaliente!\";\n"
        "}</code></pre>\n\n"

        "👉 Se ejecutan todas las condiciones que se cumplan, no son excluyentes entre sí."
    )
)

from src.lesson import Lesson

lesson = Lesson(
    title="Condicionales dobles consecutivas",
    content=(
        "Si tenemos varios bloques <code>if - else</code> independientes uno tras otro, se evalúan uno a uno, ejecutando solo uno por bloque.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>int nota = 8;\n"
        "if (nota &gt;= 9) {\n"
        "   cout &lt;&lt; \"Excelente\";\n"
        "} else {\n"
        "   cout &lt;&lt; \"No excelente\";\n"
        "}\n\n"
        "if (nota &gt;= 5) {\n"
        "   cout &lt;&lt; \"Aprobado\";\n"
        "} else {\n"
        "   cout &lt;&lt; \"Suspendido\";\n"
        "}</code></pre>\n\n"

        "👉 Son dos decisiones distintas que se evalúan de forma separada."
    )
)

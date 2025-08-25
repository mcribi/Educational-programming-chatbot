from src.lesson import Lesson

lesson = Lesson(
    title="Condicional doble (if - else)",
    content=(
        "Se usa cuando queremos ejecutar una cosa u otra dependiendo de si se cumple una condición.\n\n"

        "<b>Sintaxis:</b>\n"
        "<pre><code>if (condición) {\n"
        "   instrucciones1;\n"
        "} else {\n"
        "   instrucciones2;\n"
        "}</code></pre>\n\n"

        "📌 Se ejecuta <code>instrucciones1</code> si se cumple la condición, y <code>instrucciones2</code> si no.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>int edad = 16;\n"
        "if (edad &gt;= 18) {\n"
        "   cout &lt;&lt; \"Mayor de edad\";\n"
        "} else {\n"
        "   cout &lt;&lt; \"Menor de edad\";\n"
        "}</code></pre>\n\n"

        "Esto también se conoce como evaluar <b>condiciones mutuamente excluyentes</b>: solo una de las dos ramas se ejecuta."
    )
)

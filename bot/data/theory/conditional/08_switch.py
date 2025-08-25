from src.lesson import Lesson

lesson = Lesson(
    title="Condicional múltiple (switch)",
    content=(
        "La estructura <code>switch</code> permite tomar decisiones en base al valor exacto de una variable <code>int</code> o <code>char</code>.\n\n"

        "<b>Sintaxis básica:</b>\n"
        "<pre><code>switch (variable) {\n"
        "   case valor1:\n"
        "       instrucciones;\n"
        "       break;\n"
        "   case valor2:\n"
        "       instrucciones;\n"
        "       break;\n"
        "   default:\n"
        "       instrucciones por defecto;\n"
        "}</code></pre>\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>int dia = 3;\n"
        "switch (dia) {\n"
        "   case 1: cout &lt;&lt; \"Lunes\"; break;\n"
        "   case 2: cout &lt;&lt; \"Martes\"; break;\n"
        "   case 3: cout &lt;&lt; \"Miércoles\"; break;\n"
        "   default: cout &lt;&lt; \"Día no válido\";\n"
        "}</code></pre>\n\n"

        "👉 <code>break</code> es importante para que el flujo no pase a los siguientes casos."
    )
)

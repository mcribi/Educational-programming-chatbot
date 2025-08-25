from src.lesson import Lesson

lesson = Lesson(
    title="Condicional simple (if)",
    content=(
        "<b>¿Qué es?</b>\n"
        "Una estructura que ejecuta un bloque de código <b>solo si se cumple una condición lógica</b>.\n\n"

        "<b>Sintaxis básica:</b>\n"
        "<pre><code>if (condición) {\n"
        "   instrucciones;\n"
        "}</code></pre>\n\n"

        "Si hay solo una instrucción, se pueden omitir las llaves, pero es buena práctica usarlas.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>int edad = 20;\n"
        "if (edad &gt;= 18) {\n"
        "   cout &lt;&lt; \"Eres mayor de edad\";\n"
        "}</code></pre>\n\n"

        "<b>Estilo recomendado:</b>\n"
        "• Deja una línea en blanco antes del <code>if</code>.\n"
        "• Usa tabulaciones (3 espacios) dentro del bloque para mejorar la legibilidad.\n"
    )
)

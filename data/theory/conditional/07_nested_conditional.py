from src.lesson import Lesson

lesson = Lesson(
    title="Condicionales anidados",
    content=(
        "Se dice que un condicional está anidado cuando contiene otro <code>if</code> en su interior. "
        "Esto permite tomar decisiones más complejas.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>int edad = 20;\n"
        "bool tiene_dni = true;\n"
        "if (edad &gt;= 18) {\n"
        "   if (tiene_dni) {\n"
        "       cout &lt;&lt; \"Puedes votar.\";\n"
        "   }\n"
        "}</code></pre>\n\n"

        "👉 Solo si ambas condiciones se cumplen se ejecuta el mensaje."
    )
)

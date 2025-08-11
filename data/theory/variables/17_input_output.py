from src.lesson import Lesson

lesson = Lesson(
    title="Entrada y salida de datos",
    content=(
        "Para mostrar información usamos <code>cout</code>:\n"
        "<code>cout &lt;&lt; \"Hola\";</code>\n\n"
        "Para leer datos del teclado usamos <code>cin</code>:\n"
        "<code>int edad;\ncin &gt;&gt; edad;</code>\n\n"
        "<b>Ejemplo completo:</b>\n"
        "<pre>\n"
        "int edad;\n"
        "cout &lt;&lt; \"Introduce tu edad: \";\n"
        "cin &gt;&gt; edad;\n"
        "cout &lt;&lt; \"Tienes \" &lt;&lt; edad &lt;&lt; \" años.\";\n"
        "</pre>"
    )
)

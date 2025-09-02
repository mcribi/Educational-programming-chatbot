from src.lesson import Lesson

lesson = Lesson(
    title="Declaración y uso de registros",
    content=(
        "Una vez definido el <code>struct</code>, podemos declarar variables de ese tipo y acceder a sus campos con el operador punto (<code>.</code>).\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>Punto2D un_punto;\n"
        "un_punto.abscisa = 4.0;\n"
        "un_punto.ordenada = 6.0;\n"
        "cout &lt;&lt; \"(\" &lt;&lt; un_punto.abscisa &lt;&lt; \", \" &lt;&lt; un_punto.ordenada &lt;&lt; \")\";\n"
        "</code></pre>\n\n"
        "👉 Esto muestra: (4, 6)"
    )
)

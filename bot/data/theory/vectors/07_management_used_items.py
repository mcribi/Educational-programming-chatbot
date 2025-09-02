from src.lesson import Lesson

lesson = Lesson(
    title="Gestión de elementos utilizados",
    content=(
        "Muchas veces un vector tiene un tamaño máximo pero usamos solo una parte.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>const int MAX = 50;\n"
        "double notas[MAX];\n"
        "int usados = 0;\n\n"
        "// Guardamos 3 notas\n"
        "notas[0] = 7.5; notas[1] = 8.0; notas[2] = 6.9;\n"
        "usados = 3;\n\n"
        "// Recorremos solo las notas usadas\n"
        "for (int i = 0; i &lt; usados; i++) {\n"
        "    cout &lt;&lt; notas[i] &lt;&lt; endl;\n"
        "}</code></pre>"
    )
)

from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es un vector?",
    content=(
        "Un <b>vector</b> (o array) es una estructura que permite guardar varios datos del mismo tipo bajo un mismo nombre.\n\n"
        "👉 Cada dato ocupa una posición identificada con un número llamado <b>índice</b>.\n"
        "👉 El primer índice en C++ siempre es el <code>0</code>.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>double notas[3];\n"
        "notas[0] = 7.5;\n"
        "notas[1] = 8.0;\n"
        "notas[2] = 9.2;</code></pre>\n\n"
        "👉 Aquí hemos declarado un vector de 3 notas."
    )
)

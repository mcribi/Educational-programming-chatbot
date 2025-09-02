from src.lesson import Lesson

lesson = Lesson(
    title="Acceso y operaciones básicas",
    content=(
        "Cada componente de un vector es como una variable normal, a la que accedemos con su índice.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int valores[3];\n"
        "valores[0] = 10;\n"
        "valores[1] = valores[0] + 5;  // valores[1] = 15</code></pre>\n\n"
        "👉 El índice va desde 0 hasta tamaño-1.\n"
        "👉 Si accedes a un índice fuera del rango, el programa puede fallar."
    )
)

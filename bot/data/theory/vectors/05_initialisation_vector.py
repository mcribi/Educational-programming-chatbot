from src.lesson import Lesson

lesson = Lesson(
    title="Inicialización de vectores",
    content=(
        "Podemos dar valores iniciales a un vector al declararlo.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int numeros[4] = {1, 2, 3, 4};\n"
        "int ceros[5] = {0};   // todas las posiciones valen 0\n"
        "int mezcla[7] = {3, 5}; // los demás se inicializan a 0</code></pre>\n\n"
        "👉 Si no ponemos tamaño, el compilador lo calcula:\n"
        "<code>int pares[] = {2, 4, 6};</code> // tamaño 3"
    )
)

from src.lesson import Lesson

lesson = Lesson(
    title="Ámbito de datos en funciones",
    content=(
        "El <b>ámbito</b> indica dónde se puede usar una variable:\n\n"
        "• <b>Locales</b>: declaradas dentro de una función, solo existen ahí.\n"
        "• <b>Parámetros formales</b>: se comportan como locales a esa función.\n"
        "• <b>Globales</b>: declaradas fuera de cualquier función, se pueden usar en todo el programa (⚠️ no recomendadas).\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int global = 10; // Variable global\n\n"
        "int Suma(int a, int b) {\n"
        "    int resultado = a + b; // Variable local\n"
        "    return resultado + global;\n"
        "}</code></pre>\n\n"
        "👉 Se recomienda evitar variables globales porque pueden generar errores difíciles de depurar."
    )
)

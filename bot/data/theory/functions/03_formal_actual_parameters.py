from src.lesson import Lesson

lesson = Lesson(
    title="Parámetros formales y reales",
    content=(
        "Cuando usamos funciones, distinguimos entre:\n\n"
        "• <b>Parámetros formales</b>: los que aparecen en la definición de la función (variables internas).\n"
        "• <b>Parámetros reales</b>: los valores que pasamos al llamar a la función.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>double Cuadrado(double entrada) {  // entrada = parámetro formal\n"
        "    return entrada * entrada;\n"
        "}\n\n"
        "int main() {\n"
        "    double valor = 4;\n"
        "    double r = Cuadrado(valor);  // valor = parámetro real\n"
        "}</code></pre>\n\n"
        "👉 En C++ los parámetros se pasan por <b>valor</b> por defecto, es decir, se copia el dato."
    )
)

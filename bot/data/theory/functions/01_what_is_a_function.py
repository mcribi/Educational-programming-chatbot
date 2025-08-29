from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es una función?",
    content=(
        "Una <b>función</b> es un bloque de código que realiza una tarea específica y que podemos reutilizar en diferentes partes de un programa.\n\n"
        "👉 En lugar de repetir el mismo código varias veces, lo agrupamos en una función y la llamamos cuando la necesitemos.\n\n"
        "<b>Ventajas:</b>\n"
        "• Evita repetir código.\n"
        "• Hace los programas más claros y fáciles de mantener.\n"
        "• Permite dividir un problema en partes más pequeñas.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>double Cuadrado(double x) {\n"
        "    return x * x;\n"
        "}\n\n"
        "int main() {\n"
        "    double r = Cuadrado(4);\n"
        "    cout << r;  // Imprime 16\n"
        "}</code></pre>"
    )
)

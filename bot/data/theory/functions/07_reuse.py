from src.lesson import Lesson

lesson = Lesson(
    title="Paso de parámetros y reutilización",
    content=(
        "Una de las ventajas de las funciones es que podemos llamarlas con distintos parámetros.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int Factorial(int n) {\n"
        "    int f = 1;\n"
        "    for (int i = 2; i <= n; i++)\n"
        "        f *= i;\n"
        "    return f;\n"
        "}\n\n"
        "int main() {\n"
        "    cout << Factorial(3);  // 6\n"
        "    cout << Factorial(5);  // 120\n"
        "}</code></pre>\n\n"
        "👉 La misma función sirve para distintos valores."
    )
)

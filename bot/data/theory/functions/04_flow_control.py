from src.lesson import Lesson

lesson = Lesson(
    title="Flujo de control en funciones",
    content=(
        "Cuando llamamos a una función, el <b>flujo de control</b> del programa cambia:\n\n"
        "1️⃣ Se detiene la ejecución del <code>main()</code> (o de la función actual).\n"
        "2️⃣ El control pasa a la función llamada.\n"
        "3️⃣ Se ejecutan sus instrucciones en orden.\n"
        "4️⃣ Al llegar al <code>return</code>, se devuelve el resultado (si lo hay).\n"
        "5️⃣ El control vuelve al punto justo después de la llamada.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int Doble(int x) {\n"
        "    return x * 2;\n"
        "}\n\n"
        "int main() {\n"
        "    int n = 5;\n"
        "    int r = Doble(n); // Aquí el flujo pasa a la función\n"
        "    cout << r;        // Al volver, imprime 10\n"
        "}</code></pre>\n\n"
        "👉 Esto permite dividir un programa en pasos más pequeños y fáciles de entender."
    )
)

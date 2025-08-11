from src.lesson import Lesson

lesson = Lesson(
    title="¿Cómo está organizado un programa en C++?",
    content=(
        "Un programa en C++ tiene una estructura básica que, aunque puede parecer compleja al principio, siempre sigue un orden. Aquí te explicamos las partes más importantes:\n\n"

        "1. <b>Comentarios:</b> Son textos que no se ejecutan. Sirven para explicar el código.\n"
        "   <code>// Comentario en una línea</code>\n"
        "   <code>/* Comentario en varias líneas */</code>\n\n"

        "2. <b>Inclusión de bibliotecas:</b> Se usan para acceder a funciones ya creadas. Por ejemplo:\n"
        "   Para usar entrada y salida de datos (cin y cout): <code>#include &lt;iostream&gt;</code> \n"
        "   Para usar funciones matemáticas como <code>sqrt</code>: <code>#include &lt;cmath&gt;</code>\n\n"

        "3. <b>Espacio de nombres:</b> Para evitar tener que escribir <code>std::</code> todo el tiempo:\n"
        "   <code>using namespace std;</code>\n\n"

        "4. <b>Función principal:</b> Todo programa empieza por la función <code>main()</code>:\n"
        "   <pre><code>int main() {\n    // aquí va el código\n    return 0;\n}</code></pre>\n"
        "   Aquí dentro van las instrucciones que se ejecutan.\n\n"

        "5. <b>Declaraciones y órdenes:</b>\n"
        "   • Se declaran las variables que usaremos: <code>double lado;</code>\n"
        "   • Se escriben las instrucciones separadas por punto y coma: <code>lado = 7;</code>\n\n"

        "➡️ <i>Nota:</i> Aunque existen programas con muchos archivos, al empezar escribiremos todo en uno solo."
    )
)

from src.lesson import Lesson

lesson = Lesson(
    title="⭐ Esquema del tema: Funciones",
    content=(
        "<b>📌 ¿Qué es una función?</b>\n"
        "• Bloque de código reutilizable que realiza una tarea y (opcionalmente) devuelve un valor.\n"
        "• Ventajas: reutilización, claridad, división del problema en partes.\n\n"

        "<b>🧱 Estructura general</b>\n"
        "<pre><code>&lt;tipo&gt; &lt;nombre&gt;(&lt;parámetros&gt;) {\n"
        "    &lt;sentencias&gt;\n"
        "    return &lt;valor&gt;; // salvo en void\n"
        "}</code></pre>\n"
        "• <b>Tipo</b>: <code>int</code>, <code>double</code>, <code>bool</code>, <code>void</code>...\n"
        "• <b>Parámetros</b>: datos de entrada (por defecto, se copian: paso por valor).\n"
        "• <b>return</b>: devuelve el resultado (si el tipo no es <code>void</code>).\n\n"

        "<b>🔀 Flujo de control al llamar</b>\n"
        "1) Se detiene la ejecución donde se llama.\n"
        "2) Pasa el control a la función.\n"
        "3) Se ejecuta su cuerpo.\n"
        "4) <code>return</code> devuelve el control (y el valor) al punto de llamada.\n\n"

        "<b>👥 Parámetros</b>\n"
        "• <b>Formales</b>: en la definición de la función.\n"
        "• <b>Reales</b>: los valores usados al llamar.\n\n"

        "<b>🧰 Tipos de funciones</b>\n"
        "• Con retorno: calculan y devuelven un valor.\n"
        "• <code>void</code>: realizan acciones (no devuelven valor).\n\n"

        "<b>📍 Ámbito</b>\n"
        "• Variables locales: solo dentro de su función.\n"
        "• Evita variables globales salvo necesidad.\n\n"

        "<b>✔️ Buenas prácticas</b>\n"
        "• Nombres claros y una sola responsabilidad por función.\n"
        "• Documenta precondiciones (ej.: rangos válidos).\n"
        "• Divide funciones largas en funciones más pequeñas.\n\n"

        "<b>💡 Ejemplos típicos</b>\n"
        "• Cálculos simples (suma, cuadrado).\n"
        "• Predicados (<code>bool</code>): <code>EsPar(n)</code>.\n"
        "• Uso de bucles dentro de funciones (ej.: <code>Factorial</code>).\n"
        "• Componer funciones: una llama a otra para resolver pasos."
    )
)

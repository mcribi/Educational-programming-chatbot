from src.lesson import Lesson

lesson = Lesson(
    title="⭐ Esquema",
    content=(
        "<b>📦 ¿Qué es una variable?</b>\n"
        "• Es un espacio de memoria donde guardamos un dato.\n"
        "• Se declara indicando el tipo y el nombre: <code>int edad = 20;</code>\n"
        "• Podemos cambiar su valor con una asignación: <code>edad = 21;</code>\n\n"

        "<b>🔠 Tipos de datos básicos en C++</b>\n"
        "• <code>int</code>: números enteros → <code>int edad = 25;</code>\n"
        "• <code>double</code>: reales con decimales → <code>double pi = 3.14;</code>\n"
        "• <code>char</code>: un carácter → <code>char letra = 'A';</code>\n"
        "• <code>bool</code>: verdadero o falso → <code>bool es_mayor = true;</code>\n"
        "• <code>string</code>: texto → <code>string nombre = \"Ana\";</code>\n\n"

        "<b>📛 Nombres válidos para variables</b>\n"
        "• Solo letras, números y guiones bajos\n"
        "• Sin acentos, eñes ni símbolos\n"
        "• No pueden llamarse como palabras reservadas (como <code>int</code>, <code>return</code>)\n\n"

        "<b>🔒 Constantes</b>\n"
        "• Se definen con <code>const</code> y no cambian su valor.\n"
        "• Ejemplo: <code>const double PI = 3.1416;</code>\n\n"

        "<b>📍 Ámbito de una variable</b>\n"
        "• Es la parte del programa donde la variable existe.\n"
        "• Por ahora, usamos variables locales dentro de <code>main()</code>\n\n"

        "<b>🔤 Literales</b>\n"
        "• Son valores escritos directamente: <code>42</code>, <code>'a'</code>, <code>\"Hola\"</code>, <code>true</code>\n\n"

        "<b>🧮 Operadores y expresiones</b>\n"
        "• Aritméticos: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code>\n"
        "• Relacionales: <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, etc.\n"
        "• Lógicos: <code>&&</code>, <code>||</code>, <code>!</code>\n"
        "• Ejemplo: <code>intvale suma = 5 + 3;</code>\n\n"

        "<b>⚠️ Mezclar tipos distintos</b>\n"
        "• En operaciones con <code>int</code> y <code>double</code>, C++ convierte al tipo más preciso automáticamente.\n"
        "• Ejemplo: <code>double total = 3 * 2.5;</code>\n\n"

        "<b>🛠 Funciones estándar útiles</b>\n"
        "• <code>sqrt(x)</code>, <code>pow(x, y)</code>, <code>abs(x)</code>, <code>round(x)</code>\n"
        "• Requieren <code>#include &lt;cmath&gt;</code>\n\n"

        "<b>📥 Entrada y salida de datos</b>\n"
        "• Mostrar: <code>cout &lt;&lt; \"Hola\";</code>\n"
        "• Leer del teclado: <code>cin &gt;&gt; edad;</code>\n\n"

        "✅ <i>¡Con estos conocimientos ya puedes empezar a crear programas con datos, operaciones y entradas interactivas!</i>"
    )
)

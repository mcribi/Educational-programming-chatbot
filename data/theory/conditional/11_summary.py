from src.lesson import Lesson

lesson = Lesson(
    title="⭐ Esquema",
    content=(
        "<b>📌 ¿Qué es el flujo de control?</b>\n"
        "• Es el orden en que se ejecutan las instrucciones de un programa.\n"
        "• Por defecto es <b>secuencial</b>, pero podemos modificarlo con condicionales.\n\n"

        "<b>🔁 Estructuras condicionales</b>\n"
        "• Permiten que el programa tome decisiones.\n"
        "• Tipos:\n"
        "   - <b>Simple</b>: solo se ejecuta si la condición se cumple.\n"
        "   - <b>Doble</b>: elige entre dos bloques según la condición.\n"
        "   - <b>Múltiple</b>: evalúa varios casos posibles (<code>switch</code>).\n\n"

        "<b>🧱 Estructura básica del if</b>\n"
        "<pre><code>if (condición) {\n"
        "    instrucciones;\n"
        "}</code></pre>\n"
        "• Usa <code>else</code> si quieres una alternativa cuando no se cumpla la condición.\n"
        "• Se puede usar <code>else if</code> o escribir <code>if</code> consecutivos.\n\n"

        "<b>🔀 Otras estructuras</b>\n"
        "• Condiciones compuestas: <code>if (a &gt; 0 &amp;&amp; b &lt; 10)</code>\n"
        "• Condicionales anidados: un <code>if</code> dentro de otro.\n"
        "• <code>switch</code>: para múltiples casos concretos con <code>break</code> y <code>default</code>.\n\n"

        "<b>⚠️ Errores comunes</b>\n"
        "• Usar <code>=</code> en lugar de <code>==</code>\n"
        "• Comparar números decimales directamente\n"
        "• Olvidar inicializar variables\n"
        "• No usar llaves correctamente\n\n"

        "✅ <i>Consejo: Escribe el código claro, simple y bien indentado. ¡Te evitará muchos errores!</i>"
    )
)

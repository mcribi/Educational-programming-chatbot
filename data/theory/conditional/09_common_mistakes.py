from src.lesson import Lesson

lesson = Lesson(
    title="Errores típicos en condicionales",
    content=(
        "Al usar estructuras condicionales, es fácil cometer errores comunes. Aquí van los más frecuentes:\n\n"

        "🔸 <b>1. Comparar reales directamente</b>\n"
        "<pre><code>double x = 0.1 + 0.2;\n"
        "if (x == 0.3) { ... }</code></pre>\n"
        "❌ Esto puede fallar por redondeos. Mejor usar una tolerancia:\n"
        "<code>if (abs(x - 0.3) &lt; 1e-6)</code>\n\n"

        "🔸 <b>2. Usar variables sin asignar</b>\n"
        "<pre><code>int edad;\n"
        "if (edad &gt; 18) { ... }</code></pre>\n"
        "❌ Esto da resultado impredecible si no se ha dado valor a <code>edad</code> antes.\n\n"

        "🔸 <b>3. Confundir = con ==</b>\n"
        "<pre><code>if (x = 5) { ... }</code></pre>\n"
        "❌ Esto asigna 5 a <code>x</code>, no compara.\n"
        "✅ Usa siempre <code>==</code> para comparar.\n\n"

        "🔸 <b>4. No usar llaves adecuadamente</b>\n"
        "<pre><code>if (cond)\n"
        "   a++;\n"
        "   b++;</code></pre>\n"
        "❌ <code>b++</code> se ejecuta siempre. Usa llaves para evitar confusiones.\n\n"

        "<b>📌 Consejo general:</b>\n"
        "<i>Fomenta siempre la sencillez y la legibilidad en la escritura de código.</i>\n\n"

        "👎 Ejemplo difícil de leer:\n"
        "<code>if (x &gt; 10) cout &lt;&lt; \"ok\"; else cout &lt;&lt; \"no\";</code>\n\n"

        "👍 Más claro y mantenible:\n"
        "<pre><code>if (x &gt; 10) {\n"
        "    cout &lt;&lt; \"ok\";\n"
        "} else {\n"
        "    cout &lt;&lt; \"no\";\n"
        "}</code></pre>"
    )
)

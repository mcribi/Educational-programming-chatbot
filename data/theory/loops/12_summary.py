from src.lesson import Lesson

lesson = Lesson(
    title="⭐ Esquema",
    content=(
        "<b>📌 ¿Qué es un bucle?</b>\n"
        "• Repite instrucciones mientras se cumpla una condición.\n"
        "• Cada vuelta es una <i>iteración</i>.\n\n"
        "<b>🔁 Tipos de bucles:</b>\n"
        "• <code>while</code>: condición al principio (pre-test)\n"
        "• <code>do-while</code>: condición al final (post-test)\n"
        "• <code>for</code>: con contador, muy usado\n\n"
        "<b>🔧 Estructura básica:</b>\n"
        "<pre><code>// while\nint i = 0;\nwhile (i &lt; 3) {\n    i++;\n}</code></pre>\n"
        "<pre><code>// do-while\nint i = 0;\ndo {\n    i++;\n} while (i &lt; 3);</code></pre>\n"
        "<pre><code>// for\nfor (int i = 0; i &lt; 3; i++) {\n    // ...\n}</code></pre>\n\n"
        "<b>💡 Consejos:</b>\n"
        "• Cuidado con bucles infinitos\n"
        "• Revisa bien condiciones y contadores\n"
        "• Indenta bien tu código para entenderlo mejor"
    )
)

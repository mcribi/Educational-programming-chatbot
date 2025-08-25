from src.lesson import Lesson

lesson = Lesson(
    title="Errores y consejos",
    content=(
        "⚠️ Errores comunes con bucles:\n\n"
        "• Olvidar incrementar el contador → bucle infinito\n"
        "• Cambiar mal la condición → no se ejecuta nada\n"
        "• Usar <code>;</code> tras un <code>while</code> o <code>for</code> sin llaves:\n"
        "<code>while (x &lt; 5);</code> ❌ ← bucle vacío\n\n"
        "✅ Consejo:\n"
        "• Usa variables bien nombradas\n"
        "• Siempre indenta tu código\n"
        "• Revisa condiciones de corte\n"
        "• Si el bucle no termina, usa <code>break</code> con cuidado"
    )
)

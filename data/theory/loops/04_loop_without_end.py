from src.lesson import Lesson

lesson = Lesson(
    title="Bucles sin fin",
    content=(
        "Un <b>bucle infinito</b> se repite para siempre si no hay forma de salir de él.\n\n"
        "⚠️ Hay que usarlos con cuidado para evitar que el programa se bloquee.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>while (true) {\n    cout &lt;&lt; \"Hola\";\n}</code></pre>\n"
        "Este bucle imprime \"Hola\" sin parar.\n\n"
        "🔸 A veces son útiles si usas <code>break</code> o condiciones internas para salir."
    )
)

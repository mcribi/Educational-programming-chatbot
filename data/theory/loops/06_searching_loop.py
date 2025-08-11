from src.lesson import Lesson

lesson = Lesson(
    title="Bucles que buscan",
    content=(
        "Los bucles también sirven para buscar un valor dentro de un conjunto de datos.\n\n"
        "<b>Ejemplo: Buscar un número par entre 5 números introducidos por el usuario:</b>\n"
        "<pre><code>bool encontrado = false;\nfor (int i = 0; i &lt; 5; i++) {\n    int num;\n    cin &gt;&gt; num;\n    if (num % 2 == 0) {\n        encontrado = true;\n    }\n}</code></pre>\n"
        "🔍 Puedes usar <code>break</code> para salir en cuanto encuentres lo que buscas."
    )
)

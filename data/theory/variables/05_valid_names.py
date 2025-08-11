from src.lesson import Lesson

lesson = Lesson(
    title="Nombres válidos para variables",
    content=(
        "Las variables deben tener nombres que cumplan estas reglas:\n"
        "• Empiezan por letra o guion bajo (<code>_</code>).\n"
        "• Solo letras, números y guiones bajos.\n"
        "• No usan acentos, eñes (<code>ñ</code>), espacios ni símbolos especiales.\n"
        "• No pueden llamarse como palabras reservadas (<code>int</code>, <code>main</code>, etc).\n\n"

        "✔️ Válido: <code>precio_final</code>, <code>_total</code>\n"
        "❌ Inválido: <code>3nombre</code>, <code>main</code>, <code>dirección</code>"
    )
)

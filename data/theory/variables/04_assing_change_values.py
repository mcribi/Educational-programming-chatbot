from src.lesson import Lesson

lesson = Lesson(
    title="Asignar y cambiar valores",
    content=(
        "Después de declarar una variable, puedes cambiar su valor en cualquier momento:\n"
        "<code>int contador = 0;</code>\n"
        "<code>contador = 1;</code>   // ahora vale 1\n\n"

        "También puedes usar su valor en operaciones:\n"
        "<code>int doble = contador * 2;</code>\n\n"

        "<b>Importante:</b> No puedes usar una variable antes de declararla, y el tipo debe coincidir:\n"
        "<code>int edad = 18;</code>\n"
        "<code>edad = \"veinte\";</code>  // ❌ Error: no se puede guardar texto en una variable numérica"
    )
)

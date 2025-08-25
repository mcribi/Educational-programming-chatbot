from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es una variable y para qué sirve?",
    content=(
        "Una <b>variable</b> es un espacio reservado en la memoria del ordenador para guardar un dato. "
        "Ese dato puede cambiar de valor a lo largo del programa.\n\n"

        "Por ejemplo, si queremos guardar la edad de una persona:\n"
        "<code>int edad = 20;</code>\n\n"

        "Aquí estamos diciendo:\n"
        "• <code>int</code>: el tipo de dato (número entero).\n"
        "• <code>edad</code>: el nombre de la variable.\n"
        "• <code>= 20</code>: el valor inicial que le damos.\n\n"

        "A esto se le llama <b>declarar una variable</b> e <b>inicializarla</b> (le hemos dado un valor inicial). Si no se le da un valor inicial, será indeterminado (?) hasta que se le asigne un valor.\n\n"

        "Puedes imaginarlo como una caja con nombre, donde guardas un valor. "
        "Luego puedes usarlo o cambiarlo:\n"
        "<code>edad = 21;</code>  // Ahora la edad es 21."
    )
)

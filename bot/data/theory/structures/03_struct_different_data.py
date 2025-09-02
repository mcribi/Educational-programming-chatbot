from src.lesson import Lesson

lesson = Lesson(
    title="Structs con varios tipos de datos",
    content=(
        "Un <code>struct</code> puede tener campos de distintos tipos. Así podemos modelar objetos más complejos.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>struct Persona {\n"
        "    string nombre;\n"
        "    string apellidos;\n"
        "    string NIF;\n"
        "    char categoria;\n"
        "    double salario_bruto;\n"
        "};</code></pre>\n\n"
        "👉 Cada campo representa una característica distinta de una persona."
    )
)

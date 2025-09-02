from src.lesson import Lesson

lesson = Lesson(
    title="Inicialización de registros",
    content=(
        "Podemos asignar valores iniciales a un <code>struct</code> en el momento de declararlo.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>struct Persona {\n"
        "    string nombre;\n"
        "    string apellidos;\n"
        "    string NIF;\n"
        "    char categoria;\n"
        "    double salario_bruto;\n"
        "};\n\n"
        "Persona empleado = {\"Ana\", \"López\", \"12345678A\", 'B', 2500.0};\n"
        "</code></pre>\n\n"
        "👉 Cada valor corresponde al campo en el orden en que fueron declarados."
    )
)

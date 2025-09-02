from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es un registro?",
    content=(
        "Un <b>registro</b> (en C++ llamado <code>struct</code>) permite agrupar varios datos bajo un mismo nombre. "
        "Los datos pueden ser de distintos tipos y cada uno se llama <b>campo</b>.\n\n"
        "👉 Los registros son útiles para representar entidades reales con varias características.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>struct Punto2D {\n"
        "    double abscisa;\n"
        "    double ordenada;\n"
        "};</code></pre>\n\n"
        "Aquí hemos creado un tipo <code>Punto2D</code> con dos campos numéricos: abscisa y ordenada."
    )
)

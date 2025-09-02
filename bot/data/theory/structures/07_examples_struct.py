from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos con registros",
    content=(
        "🔹 <b>Ejemplo 1: Asignar structs</b>\n"
        "<pre><code>Punto2D a = {1, 2};\n"
        "Punto2D b;\n"
        "b = a;  // Copia todos los campos\n"
        "</code></pre>\n\n"
        "🔹 <b>Ejemplo 2: Usar campos en expresiones</b>\n"
        "<pre><code>double dist_x = abs(a.abscisa - b.abscisa);\n"
        "</code></pre>\n\n"
        "👉 Los registros se comportan como una unidad, pero accedemos a los datos con el operador punto."
    )
)

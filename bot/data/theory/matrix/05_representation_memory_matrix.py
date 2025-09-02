from src.lesson import Lesson

lesson = Lesson(
    title="Matrices en memoria",
    content=(
        "Las matrices se guardan en memoria <b>por filas</b>, de manera contigua.\n\n"
        "👉 Una matriz 2×3 ocupa 6 posiciones consecutivas.\n\n"
        "Ejemplo:\n"
        "<pre>\n"
        "m[0][0] m[0][1] m[0][2]\n"
        "m[1][0] m[1][1] m[1][2]\n"
        "</pre>\n\n"
        "⚠️ Para calcular la dirección de m[i][j], el compilador usa:\n"
        "<code>i * columnas + j</code>"
    )
)

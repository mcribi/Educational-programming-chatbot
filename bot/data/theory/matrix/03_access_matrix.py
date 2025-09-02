from src.lesson import Lesson

lesson = Lesson(
    title="Acceso y asignación en matrices",
    content=(
        "Accedemos a cada celda con dos índices: [fila][columna].\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int m[2][3];\n"
        "m[0][0] = 1;\n"
        "m[1][2] = 5;</code></pre>\n\n"
        "👉 Igual que con vectores, los índices empiezan en 0.\n"
        "⚠️ Si intentas acceder a una fila o columna inexistente, el programa puede fallar."
    )
)

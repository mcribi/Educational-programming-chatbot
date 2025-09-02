from src.lesson import Lesson

lesson = Lesson(
    title="Inicialización de matrices",
    content=(
        "Podemos asignar valores a toda la matriz en el momento de declararla.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>int parc[2][3] = {\n"
        "    {1, 2, 3},\n"
        "    {4, 5, 6}\n"
        "};</code></pre>\n\n"
        "👉 También se pueden dejar valores sin poner (se completan con 0):\n"
        "<code>int parc[2][3] = {{1}, {3, 4, 5}};</code>"
    )
)

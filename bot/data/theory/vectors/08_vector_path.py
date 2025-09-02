from src.lesson import Lesson

lesson = Lesson(
    title="Recorridos típicos sobre vectores",
    content=(
        "Podemos hacer distintos recorridos con vectores:\n\n"
        "• <b>Búsqueda</b>: encontrar un valor.\n"
        "• <b>Inserción</b>: añadir un elemento.\n"
        "• <b>Eliminación</b>: quitar un elemento.\n"
        "• <b>Ordenación</b>: reordenar los elementos.\n\n"
        "👉 Ejemplo de búsqueda secuencial:\n"
        "<pre><code>bool encontrado = false;\n"
        "for (int i = 0; i &lt; usados; i++) {\n"
        "    if (notas[i] == 10) encontrado = true;\n"
        "}</code></pre>"
    )
)

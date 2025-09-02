from src.lesson import Lesson

lesson = Lesson(
    title="Structs y funciones",
    content=(
        "Un <code>struct</code> puede usarse como parámetro o como valor de retorno de una función.\n\n"
        "<b>Ejemplo:</b>\n"
        "<pre><code>struct Punto2D {\n"
        "    double abscisa;\n"
        "    double ordenada;\n"
        "};\n\n"
        "Punto2D PuntoMedio(Punto2D p1, Punto2D p2) {\n"
        "    Punto2D medio;\n"
        "    medio.abscisa = (p1.abscisa + p2.abscisa) / 2;\n"
        "    medio.ordenada = (p1.ordenada + p2.ordenada) / 2;\n"
        "    return medio;\n"
        "}</code></pre>\n\n"
        "👉 La función devuelve el punto medio entre dos puntos."
    )
)

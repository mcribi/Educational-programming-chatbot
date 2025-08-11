from src.lesson import Lesson

lesson = Lesson(
    title="Ámbito de las variables",
    content=(
        "El <b>ámbito</b> de una variable define en qué parte del programa es accesible.\n\n"
        "Si declaras una variable dentro de <code>main()</code>, solo puedes usarla ahí:\n"
        "<code>int main() {\n"
        "    int x = 5;\n"
        "}</code>\n\n"
        "Fuera de esa zona, <code>x</code> no existe.\n\n"
        "Por ahora, todos los datos los estamos declarando dentro del programa principal y su ámbito es el propio programa principal.\n"
        "Más adelante veremos otros sitios en los que se pueden declarar datos y por tanto habrá que analizar cuál es su ámbito.\n"
    )
)

from src.lesson import Lesson

lesson = Lesson(
    title="Constructores, destructores y sobrecarga",
    content=(
        "Un <b>constructor</b> es un método especial que se ejecuta al crear un objeto.\n"
        "• Tiene el mismo nombre que la clase.\n"
        "• No devuelve nada.\n\n"
        "Un <b>destructor</b> es un método que se ejecuta al destruir el objeto (se define con <code>~</code>).\n\n"

        "<b>Ejemplo con constructor:</b>\n"
        "<pre><code>class Fecha {\n"
        "private:\n"
        "    int dia, mes, anio;\n"
        "public:\n"
        "    Fecha(int d, int m, int a) : dia(d), mes(m), anio(a) {}\n"
        "};\n\n"
        "int main() {\n"
        "    Fecha cumple(27, 2, 2020);\n"
        "}</code></pre>\n\n"

        "👉 <b>Sobrecarga de constructores</b>: podemos definir varios constructores con distintos parámetros.\n"
        "👉 <b>Constructor de copia</b>: permite crear un objeto copiando otro.\n"
        "👉 <b>Operador de asignación (=)</b>: se usa para copiar objetos ya existentes.\n"
        "👉 <b>Destructor (~Clase)</b>: libera recursos al final de la vida del objeto."
    )
)

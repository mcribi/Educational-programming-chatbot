from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué son las clases y objetos?",
    content=(
        "Una <b>clase</b> es un modelo que agrupa datos (atributos) y funciones (métodos) en una sola unidad.\n"
        "Un <b>objeto</b> es una instancia concreta de esa clase.\n\n"

        "👉 Principios básicos que cumplen las clases:\n"
        "• <b>Encapsulación</b>: agrupar datos y funciones en un mismo módulo.\n"
        "• <b>Ocultación de información</b>: proteger los datos internos, accediendo a ellos solo mediante métodos.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>class CuentaBancaria {\n"
        "private:\n"
        "    double saldo;\n\n"
        "public:\n"
        "    void Ingresa(double cantidad) { saldo += cantidad; }\n"
        "    void Retira(double cantidad) { saldo -= cantidad; }\n"
        "    double Saldo() { return saldo; }\n"
        "};\n\n"
        "int main() {\n"
        "    CuentaBancaria cuenta;\n"
        "    cuenta.Ingresa(100);\n"
        "    cout &lt;&lt; cuenta.Saldo();  // 100\n"
        "}</code></pre>"
    )
)

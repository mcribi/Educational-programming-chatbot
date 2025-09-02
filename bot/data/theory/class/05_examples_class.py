from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos con clases",
    content=(
        "🔹 <b>Ejemplo 1: Clase Rectángulo</b>\n"
        "<pre><code>class Rectangulo {\n"
        "private:\n"
        "    double ancho, alto;\n"
        "public:\n"
        "    Rectangulo(double a, double h) : ancho(a), alto(h) {}\n"
        "    double Area() { return ancho * alto; }\n"
        "};\n\n"
        "int main() {\n"
        "    Rectangulo r(3,4);\n"
        "    cout &lt;&lt; r.Area(); // 12\n"
        "}</code></pre>\n\n"

        "🔹 <b>Ejemplo 2: Clase Cuenta Bancaria con métodos</b>\n"
        "<pre><code>CuentaBancaria cuenta(\"123\", 100);\n"
        "cuenta.Ingresa(50);\n"
        "cuenta.Retira(20);\n"
        "cout &lt;&lt; cuenta.Saldo();  // 130</code></pre>\n\n"

        "👉 Estos ejemplos muestran cómo modelar objetos del mundo real en C++."
    )
)

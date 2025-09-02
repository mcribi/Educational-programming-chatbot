from src.lesson import Lesson

lesson = Lesson(
    title="Constantes, ámbitos y buenas prácticas",
    content=(
        "En las clases podemos definir constantes:\n"
        "• <b>Constantes de objeto</b>: cada objeto tiene su propio valor.\n"
        "• <b>Constantes estáticas</b>: son compartidas por todos los objetos.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>class Circulo {\n"
        "private:\n"
        "    const double PI;\n"
        "    double radio;\n"
        "public:\n"
        "    Circulo(double r) : PI(3.1416), radio(r) {}\n"
        "    double Area() { return PI * radio * radio; }\n"
        "};</code></pre>\n\n"

        "📌 Buenas prácticas:\n"
        "• Usar nombres significativos (CuentaBancaria, Persona...).\n"
        "• Métodos en mayúscula inicial (SetEdad, Mostrar).\n"
        "• Variables y objetos en minúscula (mi_cuenta).\n"
        "• Mantener clases simples y con una única responsabilidad."
    )
)

from src.lesson import Lesson

lesson = Lesson(
    title="Encapsulación: atributos y métodos",
    content=(
        "Dentro de una clase diferenciamos:\n"
        "• <b>private</b>: solo accesibles dentro de la clase.\n"
        "• <b>public</b>: accesibles desde fuera de la clase.\n\n"

        "👉 Los <b>atributos</b> son los datos que describen al objeto.\n"
        "👉 Los <b>métodos</b> son las funciones que operan sobre esos datos.\n\n"

        "<b>Ejemplo:</b>\n"
        "<pre><code>class Persona {\n"
        "private:\n"
        "    string nombre;\n"
        "    int edad;\n\n"
        "public:\n"
        "    void SetNombre(string n) { nombre = n; }\n"
        "    void SetEdad(int e) { edad = e; }\n"
        "    void Mostrar() { cout &lt;&lt; nombre &lt;&lt; \" (\" &lt;&lt; edad &lt;&lt; \")\"; }\n"
        "};</code></pre>\n\n"

        "📌 La encapsulación protege los datos internos y facilita la legibilidad."
    )
)

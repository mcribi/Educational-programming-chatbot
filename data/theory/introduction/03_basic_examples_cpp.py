from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos básicos en C++",
    content=(
        "<b>Ejemplo 1: Mostrar un mensaje</b>\n"
        "<pre><code>#include &lt;iostream&gt;\n"
        "using namespace std;\n\n"
        "int main() {\n"
        "    cout &lt;&lt; \"Hola, mundo!\";\n"
        "    return 0;\n"
        "}</code></pre>\n"
        "👉 Este código imprime <i>Hola, mundo!</i> en la consola.\n\n"

        "<b>Ejemplo 2: Sumar dos números</b>\n"
        "<pre><code>#include &lt;iostream&gt;\n"
        "using namespace std;\n\n"
        "int main() {\n"
        "    int a = 3;\n"
        "    int b = 5;\n"
        "    int suma = a + b;\n"
        "    cout &lt;&lt; \"La suma es: \" &lt;&lt; suma;\n"
        "    return 0;\n"
        "}</code></pre>\n"
        "👉 Declara dos variables, las suma y muestra el resultado.\n\n"

        "<b>Ejemplo 3: Leer datos del usuario</b>\n"
        "<pre><code>#include &lt;iostream&gt;\n"
        "using namespace std;\n\n"
        "int main() {\n"
        "    int edad;\n"
        "    cout &lt;&lt; \"Introduce tu edad: \";\n"
        "    cin &gt;&gt; edad;\n"
        "    cout &lt;&lt; \"Tienes \" &lt;&lt; edad &lt;&lt; \" años.\";\n"
        "    return 0;\n"
        "}</code></pre>\n"
        "👉 Usa <code>cin</code> para leer un valor introducido por el usuario."
    )
)

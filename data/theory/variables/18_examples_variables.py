from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos representativos con variables",
    content=(
        "Veamos algunos ejemplos prácticos que usan variables, tipos de datos, operaciones y entrada/salida de información:\n\n"

        "🔢 <b>Ejemplo 1: Sumar dos números</b>\n"
        "<pre>\n"
        "int a = 5;\n"
        "int b = 3;\n"
        "int suma = a + b;\n"
        "cout &lt;&lt; \"Resultado: \" &lt;&lt; suma;\n"
        "</pre>\n"
        "👉 Imprime: <code>Resultado: 8</code>\n\n"

        "📏 <b>Ejemplo 2: Calcular el área de un círculo</b>\n"
        "<pre>\n"
        "const double PI = 3.1416;\n"
        "double radio = 2.5;\n"
        "double area = PI * radio * radio;\n"
        "cout &lt;&lt; \"Área: \" &lt;&lt; area;\n"
        "</pre>\n"
        "👉 Usa una constante para PI y realiza una operación con <code>double</code>\n\n"

        "👤 <b>Ejemplo 3: Leer edad del usuario y mostrar mensaje</b>\n"
        "<pre>\n"
        "int edad;\n"
        "cout &lt;&lt; \"¿Cuántos años tienes? \";\n"
        "cin &gt;&gt; edad;\n"
        "cout &lt;&lt; \"Tienes \" &lt;&lt; edad &lt;&lt; \" años.\";\n"
        "</pre>\n"
        "👉 Usa <code>cin</code> para entrada de datos y <code>cout</code> para mostrar resultado\n\n"

        "🎯 <b>Ejemplo 4: Operaciones con tipos distintos</b>\n"
        "<pre>\n"
        "int unidades = 2;\n"
        "double precio = 4.99;\n"
        "double total = unidades * precio;\n"
        "cout &lt;&lt; \"Total: \" &lt;&lt; total;\n"
        "</pre>\n"
        "👉 C++ convierte automáticamente <code>int</code> a <code>double</code> en la multiplicación\n\n"

        "🔤 <b>Ejemplo 5: Combinar texto y variables tipo <code>string</code></b>\n"
        "<pre>\n"
        "#include &lt;string&gt;\n"
        "string nombre = \"Lucía\";\n"
        "cout &lt;&lt; \"Hola, \" &lt;&lt; nombre &lt;&lt; \"!\";\n"
        "</pre>\n"
        "👉 Recuerda incluir <code>&lt;string&gt;</code> para usar variables <code>string</code>\n\n"

        "➗ <b>Ejemplo 6: División entre enteros</b>\n"
        "<pre>\n"
        "int resultado = 3 / 2;\n"
        "cout &lt;&lt; resultado;\n"
        "</pre>\n"
        "👉 Aunque 3 entre 2 es 1.5, como ambos son <code>int</code>, el resultado será <code>1</code> (división entera)."
    )
)

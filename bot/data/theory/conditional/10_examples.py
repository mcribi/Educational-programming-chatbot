from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos con condicionales",
    content=(
        "Veamos cómo se aplican las estructuras condicionales en casos reales y sencillos:\n\n"

        "🔹 <b>Ejemplo 1: Verificar mayoría de edad</b>\n"
        "<pre><code>int edad = 20;\n"
        "if (edad &gt;= 18) {\n"
        "    cout &lt;&lt; \"Eres mayor de edad.\";\n"
        "}</code></pre>\n"
        "👉 Si la condición se cumple, se ejecuta el mensaje. Si no, no pasa nada.\n\n"

        "🔹 <b>Ejemplo 2: Usar if-else</b>\n"
        "<pre><code>int nota = 4;\n"
        "if (nota &gt;= 5) {\n"
        "    cout &lt;&lt; \"Aprobado\";\n"
        "} else {\n"
        "    cout &lt;&lt; \"Suspenso\";\n"
        "}</code></pre>\n"
        "👉 Se ejecuta uno de los dos bloques, pero nunca los dos.\n\n"

        "🔹 <b>Ejemplo 3: Condición compuesta</b>\n"
        "<pre><code>int edad = 25;\n"
        "int altura = 170;\n"
        "if (edad &gt;= 18 &amp;&amp; altura &gt;= 160) {\n"
        "    cout &lt;&lt; \"Puedes participar\";\n"
        "}</code></pre>\n"
        "👉 Ambas condiciones deben cumplirse para que se imprima el mensaje.\n\n"

        "🔹 <b>Ejemplo 4: else if con múltiples opciones</b>\n"
        "<pre><code>int numero = 0;\n"
        "if (numero &gt; 0) {\n"
        "    cout &lt;&lt; \"Positivo\";\n"
        "} else if (numero &lt; 0) {\n"
        "    cout &lt;&lt; \"Negativo\";\n"
        "} else {\n"
        "    cout &lt;&lt; \"Cero\";\n"
        "}</code></pre>\n"
        "👉 Se evalúan las condiciones en orden. Solo una se ejecuta.\n\n"

        "🔹 <b>Ejemplo 5: Estructura switch</b>\n"
        "<pre><code>char letra = 'b';\n"
        "switch (letra) {\n"
        "    case 'a': cout &lt;&lt; \"Vocal A\"; break;\n"
        "    case 'e': cout &lt;&lt; \"Vocal E\"; break;\n"
        "    default: cout &lt;&lt; \"Otra letra\";\n"
        "}</code></pre>\n"
        "👉 switch evalúa el valor exacto de la variable.\n\n"

        "🔹 <b>Ejemplo 6: Error común al comparar decimales</b>\n"
        "<pre><code>double x = 0.1 + 0.2;\n"
        "if (x == 0.3) {\n"
        "    cout &lt;&lt; \"Iguales\";\n"
        "} else {\n"
        "    cout &lt;&lt; \"Distintos\";\n"
        "}</code></pre>\n"
        "👉 Puede imprimir \"Distintos\" por errores de precisión. Mejor usar una tolerancia:\n"
        "<code>if (abs(x - 0.3) &lt; 1e-6)</code>"
    )
)

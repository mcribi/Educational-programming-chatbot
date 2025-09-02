from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos con vectores",
    content=(
        "🔹 <b>Ejemplo 1: Calcular media</b>\n"
        "<pre><code>double suma = 0;\n"
        "for (int i = 0; i &lt; usados; i++) suma += notas[i];\n"
        "cout &lt;&lt; \"Media = \" &lt;&lt; suma / usados;</code></pre>\n\n"
        "🔹 <b>Ejemplo 2: Contar mayores de 5</b>\n"
        "<pre><code>int contador = 0;\n"
        "for (int i = 0; i &lt; usados; i++)\n"
        "    if (notas[i] &gt; 5) contador++;\n"
        "</code></pre>\n\n"
        "🔹 <b>Ejemplo 3: Ordenación simple (burbuja)</b>\n"
        "<pre><code>for (int i = 0; i &lt; usados-1; i++)\n"
        "  for (int j = 0; j &lt; usados-1; j++)\n"
        "    if (notas[j] &gt; notas[j+1]) {\n"
        "       swap(notas[j], notas[j+1]);\n"
        "    }</code></pre>"
    )
)

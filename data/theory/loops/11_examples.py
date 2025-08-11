from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos con bucles",
    content=(
        "🔹 <b>Ejemplo 1: Sumar los números del 1 al 10</b>\n"
        "<pre><code>int suma = 0;\nfor (int i = 1; i &lt;= 10; i++) {\n    suma += i;\n}\ncout &lt;&lt; suma;</code></pre>\n\n"
        "🔹 <b>Ejemplo 2: Pedir 5 números y calcular la media</b>\n"
        "<pre><code>int total = 0;\nfor (int i = 0; i &lt; 5; i++) {\n    int n;\n    cin &gt;&gt; n;\n    total += n;\n}\ndouble media = total / 5.0;</code></pre>\n\n"
        "🔹 <b>Ejemplo 3: Mostrar los pares del 2 al 10</b>\n"
        "<pre><code>for (int i = 2; i &lt;= 10; i += 2) {\n    cout &lt;&lt; i &lt;&lt; \" \";\n}</code></pre>"
    )
)

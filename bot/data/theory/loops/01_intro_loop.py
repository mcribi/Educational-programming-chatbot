from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es una estructura repetitiva?",
    content=(
        "Una <b>estructura repetitiva</b> (o bucle) permite repetir instrucciones varias veces mientras se cumpla una condición.\n\n"
        "Esto evita tener que escribir el mismo código muchas veces y hace los programas más flexibles y potentes.\n\n"
        "📌 A cada vuelta que da el bucle se le llama <b>iteración</b>.\n\n"
        "<b>Tipos de bucles en C++:</b>\n"
        "• <b>while</b>: evalúa la condición antes de entrar.\n"
        "• <b>do-while</b>: evalúa la condición después de ejecutar.\n"
        "• <b>for</b>: bucle con contador (inicio, condición, incremento).\n\n"
        "<b>Ejemplo básico:</b>\n"
        "<pre><code>int i = 0;\nwhile (i &lt; 3) {\n    cout &lt;&lt; \"Hola\";\n    i++;\n}</code></pre>\n"
        "👉 Imprime <i>Hola</i> tres veces."
    )
)

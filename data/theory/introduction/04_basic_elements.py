from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué elementos forman un lenguaje de programación?",
    content=(
        "Para escribir programas en C++ necesitamos entender de qué está hecho el lenguaje. Estos son sus elementos básicos:\n\n"

        "1. <b>Tokens:</b> Son las piezas mínimas del lenguaje: palabras, símbolos, operadores...\n"
        "   Ejemplos: <code>main</code>, <code>;</code>, <code>=</code>, <code>+</code>, <code>sqrt</code>\n\n"

        "2. <b>Reglas sintácticas:</b> Indican cómo se combinan los tokens para formar frases válidas.\n"
        "   • Las órdenes se separan con <code>;</code>\n"
        "   • Los bloques se agrupan con <code>{ }</code>\n"
        "   • Las expresiones se agrupan con <code>( )</code>\n\n"

        "3. <b>Palabras reservadas:</b> Son palabras que tienen un significado especial y no se pueden usar como nombres de variables. Ejemplos:\n"
        "   • <code>int</code>, <code>if</code>, <code>while</code>, <code>return</code>, <code>double</code>, <code>for</code>, <code>break</code>\n\n"

        "4. <b>El compilador las reconoce</b> y les da un significado especial, así que no podemos usarlas para otras cosas.\n\n"

        "⚠️ <i>Importante:</i> Si no respetamos estas reglas, el compilador mostrará errores."
    )
)

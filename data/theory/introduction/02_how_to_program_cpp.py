from src.lesson import Lesson

lesson = Lesson(
    title="¿Cómo se programa en C++?",
    content=(
        "<b>¿Cómo se programa en C++?</b>\n\n"
        "Para programar en C++ necesitas tres elementos:\n"
        "1. Un <b>editor de texto</b> para escribir el código (puede ser VS Code, Sublime, etc).\n"
        "2. Un <b>compilador</b> como <code>g++</code> o <code>clang++</code> para traducir el código a lenguaje máquina.\n"
        "3. Una <b>terminal</b> para ejecutar los comandos y el programa compilado.\n\n"

        "<b>Pasos básicos para compilar y ejecutar:</b>\n"
        "1. Escribe tu código y guárdalo como <code>programa.cpp</code>\n"
        "2. Compílalo: <code>g++ programa.cpp -o programa</code>\n"
        "3. Ejecútalo: <code>./programa</code>\n\n"

        "<b>¿Qué hace el compilador?</b>\n"
        "Convierte el archivo fuente en un archivo ejecutable que puede correr directamente en tu sistema operativo.\n\n"

        "<b>Errores comunes:</b>\n"
        "• Olvidar poner punto y coma (<code>;</code>) al final de las instrucciones.\n"
        "• Declarar mal el tipo de una variable.\n"
        "• Usar mal los paréntesis o llaves (<code>{ }</code>).\n\n"

        "¡Con práctica estos errores se vuelven fáciles de evitar!"
    )
)

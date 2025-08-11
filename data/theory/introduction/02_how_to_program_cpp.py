from src.lesson import Lesson

lesson = Lesson(
    title="¿Cómo se programa en C++?",
    content=(
        "Para comenzar a programar en C++, necesitas tres elementos básicos:\n"
        "1. Un <b>editor de texto</b> para escribir el código fuente. Puede ser un editor sencillo como el Bloc de notas o uno más completo como <i>Visual Studio Code</i>.\n"
        "2. Un <b>compilador</b>, como <code>g++</code>, que se encarga de traducir el código en C++ a un programa que el ordenador pueda entender.\n"
        "3. Una <b>terminal</b> o consola, donde puedes dar órdenes como compilar y ejecutar tu programa.\n\n"

        "<b>Pasos básicos para compilar y ejecutar un programa en C++:</b>\n"
        "1. Escribe tu código en un archivo, por ejemplo <code>programa.cpp</code>.\n"
        "2. Compílalo con el comando: <code>g++ programa.cpp -o programa</code>\n"
        "3. Ejecuta el programa con: <code>./programa</code>\n\n"

        "<b>¿Qué hace el compilador?</b>\n"
        "Convierte el código fuente (que tú entiendes) en un archivo ejecutable (que entiende el ordenador). Si el código tiene errores, el compilador te avisará para que los corrijas.\n\n"

        "<b>¿Y si no tienes un compilador instalado?</b>\n"
        "¡No te preocupes! También puedes programar y ejecutar tus programas C++ directamente desde tu navegador usando páginas web como:\n"
        "• <a href='https://www.onlinegdb.com/online_c++_compiler'>OnlineGDB</a>\n"
        "• <a href='https://www.programiz.com/cpp-programming/online-compiler/'>Programiz</a>\n"
        "• <a href='https://www.mycompiler.io/es/online-c++-compiler'>MyCompiler</a>\n\n"

        "Además, con nuestro chatbot educativo en Telegram, ¡también podrás programar en C++ directamente desde tu móvil! En el apartado de 'Programar', podrás escribir código, ejecutarlo y recibir feedback al instante."
    )
)

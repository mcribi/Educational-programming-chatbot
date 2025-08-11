from src.lesson import Lesson

lesson = Lesson(
    title="¿Qué es programar?",
    content=(
        # "<b>¿Qué es programar?</b>\n\n"
        "Programar consiste en <i>dar instrucciones a un ordenador</i> para que realice tareas específicas. "
        "Estas instrucciones se escriben en un <b>lenguaje de programación</b> como por ejemplo C++, que permite controlar el comportamiento de la máquina.\n\n"

        "<b>¿Para qué sirve programar?</b>\n"
        "Sirve para crear aplicaciones, videojuegos, controlar robots, analizar datos...\n\n"

        "<b>Conceptos básicos:</b>\n"
        "• <b>Algoritmo</b>: Conjunto de pasos ordenados para resolver un problema.\n"
        "• <b>Lenguaje de programación</b>: Lenguaje formal utilizado para comunicarnos con un ordenador e imponerle la ejecución de un conjunto de órdenes. Ejemplos más utilizados actualmente: C++, Python, Java...\n"
        "• <b>Programa</b>: Archivo o conjunto de archivos que contienen las instrucciones que sigue el ordenador.\n\n"

        "<b>Definiciones importantes:</b>\n"
        "• <b>Programación</b>: Es el proceso de diseñar, escribir, depurar y mantener el código fuente de programas informáticos. "
        "Involucra tanto la parte lógica (pensar el algoritmo) como la parte técnica (escribirlo en un lenguaje).\n"
        "• <b>Compilación</b>: Es el proceso mediante el cual el código fuente escrito por el programador se traduce a un lenguaje "
        "que entiende la máquina (código objeto o ejecutable), mediante un programa llamado <i>compilador</i>.\n\n"

        "<b>Ejemplo simple en C++:</b>\n"
        "<pre><code>#include &lt;iostream&gt;\n"
        "using namespace std;\n\n"
        "int main() {\n"
        "    cout &lt;&lt; \\\"Hola mundo\\\";\n"
        "    return 0;\n"
        "}</code></pre>\n\n"

        "Este programa muestra por pantalla el mensaje <i>Hola mundo</i>. "
        "Es uno de los primeros pasos al aprender cualquier lenguaje."
    )
)

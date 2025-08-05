from src.exercise import Exercise

#exercises of topic introduction 

exercises_introduction = [
    Exercise(
        type_="test",
        question="¿Cuál es el punto de entrada de un programa en C++?",
        options=["inicio", "start", "main", "run"],
        answer="main",
        explanation="La función <code>main()</code> es el punto de inicio obligatorio de un programa en C++."
    ),
    Exercise(
        type_="test",
        question="¿Qué hace un compilador?",
        options=[
            "Ejecuta directamente el programa",
            "Traduce el código fuente a lenguaje máquina",
            "Corrige errores de lógica automáticamente",
            "Guarda el programa en la nube"
        ],
        answer="Traduce el código fuente a lenguaje máquina",
        explanation="El compilador convierte el código que escribe el programador en un archivo ejecutable que entiende la máquina."
    ),
    Exercise(
        type_="test",
        question="¿Qué significa programar?",
        options=[
            "Dar órdenes a un ordenador usando lenguaje natural",
            "Configurar hardware manualmente",
            "Escribir instrucciones en un lenguaje que entienda el ordenador",
            "Instalar programas desde internet"
        ],
        answer="Escribir instrucciones en un lenguaje que entienda el ordenador",
        explanation="Programar es expresar algoritmos mediante lenguajes formales para que el ordenador los ejecute."
    ),
    Exercise(
        type_="test",
        question="¿Cuál de estas opciones representa un algoritmo?",
        options=[
            "Una lista de compras",
            "Una receta de cocina paso a paso",
            "Una imagen JPEG",
            "Un botón del menú"
        ],
        answer="Una receta de cocina paso a paso",
        explanation="Un algoritmo es una secuencia ordenada de pasos para resolver un problema, como una receta."
    ),
    Exercise(
        type_="test",
        question="¿Cuál de las siguientes afirmaciones es cierta sobre C++?",
        options=[
            "Es un lenguaje visual sin código",
            "Solo sirve para diseño gráfico",
            "Es un lenguaje de programación de propósito general",
            "No necesita compilador"
        ],
        answer="Es un lenguaje de programación de propósito general",
        explanation="C++ es un lenguaje muy potente y versátil, usado en múltiples áreas desde videojuegos hasta sistemas embebidos."
    ),
    Exercise(
        type_="test",
        question="¿Qué archivo contiene el código que el programador escribe?",
        options=[
            "Archivo ejecutable",
            "Archivo fuente",
            "Archivo comprimido",
            "Archivo de datos"
        ],
        answer="Archivo fuente",
        explanation="El archivo fuente contiene el código original (<code>.cpp</code> en C++) que será compilado."
    ),
    Exercise(
        type_="test",
        question="¿Cuál es la extensión habitual de un archivo fuente en C++?",
        options=[".py", ".java", ".cpp", ".exe"],
        answer=".cpp",
        explanation="En C++, los archivos de código fuente suelen tener la extensión <code>.cpp</code>."
    ),
    Exercise(
        type_="test",
        question="¿Qué instrucción se usa en C++ para mostrar texto por pantalla?",
        options=["printf", "print", "cout", "echo"],
        answer="cout",
        explanation="La instrucción <code>cout</code> (de <i>character output</i>) se usa en C++ junto con el operador <code>&lt;&lt;</code> para mostrar texto."
    )
]

from src.exercise import Exercise

exercises_introduction = [
    Exercise(
        type_="test",
        question="¿Cuál es el punto de entrada de un programa en C++?",
        options=["inicio", "start", "main", "run"],
        answer="main",
        explanation="La función <code>main()</code> es obligatoria y marca el inicio de la ejecución en un programa en C++."
    ),
    Exercise(
        type_="test",
        question="¿Qué hace un compilador?",
        options=[
            "Ejecuta directamente el programa",
            "Traduce el código fuente a lenguaje máquina",
            "Corrige errores automáticamente",
            "Transforma imágenes en código"
        ],
        answer="Traduce el código fuente a lenguaje máquina",
        explanation="El compilador convierte el código que escribe el programador en un ejecutable que entiende el ordenador."
    ),
    Exercise(
        type_="test",
        question="¿Qué significa programar?",
        options=[
            "Dar órdenes usando lenguaje natural",
            "Diseñar aplicaciones sin escribir código",
            "Escribir instrucciones que entiende el ordenador",
            "Instalar programas desde internet"
        ],
        answer="Escribir instrucciones que entiende el ordenador",
        explanation="Programar consiste en dar instrucciones al ordenador usando un lenguaje formal como C++."
    ),
    Exercise(
        type_="test",
        question="¿Cuál de estos ejemplos representa un algoritmo?",
        options=[
            "Una lista de la compra",
            "Una receta paso a paso",
            "Una canción en mp3",
            "Un mapa de carreteras"
        ],
        answer="Una receta paso a paso",
        explanation="Un algoritmo es una secuencia ordenada de pasos para resolver un problema, como una receta."
    ),
    Exercise(
        type_="test",
        question="¿Cuál de estas afirmaciones sobre C++ es verdadera?",
        options=[
            "Es un lenguaje visual sin código",
            "Solo sirve para diseño gráfico",
            "Es un lenguaje de propósito general",
            "No necesita compilador"
        ],
        answer="Es un lenguaje de propósito general",
        explanation="C++ es un lenguaje de programación potente y versátil que sirve para muchas aplicaciones."
    ),
    Exercise(
        type_="test",
        question="¿Qué tipo de archivo contiene el código que escribe el programador?",
        options=[
            "Archivo ejecutable",
            "Archivo fuente",
            "Archivo comprimido",
            "Archivo multimedia"
        ],
        answer="Archivo fuente",
        explanation="El archivo fuente (<code>.cpp</code>) contiene el código en C++ que será compilado."
    ),
    Exercise(
        type_="test",
        question="¿Cuál es la extensión habitual de un archivo fuente en C++?",
        options=[".py", ".java", ".cpp", ".exe"],
        answer=".cpp",
        explanation="Los archivos de código en C++ suelen tener la extensión <code>.cpp</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué instrucción se usa en C++ para mostrar texto en pantalla?",
        options=["printf", "print", "cout", "echo"],
        answer="cout",
        explanation="<code>cout</code> se utiliza junto con <code>&lt;&lt;</code> para mostrar mensajes por pantalla en C++."
    ), 
    Exercise(
        type_="test",
        question="¿Qué biblioteca necesitas incluir para usar <code>cout</code> en C++?",
        options=["<math>", "<string>", "<iostream>", "<stdio.h>"],
        answer="<iostream>",
        explanation="<code>#include &lt;iostream&gt;</code> permite usar <code>cout</code> y <code>cin</code> en C++."
    ),

    Exercise(
        type_="truefalse",
        question="La función <code>main()</code> en C++ puede escribirse sin llaves <code>{ }</code>.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Todas las funciones en C++ deben tener su contenido entre llaves <code>{ }</code>."
    ),

    Exercise(
        type_="yesno",
        question="¿Es obligatorio escribir <code>return 0;</code> al final de la función <code>main()</code>?",
        options=["Sí", "No"],
        answer="Sí",
        explanation="Aunque algunos compiladores lo permiten omitir, lo correcto es terminar <code>main()</code> con <code>return 0;</code>."
    ),

    Exercise(
        type_="truefalse",
        question="Los comentarios en C++ pueden ayudar a entender el código pero no afectan al funcionamiento del programa.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Los comentarios son ignorados por el compilador y sirven solo para explicar o documentar el código."
    ),

    Exercise(
        type_="test",
        question="¿Qué espacio de nombres se usa habitualmente para evitar escribir <code>std::</code>?",
        options=["namespace global", "iostream", "std", "main"],
        answer="std",
        explanation="<code>using namespace std;</code> permite usar <code>cout</code> en lugar de <code>std::cout</code>."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estos NO es un elemento básico de un lenguaje de programación según el temario?",
        options=["Tokens", "Sintaxis", "Tipos de letra", "Palabras reservadas"],
        answer="Tipos de letra",
        explanation="Los elementos básicos incluyen tokens, sintaxis y palabras reservadas. 'Tipos de letra' no forma parte del lenguaje."
    ),

    Exercise(
        type_="yesno",
        question="¿Se pueden usar palabras como <code>if</code> o <code>while</code> como nombres de variables?",
        options=["Sí", "No"],
        answer="No",
        explanation="No se pueden usar palabras reservadas como nombres de variables porque tienen un significado especial en el lenguaje."
    ),

    Exercise(
        type_="truefalse",
        question="Un programa en C++ puede funcionar correctamente sin incluir ninguna biblioteca.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Para usar funcionalidades como entrada/salida, se deben incluir bibliotecas como <code>iostream</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué operador se usa con <code>cout</code> para mostrar texto?",
        options=["<<", ">>", "**", "::"],
        answer="<<",
        explanation="El operador <code>&lt;&lt;</code> se usa para enviar datos a la salida estándar con <code>cout</code>."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el orden correcto de las partes básicas de un programa en C++?",
        options=[
            "main(), comentarios, bibliotecas",
            "comentarios, bibliotecas, main()",
            "bibliotecas, main(), comentarios",
            "bibliotecas, comentarios, main()"
        ],
        answer="comentarios, bibliotecas, main()",
        explanation="Normalmente un programa empieza con comentarios, luego incluye bibliotecas, y finalmente define <code>main()</code>."
    ),
    
    #exercises of thinking, little piece of code
    Exercise(
        type_="test",
        question="¿Qué muestra este programa?\n<pre><code>#include &lt;iostream&gt;\nusing namespace std;\n\nint main() {\n    cout &lt;&lt; \"Hola\";\n    return 0;\n}</code></pre>",
        options=["Hola", "hola", "Error", "Nada"],
        answer="Hola",
        explanation="El texto entre comillas se imprime tal cual en pantalla, y C++ distingue mayúsculas."
    ),

    Exercise(
        type_="test",
        question="¿Qué se imprime?\n<pre><code>int main() {\n    cout &lt;&lt; \"Hola\" &lt;&lt; \" mundo\";\n    return 0;\n}</code></pre>",
        options=["Hola", "Hola mundo", "mundo", "Hola\nmundo"],
        answer="Hola mundo",
        explanation="Se pueden encadenar cadenas con <code>&lt;&lt;</code>. No hay salto de línea."
    ),

    Exercise(
        type_="test",
        question="¿Qué resultado tiene este código?\n<pre><code>int main() {\n    cout &lt;&lt; \"1 + 1\";\n    return 0;\n}</code></pre>",
        options=["2", "11", "1 + 1", "Error"],
        answer="1 + 1",
        explanation="El texto entre comillas no se evalúa como operación matemática."
    ),

    Exercise(
        type_="test",
        question="¿Qué aparece en pantalla?\n<pre><code>int main() {\n    cout &lt;&lt; \"Hola\";\n    cout &lt;&lt; \" mundo\";\n    return 0;\n}</code></pre>",
        options=["Hola", "Hola mundo", "Hola (salto de línea) mundo", "Error"],
        answer="Hola mundo",
        explanation="Ambas instrucciones imprimen una cadena cada una sin salto de línea."
    ),

    Exercise(
        type_="test",
        question="¿Qué muestra este programa?\n<pre><code>int main() {\n    // cout &lt;&lt; \"Hola\";\n    cout &lt;&lt; \"Adiós\";\n    return 0;\n}</code></pre>",
        options=["Hola", "Adiós", "Hola Adiós", "Error"],
        answer="Adiós",
        explanation="La primera línea está comentada, así que no se ejecuta."
    ),

    Exercise(
        type_="test",
        question="¿Qué se imprime?\n<pre><code>int main() {\n    cout &lt;&lt; \"Hola\" &lt;&lt; endl;\n    return 0;\n}</code></pre>",
        options=["Hola", "Hola\n", "endl", "Error"],
        answer="Hola\n",
        explanation="<code>endl</code> genera un salto de línea después de imprimir 'Hola'."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime este programa?\n<pre><code>int main() {\n    cout &lt;&lt; \"Hola\" &lt;&lt; \", \" &lt;&lt; \"mundo\";\n    return 0;\n}</code></pre>",
        options=["Hola mundo", "Hola, mundo", "Hola,mundo", "Error"],
        answer="Hola, mundo",
        explanation="Las cadenas se concatenan y se imprimen tal cual aparecen entre comillas."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el resultado?\n<pre><code>int main() {\n    cout &lt;&lt; \"Hola\";\n    return 0;\n    cout &lt;&lt; \"Adiós\";\n}</code></pre>",
        options=["Hola Adiós", "Adiós", "Hola", "Nada"],
        answer="Hola",
        explanation="El <code>return 0;</code> termina el programa, así que 'Adiós' no se imprime."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este código?\n<pre><code>int main() {\n    cout &lt;&lt; 3 &lt;&lt; 5;\n    return 0;\n}</code></pre>",
        options=["8", "35", "Error", "3 5"],
        answer="35",
        explanation="Se imprimen los números 3 y 5 uno tras otro, sin espacio entre ellos."
    )
    
]

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
    ),
    Exercise(
        type_="code",
        question="Lee un nombre y muestra 'Hola, <nombre>'.",
        tests_json={
            "sample": [{"input": "Maria\n", "output": "Hola, Maria"}],
            "hidden": [
                {"input": "Juan\n", "output": "Hola, Juan"},
                {"input": "C++\n", "output": "Hola, C++"}
            ]
        },
        hint="Usa getline para admitir espacios. El verificador ignora un salto de línea FINAL si lo añades.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ string s; getline(cin, s); cout << "Hola, " << s; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos enteros y muestra su suma.",
        tests_json={
            "sample": [{"input": "7 5\n", "output": "12"}],
            "hidden": [
                {"input": "-3 10\n", "output": "7"},
                {"input": "0 0\n", "output": "0"}
            ]
        },
        hint="Lee con cin dos enteros y súmalos. El salto de línea final es opcional para el verificador.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; if(!(cin>>a>>b)) return 0; cout<<a+b; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos enteros y muestra su producto.",
        tests_json={
            "sample": [{"input": "4 5\n", "output": "20"}],
            "hidden": [
                {"input": "-3 6\n", "output": "-18"},
                {"input": "1000 0\n", "output": "0"}
            ]
        },
        hint="Multiplica los dos enteros. El verificador tolera el salto de línea FINAL.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; cin>>a>>b; cout<<(a*b); }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero y muestra su cuadrado.",
        tests_json={
            "sample": [{"input": "5\n", "output": "25"}],
            "hidden": [
                {"input": "-3\n", "output": "9"},
                {"input": "12\n", "output": "144"}
            ]
        },
        hint="x*x es suficiente; no necesitas pow. (Salto de línea final opcional para el verificador.)",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long x; cin>>x; cout<<x*x; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un ancho y un alto (enteros) y muestra el área del rectángulo.",
        tests_json={
            "sample": [{"input": "3 4\n", "output": "12"}],
            "hidden": [
                {"input": "7 1\n", "output": "7"},
                {"input": "0 5\n", "output": "0"}
            ]
        },
        hint="Multiplica ancho*alto (usa enteros grandes por seguridad). El salto final es opcional.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long w,h; cin>>w>>h; cout<<w*h; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero y muestra el anterior y el siguiente en líneas separadas (primero el anterior).",
        tests_json={
            "sample": [{"input": "10\n", "output": "9\n11"}],
            "hidden": [
                {"input": "0\n", "output": "-1\n1"},
                {"input": "-5\n", "output": "-6\n-4"}
            ]
        },
        hint="Imprime x-1 y x+1 en dos líneas. El verificador solo ignora un salto de línea FINAL tras la segunda línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long x; cin>>x; cout<<x-1<<"\\n"<<x+1; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un número real (double) y muestra su raíz cuadrada con 6 decimales.",
        tests_json={
            "sample": [{"input": "9\n", "output": "3.000000"}],
            "hidden": [
                {"input": "2\n", "output": "1.414214"},
                {"input": "0\n", "output": "0.000000"}
            ]
        },
        hint="Incluye <cmath> y <iomanip>; usa sqrt y fixed+setprecision(6). El salto final es opcional para el verificador.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\n#include <cmath>\nusing namespace std;\n'
            'int main(){ ios::sync_with_stdio(false); cin.tie(nullptr);\n'
            ' double x; cin>>x; cout.setf(ios::fixed); cout<<setprecision(6)<<sqrt(x); }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee una temperatura en grados Celsius (double) y muestra su equivalente en Fahrenheit con 2 decimales.",
        tests_json={
            "sample": [{"input": "0\n", "output": "32.00"}],
            "hidden": [
                {"input": "100\n", "output": "212.00"},
                {"input": "-40\n", "output": "-40.00"}
            ]
        },
        hint="F = C * 9/5 + 32. Formatea con fixed+setprecision(2). El salto final es opcional.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ double c; cin>>c; double f = c*9.0/5.0 + 32.0;\n'
            ' cout.setf(ios::fixed); cout<<setprecision(2)<<f; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee tres números reales y muestra su media aritmética con 3 decimales.",
        tests_json={
            "sample": [{"input": "3 4 5\n", "output": "4.000"}],
            "hidden": [
                {"input": "1 2 2\n", "output": "1.667"},
                {"input": "-1 0 1\n", "output": "0.000"}
            ]
        },
        hint="Usa double y (a+b+c)/3.0 con fixed+setprecision(3). El salto de línea final es opcional.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ double a,b,c; cin>>a>>b>>c; double m=(a+b+c)/3.0;\n'
            ' cout.setf(ios::fixed); cout<<setprecision(3)<<m; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee una línea de texto y muestra 'Dijiste: <texto>'.",
        tests_json={
            "sample": [{"input": "Hola mundo\n", "output": "Dijiste: Hola mundo"}],
            "hidden": [
                {"input": "   espacios delante\n", "output": "Dijiste:    espacios delante"},
                {"input": "C++ es genial\n", "output": "Dijiste: C++ es genial"}
            ]
        },
        hint="Usa getline(cin, s) para capturar toda la línea (con espacios). El verificador ignora el salto FINAL.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'int main(){ string s; getline(cin, s); cout << "Dijiste: " << s; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Convierte un total de minutos (entero) a horas y minutos. Imprime en dos líneas: horas en la primera y minutos en la segunda.",
        tests_json={
            "sample": [{"input": "130\n", "output": "2\n10"}],
            "hidden": [
                {"input": "60\n", "output": "1\n0"},
                {"input": "59\n", "output": "0\n59"}
            ]
        },
        hint="Usa h=m/60 y r=m%60. El verificador solo ignora un salto de línea FINAL tras la 2ª línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long m; cin>>m; cout<<(m/60)<<"\\n"<<(m%60); }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee el radio de un círculo (double) y muestra su área con 6 decimales. Usa π = 3.141592653589793.",
        tests_json={
            "sample": [{"input": "1\n", "output": "3.141593"}],
            "hidden": [
                {"input": "0\n", "output": "0.000000"},
                {"input": "2.5\n", "output": "19.634955"}
            ]
        },
        hint="Área = π * r * r. Usa fixed+setprecision(6). El salto final es opcional para el verificador.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ const double PI=3.141592653589793; double r; cin>>r;\n'
            ' cout.setf(ios::fixed); cout<<setprecision(6)<<(PI*r*r); }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee nombre y apellido (dos palabras) y muestra 'Nombre completo: <nombre> <apellido>'.",
        tests_json={
            "sample": [{"input": "Ada Lovelace\n", "output": "Nombre completo: Ada Lovelace"}],
            "hidden": [
                {"input": "Alan Turing\n", "output": "Nombre completo: Alan Turing"},
                {"input": "Marie Curie\n", "output": "Nombre completo: Marie Curie"}
            ]
        },
        hint="Lee dos strings con cin (separados por espacio). El salto de línea final es opcional.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ string nombre, apellido; cin>>nombre>>apellido;\n'
            ' cout<<"Nombre completo: "<<nombre<<" "<<apellido; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un carácter y muestra su código ASCII como entero.",
        tests_json={
            "sample": [{"input": "A\n", "output": "65"}],
            "hidden": [
                {"input": "a\n", "output": "97"},
                {"input": "0\n", "output": "48"}
            ]
        },
        hint="Convierte el char a int al imprimir (promoción implícita). El salto de línea final es opcional.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ char c; cin>>c; cout<< (int)c; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    
]

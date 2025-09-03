from src.exercise import Exercise

exercises_conditional = [

    Exercise(
        type_="test",
        question="¿Qué palabra clave se usa para evaluar múltiples casos según el valor de una variable?",
        options=["if", "switch", "case", "else"],
        answer="switch",
        explanation="La instrucción switch evalúa una variable contra múltiples casos posibles."
    ),

    Exercise(
        type_="test",
        question="¿Qué operador lógico se usa para comprobar que se cumplan dos condiciones al mismo tiempo?",
        options=["||", "!", "&&", "=="],
        answer="&&",
        explanation="El operador lógico '&&' significa 'y': ambas condiciones deben cumplirse."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estas instrucciones se ejecuta si la condición de un if no se cumple y hay una alternativa?",
        options=["case", "else", "default", "switch"],
        answer="else",
        explanation="El bloque else se ejecuta solo si la condición del if no se cumple."
    ),

    Exercise(
        type_="true_false",
        question="En un switch siempre es obligatorio incluir un caso default.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="El caso default es opcional, aunque se recomienda usarlo como valor por defecto."
    ),

    Exercise(
        type_="true_false",
        question="Un condicional puede tener otro condicional dentro.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Esto se conoce como condicional anidado, útil para decisiones más complejas."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estas comparaciones es un error común en C++?",
        options=[
            "if (x == 5)",
            "if (x = 5)",
            "if (x >= 5)",
            "if (x != 5)"
        ],
        answer="if (x = 5)",
        explanation="Esto asigna el valor 5 a x, no lo compara. La comparación correcta es '=='"
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime el siguiente código?\n"
            "<pre><code>int x = 7;\n"
            "if (x > 10) {\n"
            "    cout &lt;&lt; \"Grande\";\n"
            "} else {\n"
            "    cout &lt;&lt; \"Pequeño\";\n"
            "}</code></pre>"
        ),
        options=["Grande", "Pequeño", "Nada", "Error de compilación"],
        answer="Pequeño",
        explanation="Como 7 no es mayor que 10, se ejecuta el bloque else."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué se muestra por pantalla?\n"
            "<pre><code>int x = 3, y = 5;\n"
            "if (x > 0 && y < 10) {\n"
            "    cout &lt;&lt; \"Cumple\";\n"
            "}</code></pre>"
        ),
        options=["Cumple", "No cumple", "Error", "Nada"],
        answer="Cumple",
        explanation="Ambas condiciones son verdaderas, así que se imprime 'Cumple'."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué resultado muestra el siguiente código?\n"
            "<pre><code>int edad = 17;\n"
            "bool tiene_dni = true;\n"
            "if (edad &gt;= 18) {\n"
            "    if (tiene_dni) {\n"
            "        cout &lt;&lt; \"Puede votar\";\n"
            "    }\n"
            "}</code></pre>"
        ),
        options=["Puede votar", "No puede votar", "Nada", "Error"],
        answer="Nada",
        explanation="La condición principal (edad >= 18) no se cumple, por lo que no entra al segundo if."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprimirá este programa?\n"
            "<pre><code>int nota = 8;\n"
            "if (nota &gt;= 9) {\n"
            "    cout &lt;&lt; \"Excelente\";\n"
            "} else if (nota &gt;= 5) {\n"
            "    cout &lt;&lt; \"Aprobado\";\n"
            "} else {\n"
            "    cout &lt;&lt; \"Suspenso\";\n"
            "}</code></pre>"
        ),
        options=["Excelente", "Aprobado", "Suspenso", "Nada"],
        answer="Aprobado",
        explanation="Como nota no llega a 9 pero sí a 5, entra en el bloque 'Aprobado'."
    ),

    Exercise(
        type_="true_false",
        question="Los bloques if y else pueden ir sin llaves si solo hay una instrucción.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Es posible omitir las llaves, pero se recomienda usarlas por claridad."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Cuál es el error de este código?\n"
            "<pre><code>int edad;\n"
            "if (edad &gt; 18) {\n"
            "    cout &lt;&lt; \"Mayor\";\n"
            "}</code></pre>"
        ),
        options=["Faltan llaves", "edad no tiene valor inicial", "Error de sintaxis", "Nada"],
        answer="edad no tiene valor inicial",
        explanation="Edad se declara pero no se le da un valor, por lo que su contenido es indeterminado."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace la palabra clave break dentro de un switch?",
        options=[
            "Termina el programa",
            "Evita que se ejecuten los siguientes casos",
            "Muestra un mensaje",
            "Cierra el switch"
        ],
        answer="Evita que se ejecuten los siguientes casos",
        explanation="Sin break, el flujo del programa continúa ejecutando los siguientes casos."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué muestra el siguiente código?\n"
            "<pre><code>int x = 5;\n"
            "if (x > 0)\n"
            "    cout &lt;&lt; \"Positivo\";\n"
            "    cout &lt;&lt; \"Número\";\n"
            "</code></pre>"
        ),
        options=["Positivo", "Número", "PositivoNúmero", "Error de sintaxis"],
        answer="PositivoNúmero",
        explanation="Solo la primera línea está dentro del if. La segunda se ejecuta siempre."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprimirá este código?\n"
            "<pre><code>int dia = 2;\n"
            "switch (dia) {\n"
            "    case 1: cout &lt;&lt; \"Lunes\"; break;\n"
            "    case 2: cout &lt;&lt; \"Martes\"; break;\n"
            "    default: cout &lt;&lt; \"Otro\";\n"
            "}</code></pre>"
        ),
        options=["Lunes", "Martes", "Otro", "Error"],
        answer="Martes",
        explanation="dia == 2, por lo que entra en el case 2 y ejecuta ese bloque."
    ),

    Exercise(
        type_="true_false",
        question="Es correcto usar un if dentro de otro if.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Esto se llama anidamiento y es válido en C++."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es una buena práctica al escribir condicionales?",
        options=[
            "No usar llaves para ahorrar líneas",
            "Usar '=' en lugar de '=='",
            "Mantener el código legible y bien indentado",
            "Comparar siempre reales con '=='"
        ],
        answer="Mantener el código legible y bien indentado",
        explanation="La claridad del código evita errores y mejora el mantenimiento."
    ),

    Exercise(
        type_="test",
        question="¿Qué operador se usa para negar una condición?",
        options=["&", "||", "!", "#"],
        answer="!",
        explanation="El operador '!' invierte el valor lógico: true → false y viceversa."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué muestra este código?\n"
            "<pre><code>int a = 5;\n"
            "int b = 2;\n"
            "if (a % b == 1 || a == 4) {\n"
            "    cout &lt;&lt; \"Correcto\";\n"
            "}</code></pre>"
        ),
        options=["Correcto", "Nada", "Error", "Incorrecto"],
        answer="Correcto",
        explanation="5 % 2 == 1, así que la condición es verdadera."
    ), 

    Exercise(
        type_="test",
        question="¿Cuál es el resultado de 3 > 5 || 10 > 2?",
        options=["true", "false", "0", "Error de sintaxis"],
        answer="true",
        explanation="La segunda condición (10 > 2) es verdadera, así que el operador lógico OR (||) devuelve true."
    ),

    Exercise(
        type_="test",
        question="¿Qué operador lógico invierte el valor de una condición?",
        options=["&", "|", "!", "!="],
        answer="!",
        explanation="El operador ! niega la condición: convierte true en false y viceversa."
    ),

    Exercise(
        type_="true_false",
        question="La instrucción 'else if' permite comprobar varias condiciones en orden.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Cada 'else if' se evalúa solo si los anteriores han fallado."
    ),

    Exercise(
        type_="true_false",
        question="Un switch puede evaluar variables de tipo string.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="En C++ solo puede evaluar tipos enteros o caracteres (int o char)."
    ),

    Exercise(
        type_="test",
        question="¿Qué se necesita para que un bloque 'if' anidado se ejecute?",
        options=[
            "Que el primer if sea falso",
            "Que todas las condiciones hasta el interior se cumplan",
            "Que la variable sea booleana",
            "Nada especial"
        ],
        answer="Que todas las condiciones hasta el interior se cumplan",
        explanation="En condicionales anidados, deben cumplirse las condiciones externas para que se llegue a evaluar la interna."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime este código?\n"
            "<pre><code>int edad = 18;\n"
            "if (edad &gt; 18) {\n"
            "    cout &lt;&lt; \"Mayor\";\n"
            "} else {\n"
            "    cout &lt;&lt; \"Justo o menor\";\n"
            "}</code></pre>"
        ),
        options=["Mayor", "Justo o menor", "Error", "Nada"],
        answer="Justo o menor",
        explanation="La condición es estrictamente mayor que 18, así que no se cumple y se ejecuta el else."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué muestra el siguiente código?\n"
            "<pre><code>int x = 2;\n"
            "int y = 4;\n"
            "if (x * y == 8) {\n"
            "    cout &lt;&lt; \"Correcto\";\n"
            "} else {\n"
            "    cout &lt;&lt; \"Incorrecto\";\n"
            "}</code></pre>"
        ),
        options=["Correcto", "Incorrecto", "Nada", "Error"],
        answer="Correcto",
        explanation="2 * 4 == 8, así que la condición se cumple y se imprime 'Correcto'."
    ),

    Exercise(
        type_="test",
        question="¿Qué palabra clave se usa para salir de un caso en un switch?",
        options=["exit", "end", "break", "close"],
        answer="break",
        explanation="Sin break, el flujo continúa ejecutando el siguiente case."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre si no hay un break dentro de un switch?",
        options=[
            "Se termina el programa",
            "Solo se ejecuta el caso actual",
            "Se ejecutan todos los casos siguientes",
            "El programa da error"
        ],
        answer="Se ejecutan todos los casos siguientes",
        explanation="Sin break, C++ hace 'fall-through' y continúa ejecutando los siguientes bloques case."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué resultado produce este código?\n"
            "<pre><code>int temp = 30;\n"
            "if (temp &gt; 25) {\n"
            "    cout &lt;&lt; \"Calor\";\n"
            "}\n"
            "if (temp &gt; 20) {\n"
            "    cout &lt;&lt; \"Templado\";\n"
            "}</code></pre>"
        ),
        options=["Calor", "Templado", "CalorTemplado", "Nada"],
        answer="CalorTemplado",
        explanation="Ambas condiciones se cumplen, así que se ejecutan ambos bloques if."
    ),

    Exercise(
        type_="true_false",
        question="Es correcto escribir: if (nota = 10)",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Esto asigna el valor 10 a 'nota'. Para comparar, se debe usar ==."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el resultado de la siguiente condición: !(false || true)?",
        options=["true", "false", "0", "1"],
        answer="false",
        explanation="false || true = true → !true = false"
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime este código?\n"
            "<pre><code>int a = 3;\n"
            "int b = 5;\n"
            "if (a &gt; 2 &amp;&amp; b &lt; 10) {\n"
            "    cout &lt;&lt; \"Dentro del rango\";\n"
            "} else {\n"
            "    cout &lt;&lt; \"Fuera de rango\";\n"
            "}</code></pre>"
        ),
        options=["Dentro del rango", "Fuera de rango", "Error", "Nada"],
        answer="Dentro del rango",
        explanation="Ambas condiciones se cumplen, así que se imprime 'Dentro del rango'."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Cuál es el resultado?\n"
            "<pre><code>int n = -5;\n"
            "if (n &gt; 0) {\n"
            "    cout &lt;&lt; \"Positivo\";\n"
            "} else if (n == 0) {\n"
            "    cout &lt;&lt; \"Cero\";\n"
            "} else {\n"
            "    cout &lt;&lt; \"Negativo\";\n"
            "}</code></pre>"
        ),
        options=["Positivo", "Cero", "Negativo", "Nada"],
        answer="Negativo",
        explanation="-5 no es mayor que 0 ni igual a 0, así que entra en el bloque else."
    ),

    Exercise(
        type_="test",
        question="¿Qué tipo de condicional usarías para elegir entre muchas opciones basadas en un número exacto?",
        options=["if", "else if", "switch", "while"],
        answer="switch",
        explanation="switch es ideal cuando se compara una variable contra valores concretos."
    ),

    Exercise(
        type_="test",
        question="¿Qué operador usarías para comprobar si dos valores NO son iguales?",
        options=["=", "==", "!=", "<>"],
        answer="!=",
        explanation="El operador '!=' significa 'distinto de'."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Cuál es el resultado?\n"
            "<pre><code>int x = 1;\n"
            "if (x > 0)\n"
            "    if (x < 5)\n"
            "        cout &lt;&lt; \"A\";\n"
            "    else\n"
            "        cout &lt;&lt; \"B\";</code></pre>"
        ),
        options=["A", "B", "Nada", "Error"],
        answer="A",
        explanation="x es mayor que 0 y menor que 5. Se ejecuta el primer bloque anidado."
    ),

    Exercise(
        type_="true_false",
        question="El operador lógico && devuelve true si ambas condiciones son verdaderas.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="&& es la conjunción lógica. Solo es true si ambas condiciones lo son."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué se imprime?\n"
            "<pre><code>int valor = 5;\n"
            "switch (valor) {\n"
            "    case 4:\n"
            "    case 5:\n"
            "        cout &lt;&lt; \"Cuatro o cinco\"; break;\n"
            "    default:\n"
            "        cout &lt;&lt; \"Otro\";\n"
            "}</code></pre>"
        ),
        options=["Cuatro o cinco", "Otro", "Error", "Nada"],
        answer="Cuatro o cinco",
        explanation="Al no haber instrucciones entre case 4 y case 5, ambos activan el mismo bloque."
    ), 

    Exercise(
        type_="code",
        question="Lee un entero y muestra 'Par' si es múltiplo de 2 o 'Impar' en caso contrario.",
        tests_json={
            "sample": [{"input": "8\n", "output": "Par"}],
            "hidden": [
                {"input": "-3\n", "output": "Impar"},
                {"input": "0\n", "output": "Par"}
            ]
        },
        hint="Usa if con x % 2 == 0. (El verificador tolera salto y espacios finales.)",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long x; if(!(cin>>x)) return 0; cout<<(x%2==0? "Par":"Impar"); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos enteros a y b y muestra un único símbolo: '>', '<' o '=' comparando a con b.",
        tests_json={
            "sample": [{"input": "7 5\n", "output": ">"}],
            "hidden": [
                {"input": "-2 -2\n", "output": "="},
                {"input": "3 10\n", "output": "<"}
            ]
        },
        hint="Imprime exactamente uno de estos tres símbolos. (El verificador tolera salto/espacios finales.)",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; cin>>a>>b; cout<<(a>b?">":(a<b?"<":"=")); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee tres enteros y muestra el mayor de ellos.",
        tests_json={
            "sample": [{"input": "3 9 5\n", "output": "9"}],
            "hidden": [
                {"input": "-7 -2 -5\n", "output": "-2"},
                {"input": "10 10 7\n", "output": "10"}
            ]
        },
        hint="Inicializa max con el primero y actualiza con if sobre los demás.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b,c; cin>>a>>b>>c; long long mx=a; if(b>mx) mx=b; if(c>mx) mx=c; cout<<mx; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero y muestra 'Positivo', 'Cero' o 'Negativo' según corresponda.",
        tests_json={
            "sample": [{"input": "0\n", "output": "Cero"}],
            "hidden": [
                {"input": "-12\n", "output": "Negativo"},
                {"input": "7\n", "output": "Positivo"}
            ]
        },
        hint="Encadena if/else if/else comparando con 0.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long x; cin>>x; if(x>0) cout<<"Positivo"; else if(x==0) cout<<"Cero"; else cout<<"Negativo"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero y muestra su valor absoluto (sin usar funciones de librería).",
        tests_json={
            "sample": [{"input": "-7\n", "output": "7"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "15\n", "output": "15"}
            ]
        },
        hint="Si x<0, cambia el signo con x = -x; luego imprime.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long x; cin>>x; if(x<0) x=-x; cout<<x; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un año (entero) y muestra 'Bisiesto' si lo es o 'No bisiesto' en caso contrario.",
        tests_json={
            "sample": [{"input": "2020\n", "output": "Bisiesto"}],
            "hidden": [
                {"input": "1900\n", "output": "No bisiesto"},
                {"input": "2000\n", "output": "Bisiesto"}
            ]
        },
        hint="Regla: divisible entre 400, o divisible entre 4 y no entre 100.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long y; cin>>y; bool b=(y%400==0)||((y%4==0)&&(y%100!=0)); cout<<(b? "Bisiesto":"No bisiesto"); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee mes (1..12) y año, y muestra los días del mes (considera febrero bisiesto).",
        tests_json={
            "sample": [{"input": "2 2024\n", "output": "29"}],
            "hidden": [
                {"input": "2 2023\n", "output": "28"},
                {"input": "11 2021\n", "output": "30"}
            ]
        },
        hint="Usa switch para 31/30 días y calcula febrero con la regla de año bisiesto.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int m; long long y; cin>>m>>y; bool b=(y%400==0)||((y%4==0)&&(y%100!=0));\n'
            ' int d; switch(m){ case 1: case 3: case 5: case 7: case 8: case 10: case 12: d=31; break;'
            ' case 4: case 6: case 9: case 11: d=30; break;'
            ' case 2: d = b?29:28; break; default: d=0; }\n'
            ' cout<<d; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee a, un operador (+ - * / %) y b; muestra el resultado (entero). Si hay división o módulo por 0, imprime 'Error'.",
        tests_json={
            "sample": [{"input": "8 / 3\n", "output": "2"}],
            "hidden": [
                {"input": "7 % 4\n", "output": "3"},
                {"input": "5 / 0\n", "output": "Error"}
            ]
        },
        hint="Lee como: long long a; char op; long long b; Para '/', usa división entera. Si b==0 en '/' o '%', muestra 'Error'.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; char op; if(!(cin>>a>>op>>b)) return 0; \n'
            ' if((op==\'/\'||op==\'%\') && b==0){ cout<<"Error"; return 0; }\n'
            ' if(op==\'+\') cout<<a+b; else if(op==\'-\') cout<<a-b; else if(op==\'*\') cout<<a*b;\n'
            ' else if(op==\'/\') cout<<a/b; else if(op==\'%\') cout<<a%b; else cout<<"Error"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),


    Exercise(
        type_="code",
        question="Lee una calificación entera en [0,10] y muestra 'Excelente' (≥9), 'Aprobado' (≥5) o 'Suspenso' (<5). Si está fuera de rango, muestra 'Error'.",
        tests_json={
            "sample": [{"input": "8\n", "output": "Aprobado"}],
            "hidden": [
                {"input": "10\n", "output": "Excelente"},
                {"input": "-1\n", "output": "Error"}
            ]
        },
        hint="Valida 0..10 antes de clasificar.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; cin>>n; if(n<0||n>10) { cout<<"Error"; }\n'
            ' else if(n>=9) cout<<"Excelente"; else if(n>=5) cout<<"Aprobado"; else cout<<"Suspenso"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee tres enteros a,b,c y muestra 'Equilatero', 'Isosceles', 'Escaleno' o 'No valido' según formen triángulo.",
        tests_json={
            "sample": [{"input": "3 3 3\n", "output": "Equilatero"}],
            "hidden": [
                {"input": "3 4 5\n", "output": "Escaleno"},
                {"input": "1 2 3\n", "output": "No valido"}
            ]
        },
        hint="Valida a,b,c>0 y desigualdades del triángulo: a+b>c, a+c>b, b+c>a.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b,c; cin>>a>>b>>c; \n'
            ' bool ok = (a>0&&b>0&&c>0) && (a+b>c) && (a+c>b) && (b+c>a);\n'
            ' if(!ok) cout<<"No valido";\n'
            ' else if(a==b && b==c) cout<<"Equilatero";\n'
            ' else if(a==b || a==c || b==c) cout<<"Isosceles";\n'
            ' else cout<<"Escaleno"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un carácter y muestra 'Vocal', 'Consonante' o 'No letra'.",
        tests_json={
            "sample": [{"input": "A\n", "output": "Vocal"}],
            "hidden": [
                {"input": "b\n", "output": "Consonante"},
                {"input": "9\n", "output": "No letra"}
            ]
        },
        hint="Usa tolower y isalpha (requiere <cctype>). Vocales: a,e,i,o,u.",
        solution_code=(
            '#include <iostream>\n#include <cctype>\nusing namespace std;\n'
            'int main(){ char c; cin>>c; if(!isalpha((unsigned char)c)){ cout<<"No letra"; return 0; }\n'
            ' char d=tolower((unsigned char)c); string r=(d==\'a\'||d==\'e\'||d==\'i\'||d==\'o\'||d==\'u\')? "Vocal":"Consonante";\n'
            ' cout<<r; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos enteros x e y y muestra 'Origen' si (0,0), 'Eje X' si y==0, 'Eje Y' si x==0 o 'Cuadrante I/II/III/IV' según corresponda.",
        tests_json={
            "sample": [{"input": "3 -2\n", "output": "Cuadrante IV"}],
            "hidden": [
                {"input": "0 0\n", "output": "Origen"},
                {"input": "0 5\n", "output": "Eje Y"}
            ]
        },
        hint="Recuerda: I(+,+), II(-,+), III(-,-), IV(+,-). Prioriza Origen y ejes antes de cuadrantes.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long x,y; cin>>x>>y; \n'
            ' if(x==0 && y==0) cout<<"Origen";\n'
            ' else if(y==0) cout<<"Eje X";\n'
            ' else if(x==0) cout<<"Eje Y";\n'
            ' else if(x>0 && y>0) cout<<"Cuadrante I";\n'
            ' else if(x<0 && y>0) cout<<"Cuadrante II";\n'
            ' else if(x<0 && y<0) cout<<"Cuadrante III";\n'
            ' else cout<<"Cuadrante IV"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos enteros y muestra en dos líneas: primero el menor y después el mayor.",
        tests_json={
            "sample": [{"input": "7 9\n", "output": "7\n9"}],
            "hidden": [
                {"input": "5 5\n", "output": "5\n5"},
                {"input": "-3 10\n", "output": "-3\n10"}
            ]
        },
        hint="Puedes calcular min y max con if. El verificador ignora SOLO el salto de línea FINAL.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; cin>>a>>b; long long mn=a<b?a:b, mx=a>b?a:b; cout<<mn<<"\\n"<<mx; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee tres enteros y muéstralos en orden ascendente separados por un espacio (sin usar sort).",
        tests_json={
            "sample": [{"input": "3 1 2\n", "output": "1 2 3"}],
            "hidden": [
                {"input": "10 10 7\n", "output": "7 10 10"},
                {"input": "-1 -5 0\n", "output": "-5 -1 0"}
            ]
        },
        hint="Usa intercambios condicionales con if (p.ej., si a>b entonces intercambia). El verificador tolera salto/espacios finales.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b,c; cin>>a>>b>>c; long long t;\n'
            ' if(a>b){ t=a; a=b; b=t; }\n'
            ' if(b>c){ t=b; b=c; c=t; }\n'
            ' if(a>b){ t=a; a=b; b=t; }\n'
            ' cout<<a<<" "<<b<<" "<<c; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee una edad (entero) y muestra 'Gratis' (&lt;4), 'Reducida' (4..12), 'General' (13..64) o 'Senior' (≥65).",
        tests_json={
            "sample": [{"input": "12\n", "output": "Reducida"}],
            "hidden": [
                {"input": "3\n", "output": "Gratis"},
                {"input": "70\n", "output": "Senior"}
            ]
        },
        hint="Encadena else-if cubriendo todos los rangos. Verificador tolerante a salto/espacios finales.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long e; cin>>e; if(e<4) cout<<"Gratis"; else if(e<=12) cout<<"Reducida";\n'
            ' else if(e<=64) cout<<"General"; else cout<<"Senior"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un carácter ('R','A','V') y muestra 'Detente', 'Precaucion' o 'Avanza'. Cualquier otro, 'Desconocido'.",
        tests_json={
            "sample": [{"input": "V\n", "output": "Avanza"}],
            "hidden": [
                {"input": "A\n", "output": "Precaucion"},
                {"input": "X\n", "output": "Desconocido"}
            ]
        },
        hint="Usa switch con casos 'R', 'A', 'V'. (No hace falta distinguir mayúsculas/minúsculas.)",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ char c; cin>>c; switch(c){\n'
            ' case \'R\': cout<<"Detente"; break;\n'
            ' case \'A\': cout<<"Precaucion"; break;\n'
            ' case \'V\': cout<<"Avanza"; break;\n'
            ' default: cout<<"Desconocido"; }\n'
            ' }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),
]

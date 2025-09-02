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
    )
]

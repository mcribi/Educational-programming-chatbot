
from src.exercise import Exercise

exercises_variables = [

    Exercise(
        type_="test",
        question="¿Cuál de estas opciones representa una declaración válida de variable en C++?",
        options=[
            "edad int = 20;",
            "int edad = 20;",
            "int = 20 edad;",
            "20 = int edad;"
        ],
        answer="int edad = 20;",
        explanation="La sintaxis correcta es: tipo, nombre y (opcionalmente) un valor inicial."
    ),

    Exercise(
        type_="test",
        question="¿Qué tipo de dato usarías para guardar un valor decimal como 3.14?",
        options=["int", "char", "bool", "double"],
        answer="double",
        explanation="El tipo double se usa para valores con decimales."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el resultado de esta operación: <code>17 % 5</code>?",
        options=["2", "3", "1", "5"],
        answer="2",
        explanation="El operador % devuelve el resto de la división entera (17 dividido entre 5 da 3 y sobra 2)."
    ),

    Exercise(
        type_="test",
        question="¿Qué operador se usa para comprobar si dos valores son iguales?",
        options=["=", "==", "!=", "equals"],
        answer="==",
        explanation="El operador == compara si dos valores son iguales. = se usa para asignar valores."
    ),

    Exercise(
        type_="test",
        question="¿Qué tipo de dato corresponde a la instrucción: <code>char letra = 'A';</code>?",
        options=["bool", "char", "string", "int"],
        answer="char",
        explanation="El tipo char guarda un único carácter entre comillas simples."
    ),

    Exercise(
        type_="truefalse",
        question="Una constante puede cambiar su valor una vez declarada.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Las constantes, declaradas con <code>const</code>, no se pueden modificar."
    ),

    Exercise(
        type_="truefalse",
        question="<code>5 / 2</code> en C++ da como resultado 2.5.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Si ambos operandos son enteros, la división también lo será: 5 / 2 = 2."
    ),

    Exercise(
        type_="truefalse",
        question="Una variable declarada dentro de <code>main()</code> no puede usarse fuera de él.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="El ámbito de una variable local está limitado al bloque donde se declara."
    ),

    Exercise(
        type_="truefalse",
        question="La instrucción <code>bool es_valido = true;</code> es válida en C++.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="El tipo <code>bool</code> acepta los valores <code>true</code> y <code>false</code>."
    ),

    Exercise(
        type_="yesno",
        question="¿Se pueden usar acentos o la letra ñ en el nombre de una variable?",
        options=["Sí", "No"],
        answer="No",
        explanation="Los nombres de variables no pueden tener acentos, eñes ni caracteres especiales."
    ),

    Exercise(
        type_="yesno",
        question="¿Es obligatorio dar un valor inicial al declarar una variable?",
        options=["Sí", "No"],
        answer="No",
        explanation="Una variable puede declararse sin valor inicial, aunque tendrá un valor indeterminado."
    ),

    Exercise(
        type_="yesno",
        question="¿Puede una expresión mezclar <code>int</code> y <code>double</code>?",
        options=["Sí", "No"],
        answer="Sí",
        explanation="C++ convierte automáticamente el tipo más simple al más complejo (a <code>double</code>)."
    ),

    Exercise(
        type_="yesno",
        question="¿Necesitas incluir alguna biblioteca para usar <code>cout</code>?",
        options=["Sí", "No"],
        answer="Sí",
        explanation="Para usar <code>cout</code> necesitas <code>#include &lt;iostream&gt;</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor guarda esta variable?\n<code>int resultado = 15 / 4;</code>",
        options=["3.75", "3", "4", "Error de compilación"],
        answer="3",
        explanation="Es una división entre enteros. El resultado también es entero: 15 / 4 = 3 (sin decimales)."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace el siguiente operador: <code>!=</code>?",
        options=["Compara si dos valores son iguales", "Niega una condición", "Comprueba si dos valores son diferentes", "Asigna un valor"],
        answer="Comprueba si dos valores son diferentes",
        explanation="El operador <code>!=</code> significa 'distinto de'."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estas variables tiene un nombre inválido?",
        options=["_total", "3edad", "nombre_completo", "edad3"],
        answer="3edad",
        explanation="Los nombres no pueden empezar por un número."
    ),

    Exercise(
        type_="test",
        question="¿Qué tipo de dato utilizarías para guardar 'true' o 'false'?",
        options=["bool", "int", "char", "string"],
        answer="bool",
        explanation="El tipo <code>bool</code> guarda valores lógicos: <code>true</code> o <code>false</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace esta línea de código?\n<code>cout &lt;&lt; \"Hola\";</code>",
        options=["Declara una variable", "Lee datos del teclado", "Muestra el texto 'Hola'", "Guarda un dato en una variable"],
        answer="Muestra el texto 'Hola'",
        explanation="La instrucción <code>cout</code> se usa para mostrar información en pantalla."
    ),

    Exercise(
        type_="test",
        question="¿Qué función devuelve la raíz cuadrada de un número?",
        options=["root()", "sqrt()", "pow()", "abs()"],
        answer="sqrt()",
        explanation="<code>sqrt(x)</code> devuelve la raíz cuadrada de <code>x</code> y pertenece a la librería <code>&lt;cmath&gt;</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre si intentas guardar un texto en una variable <code>int</code>?",
        options=["Se guarda sin problema", "Se convierte a número automáticamente", "Da error de compilación", "Se guarda como cero"],
        answer="Da error de compilación",
        explanation="No se puede guardar texto en una variable de tipo <code>int</code>."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el resultado de esta expresión?\n<code>10 % 3</code>",
        options=["3", "0", "1", "10"],
        answer="1",
        explanation="El operador <code>%</code> devuelve el resto: 10 dividido entre 3 deja resto 1."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace esta línea?\n<code>const double PI = 3.1416;</code>",
        options=["Declara una constante real", "Declara una variable entera", "Declara una función", "Lee un dato del usuario"],
        answer="Declara una constante real",
        explanation="Declara un valor que no se puede cambiar y es de tipo <code>double</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué biblioteca necesitas para usar funciones como <code>sqrt()</code> o <code>pow()</code>?",
        options=["<iostream>", "<cmath>", "<string>", "<stdlib>"],
        answer="<cmath>",
        explanation="Las funciones matemáticas estándar están en la biblioteca <code>&lt;cmath&gt;</code>."
    ), 

    Exercise(
        type_="test",
        question="¿Qué tipo de dato usarías para almacenar el nombre de una persona?",
        options=["char", "string", "bool", "int"],
        answer="string",
        explanation="Un <code>string</code> permite guardar cadenas de texto, como nombres completos."
    ),

    Exercise(
        type_="test",
        question="¿Qué operador sirve para aumentar el valor de una variable en 1?",
        options=["--", "+=", "++", "="],
        answer="++",
        explanation="El operador <code>++</code> incrementa una variable en una unidad."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre si haces esta operación?\n<code>bool activo = 1;</code>",
        options=["Da error", "Guarda true", "Guarda false", "Guarda el número 1 como texto"],
        answer="Guarda true",
        explanation="En C++, el valor 1 se interpreta como <code>true</code> cuando se asigna a un <code>bool</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace esta instrucción?\n<code>cin &gt;&gt; edad;</code>",
        options=["Muestra el valor de edad", "Declara una variable", "Lee un dato del teclado y lo guarda en edad", "Borra la variable edad"],
        answer="Lee un dato del teclado y lo guarda en edad",
        explanation="<code>cin</code> se usa para leer valores introducidos por el usuario."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estas variables está mal nombrada según las reglas de C++?",
        options=["nombre_usuario", "_total", "3dias", "esMayor"],
        answer="3dias",
        explanation="Los nombres de variables no pueden comenzar con un número."
    ),

    Exercise(
        type_="truefalse",
        question="La palabra clave <code>const</code> se usa para declarar variables que cambian de valor constantemente.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="<code>const</code> se usa para declarar constantes, que no cambian su valor."
    ),

    Exercise(
        type_="truefalse",
        question="Un <code>char</code> solo puede contener un único carácter.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="El tipo <code>char</code> solo almacena un carácter entre comillas simples, como <code>'A'</code>."
    ),

    Exercise(
        type_="truefalse",
        question="Si haces <code>double x = 5 / 2;</code>, x valdrá 2.5.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Aunque <code>x</code> sea <code>double</code>, <code>5 / 2</code> es división entera: resultado 2."
    ),

    Exercise(
        type_="truefalse",
        question="Los literales como <code>42</code>, <code>'a'</code> o <code>\"Hola\"</code> son valores fijos en el código.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Los literales son valores escritos directamente en el código fuente."
    ),

    Exercise(
        type_="truefalse",
        question="Las funciones <code>sqrt()</code> o <code>pow()</code> están incluidas en la biblioteca <code>&lt;iostream&gt;</code>.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Pertenecen a <code>&lt;cmath&gt;</code>, no a <code>&lt;iostream&gt;</code>."
    ), 

    Exercise(
        type_="test",
        question="¿Qué valor guarda la variable <code>resultado</code>?\n<pre>int resultado = 10 / 2;</pre>",
        options=["5", "2", "0", "5.0"],
        answer="5",
        explanation="Se trata de una división entre enteros, así que el resultado también es entero."
    ),

    Exercise(
        type_="test",
        question="¿Qué se mostrará por pantalla?\n<pre>int a = 3;\nint b = 4;\ncout &lt;&lt; a * b;</pre>",
        options=["7", "12", "3 * 4", "Error"],
        answer="12",
        explanation="3 * 4 = 12. Se realiza una multiplicación entre enteros."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurrirá al ejecutar este código?\n<pre>int edad;\ncout &lt;&lt; edad;</pre>",
        options=["Se mostrará 0", "Dará error de compilación", "Mostrará un valor basura", "Mostrará un texto"],
        answer="Mostrará un valor basura",
        explanation="La variable <code>edad</code> no tiene valor inicial, por lo que mostrará un valor indeterminado."
    ),

    Exercise(
        type_="test",
        question="¿Qué se imprimirá?\n<pre>bool activo = false;\ncout &lt;&lt; activo;</pre>",
        options=["true", "false", "0", "1"],
        answer="0",
        explanation="En C++, <code>false</code> se representa como 0 cuando se imprime por consola."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurrirá?\n<pre>const int x = 10;\nx = 20;</pre>",
        options=["x vale 20", "x vale 10", "Se ejecuta sin problemas", "Error de compilación"],
        answer="Error de compilación",
        explanation="No se puede cambiar el valor de una constante declarada con <code>const</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué se imprime?\n<pre>int a = 7 % 3;\ncout &lt;&lt; a;</pre>",
        options=["1", "2", "3", "0"],
        answer="1",
        explanation="7 dividido entre 3 deja un resto de 1. Eso es lo que guarda <code>a</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor se guarda en <code>media</code>?\n<pre>int media = (3 + 4) / 2;</pre>",
        options=["3", "3.5", "4", "7"],
        answer="3",
        explanation="La operación es entera. (3+4)/2 = 7/2 = 3 (parte entera)."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre al compilar este código?\n<pre>int x = \"Hola\";</pre>",
        options=["Se guarda Hola", "Se guarda 0", "Error de compilación", "x vale 4"],
        answer="Error de compilación",
        explanation="No se puede asignar una cadena de texto a una variable <code>int</code>."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el valor de <code>c</code>?\n<pre>char c = 'A' + 1;\ncout &lt;&lt; c;</pre>",
        options=["'A'", "'B'", "66", "'1'"],
        answer="'B'",
        explanation="El carácter 'A' tiene valor ASCII 65. Al sumarle 1, se obtiene 'B' (66)."
    ),

    Exercise(
        type_="test",
        question="¿Qué resultado se imprime?\n<pre>int a = 3;\ndouble b = 2.5;\ncout &lt;&lt; a * b;</pre>",
        options=["7.5", "6", "Error", "5"],
        answer="7.5",
        explanation="El <code>int</code> se convierte automáticamente a <code>double</code> → 3 × 2.5 = 7.5"
    ),
]

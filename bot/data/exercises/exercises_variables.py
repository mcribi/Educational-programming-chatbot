
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

    #codeee

    Exercise(
        type_="code",
        question="Lee un nombre (línea completa) y una edad (entero) y muestra: 'Edad de &lt;nombre&gt;: &lt;edad&gt;'.",
        tests_json={
            "sample": [{"input": "Ada Lovelace\n36\n", "output": "Edad de Ada Lovelace: 36"}],
            "hidden": [
                {"input": "Alan Turing\n41\n", "output": "Edad de Alan Turing: 41"},
                {"input": "Grace Hopper\n85\n", "output": "Edad de Grace Hopper: 85"}
            ]
        },
        hint="Primero getline para el nombre (con espacios), luego lee la edad con cin. El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'int main(){ ios::sync_with_stdio(false); cin.tie(nullptr);\n'
            ' string nombre; getline(cin, nombre); long long edad; cin >> edad; \n'
            ' cout << "Edad de " << nombre << ": " << edad; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee dos enteros a y b y muestra en 5 líneas, en este orden: a+b, a-b, a*b, a/b (entera), a%b. "
                  "La última línea no debe terminar con salto de línea."),
        tests_json={
            "sample": [{"input": "8 3\n", "output": "11\n5\n24\n2\n2"}],
            "hidden": [
                {"input": "25 9\n", "output": "34\n16\n225\n2\n7"},
                {"input": "-7 5\n", "output": "-2\n-12\n-35\n-1\n-2"}
            ]
        },
        hint="Usa + - * / % sobre enteros. División entera trunca hacia 0 (p. ej., -7/5 = -1). El verificador ignora SOLO el salto FINAL.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; if(!(cin>>a>>b)) return 0; \n'
            ' cout<<(a+b)<<"\\n"<<(a-b)<<"\\n"<<(a*b)<<"\\n"<<(a/b)<<"\\n"<<(a%b); } \n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos números reales x e y y muestra x/y con 6 decimales.",
        tests_json={
            "sample": [{"input": "5 2\n", "output": "2.500000"}],
            "hidden": [
                {"input": "7 3.5\n", "output": "2.000000"},
                {"input": "2 3\n", "output": "0.666667"}
            ]
        },
        hint="Activa fixed y setprecision(6). El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ double x,y; cin>>x>>y; cout.setf(ios::fixed); cout<<setprecision(6)<<(x/y); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee un radio (double) y muestra en dos líneas: área del círculo y longitud de la circunferencia, "
                  "con 6 decimales. Usa PI como constante 3.141592653589793."),
        tests_json={
            "sample": [{"input": "1\n", "output": "3.141593\n6.283185"}],
            "hidden": [
                {"input": "0\n", "output": "0.000000\n0.000000"},
                {"input": "2.5\n", "output": "19.634955\n15.707963"}
            ]
        },
        hint="Área = PI*r*r, Longitud = 2*PI*r. Formatea con fixed y 6 decimales. El verificador ignora SOLO el salto FINAL.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            "int main(){ const double PI=3.141592653589793; double r; cin>>r; \n"
            ' cout.setf(ios::fixed); cout<<setprecision(6)<<(PI*r*r)<<"\\n"<<(2*PI*r); }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Convierte Celsius a Fahrenheit. Lee C (double) y muestra F con 2 decimales.",
        tests_json={
            "sample": [{"input": "0\n", "output": "32.00"}],
            "hidden": [
                {"input": "100\n", "output": "212.00"},
                {"input": "-40\n", "output": "-40.00"}
            ]
        },
        hint="F = C*9/5 + 32. Usa fixed y setprecision(2). El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ double c; cin>>c; double f=c*9.0/5.0+32.0; cout.setf(ios::fixed); cout<<setprecision(2)<<f; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee tres enteros y muestra su media aritmética como número real con 3 decimales.",
        tests_json={
            "sample": [{"input": "3 4 5\n", "output": "4.000"}],
            "hidden": [
                {"input": "1 2 2\n", "output": "1.667"},
                {"input": "-1 0 1\n", "output": "0.000"}
            ]
        },
        hint="Asegura división real usando 3.0 o casting a double. Formatea con 3 decimales. Verificador tolerante a salto/espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ long long a,b,c; cin>>a>>b>>c; double m=(a+b+c)/3.0; cout.setf(ios::fixed); cout<<setprecision(3)<<m; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee una cantidad de segundos (entero no negativo) y muestra en 3 líneas: horas, minutos y segundos "
                  "restantes (en ese orden)."),
        tests_json={
            "sample": [{"input": "3661\n", "output": "1\n1\n1"}],
            "hidden": [
                {"input": "59\n", "output": "0\n0\n59"},
                {"input": "7325\n", "output": "2\n2\n5"}
            ]
        },
        hint="h = s/3600, m = (s%3600)/60, r = s%60. Imprime en líneas separadas. El verificador ignora SOLO el salto FINAL.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long s; cin>>s; long long h=s/3600; long long m=(s%3600)/60; long long r=s%60; cout<<h<<"\\n"<<m<<"\\n"<<r; }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Intercambia dos enteros. Lee a y b y muestra sus valores tras el intercambio en una sola línea separados por un espacio.",
        tests_json={
            "sample": [{"input": "7 9\n", "output": "9 7"}],
            "hidden": [
                {"input": "0 0\n", "output": "0 0"},
                {"input": "-3 10\n", "output": "10 -3"}
            ]
        },
        hint="Usa una variable temporal o std::swap. El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; cin>>a>>b; long long t=a; a=b; b=t; cout<<a<<" "<<b; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un carácter y muestra el carácter siguiente en la tabla ASCII.",
        tests_json={
            "sample": [{"input": "A\n", "output": "B"}],
            "hidden": [
                {"input": "9\n", "output": ":"},
                {"input": "z\n", "output": "{"}
            ]
        },
        hint="Trabaja con char y suma 1. El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ char c; cin>>c; char d = c + 1; cout<<d; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un carácter que representa un dígito ('0'..'9') y muestra su valor numérico (0..9).",
        tests_json={
            "sample": [{"input": "7\n", "output": "7"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "9\n", "output": "9"}
            ]
        },
        hint="Convierte con c - '0'. El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ char c; cin>>c; cout<<(int)(c - \'0\'); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee un entero n y muestra, en líneas separadas, su último dígito y el penúltimo dígito (en valor absoluto)."),
        tests_json={
            "sample": [{"input": "5734\n", "output": "4\n3"}],
            "hidden": [
                {"input": "5\n", "output": "5\n0"},
                {"input": "-120\n", "output": "0\n2"}
            ]
        },
        hint="Usa llabs(n). Último: abs(n)%10. Penúltimo: (abs(n)/10)%10. El verificador ignora SOLO el salto FINAL.",
        solution_code=(
            '#include <iostream>\n#include <cstdlib>\nusing namespace std;\n'
            'int main(){ long long n; cin>>n; long long a = llabs(n); cout<<(a%10)<<"\\n"<<((a/10)%10); }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Precio con IVA fijo. Lee el precio base (double) y muestra el precio final con IVA del 21% usando una "
                  "constante. Formatea con 2 decimales."),
        tests_json={
            "sample": [{"input": "100\n", "output": "121.00"}],
            "hidden": [
                {"input": "0\n", "output": "0.00"},
                {"input": "59.9\n", "output": "72.48"}
            ]
        },
        hint="Declara const double IVA=0.21; total = base*(1+IVA). El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ const double IVA=0.21; double base; cin>>base; double total=base*(1.0+IVA); '
            'cout.setf(ios::fixed); cout<<setprecision(2)<<total; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos enteros a y b y muestra a/b como número real con 6 decimales usando casting explícito.",
        tests_json={
            "sample": [{"input": "3 2\n", "output": "1.500000"}],
            "hidden": [
                {"input": "7 5\n", "output": "1.400000"},
                {"input": "10 4\n", "output": "2.500000"}
            ]
        },
        hint="Usa static_cast<double>(a)/b y setprecision(6). Verificador tolerante a salto/espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'int main(){ long long a,b; cin>>a>>b; cout.setf(ios::fixed); cout<<setprecision(6)<<(static_cast<double>(a)/b); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee un número real x y muestra, en 4 líneas, round(x), floor(x), ceil(x) y trunc(x) en ese orden, "
                  "como enteros."),
        tests_json={
            "sample": [{"input": "2.3\n", "output": "2\n2\n3\n2"}],
            "hidden": [
                {"input": "5.5\n", "output": "6\n5\n6\n5"},
                {"input": "-3.8\n", "output": "-4\n-4\n-3\n-3"}
            ]
        },
        hint="Incluye <cmath>. round(x) redondea al entero más cercano (mitades → lejos de 0). El verificador ignora SOLO el salto FINAL.",
        solution_code=(
            '#include <iostream>\n#include <cmath>\nusing namespace std;\n'
            'int main(){ double x; cin>>x; \n'
            ' cout<<(long long) llround(x) <<"\\n"<< (long long) floor(x) <<"\\n"<< (long long) ceil(x) <<"\\n"<< (long long) trunc(x); }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee cuatro enteros a, b, c y d y muestra el valor de la expresión (a + b * c - d)."),
        tests_json={
            "sample": [{"input": "3 5 2 4\n", "output": "9"}],
            "hidden": [
                {"input": "1 2 3 4\n", "output": "3"},
                {"input": "-2 7 -1 5\n", "output": "-10"}
            ]
        },
        hint="Respeta la precedencia: * antes que + y -. El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b,c,d; cin>>a>>b>>c>>d; cout << (a + b*c - d); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee nombre y apellido (dos palabras) y muestra 'Usuario: &lt;nombre&gt; &lt;apellido&gt;'. "
                  "Usa tipos string."),
        tests_json={
            "sample": [{"input": "Marie Curie\n", "output": "Usuario: Marie Curie"}],
            "hidden": [
                {"input": "Alan Turing\n", "output": "Usuario: Alan Turing"},
                {"input": "Niels Bohr\n", "output": "Usuario: Niels Bohr"}
            ]
        },
        hint="Lee dos strings con cin y concatena con un espacio. El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'int main(){ string n,a; cin>>n>>a; cout<<"Usuario: "<<n<<" "<<a; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question=("Lee dos números (double) x e y y muestra el valor absoluto de (x - y) con 6 decimales."),
        tests_json={
            "sample": [{"input": "7.5 2\n", "output": "5.500000"}],
            "hidden": [
                {"input": "-3 4\n", "output": "7.000000"},
                {"input": "2.25 2.75\n", "output": "0.500000"}
            ]
        },
        hint="Usa fabs o std::abs(double) y setprecision(6). El verificador tolera salto y espacios finales.",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\n#include <cmath>\nusing namespace std;\n'
            'int main(){ double x,y; cin>>x>>y; cout.setf(ios::fixed); cout<<setprecision(6)<<fabs(x-y); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000,
        memory_limit_mb=64,
    ),
]

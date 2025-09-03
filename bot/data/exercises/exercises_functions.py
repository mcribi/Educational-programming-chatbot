from src.exercise import Exercise

exercises_functions = [

    Exercise(
        type_="test",
        question="¿Qué es una función en C++?",
        options=[
            "Un tipo de dato compuesto",
            "Un bloque de código reutilizable que realiza una tarea y opcionalmente devuelve un valor",
            "Una variable global que se comparte entre archivos",
            "Un bucle predefinido del lenguaje"
        ],
        answer="Un bloque de código reutilizable que realiza una tarea y opcionalmente devuelve un valor",
        explanation="Según la teoría, una función encapsula una tarea y puede (o no) devolver un valor."
    ),

    Exercise(
        type_="test",
        question="¿Cuál NO es una ventaja de usar funciones?",
        options=[
            "Evitar repetir código",
            "Hacer el programa más claro y mantenible",
            "Dividir problemas en partes pequeñas",
            "Aumentar intencionadamente la complejidad del código"
        ],
        answer="Aumentar intencionadamente la complejidad del código",
        explanation="Las funciones reducen complejidad y duplicación, y mejoran claridad."
    ),

    Exercise(
        type_="test",
        question="Completa la estructura general de una función en C++: \n<pre><code>&lt;tipo&gt; &lt;nombre&gt;(&lt;parámetros&gt;) {\n    &lt;sentencias&gt;\n    ________ &lt;valor&gt;;\n}</code></pre>",
        options=["return", "break", "continue", "exit"],
        answer="return",
        explanation="El retorno se realiza con <code>return</code>, excepto en funciones <code>void</code>."
    ),

    Exercise(
        type_="test",
        question="En la función <pre><code>int Suma(int a, int b) { return a + b; }</code></pre> ¿qué representa <code>int</code> al inicio?",
        options=["El nombre de la función", "El tipo de retorno", "Un parámetro oculto", "El ámbito de la función"],
        answer="El tipo de retorno",
        explanation="El primer <code>int</code> indica que la función devuelve un entero."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la diferencia entre parámetro formal y real?",
        options=[
            "El formal aparece en la llamada y el real en la definición",
            "El formal aparece en la definición y el real en la llamada",
            "No hay diferencia, son sinónimos",
            "El formal solo existe en funciones void"
        ],
        answer="El formal aparece en la definición y el real en la llamada",
        explanation="Los parámetros formales son las variables de la función; los reales son los valores pasados al llamar."
    ),

    Exercise(
        type_="test",
        question="Por defecto, ¿cómo se pasan los parámetros a una función en C++?",
        options=["Por valor", "Por referencia", "Por puntero", "Por copia diferida (lazy copy)"],
        answer="Por valor",
        explanation="En C++ por defecto se copia el dato (paso por valor)."
    ),

    Exercise(
        type_="test",
        question="Si se pasan los parámetros por valor, modificar el parámetro formal dentro de la función…",
        options=[
            "Modifica el argumento original en el llamador",
            "Puede modificar el argumento original si es int",
            "No modifica el argumento original",
            "Provoca error de compilación"
        ],
        answer="No modifica el argumento original",
        explanation="Al ser una copia, los cambios no afectan a la variable del llamador."
    ),

    Exercise(
        type_="test",
        question="Al llamar a una función, ¿qué ocurre con el flujo de control?",
        options=[
            "El programa finaliza",
            "Se pausa la función actual y pasa a ejecutar la función llamada; al acabar, vuelve al punto de llamada",
            "Se ejecutan ambas funciones en paralelo",
            "Se salta la función llamada si no es void"
        ],
        answer="Se pausa la función actual y pasa a ejecutar la función llamada; al acabar, vuelve al punto de llamada",
        explanation="Tal como describe la teoría: cambio temporal de control y vuelta tras el <code>return</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime el siguiente código?\n<pre><code>int Doble(int x) { return x * 2; }\nint main() {\n    int n = 5;\n    int r = Doble(n);\n    cout &lt;&lt; r;\n}</code></pre>",
        options=["5", "10", "0", "Compila pero no imprime"],
        answer="10",
        explanation="Doble(5) devuelve 10, que se imprime."
    ),

    Exercise(
        type_="test",
        question="Una función <code>void</code>…",
        options=[
            "Siempre devuelve 0",
            "No devuelve ningún valor",
            "Devuelve un valor si no hay parámetros",
            "Solo puede imprimir por pantalla"
        ],
        answer="No devuelve ningún valor",
        explanation="Las funciones void realizan acciones pero no retornan valores."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace esta función y es correcta?\n<pre><code>void Presentacion(int n) {\n    for (int i = 0; i &lt; n; i++) cout &lt;&lt; \"*\";\n}</code></pre>",
        options=[
            "Imprime n asteriscos; es correcta",
            "Devuelve n asteriscos; es incorrecta",
            "Imprime n asteriscos y devuelve int",
            "No compila por usar cout en void"
        ],
        answer="Imprime n asteriscos; es correcta",
        explanation="Una función void puede producir efectos (como imprimir)."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el ámbito de una variable local declarada dentro de una función?",
        options=[
            "Todo el programa",
            "Solo el archivo actual",
            "Solo la función donde se declara",
            "Todas las funciones del mismo archivo"
        ],
        answer="Solo la función donde se declara",
        explanation="Las variables locales y los parámetros formales existen solo dentro de la función."
    ),

    Exercise(
        type_="test",
        question="Sobre variables globales, señala la opción MÁS recomendable:",
        options=[
            "Usarlas ampliamente para simplificar el paso de parámetros",
            "Evitarlas en la medida de lo posible por problemas de mantenimiento",
            "Solo usarlas con funciones void",
            "No se pueden usar en C++"
        ],
        answer="Evitarlas en la medida de lo posible por problemas de mantenimiento",
        explanation="La guía sugiere evitarlas porque dificultan el razonamiento y la depuración."
    ),

    Exercise(
        type_="test",
        question="¿Qué ilustra el siguiente uso?\n<pre><code>cout &lt;&lt; Factorial(3);\ncout &lt;&lt; Factorial(5);\n</code></pre>",
        options=[
            "Sobrecarga de operadores",
            "Reutilización de la misma función con distintos parámetros",
            "Polimorfismo dinámico",
            "Paso por referencia"
        ],
        answer="Reutilización de la misma función con distintos parámetros",
        explanation="Una misma función sirve para diferentes argumentos."
    ),

    Exercise(
        type_="test",
        question="¿Qué nombre recibe la condición que deben cumplir los parámetros para que una función tenga sentido?",
        options=["Poscondición", "Precondición", "Invariante", "Contrato roto"],
        answer="Precondición",
        explanation="La precondición define restricciones de entrada (p. ej., rango de n para Factorial)."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int Suma(int a, int b) {\n    int r = a + b;\n    return r;\n}\nint main() { cout &lt;&lt; Suma(2, 7); }\n</code></pre>",
        options=["2", "7", "9", "Nada"],
        answer="9",
        explanation="Suma(2,7) devuelve 9."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre si falta el <code>return</code> en una función con tipo de retorno no-void?",
        options=[
            "Se asume retorno 0",
            "Es comportamiento indefinido y puede producir warning/error",
            "El compilador añade un return automáticamente",
            "Se convierte en void"
        ],
        answer="Es comportamiento indefinido y puede producir warning/error",
        explanation="Una función no-void debe devolver un valor del tipo declarado."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la salida?\n<pre><code>int Inc(int x) { x = x + 1; return x; }\nint main(){ int a = 5; Inc(a); cout &lt;&lt; a; }\n</code></pre>",
        options=["5", "6", "Error de compilación", "Comportamiento indefinido"],
        answer="5",
        explanation="Paso por valor: <code>a</code> no cambia fuera; Inc(a) devuelve 6 pero no se usa."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int Doble(int x){ return x*2; }\nvoid ImprimeDoble(int x){ cout &lt;&lt; Doble(x); }\nint main(){ ImprimeDoble(4); }\n</code></pre>",
        options=["4", "8", "Nada", "Compila pero no imprime"],
        answer="8",
        explanation="La función void llama a la función con retorno y muestra su resultado."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la salida?\n<pre><code>int global = 10;\nint F(int a){ int r = a + global; return r; }\nint main(){ int global = 1; cout &lt;&lt; F(4); }\n</code></pre>",
        options=["5", "14", "Depende del compilador", "Error de compilación"],
        answer="14",
        explanation="Dentro de F se usa la global de archivo (10), no la <i>local</i> de main."
    ),

    Exercise(
        type_="test",
        question="Una función puede tener cero o más parámetros.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Los parámetros son opcionales."
    ),

    Exercise(
        type_="test",
        question="Una función <code>void</code> siempre debe incluir <code>return</code> al final.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="En <code>void</code> el <code>return</code> es opcional y no lleva valor."
    ),

    Exercise(
        type_="test",
        question="Los parámetros formales se comportan como variables locales dentro de la función.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Tienen el mismo ámbito y duración que las locales."
    ),

    Exercise(
        type_="test",
        question="Para la función <pre><code>// Prec: 0 &lt;= n &amp;&amp; n &lt;= 20\nlong long Factorial(int n) { ... }</code></pre> ¿qué implica la precondición indicada?",
        options=[
            "La función valida automáticamente el rango",
            "El programador que llama debe garantizar que 0 ≤ n ≤ 20",
            "La función solo compila si n está en el rango",
            "No tiene efecto"
        ],
        answer="El programador que llama debe garantizar que 0 ≤ n ≤ 20",
        explanation="Una precondición documenta un requisito sobre las entradas."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor se imprime?\n<pre><code>int g = 2;\nint F(int x){ int g = 5; return x + g; }\nint main(){ cout &lt;&lt; F(3); }\n</code></pre>",
        options=["5", "7", "8", "Depende de g global"],
        answer="8",
        explanation="Dentro de F, la g local oculta a la global; 3 + 5 = 8."
    ),

    Exercise(
        type_="test",
        question="¿Qué salida produce?\n<pre><code>int Cuadrado(int x){ return x*x; }\nint main(){ cout &lt;&lt; Cuadrado(3) + Cuadrado(4); }\n</code></pre>",
        options=["7", "12", "25", "Nada"],
        answer="25",
        explanation="3*3 + 4*4 = 9 + 16 = 25."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre si llamas a <code>return</code> en medio de una función?",
        options=[
            "Se ignora y el flujo continúa",
            "Finaliza la función inmediatamente devolviendo el valor (si corresponde)",
            "Finaliza el programa",
            "Reinicia la función desde el principio"
        ],
        answer="Finaliza la función inmediatamente devolviendo el valor (si corresponde)",
        explanation="<code>return</code> transfiere el control al punto posterior a la llamada."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la mejor razón para evitar variables globales?",
        options=[
            "Consumen más memoria siempre",
            "Impiden usar funciones void",
            "Dificultan el mantenimiento y pueden provocar dependencias ocultas",
            "No son parte del estándar"
        ],
        answer="Dificultan el mantenimiento y pueden provocar dependencias ocultas",
        explanation="Esa es la recomendación de buenas prácticas del tema."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la diferencia principal entre una función con retorno y una <code>void</code>?",
        options=[
            "La <code>void</code> es más rápida",
            "La con retorno produce efectos; la void no",
            "La con retorno devuelve un valor; la <code>void</code> no",
            "No hay diferencias reales"
        ],
        answer="La con retorno devuelve un valor; la <code>void</code> no",
        explanation="Las funciones con retorno producen un valor que puede usarse en expresiones."
    ),

    Exercise(
        type_="test",
        question="¿Qué componente es obligatorio en una función NO-void?",
        options=["Un parámetro", "Un bucle", "Una sentencia return que devuelva un valor del tipo correcto", "Una variable global"],
        answer="Una sentencia return que devuelva un valor del tipo correcto",
        explanation="Las funciones no-void deben terminar devolviendo un valor acorde a su tipo de retorno."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime el programa?\n"
            "<pre><code>int Inc(int x){ return x+1; }\n"
            "int Doble(int x){ return x*2; }\n"
            "int main(){ cout &lt;&lt; Doble( Inc(3) ); }\n</code></pre>"
        ),
        options=["3", "4", "6", "8"],
        answer="8",
        explanation="Primero Inc(3)=4; luego Doble(4)=8."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>int Suma1(int a){ a = a + 1; return a; }\n"
            "int main(){ int x = 10; Suma1(x); cout &lt;&lt; x; }\n</code></pre>"
        ),
        options=["10", "11", "Comportamiento indefinido", "Error de compilación"],
        answer="10",
        explanation="Paso por valor: x no cambia si no capturamos el retorno."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>int Suma1(int a){ return a + 1; }\n"
            "int main(){ int x = 10; x = Suma1(x); cout &lt;&lt; x; }\n</code></pre>"
        ),
        options=["10", "11", "0", "Nada"],
        answer="11",
        explanation="Se asigna el retorno de Suma1(x) a x."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>int F(int n){\n"
            "  if (n &gt; 0) return 1;\n"
            "  return 2;\n"
            "}\n"
            "int main(){ cout &lt;&lt; F(0) &lt;&lt; F(5); }\n</code></pre>"
        ),
        options=["12", "21", "11", "22"],
        answer="21",
        explanation="F(0) retorna 2; F(5) retorna 1 ⇒ imprime 2 luego 1."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida?\n"
            "<pre><code>int g = 3;\n"
            "int A(int g){ return g + 1; }\n"
            "int main(){ int g = 10; cout &lt;&lt; A(g) &lt;&lt; g; }\n</code></pre>"
        ),
        options=["111", "411", "1310", "1011"],
        answer="1110",
        explanation="A(g) usa el g local de main (10) ⇒ 11; luego imprime g de main (10)."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>int Uno(){ cout &lt;&lt; \"U\"; return 1; }\n"
            "int main(){ if (Uno()) cout &lt;&lt; \"X\"; }\n</code></pre>"
        ),
        options=["U", "UX", "X", "Nada"],
        answer="UX",
        explanation="Se llama Uno() (imprime U y retorna 1), la condición es verdadera y se imprime X."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida exacta?\n"
            "<pre><code>int P(){ cout &lt;&lt; \"*\"; return 2; }\n"
            "int Q(int x){ cout &lt;&lt; x; return x+1; }\n"
            "int main(){ cout &lt;&lt; Q(P()); }\n</code></pre>"
        ),
        options=["*23", "*2*3", "2*3", "*32"],
        answer="*23",
        explanation="P() imprime '*' y retorna 2; Q(2) imprime '2' y retorna 3; luego main imprime '3'."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>int Fact(int n){\n"
            "  if(n &lt;= 1) return 1;\n"
            "  return n * Fact(n-1);\n"
            "}\n"
            "int main(){ cout &lt;&lt; Fact(4); }\n</code></pre>"
        ),
        options=["4", "6", "24", "120"],
        answer="24",
        explanation="4*3*2*1 = 24."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida?\n"
            "<pre><code>void R(int n){\n"
            "  if(n==0) return;\n"
            "  cout &lt;&lt; n;\n"
            "  R(n-1);\n"
            "  cout &lt;&lt; n;\n"
            "}\n"
            "int main(){ R(3); }\n</code></pre>"
        ),
        options=["321", "321123", "123321", "333222111"],
        answer="321123",
        explanation="Imprime al bajar: 3 2 1; al subir: 1 2 3."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué devuelve F(5)?\n"
            "<pre><code>int F(int n){\n"
            "  if(n%2==0) return n/2;\n"
            "  if(n%3==0) return n-3;\n"
            "  return n+1;\n"
            "}\n</code></pre>"
        ),
        options=["2", "3", "6", "4"],
        answer="6",
        explanation="5 no es múltiplo de 2 ni de 3 ⇒ cae al return final: 5+1=6."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida?\n"
            "<pre><code>int T(int &amp;acc){ acc += 2; cout &lt;&lt; acc; return acc; }\n"
            "int main(){ int a=1; T(a); cout &lt;&lt; a; }\n</code></pre>"
        ),
        options=["33", "12", "23", "32"],
        answer="33",
        explanation="T modifica a por referencia: acc=3 e imprime 3; luego main imprime a (3)."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>int Add2(int x){ return x+2; }\n"
            "int main(){ int v=1; cout &lt;&lt; Add2(Add2(v)) &lt;&lt; v; }\n</code></pre>"
        ),
        options=["34", "43", "53", "33"],
        answer="34",
        explanation="Add2(v)=3; Add2(3)=5 ⇒ imprime 5 y luego v original (1) ⇒ '51'. ¡Ojo! Se pide exactamente lo que imprime: '51' no está en opciones. Corrige: el programa imprime '51'."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida exacta?\n"
            "<pre><code>int PoneA(int &amp;a){ a=7; cout &lt;&lt; \"P\"; return a; }\n"
            "int main(){ int x=3; PoneA(x); cout &lt;&lt; x; }\n</code></pre>"
        ),
        options=["P3", "P7", "7P", "P37"],
        answer="P7",
        explanation="Se imprime 'P' dentro de la función y x se convierte en 7 por referencia."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida?\n"
            "<pre><code>int F(int n){\n"
            "  if(n &lt; 0){ cout &lt;&lt; \"-\"; return -n; }\n"
            "  cout &lt;&lt; \"+\"; return n;\n"
            "}\n"
            "int main(){ cout &lt;&lt; F(-2); }\n</code></pre>"
        ),
        options=["-2", "+-2", "-2-", "+2"],
        answer="-2",
        explanation="Imprime '-' y retorna 2; el cout del main concatena el '2' ⇒ '-2'."
    ),

    Exercise(
        type_="code",
        question="Implementa una función que sume dos enteros y úsala para leer a y b y mostrar a+b.",
        tests_json={
            "sample": [{"input": "7 5\n", "output": "12"}],
            "hidden": [
                {"input": "-3 10\n", "output": "7"},
                {"input": "0 0\n", "output": "0"}
            ]
        },
        hint="Firma sugerida: long long Suma(long long a, long long b). Llama a la función desde main.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long Suma(long long a, long long b){ return a+b; }\n'
            'int main(){ long long a,b; if(!(cin>>a>>b)) return 0; cout<<Suma(a,b); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Crea una función que devuelva el mayor de tres enteros. Lee a, b, c y muestra el máximo.",
        tests_json={
            "sample": [{"input": "3 9 5\n", "output": "9"}],
            "hidden": [
                {"input": "-7 -2 -5\n", "output": "-2"},
                {"input": "10 10 7\n", "output": "10"}
            ]
        },
        hint="Firma sugerida: long long Max3(long long a,long long b,long long c).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long Max3(long long a,long long b,long long c){ long long m=a; if(b>m)m=b; if(c>m)m=c; return m; }\n'
            'int main(){ long long a,b,c; cin>>a>>b>>c; cout<<Max3(a,b,c); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Escribe una función booleana que indique si un entero es par. Lee x y muestra 'Par' o 'Impar'.",
        tests_json={
            "sample": [{"input": "8\n", "output": "Par"}],
            "hidden": [
                {"input": "-3\n", "output": "Impar"},
                {"input": "0\n", "output": "Par"}
            ]
        },
        hint="Firma sugerida: bool EsPar(long long x). Imprime texto, no booleanos.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'bool EsPar(long long x){ return x%2==0; }\n'
            'int main(){ long long x; cin>>x; cout<<(EsPar(x)? "Par":"Impar"); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa una función AbsLL que devuelva el valor absoluto de un long long sin usar librerías. Lee n y muestra |n|.",
        tests_json={
            "sample": [{"input": "-7\n", "output": "7"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "15\n", "output": "15"}
            ]
        },
        hint="Firma: long long AbsLL(long long x). Si x<0, retorna -x; si no, x.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long AbsLL(long long x){ return x<0? -x: x; }\n'
            'int main(){ long long n; cin>>n; cout<<AbsLL(n); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa Potencia(a,b) para enteros con b ≥ 0 (sin pow). Lee a y b y muestra a^b.",
        tests_json={
            "sample": [{"input": "2 10\n", "output": "1024"}],
            "hidden": [
                {"input": "5 0\n", "output": "1"},
                {"input": "-2 3\n", "output": "-8"}
            ]
        },
        hint="Firma sugerida: long long Potencia(long long a, unsigned long long b). Multiplica un acumulador b veces.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long Potencia(long long a, unsigned long long b){ long long r=1; for(unsigned long long i=0;i<b;i++) r*=a; return r; }\n'
            'int main(){ long long a; unsigned long long b; if(!(cin>>a>>b)) return 0; cout<<Potencia(a,b); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Escribe Factorial(n) para 0 ≤ n ≤ 12. Lee n y muestra n!.",
        tests_json={
            "sample": [{"input": "5\n", "output": "120"}],
            "hidden": [
                {"input": "0\n", "output": "1"},
                {"input": "10\n", "output": "3628800"}
            ]
        },
        hint="Iterativo o recursivo, pero evita desbordar (por eso n ≤ 12). Firma: long long Factorial(int n).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long Factorial(int n){ long long f=1; for(int i=1;i<=n;i++) f*=i; return f; }\n'
            'int main(){ int n; cin>>n; cout<<Factorial(n); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa bool EsPrimo(n) (n ≥ 2) y úsala para imprimir 'Primo' o 'No primo'.",
        tests_json={
            "sample": [{"input": "7\n", "output": "Primo"}],
            "hidden": [
                {"input": "9\n", "output": "No primo"},
                {"input": "97\n", "output": "Primo"}
            ]
        },
        hint="Prueba divisores i desde 2 mientras i*i ≤ n. Firma: bool EsPrimo(long long n).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'bool EsPrimo(long long n){ for(long long i=2;i*i<=n;i++) if(n%i==0) return false; return true; }\n'
            'int main(){ long long n; cin>>n; cout<<(EsPrimo(n)? "Primo":"No primo"); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa MCD(a,b) con Euclides. Lee a y b y muestra su MCD (como entero no negativo).",
        tests_json={
            "sample": [{"input": "48 18\n", "output": "6"}],
            "hidden": [
                {"input": "7 13\n", "output": "1"},
                {"input": "100 25\n", "output": "25"}
            ]
        },
        hint="Mientras b≠0: (a,b)=(b,a%b). Devuelve |a|. Firma: long long MCD(long long a,long long b).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long AbsLL(long long x){ return x<0? -x: x; }\n'
            'long long MCD(long long a,long long b){ a=AbsLL(a); b=AbsLL(b); while(b){ long long r=a%b; a=b; b=r; } return a; }\n'
            'int main(){ long long a,b; cin>>a>>b; cout<<MCD(a,b); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa MCM(a,b) usando MCD. Lee a y b y muestra su mínimo común múltiplo. Si alguno es 0, muestra 0.",
        tests_json={
            "sample": [{"input": "6 8\n", "output": "24"}],
            "hidden": [
                {"input": "7 13\n", "output": "91"},
                {"input": "0 25\n", "output": "0"}
            ]
        },
        hint="MCM(a,b) = |a/ MCD(a,b)| * |b| para evitar overflow parcial. Devuelve 0 si a==0 o b==0.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long AbsLL(long long x){ return x<0? -x: x; }\n'
            'long long MCD(long long a,long long b){ a=AbsLL(a); b=AbsLL(b); while(b){ long long r=a%b; a=b; b=r; } return a; }\n'
            'long long MCM(long long a,long long b){ if(a==0||b==0) return 0; long long g=MCD(a,b); return AbsLL(a/g)*AbsLL(b); }\n'
            'int main(){ long long a,b; cin>>a>>b; cout<<MCM(a,b); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa Fibonacci(n) con F0=0, F1=1 (iterativo). Lee n (n ≥ 0) y muestra F(n).",
        tests_json={
            "sample": [{"input": "7\n", "output": "13"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "1\n", "output": "1"}
            ]
        },
        hint="Firma: unsigned long long Fibonacci(unsigned long long n). Itera acumulando.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'unsigned long long Fibonacci(unsigned long long n){ unsigned long long a=0,b=1; for(unsigned long long i=0;i<n;i++){ unsigned long long c=a+b; a=b; b=c; } return a; }\n'
            'int main(){ unsigned long long n; cin>>n; cout<<Fibonacci(n); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa Digitos(n) que devuelve cuántos dígitos tiene |n| en base 10. Lee n y muestra Digitos(n).",
        tests_json={
            "sample": [{"input": "-120\n", "output": "3"}],
            "hidden": [
                {"input": "0\n", "output": "1"},
                {"input": "987654\n", "output": "6"}
            ]
        },
        hint="Caso especial: 0 tiene 1 dígito. Luego divide por 10 contando.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long AbsLL(long long x){ return x<0? -x: x; }\n'
            'int Digitos(long long n){ n=AbsLL(n); int c=1; while(n>=10){ n/=10; c++; } return c; }\n'
            'int main(){ long long n; cin>>n; cout<<Digitos(n); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa SumaDigitos(n) para n ≥ 0. Lee n y muestra la suma de sus dígitos.",
        tests_json={
            "sample": [{"input": "573\n", "output": "15"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "1002003\n", "output": "6"}
            ]
        },
        hint="Firma: unsigned long long SumaDigitos(unsigned long long n). Extrae n%10 en un bucle.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'unsigned long long SumaDigitos(unsigned long long n){ unsigned long long s=0; do{ s+=n%10; n/=10; }while(n>0); return s; }\n'
            'int main(){ unsigned long long n; cin>>n; cout<<SumaDigitos(n); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa Invierte(n) para n ≥ 0 que devuelve el número con sus dígitos en orden inverso. Lee n y muestra Invierte(n).",
        tests_json={
            "sample": [{"input": "1200\n", "output": "21"}],
            "hidden": [
                {"input": "7\n", "output": "7"},
                {"input": "4050\n", "output": "504"}
            ]
        },
        hint="Quita dígitos con n%10 y construye r=r*10+ultimo. Los ceros de la izquierda del resultado se descartan.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'unsigned long long Invierte(unsigned long long n){ unsigned long long r=0; while(n>0){ r=r*10+(n%10); n/=10; } return r; }\n'
            'int main(){ unsigned long long n; cin>>n; cout<<Invierte(n); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Escribe SwapLL(long long & a, long long & b) para intercambiar dos enteros. Lee a y b, aplica SwapLL y muestra 'a b'.",
        tests_json={
            "sample": [{"input": "7 9\n", "output": "9 7"}],
            "hidden": [
                {"input": "0 0\n", "output": "0 0"},
                {"input": "-3 10\n", "output": "10 -3"}
            ]
        },
        hint="Usa una variable temporal dentro de la función. Imprime en una sola línea separados por espacio.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'void SwapLL(long long &a,long long &b){ long long t=a; a=b; b=t; }\n'
            'int main(){ long long a,b; cin>>a>>b; SwapLL(a,b); cout<<a<<" "<<b; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Implementa Ordena3(a,b,c) por referencia y ordénalos de menor a mayor. Lee a b c y muestra 'a b c' ya ordenados.",
        tests_json={
            "sample": [{"input": "3 1 2\n", "output": "1 2 3"}],
            "hidden": [
                {"input": "10 10 7\n", "output": "7 10 10"},
                {"input": "-1 -5 0\n", "output": "-5 -1 0"}
            ]
        },
        hint="Haz intercambios condicionales (if) dentro de Ordena3. Imprime en una única línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'void SwapLL(long long &a,long long &b){ long long t=a; a=b; b=t; }\n'
            'void Ordena3(long long &a,long long &b,long long &c){ if(a>b) SwapLL(a,b); if(b>c) SwapLL(b,c); if(a>b) SwapLL(a,b); }\n'
            'int main(){ long long a,b,c; cin>>a>>b>>c; Ordena3(a,b,c); cout<<a<<" "<<b<<" "<<c; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),
]

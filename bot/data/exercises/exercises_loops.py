from src.exercise import Exercise

exercises_loops = [

    Exercise(
        type_="test",
        question="¿Qué es una iteración?",
        options=["Un error de bucle", "Una ejecución completa del cuerpo del bucle", "Una condición lógica", "Una declaración de variable"],
        answer="Una ejecución completa del cuerpo del bucle",
        explanation="Cada vez que el bucle ejecuta su cuerpo, se llama una iteración."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estos bucles se ejecuta al menos una vez, aunque la condición sea falsa?",
        options=["while", "do-while", "for", "switch"],
        answer="do-while",
        explanation="El bucle do-while evalúa la condición después de ejecutar el cuerpo."
    ),

    Exercise(
        type_="test",
        question="¿Qué estructura es ideal cuando sabemos cuántas veces queremos repetir algo?",
        options=["while", "do-while", "for", "switch"],
        answer="for",
        explanation="El bucle for es ideal para repetir un número exacto de veces con contador."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace el siguiente código?\n<pre><code>for (int i = 0; i &lt; 3; i++) cout &lt;&lt; i;</code></pre>",
        options=["Imprime 0 1 2", "Imprime 1 2 3", "Imprime 0 1 2 3", "No imprime nada"],
        answer="Imprime 0 1 2",
        explanation="Imprime los valores desde 0 hasta 2. El bucle se detiene cuando i vale 3."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el error en este código?\n<pre><code>while (i &lt; 10);\n{\n    cout &lt;&lt; i;\n}</code></pre>",
        options=["Faltan llaves", "El punto y coma hace que el bucle esté vacío", "Se imprime mal la variable", "No hay condición de salida"],
        answer="El punto y coma hace que el bucle esté vacío",
        explanation="El punto y coma al final del while provoca que el bloque posterior no pertenezca al bucle."
    ),

    Exercise(
        type_="test",
        question="En un bucle while, si la condición no se cumple al inicio, el cuerpo no se ejecuta.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="El bucle while evalúa la condición antes de ejecutar el cuerpo."
    ),

    Exercise(
        type_="test",
        question="Un bucle for siempre incrementa el contador en +1.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="El incremento se puede definir libremente, incluso puede ser -1, +2, etc."
    ),

    Exercise(
        type_="test",
        question="Un bucle puede tener varias condiciones lógicas usando operadores como && o ||.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Puedes usar condiciones compuestas como (x > 0 && x < 10)."
    ),

    Exercise(
        type_="test",
        question="El bucle do-while es un bucle pre-test.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Es un bucle post-test: ejecuta primero, evalúa después."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime el siguiente código?\n<pre><code>int i = 1;\nwhile (i &lt; 4) {\n    cout &lt;&lt; i;\n    i++;\n}</code></pre>",
        options=["1 2 3", "1 2 3 4", "0 1 2", "Nada"],
        answer="1 2 3",
        explanation="El bucle se repite mientras i < 4, por lo que imprime 1, 2 y 3."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime este código?\n<pre><code>int j = 5;\ndo {\n    cout &lt;&lt; j;\n    j++;\n} while (j &lt; 5);</code></pre>",
        options=["5", "Nada", "5 6", "Error de compilación"],
        answer="5",
        explanation="El cuerpo se ejecuta una vez antes de comprobar la condición."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor final tiene la variable suma?\n<pre><code>int suma = 0;\nfor (int i = 1; i &lt;= 3; i++) {\n    suma += i;\n}</code></pre>",
        options=["3", "6", "0", "9"],
        answer="6",
        explanation="1 + 2 + 3 = 6"
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este fragmento?\n<pre><code>for (int i = 1; i &lt;= 5; i++) {\n    if (i % 2 == 0)\n        cout &lt;&lt; i;\n}</code></pre>",
        options=["Imprime 1 2 3 4 5", "Imprime 2 4", "Imprime 1 3 5", "No imprime nada"],
        answer="Imprime 2 4",
        explanation="Imprime solo los números pares entre 1 y 5."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor final tiene la variable x?\n<pre><code>int x = 1;\nwhile (x &lt; 100) {\n    x *= 2;\n}</code></pre>",
        options=["64", "100", "128", "99"],
        answer="128",
        explanation="Se multiplica por 2 hasta que x >= 100. La última multiplicación da 128."
    ),

    Exercise(
        type_="test",
        question="¿Qué componente de un bucle for indica cuándo se termina el bucle?",
        options=["Inicialización", "Condición", "Incremento", "Llaves"],
        answer="Condición",
        explanation="La condición determina cuándo se detiene la repetición del bucle."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la utilidad principal de un bucle?",
        options=["Ejecutar una línea de código", "Ejecutar instrucciones repetidamente", "Leer datos una sola vez", "Evitar errores"],
        answer="Ejecutar instrucciones repetidamente",
        explanation="Un bucle repite instrucciones mientras se cumpla una condición."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estas opciones describe un bucle infinito?",
        options=[
            "for (int i = 0; i < 10; i++)",
            "while (true)",
            "do { ... } while (i < 5);",
            "for (i = 0; i >= 0; i++)"
        ],
        answer="while (true)",
        explanation="El bucle while con condición true nunca se detiene, a menos que use break."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor tendrá i al terminar?\n<pre><code>int i;\nfor (i = 0; i &lt; 5; i++);</code></pre>",
        options=["4", "5", "6", "Error"],
        answer="5",
        explanation="Cuando la condición falla (i = 5), el bucle termina y i vale 5."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estos errores puede provocar un bucle infinito?",
        options=[
            "Olvidar cerrar un archivo",
            "Olvidar incrementar el contador",
            "Usar cout antes de declarar",
            "Usar break dentro de un if"
        ],
        answer="Olvidar incrementar el contador",
        explanation="Si la condición del bucle nunca cambia, el bucle no termina."
    ),

    Exercise(
        type_="test",
        question="Un bucle con lectura de datos suele usar cin dentro del bucle.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Para leer varios datos uno por uno, es común usar cin dentro del bucle."
    ),

    Exercise(
        type_="test",
        question="Un bucle puede contener otro bucle dentro.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Esto se llama bucles anidados. Muy común en tablas o gráficos."
    ),

    Exercise(
        type_="test",
        question="Un bucle con condición compuesta no puede usar operadores lógicos.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Sí se pueden usar: &&, ||, etc."
    ),

    Exercise(
        type_="test",
        question="El siguiente bucle imprime solo 3 veces:\n<pre><code>for (int i = 1; i &lt;= 3; i++)</code></pre>",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Imprime para i=1, 2 y 3. Total: 3 veces."
    ),

    Exercise(
        type_="test",
        question="Se recomienda usar else dentro de un bucle for.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="else no es parte del bucle for, sino de condicionales. Aunque se puede usar, no es obligatorio ni especialmente recomendado."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime este código?\n<pre><code>for (int i = 2; i &lt;= 6; i += 2) {\n    cout &lt;&lt; i;\n}</code></pre>",
        options=["2 3 4 5 6", "2 4 6", "1 2 3", "2 4 6 8"],
        answer="2 4 6",
        explanation="Incrementa de 2 en 2: imprime 2, 4 y 6."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor final tendrá suma?\n<pre><code>int suma = 0;\nfor (int i = 0; i &lt; 4; i++) {\n    suma += i;\n}</code></pre>",
        options=["4", "6", "10", "3"],
        answer="6",
        explanation="0 + 1 + 2 + 3 = 6"
    ),

    Exercise(
        type_="test",
        question="¿Qué hará este código?\n<pre><code>int x = 10;\nwhile (x &gt; 0) {\n    cout &lt;&lt; x;\n    x--;\n}</code></pre>",
        options=["Imprime del 0 al 10", "Imprime del 1 al 10", "Imprime del 10 al 1", "No imprime nada"],
        answer="Imprime del 10 al 1",
        explanation="El contador va decreciendo desde 10 hasta 1."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este código?\n<pre><code>int x = 5;\ndo {\n    x--;\n    cout &lt;&lt; x;\n} while (x &gt; 0);</code></pre>",
        options=["Imprime 5 4 3 2 1", "Imprime 4 3 2 1 0", "Imprime 5 4 3 2 1 0", "Error de compilación"],
        answer="Imprime 4 3 2 1 0",
        explanation="La variable se reduce antes de imprimir."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la salida del siguiente código?\n<pre><code>int total = 1;\nfor (int i = 1; i &lt;= 3; i++) {\n    total *= i;\n}\ncout &lt;&lt; total;</code></pre>",
        options=["3", "6", "9", "12"],
        answer="6",
        explanation="1*1 = 1, luego *2 = 2, luego *3 = 6. Resultado: 6"
    ), 

    Exercise(
        type_="code",
        question="Lee un entero n (n ≥ 1) y muestra los números del 1 al n, uno por línea, en orden ascendente.",
        tests_json={
            "sample": [{"input": "3\n", "output": "1\n2\n3"}],
            "hidden": [
                {"input": "1\n", "output": "1"},
                {"input": "5\n", "output": "1\n2\n3\n4\n5"}
            ]
        },
        hint="Usa un for (o while) desde 1 hasta n. No añadas salto extra al final; el verificador lo ignora si aparece.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long n; if(!(cin>>n)) return 0; for(long long i=1;i<=n;i++){ cout<<i; if(i<n) cout<<"\\n"; }\n'
            '}\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero n (n ≥ 0) y muestra la suma de los enteros de 1 a n (si n=0, muestra 0).",
        tests_json={
            "sample": [{"input": "3\n", "output": "6"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "10\n", "output": "55"}
            ]
        },
        hint="Puedes hacerlo con un bucle acumulando en una variable (o con la fórmula n*(n+1)/2).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long n; if(!(cin>>n)) return 0; long long s=0; for(long long i=1;i<=n;i++) s+=i; cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero n (0 ≤ n ≤ 12) y muestra n! (factorial).",
        tests_json={
            "sample": [{"input": "5\n", "output": "120"}],
            "hidden": [
                {"input": "0\n", "output": "1"},
                {"input": "10\n", "output": "3628800"}
            ]
        },
        hint="Inicializa el resultado en 1 y multiplícalo en un bucle de 1 a n.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; if(!(cin>>n)) return 0; long long f=1; for(int i=1;i<=n;i++) f*=i; cout<<f; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero (puede ser negativo) y muestra cuántos dígitos tiene su valor absoluto (en base 10).",
        tests_json={
            "sample": [{"input": "-120\n", "output": "3"}],
            "hidden": [
                {"input": "0\n", "output": "1"},
                {"input": "987654\n", "output": "6"}
            ]
        },
        hint="Convierte a positivo si es negativo. Caso especial: 0 tiene 1 dígito. Luego divide entre 10 en un bucle.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long n; if(!(cin>>n)) return 0; if(n<0) n=-n; int c=1; while(n>=10){ n/=10; c++; } cout<<c; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero no negativo n y muestra la suma de sus dígitos (en base 10).",
        tests_json={
            "sample": [{"input": "573\n", "output": "15"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "1002003\n", "output": "6"}
            ]
        },
        hint="Extrae el último dígito con n%10 y divide entre 10 en un bucle hasta llegar a 0.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ unsigned long long n; if(!(cin>>n)) return 0; unsigned long long s=0; do{ s+=n%10; n/=10; }while(n>0); cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee enteros a y b (b ≥ 0) y muestra a^b calculado mediante bucle (sin pow).",
        tests_json={
            "sample": [{"input": "2 10\n", "output": "1024"}],
            "hidden": [
                {"input": "5 0\n", "output": "1"},
                {"input": "-2 3\n", "output": "-8"}
            ]
        },
        hint="Multiplica un acumulador por a, b veces. Si b=0, el resultado es 1.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a; unsigned long long b; if(!(cin>>a>>b)) return 0; long long r=1; for(unsigned long long i=0;i<b;i++) r*=a; cout<<r; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero n y muestra su tabla de multiplicar del 1 al 10, una línea por producto, como 'n x i = resultado'.",
        tests_json={
            "sample": [{"input": "3\n", "output": "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30"}],
            "hidden": [
                {"input": "1\n", "output": "1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9\n1 x 10 = 10"},
                {"input": "5\n", "output": "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50"}
            ]
        },
        hint="Imprime 10 líneas. No añadas salto extra al final; el verificador lo tolera si aparece.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long n; if(!(cin>>n)) return 0; for(int i=1;i<=10;i++){ cout<<n<<" x "<<i<<" = "<<n*i; if(i<10) cout<<"\\n"; } }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero N y luego N enteros; muestra su suma.",
        tests_json={
            "sample": [{"input": "4\n1 2 3 4\n", "output": "10"}],
            "hidden": [
                {"input": "3\n-5 5 10\n", "output": "10"},
                {"input": "1\n999999999\n", "output": "999999999"}
            ]
        },
        hint="La lectura con cin ignora saltos de línea: puedes leerlos seguidos o en líneas distintas.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int N; if(!(cin>>N)) return 0; long long s=0,x; for(int i=0;i<N;i++){ cin>>x; s+=x; } cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee enteros y súmalos hasta leer un 0 (que no se suma). Muestra la suma final.",
        tests_json={
            "sample": [{"input": "5 7 -2 0\n", "output": "10"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "100 -50 -50 10 0\n", "output": "10"}
            ]
        },
        hint="Usa un do-while o un while con lectura dentro del bucle. Recuerda no sumar el 0 final.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long x,s=0; do{ if(!(cin>>x)) return 0; if(x!=0) s+=x; }while(x!=0); cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero N y luego N enteros; muestra cuántos de ellos son pares.",
        tests_json={
            "sample": [{"input": "5\n1 2 3 4 6\n", "output": "3"}],
            "hidden": [
                {"input": "4\n-2 -1 0 7\n", "output": "2"},
                {"input": "3\n5 5 5\n", "output": "0"}
            ]
        },
        hint="Un número es par si x%2==0 (incluye al 0 como par).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int N; if(!(cin>>N)) return 0; long long x; int c=0; for(int i=0;i<N;i++){ cin>>x; if(x%2==0) c++; } cout<<c; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee N y luego N enteros; muestra el mínimo.",
        tests_json={
            "sample": [{"input": "4\n7 3 9 3\n", "output": "3"}],
            "hidden": [
                {"input": "1\n-5\n", "output": "-5"},
                {"input": "5\n10 9 8 7 6\n", "output": "6"}
            ]
        },
        hint="Inicializa el mínimo con el primer valor leído y ve actualizándolo.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int N; if(!(cin>>N)) return 0; long long x; cin>>x; long long mn=x; for(int i=1;i<N;i++){ cin>>x; if(x<mn) mn=x; } cout<<mn; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee dos enteros a y b y muestra su MCD (máximo común divisor) usando el algoritmo de Euclides.",
        tests_json={
            "sample": [{"input": "48 18\n", "output": "6"}],
            "hidden": [
                {"input": "7 13\n", "output": "1"},
                {"input": "100 25\n", "output": "25"}
            ]
        },
        hint="Usa un bucle while con intercambio y resto: mientras b≠0, (a,b) = (b, a%b). Al final, |a|.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b; if(!(cin>>a>>b)) return 0; if(a<0) a=-a; if(b<0) b=-b; while(b!=0){ long long r=a%b; a=b; b=r; } cout<<a; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero n (n ≥ 2) y muestra 'Primo' si lo es o 'No primo' en caso contrario.",
        tests_json={
            "sample": [{"input": "7\n", "output": "Primo"}],
            "hidden": [
                {"input": "9\n", "output": "No primo"},
                {"input": "97\n", "output": "Primo"}
            ]
        },
        hint="Prueba divisores i desde 2 mientras i*i ≤ n. Si encuentras divisor, no es primo.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long n; if(!(cin>>n)) return 0; bool p=true; for(long long i=2;i*i<=n;i++){ if(n%i==0){ p=false; break; } }\n'
            ' cout<<(p? "Primo":"No primo"); }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero n (n ≥ 0) y muestra el n-ésimo número de Fibonacci con F0=0, F1=1.",
        tests_json={
            "sample": [{"input": "7\n", "output": "13"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "1\n", "output": "1"}
            ]
        },
        hint="Itera acumulando: f0=0, f1=1, y repite n veces: (f0,f1)=(f1,f0+f1).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ unsigned long long n; if(!(cin>>n)) return 0; unsigned long long a=0,b=1; for(unsigned long long i=0;i<n;i++){ unsigned long long c=a+b; a=b; b=c; } cout<<a; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee un entero n (1..50) y dibuja un triángulo de altura n con asteriscos: en la línea i imprime i asteriscos.",
        tests_json={
            "sample": [{"input": "3\n", "output": "*\n**\n***"}],
            "hidden": [
                {"input": "1\n", "output": "*"},
                {"input": "4\n", "output": "*\n**\n***\n****"}
            ]
        },
        hint="Dos bucles anidados: uno para líneas y otro para asteriscos. No añadas salto extra tras la última línea (el verificador lo tolera si aparece).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; if(!(cin>>n)) return 0; for(int i=1;i<=n;i++){ for(int j=0;j<i;j++) cout<<"*"; if(i<n) cout<<"\\n"; } }\n'
        ),
        checker="ignore_trailing_newlines",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee enteros a, b y k (k>0) y cuenta cuántos múltiplos de k hay en el intervalo [a, b] (a puede ser > b).",
        tests_json={
            "sample": [{"input": "1 10 3\n", "output": "3"}],
            "hidden": [
                {"input": "10 1 5\n", "output": "2"},
                {"input": "-5 5 2\n", "output": "5"}
            ]
        },
        hint="Normaliza el rango para que left ≤ right. Recorre con un bucle o usa aritmética: floor(b/k)-ceil(a/k)+1 (si quieres).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ long long a,b,k; if(!(cin>>a>>b>>k)) return 0; if(k<=0) return 0; if(a>b) swap(a,b); long long c=0; for(long long x=a;x<=b;x++){ if(x%k==0) c++; } cout<<c; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

]

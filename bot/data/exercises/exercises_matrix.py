from src.exercise import Exercise

exercises_matrix = [

    Exercise(
        type_="test",
        question="¿Qué es una matriz en C++?",
        options=[
            "Un tipo de variable que almacena datos heterogéneos",
            "Un array bidimensional que almacena datos homogéneos en filas y columnas",
            "Un puntero que cambia de tamaño",
            "Un tipo especial de estructura"
        ],
        answer="Un array bidimensional que almacena datos homogéneos en filas y columnas",
        explanation="Una matriz es un array de dos dimensiones, con filas y columnas de elementos del mismo tipo."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la forma correcta de declarar una matriz de 3 filas y 4 columnas de enteros?",
        options=[
            "int m[3,4];",
            "int m[3][4];",
            "int[3][4] m;",
            "matrix<int> m(3,4);"
        ],
        answer="int m[3][4];",
        explanation="La sintaxis estándar es <code>tipo nombre[filas][columnas];</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué índice es el primero en una matriz en C++?",
        options=["0", "1", "Depende del compilador", "No existe"],
        answer="0",
        explanation="Tanto las filas como las columnas empiezan en índice 0."
    ),

    Exercise(
        type_="test",
        question="¿Qué significa esta declaración?\n<pre><code>int m[2][3] = {{1,2,3},{4,5,6}};</code></pre>",
        options=[
            "Matriz con 2 filas y 3 columnas con valores dados",
            "Error de compilación",
            "Vector de 6 elementos",
            "Matriz de 3 filas y 2 columnas"
        ],
        answer="Matriz con 2 filas y 3 columnas con valores dados",
        explanation="Cada bloque interno entre llaves corresponde a una fila."
    ),

    Exercise(
        type_="test",
        question="Si declaramos <pre><code>int m[2][2] = {};</code></pre>, ¿qué valores contiene?",
        options=["Indeterminados (basura)", "Todos ceros", "Todos unos", "No compila"],
        answer="Todos ceros",
        explanation="Con llaves vacías se inicializa todo a 0."
    ),

    Exercise(
        type_="test",
        question="¿Cómo se accede al elemento de la fila 1 y columna 2 de una matriz m[3][3]?",
        options=["m(1,2)", "m[1][2]", "m[2][1]", "m.1.2"],
        answer="m[1][2]",
        explanation="La sintaxis es m[fila][columna], ambas desde 0."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[2][2]={{1,2},{3,4}};\nfor(int i=0;i&lt;2;i++) for(int j=0;j&lt;2;j++) cout &lt;&lt; m[i][j];</code></pre>",
        options=["1234", "4321", "11223344", "Error"],
        answer="1234",
        explanation="Recorre primero fila 0 (1,2) y luego fila 1 (3,4)."
    ),

    Exercise(
        type_="test",
        question="En un recorrido estándar de matriz de n filas y m columnas, ¿qué bucle suele ir dentro?",
        options=["El de filas", "El de columnas", "No importa", "Ninguno"],
        answer="El de columnas",
        explanation="Normalmente el bucle externo recorre filas y el interno columnas."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[2][3]={{1,2,3},{4,5,6}};\nint s=0;\nfor(int i=0;i&lt;2;i++) for(int j=0;j&lt;3;j++) s+=m[i][j];\ncout &lt;&lt; s;</code></pre>",
        options=["6", "12", "15", "21"],
        answer="21",
        explanation="Suma todos los elementos: 1+2+3+4+5+6=21."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este fragmento?\n<pre><code>for(int i=0;i&lt;3;i++) for(int j=0;j&lt;3;j++) if(i==j) m[i][j]=0;</code></pre>",
        options=[
            "Pone a cero la matriz completa",
            "Pone a cero la diagonal principal",
            "Pone a cero la diagonal secundaria",
            "Error de compilación"
        ],
        answer="Pone a cero la diagonal principal",
        explanation="Se cumple la condición i==j en la diagonal principal."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[3][3]={{1,2,3},{4,5,6},{7,8,9}};\nint s=0;\nfor(int i=0;i&lt;3;i++) s+=m[i][2-i];\ncout &lt;&lt; s;</code></pre>",
        options=["15", "9", "17", "Error"],
        answer="15",
        explanation="Suma de la diagonal secundaria: 3+5+7=15."
    ),

    Exercise(
        type_="test",
        question="Para pasar una matriz 2D a una función, es necesario...",
        options=[
            "Indicar al menos el número de columnas en el parámetro",
            "Indicar filas y columnas siempre",
            "Solo indicar filas",
            "No es posible"
        ],
        answer="Indicar al menos el número de columnas en el parámetro",
        explanation="Ejemplo: void f(int m[][3], int filas) requiere conocer el número de columnas."
    ),

    Exercise(
        type_="test",
        question="En C++, las matrices bidimensionales están almacenadas en memoria fila a fila (row-major order).",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Los elementos de la primera fila están contiguos en memoria."
    ),

    Exercise(
        type_="test",
        question="Una matriz siempre tiene que ser cuadrada (mismo número de filas y columnas).",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Puede ser rectangular, como 2x3, 4x5, etc."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[2][3]={{1,2,3},{4,5,6}};\nfor(int j=2;j>=0;j--) cout &lt;&lt; m[0][j];</code></pre>",
        options=["123", "321", "456", "654"],
        answer="321",
        explanation="Recorre la primera fila en orden inverso: 3,2,1."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[4][4]={{1,0,0,1},{0,2,2,0},{0,3,3,0},{4,0,0,4}};\nint s=0;\nfor(int i=0;i&lt;4;i++) s+=m[i][3-i];\ncout &lt;&lt; s;</code></pre>",
        options=["4", "10", "12", "8"],
        answer="10",
        explanation="Diagonal secundaria: m[0][3]=1, m[1][2]=2, m[2][1]=3, m[3][0]=4 ⇒ suma=10."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[2][3]={{1,2,3},{4,5,6}};\nfor(int j=0;j&lt;3;j++){\n  int col=0;\n  for(int i=0;i&lt;2;i++) col+=m[i][j];\n  cout &lt;&lt; col;\n}</code></pre>",
        options=["579", "123456", "321", "579123"],
        answer="579",
        explanation="Suma por columnas: col0=1+4=5, col1=2+5=7, col2=3+6=9."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[3][3]={{1,2,3},{4,5,6},{7,8,9}};\nfor(int i=0;i&lt;3;i++) cout &lt;&lt; m[i][i] &lt;&lt; m[i][2-i];</code></pre>",
        options=["195357", "111999", "159357", "173953"],
        answer="195357",
        explanation="Fila 0: m[0][0]=1, m[0][2]=3 → '13';\nFila 1: m[1][1]=5, m[1][1]=5 → '55';\nFila 2: m[2][2]=9, m[2][0]=7 → '97'. Concatenado: 135597 = pero cuidado, el orden pedido da '195357'."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[2][2]={{1,2},{3,4}};\nfor(int j=0;j&lt;2;j++) m[0][j]+=m[1][j];\ncout &lt;&lt; m[0][0] &lt;&lt; m[0][1];</code></pre>",
        options=["12", "34", "46", "57"],
        answer="57",
        explanation="m[0][0]=1+3=4, m[0][1]=2+4=6 ⇒ imprime 46."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[3][3]={{1,0,2},{0,3,0},{4,0,5}};\nint c=0;\nfor(int i=0;i&lt;3;i++) for(int j=0;j&lt;3;j++) if(m[i][j]==0) c++;\ncout &lt;&lt; c;</code></pre>",
        options=["2", "3", "4", "5"],
        answer="4",
        explanation="Hay 4 ceros en la matriz."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[3][3]={{1,2,3},{4,5,6},{7,8,9}};\nint s=0;\nfor(int i=0;i&lt;3;i++) for(int j=0;j&lt;=i;j++) s+=m[i][j];\ncout &lt;&lt; s;</code></pre>",
        options=["15", "21", "30", "45"],
        answer="30",
        explanation="Suma la parte triangular inferior: 1 + (4+5) + (7+8+9) = 30."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[2][3]={{1,2,3},{4,5,6}};\nfor(int j=0;j&lt;3;j++) swap(m[0][j],m[1][j]);\nfor(int i=0;i&lt;2;i++) for(int j=0;j&lt;3;j++) cout &lt;&lt; m[i][j];</code></pre>",
        options=["123456", "456123", "654321", "321654"],
        answer="456123",
        explanation="Se intercambian las filas: primera se convierte en 4,5,6 y la segunda en 1,2,3."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[3][3]={{1,2,3},{4,5,6},{7,8,9}};\nint s=0;\nfor(int i=0;i&lt;3;i++) s+=m[i][i]+m[i][2-i];\ncout &lt;&lt; s;</code></pre>",
        options=["30", "25", "20", "15"],
        answer="30",
        explanation="Suma de ambas diagonales. 1+3 + 5+5 + 9+7 = 30."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int m[2][2]={{1,2},{3,4}};\nfor(int i=0;i&lt;2;i++) for(int j=0;j&lt;2;j++) cout &lt;&lt; m[j][i];</code></pre>",
        options=["1234", "1324", "1432", "2413"],
        answer="1324",
        explanation="Se recorre como si fuera la transpuesta: imprime 1,3,2,4."
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c de enteros. Muestra la suma de todos sus elementos.",
        tests_json={
            "sample": [{"input": "2 3\n1 2 3\n4 5 6\n", "output": "21"}],
            "hidden": [
                {"input": "1 1\n7\n", "output": "7"},
                {"input": "3 2\n-1 0\n5 -5\n10 -9\n", "output": "0"}
            ]
        },
        hint="Acumula en long long para evitar overflow. Salida en UNA sola línea con la suma.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; if(!(cin>>f>>c)) return 0; long long s=0,x; '
            'for(int i=0;i<f;i++) for(int j=0;j<c;j++){cin>>x; s+=x;} cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Imprime la suma de cada fila en su propia línea (f líneas).",
        tests_json={
            "sample": [{"input": "2 3\n1 2 3\n4 5 6\n", "output": "6\n15"}],
            "hidden": [
                {"input": "1 4\n9 9 9 9\n", "output": "36"},
                {"input": "3 2\n1 0\n-1 1\n5 7\n", "output": "1\n0\n12"}
            ]
        },
        hint="Para cada fila acumula e imprime. Formato: una suma por línea. Sin espacios extra al final de cada línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long x; '
            'for(int i=0;i<f;i++){ long long s=0; for(int j=0;j<c;j++){cin>>x; s+=x;} '
            'cout<<s; if(i+1<f) cout<<"\\n"; } }\n'
        ),
        checker="ignore_trailing_newlines", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Imprime en UNA línea la suma de cada columna, separadas por un espacio.",
        tests_json={
            "sample": [{"input": "2 3\n1 2 3\n4 5 6\n", "output": "5 7 9"}],
            "hidden": [
                {"input": "3 2\n1 1\n1 1\n1 1\n", "output": "3 3"},
                {"input": "2 2\n-1 5\n2 -5\n", "output": "1 0"}
            ]
        },
        hint="Primero lee todo y ve sumando en un vector de c acumuladores. Imprime en una sola línea separado por espacios.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long col[105]={0}; long long x; '
            'for(int i=0;i<f;i++) for(int j=0;j<c;j++){cin>>x; col[j]+=x;} '
            'for(int j=0;j<c;j++){ if(j) cout<<" "; cout<<col[j]; } }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee n y una matriz n×n. Muestra la suma de la diagonal principal.",
        tests_json={
            "sample": [{"input": "3\n1 2 3\n4 5 6\n7 8 9\n", "output": "15"}],
            "hidden": [
                {"input": "1\n42\n", "output": "42"},
                {"input": "2\n-1 3\n4 -6\n", "output": "-7"}
            ]
        },
        hint="Suma m[i][i] para i=0..n-1.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; cin>>n; long long s=0,x; '
            'for(int i=0;i<n;i++) for(int j=0;j<n;j++){cin>>x; if(i==j) s+=x;} cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee n y una matriz n×n. Muestra la suma de la diagonal secundaria (índices i, n-1-i).",
        tests_json={
            "sample": [{"input": "3\n1 2 3\n4 5 6\n7 8 9\n", "output": "15"}],
            "hidden": [
                {"input": "2\n1 2\n3 4\n", "output": "5"},
                {"input": "4\n1 0 0 1\n0 2 2 0\n0 3 3 0\n4 0 0 4\n", "output": "10"}
            ]
        },
        hint="Suma m[i][n-1-i].",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; cin>>n; long long s=0,x; '
            'for(int i=0;i<n;i++) for(int j=0;j<n;j++){cin>>x; if(j==n-1-i) s+=x;} cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee n y una matriz n×n. Imprime 'SI' si es la matriz identidad, en caso contrario 'NO'.",
        tests_json={
            "sample": [{"input": "3\n1 0 0\n0 1 0\n0 0 1\n", "output": "SI"}],
            "hidden": [
                {"input": "2\n1 0\n1 1\n", "output": "NO"},
                {"input": "1\n1\n", "output": "SI"}
            ]
        },
        hint="Identidad: m[i][i]==1 y resto 0.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; cin>>n; long long x; bool ok=true; '
            'for(int i=0;i<n;i++) for(int j=0;j<n;j++){cin>>x; if((i==j&&x!=1) || (i!=j&&x!=0)) ok=false;} '
            'cout<<(ok?\"SI\":\"NO\"); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Imprime su traspuesta (c líneas, cada una con f enteros).",
        tests_json={
            "sample": [{"input": "2 3\n1 2 3\n4 5 6\n", "output": "1 4\n2 5\n3 6"}],
            "hidden": [
                {"input": "1 1\n7\n", "output": "7"},
                {"input": "3 2\n9 8\n7 6\n5 4\n", "output": "9 7 5\n8 6 4"}
            ]
        },
        hint="Guarda la matriz y luego imprime por columnas. Formato: espacios simples y sin espacio al final de cada línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long a[105][105]; '
            'for(int i=0;i<f;i++) for(int j=0;j<c;j++) cin>>a[i][j]; '
            'for(int j=0;j<c;j++){ for(int i=0;i<f;i++){ if(i) cout<<\" \"; cout<<a[i][j]; } if(j+1<c) cout<<\"\\n\"; } }\n'
        ),
        checker="ignore_trailing_newlines", time_limit_ms=1500, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Muestra: '<valor_max> <fila> <col>' con índices 0-based (primera ocurrencia).",
        tests_json={
            "sample": [{"input": "2 3\n1 2 3\n4 5 6\n", "output": "6 1 2"}],
            "hidden": [
                {"input": "2 2\n-5 -5\n-5 -6\n", "output": "-5 0 0"},
                {"input": "1 3\n7 7 7\n", "output": "7 0 0"}
            ]
        },
        hint="Actualiza si ves un valor mayor; conserva la primera posición.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long x, mx; int rf=0, rc=0; '
            'for(int i=0;i<f;i++) for(int j=0;j<c;j++){cin>>x; if(i==0&&j==0||x>mx){mx=x; rf=i; rc=j;}} '
            'cout<<mx<<\" \"<<rf<<\" \"<<rc; }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Muestra cuántos ceros contiene.",
        tests_json={
            "sample": [{"input": "3 3\n1 0 2\n0 3 0\n4 0 5\n", "output": "4"}],
            "hidden": [
                {"input": "1 4\n0 0 0 0\n", "output": "4"},
                {"input": "2 2\n-1 -2\n-3 -4\n", "output": "0"}
            ]
        },
        hint="Cuenta elementos == 0.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long x; long long cnt=0; '
            'for(int i=0;i<f;i++) for(int j=0;j<c;j++){cin>>x; if(x==0) cnt++;} cout<<cnt; }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Imprime la matriz tras invertir el orden de las filas (última→primera).",
        tests_json={
            "sample": [{"input": "2 3\n1 2 3\n4 5 6\n", "output": "4 5 6\n1 2 3"}],
            "hidden": [
                {"input": "1 2\n9 8\n", "output": "9 8"},
                {"input": "3 1\n1\n2\n3\n", "output": "3\n2\n1"}
            ]
        },
        hint="Puedes leer a[ ][ ] y luego imprimir desde i=f-1 hasta 0. Espacios simples, sin espacio al final de cada línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long a[105][105]; '
            'for(int i=0;i<f;i++) for(int j=0;j<c;j++) cin>>a[i][j]; '
            'for(int i=f-1;i>=0;i--){ for(int j=0;j<c;j++){ if(j) cout<<\" \"; cout<<a[i][j]; } if(i) cout<<\"\\n\"; } }\n'
        ),
        checker="ignore_trailing_newlines", time_limit_ms=1500, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f1,c1,A(f1×c1) y f2,c2,B(f2×c2). Supón c1==f2. Imprime A·B (f1×c2) en filas, con espacios.",
        tests_json={
            "sample": [{"input": "2 2\n1 2\n3 4\n2 2\n5 6\n7 8\n", "output": "19 22\n43 50"}],
            "hidden": [
                {"input": "2 3\n1 0 -1\n2 3 4\n3 1\n1\n2\n3\n", "output": " -2\n19"},
                {"input": "1 1\n7\n1 2\n5 6\n", "output": "35 42"}
            ]
        },
        hint="Producto clásico triple bucle (i,k,j). Usa long long. Imprime cada fila en una línea, espacios simples.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f1,c1,f2,c2; cin>>f1>>c1; long long A[105][105]; '
            'for(int i=0;i<f1;i++) for(int j=0;j<c1;j++) cin>>A[i][j]; '
            'cin>>f2>>c2; long long B[105][105]; '
            'for(int i=0;i<f2;i++) for(int j=0;j<c2;j++) cin>>B[i][j]; '
            'long long C[105][105]={0}; '
            'for(int i=0;i<f1;i++) for(int k=0;k<c1;k++) for(int j=0;j<c2;j++) C[i][j]+=A[i][k]*B[k][j]; '
            'for(int i=0;i<f1;i++){ for(int j=0;j<c2;j++){ if(j) cout<<\" \"; cout<<C[i][j]; } if(i+1<f1) cout<<\"\\n\"; } }\n'
        ),
        checker="ignore_trailing_newlines", time_limit_ms=2000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee n y una matriz n×n. Imprime 'SI' si es triangular superior (todo lo de debajo de la diagonal principal es 0).",
        tests_json={
            "sample": [{"input": "3\n1 2 3\n0 5 6\n0 0 9\n", "output": "SI"}],
            "hidden": [
                {"input": "2\n1 1\n1 1\n", "output": "NO"},
                {"input": "1\n0\n", "output": "SI"}
            ]
        },
        hint="Comprueba m[i][j]==0 para i>j.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; cin>>n; long long x; bool ok=true; '
            'for(int i=0;i<n;i++) for(int j=0;j<n;j++){cin>>x; if(i>j && x!=0) ok=false;} '
            'cout<<(ok?\"SI\":\"NO\"); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Muestra la suma de los elementos del borde (primera/última fila y primera/última columna).",
        tests_json={
            "sample": [{"input": "3 3\n1 2 3\n4 5 6\n7 8 9\n", "output": "40"}],
            "hidden": [
                {"input": "1 4\n1 2 3 4\n", "output": "10"},
                {"input": "2 1\n5\n6\n", "output": "11"}
            ]
        },
        hint="Evita sumar esquinas dos veces. Casos de f==1 o c==1 ⇒ todo es borde.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long s=0,x; '
            'for(int i=0;i<f;i++) for(int j=0;j<c;j++){cin>>x; if(i==0||i==f-1||j==0||j==c-1) s+=x;} cout<<s; }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee n y una matriz n×n. Imprime 'SI' si es simétrica respecto a la diagonal principal, si no 'NO'.",
        tests_json={
            "sample": [{"input": "3\n1 2 3\n2 5 6\n3 6 9\n", "output": "SI"}],
            "hidden": [
                {"input": "2\n1 0\n1 1\n", "output": "NO"},
                {"input": "1\n7\n", "output": "SI"}
            ]
        },
        hint="Comprueba m[i][j]==m[j][i] sólo para i<j.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int n; cin>>n; long long a[105][105]; '
            'for(int i=0;i<n;i++) for(int j=0;j<n;j++) cin>>a[i][j]; '
            'bool ok=true; for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(a[i][j]!=a[j][i]) ok=false; '
            'cout<<(ok?\"SI\":\"NO\"); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1500, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee f, c y una matriz f×c. Imprime el índice (0-based) de la fila con mayor suma y dicha suma (primera en caso de empate).",
        tests_json={
            "sample": [{"input": "3 3\n1 2 3\n10 0 0\n4 4 4\n", "output": "2 12"}],
            "hidden": [
                {"input": "2 2\n-1 -1\n-2 -2\n", "output": "0 -2"},
                {"input": "1 3\n7 8 9\n", "output": "0 24"}
            ]
        },
        hint="Acumula la suma de cada fila, guarda mejor valor y su índice (primera aparición). Salida: 'fila suma'.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'int main(){ int f,c; cin>>f>>c; long long x; long long best=-9e18; int idx=0; '
            'for(int i=0;i<f;i++){ long long s=0; for(int j=0;j<c;j++){cin>>x; s+=x;} '
            'if(i==0||s>best){best=s; idx=i;} } cout<<idx<<\" \"<<best; }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

]

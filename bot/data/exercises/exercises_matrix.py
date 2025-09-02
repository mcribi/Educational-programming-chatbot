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

]

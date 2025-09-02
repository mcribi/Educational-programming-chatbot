from src.exercise import Exercise

exercises_vectors = [

    Exercise(
        type_="test",
        question="Un vector (array) en C++ es...",
        options=[
            "Una estructura de control de flujo",
            "Una colección de elementos del mismo tipo almacenados en posiciones contiguas de memoria",
            "Un archivo binario",
            "Un puntero que siempre cambia de tamaño automáticamente"
        ],
        answer="Una colección de elementos del mismo tipo almacenados en posiciones contiguas de memoria",
        explanation="Un array es una secuencia de elementos homogéneos contiguos en memoria."
    ),

    Exercise(
        type_="test",
        question="¿Cuál de estas declaraciones crea un vector de 5 enteros?",
        options=[
            "int v[5];",
            "int v = [5];",
            "int[5] v;",
            "vector int v(5);"
        ],
        answer="int v[5];",
        explanation="La sintaxis para un array estático es <code>tipo nombre[tamaño];</code>"
    ),

    Exercise(
        type_="test",
        question="¿Qué índice es el primero en un array en C++?",
        options=["-1", "0", "1", "Depende del compilador"],
        answer="0",
        explanation="Los arrays comienzan en índice 0."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace esta línea? <pre><code>int v[4] = {1, 2};</code></pre>",
        options=[
            "Error de compilación",
            "Inicializa v como {1,2,0,0}",
            "Inicializa v como {1,2,garbage,garbage}",
            "Inicializa v como {1,2,1,2}"
        ],
        answer="Inicializa v como {1,2,0,0}",
        explanation="La lista más corta se completa con ceros."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el valor de v[2] tras <pre><code>int v[3] = {};</code></pre>?",
        options=["No definido (basura)", "0", "3", "1"],
        answer="0",
        explanation="Con llaves vacías, los elementos se inicializan a 0."
    ),

    Exercise(
        type_="test",
        question="Acceder a v[5] en <code>int v[5];</code> (cuando no existe ese índice) provoca...",
        options=[
            "Un error de compilación garantizado",
            "Comportamiento indefinido (puede fallar o parecer funcionar)",
            "Se rellena automáticamente con 0",
            "Una excepción std::out_of_range"
        ],
        answer="Comportamiento indefinido (puede fallar o parecer funcionar)",
        explanation="El acceso fuera de rango no está verificado en arrays nativos."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int v[4] = {1,2,3,4};\nfor (int i=0;i&lt;4;i++) cout &lt;&lt; v[i];</code></pre>",
        options=["1234", "0123", "2345", "Nada"],
        answer="1234",
        explanation="Recorre del índice 0 al 3."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int v[5] = {0,1,2,3,4};\nfor (int i=4;i&gt;=0;i--) cout &lt;&lt; v[i];</code></pre>",
        options=["01234", "43210", "Error de compilación", "12340"],
        answer="43210",
        explanation="Recorre en orden inverso del 4 al 0."
    ),

    Exercise(
        type_="test",
        question="Para leer 5 enteros en un array v de tamaño 5 desde cin, ¿qué patrón es correcto?",
        options=[
            "for (int i=1;i&lt;=5;i++) cin &gt;&gt; v[i];",
            "for (int i=0;i&lt;5;i++) cin &gt;&gt; v[i];",
            "for (int i=0;i&lt;=5;i++) cin &gt;&gt; v[i];",
            "for (int i=0;i&lt;4;i++) cin &gt;&gt; v[i];"
        ],
        answer="for (int i=0;i&lt;5;i++) cin &gt;&gt; v[i];",
        explanation="Índices válidos: 0..4."
    ),

    Exercise(
        type_="test",
        question="¿Valor de suma?\n<pre><code>int v[3]={2,4,6};\nint suma=0;\nfor(int i=0;i&lt;3;i++) suma+=v[i];</code></pre>",
        options=["6", "10", "12", "0"],
        answer="12",
        explanation="2+4+6=12."
    ),

    Exercise(
        type_="test",
        question="¿Resultado?\n<pre><code>int v[5]={1,3,5,7,9};\nint pares=0;\nfor(int i=0;i&lt;5;i++) if(v[i]%2==0) pares++;\ncout &lt;&lt; pares;</code></pre>",
        options=["0", "2", "5", "Error"],
        answer="0",
        explanation="Todos son impares."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int v[4]={-2,7,0,7};\nint mx=v[0];\nfor(int i=1;i&lt;4;i++) if(v[i]&gt;mx) mx=v[i];\ncout &lt;&lt; mx;</code></pre>",
        options=["-2", "0", "7", "Error"],
        answer="7",
        explanation="El máximo es 7."
    ),

    Exercise(
        type_="test",
        question="Para encontrar la posición del primer 0 en v[5], ¿qué condición es correcta?",
        options=[
            "if (v[i] = 0) pos = i;",
            "if (v[i] == 0) pos = i;",
            "if (v[i] := 0) pos = i;",
            "if (v[i] != 0) pos = i;"
        ],
        answer="if (v[i] == 0) pos = i;",
        explanation="Atención al operador de comparación <code>==</code>."
    ),

    Exercise(
        type_="test",
        question="En una búsqueda lineal típica, al encontrar el elemento se suele...",
        options=[
            "Seguir hasta el final por si hay más",
            "Salir del bucle si solo interesa la primera ocurrencia",
            "Reiniciar el índice a 0",
            "Duplicar el tamaño del array"
        ],
        answer="Salir del bucle si solo interesa la primera ocurrencia",
        explanation="Optimiza el tiempo si no necesitas más apariciones."
    ),

    Exercise(
        type_="test",
        question="Al pasar un array a una función como <code>void f(int v[])</code>, dentro de la función <code>v</code> se comporta como...",
        options=[
            "Una copia independiente del array",
            "Un puntero al primer elemento del array original",
            "Una referencia constante",
            "Un vector auto-redimensionable"
        ],
        answer="Un puntero al primer elemento del array original",
        explanation="Los arrays decaen a punteros; hay que pasar también el tamaño."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>void setCeros(int v[], int n){\n  for(int i=0;i&lt;n;i++) v[i]=0;\n}\nint main(){ int a[3]={1,2,3}; setCeros(a,3); cout &lt;&lt; a[0] &lt;&lt; a[1] &lt;&lt; a[2]; }</code></pre>",
        options=["123", "000", "111", "Error"],
        answer="000",
        explanation="Se modifica el array original a través del puntero."
    ),

    Exercise(
        type_="test",
        question="¿Qué está mal en este bucle sobre v[5]?\n<pre><code>for(int i=0;i&lt;=5;i++) cout &lt;&lt; v[i];</code></pre>",
        options=[
            "Nada",
            "Se desborda: i toma el valor 5 e intenta acceder v[5]",
            "Falta el incremento",
            "La condición debería ser i==5"
        ],
        answer="Se desborda: i toma el valor 5 e intenta acceder v[5]",
        explanation="El último índice válido es 4."
    ),

    Exercise(
        type_="test",
        question="Se desea invertir un array <code>v</code> de tamaño <code>n</code>. ¿Qué intercambio es correcto en un bucle <code>for (int i=0;i&lt;n/2;i++)</code>?",
        options=[
            "swap(v[i], v[i+1])",
            "swap(v[i], v[n-1-i])",
            "swap(v[i], v[n-i])",
            "swap(v[i+1], v[n-i])"
        ],
        answer="swap(v[i], v[n-1-i])",
        explanation="Intercambia extremos simétricos."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[5]={1,2,3,4,5};\nint s=0;\nfor(int i=0;i&lt;5;i+=2) s+=v[i];\ncout &lt;&lt; s;</code></pre>",
        options=["6", "8", "9", "15"],
        answer="9",
        explanation="Suma posiciones 0,2,4: 1+3+5=9."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[4]={2,2,2,2};\nfor(int i=1;i&lt;4;i++) v[i]+=v[i-1];\ncout &lt;&lt; v[3];</code></pre>",
        options=["2", "4", "6", "8"],
        answer="8",
        explanation="v[1]=4, v[2]=6, v[3]=8."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[4]={1,4,9,16};\nint c=0;\nfor(int i=0;i&lt;4;i++) if(v[i]&gt;=i*i) c++;\ncout &lt;&lt; c;</code></pre>",
        options=["2", "3", "4", "0"],
        answer="4",
        explanation="Para i=0..3 se cumple v[i] >= i*i en todos los casos."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[5]={5,4,3,2,1};\nint pos=0;\nfor(int i=1;i&lt;5;i++) if(v[i]&lt;v[pos]) pos=i;\ncout &lt;&lt; pos;</code></pre>",
        options=["0", "1", "3", "4"],
        answer="4",
        explanation="El mínimo (1) está en la posición 4."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[6]={1,2,2,3,3,3};\nint c=0;\nfor(int i=0;i&lt;6;i++) if(v[i]==3) c++;\ncout &lt;&lt; c;</code></pre>",
        options=["1", "2", "3", "6"],
        answer="3",
        explanation="Hay tres 3."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este código?\n<pre><code>int v[6]={1,4,2,4,2,1};\nbool sim=true;\nfor(int i=0;i&lt;6/2;i++) if(v[i]!=v[5-i]) sim=false;\ncout &lt;&lt; sim;</code></pre>",
        options=[
            "Comprueba si el array está ordenado",
            "Comprueba si el array es palíndromo (simétrico)",
            "Cuenta los pares",
            "Calcula máxima diferencia"
        ],
        answer="Comprueba si el array es palíndromo (simétrico)",
        explanation="Compara extremos opuestos."
    ),

    Exercise(
        type_="test",
        question="Para escribir una función que lea un array y devuelva cuántos elementos válidos se han leído, lo habitual es...",
        options=[
            "Devolver el array",
            "Pasar el array y devolver el tamaño leído como valor de retorno",
            "Pasar el array como const",
            "Modificar la longitud con realloc"
        ],
        answer="Pasar el array y devolver el tamaño leído como valor de retorno",
        explanation="Los arrays nativos no llevan su tamaño; hay que gestionarlo aparte."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[7]={-1,0,2,-3,4,-5,6};\nint positivos=0;\nfor(int i=0;i&lt;7;i++) if(v[i]&gt;0) positivos++;\ncout &lt;&lt; positivos;</code></pre>",
        options=["2", "3", "4", "5"],
        answer="3",
        explanation="Positivos: 2,4,6."
    ),

    Exercise(
        type_="test",
        question="¿Qué está mal?\n<pre><code>if (v[i] = 0) cout &lt;&lt; \"cero\";</code></pre>",
        options=[
            "Nada",
            "Se usa asignación (=) en lugar de comparación (==)",
            "Falta un ;",
            "Se debe usar v[i]==true"
        ],
        answer="Se usa asignación (=) en lugar de comparación (==)",
        explanation="Esto sobrescribe v[i] con 0 y la condición será falsa."
    ),

    Exercise(
        type_="test",
        question="Para rotar un array a la derecha una posición (último elemento pasa a la posición 0), ¿qué paso NO es necesario?",
        options=[
            "Guardar el último en una variable temporal",
            "Mover los elementos de derecha a izquierda",
            "Poner a cero todos los elementos al final",
            "Colocar el temporal en v[0]"
        ],
        answer="Poner a cero todos los elementos al final",
        explanation="No se ponen a cero; solo se recolocan."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[4]={1,2,3,4};\nint pref[4];\npref[0]=v[0];\nfor(int i=1;i&lt;4;i++) pref[i]=pref[i-1]+v[i];\ncout &lt;&lt; pref[3];</code></pre>",
        options=["4", "6", "9", "10"],
        answer="10",
        explanation="Suma acumulada: 1,3,6,10."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[5]={2,2,2,2,3};\nbool todosIguales=true;\nfor(int i=1;i&lt;5;i++) if(v[i]!=v[0]) { todosIguales=false; break; }\ncout &lt;&lt; todosIguales;</code></pre>",
        options=["0", "1", "2", "3"],
        answer="0",
        explanation="El último elemento es 3, distinto de 2 ⇒ false (0)."
    ),

    Exercise(
        type_="test",
        question="Se desea intercambiar las posiciones del mínimo y el máximo en v[ n ]. ¿Qué par de índices hay que hallar antes del swap?",
        options=[
            "El primero y el último",
            "La posición del mínimo y la del máximo",
            "La posición del mínimo y el tamaño",
            "El tamaño y la posición central"
        ],
        answer="La posición del mínimo y la del máximo",
        explanation="Con esos índices se puede hacer <code>swap(v[posMin], v[posMax])</code>."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este código?\n<pre><code>int a[3]={1,2,3};\nint b[3];\nfor(int i=0;i&lt;3;i++) b[i]=a[i];\ncout &lt;&lt; b[2];</code></pre>",
        options=["Copia en sentido inverso", "Copia elemento a elemento y muestra 3", "No compila", "b queda con basura"],
        answer="Copia elemento a elemento y muestra 3",
        explanation="Copia simple con bucle for."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[6]={1,1,2,2,2,3};\nint cambios=0;\nfor(int i=1;i&lt;6;i++) if(v[i]!=v[i-1]) cambios++;\ncout &lt;&lt; cambios;</code></pre>",
        options=["1", "2", "3", "4"],
        answer="2",
        explanation="Transiciones 1→2 y 2→3."
    ),

    Exercise(
        type_="test",
        question="Los arrays nativos en C++ conocen su tamaño en tiempo de ejecución (puedo preguntar v.size()).",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="El tamaño no se almacena con el array. Pista: <code>sizeof(v)/sizeof(v[0])</code> solo funciona en el mismo ámbito."
    ),

    Exercise(
        type_="test",
        question="Un bucle <code>for</code> que recorra un array de tamaño n en C++ suele usar índices de 0 a n-1.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Convención estándar en arrays."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[6]={1,2,3,4,5,6};\nint s=0;\nfor(int i=0;i&lt;6;i++) s += (i%2==0? v[i] : -v[i]);\ncout &lt;&lt; s;</code></pre>",
        options=["-3", "3", "0", "1"],
        answer="-3",
        explanation="(1-2)+(3-4)+(5-6) = -3."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace?\n<pre><code>bool asc=true;\nfor(int i=1;i&lt;n;i++) if(v[i]&lt;v[i-1]) { asc=false; break; }</code></pre>",
        options=[
            "Comprueba si v está ordenado no decreciente (ascendente)",
            "Comprueba si v es palíndromo",
            "Cuenta los pares",
            "Invierte v"
        ],
        answer="Comprueba si v está ordenado no decreciente (ascendente)",
        explanation="Si se detecta un descenso, no está ordenado."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre?\n<pre><code>int v[5]={1,2,3,4,5};\nfor(int i=0;i&lt;=5;i++) cout &lt;&lt; v[i];</code></pre>",
        options=["Imprime 12345", "Error de compilación", "Accede fuera de rango", "Imprime basura al final"],
        answer="Accede fuera de rango",
        explanation="El bucle llega a i=5, pero el último índice válido es 4."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[3]={1,2,3};\nfor(int i=1;i&lt;3;i++) v[i]+=v[i-1];\ncout &lt;&lt; v[2];</code></pre>",
        options=["3", "5", "6", "7"],
        answer="6",
        explanation="v[1]=2+1=3; v[2]=3+3=6."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[4]={10,20,30,40};\nint i=3;\ncout &lt;&lt; v[i--];\ncout &lt;&lt; v[i];</code></pre>",
        options=["4040", "4030", "3030", "3040"],
        answer="4030",
        explanation="Primero usa i=3 (imprime 40), luego i se decrementa a 2 e imprime v[2]=30."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[5]={0,1,0,1,0};\nint c=0;\nfor(int i=0;i&lt;5;i++) if(v[i]) c+=v[i];\ncout &lt;&lt; c;</code></pre>",
        options=["0", "1", "2", "5"],
        answer="2",
        explanation="Solo suma posiciones donde v[i]=1 (dos veces)."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[4]={1,2,3,4};\nint s=0;\nfor(int i=0;i&lt;4;i++) s+=v[i]+v[3-i];\ncout &lt;&lt; s;</code></pre>",
        options=["20", "16", "10", "Error"],
        answer="20",
        explanation="Cada par se suma dos veces: (1+4)+(2+3)+(3+2)+(4+1)=20."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int v[5]={5,4,3,2,1};\nint s=0;\nfor(int i=0;i&lt;5;i++){\n  if(v[i]&lt;3) break;\n  s+=v[i];\n}\ncout &lt;&lt; s;</code></pre>",
        options=["15", "12", "9", "0"],
        answer="12",
        explanation="Suma 5+4+3=12, al llegar a 2 (<3) se rompe el bucle."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre aquí?\n<pre><code>int v[3]={1,0,2};\nfor(int i=0;i&lt;3;i++) if(v[i]=0) cout&lt;&lt;\"*\";</code></pre>",
        options=["Imprime **", "No imprime nada", "Error de compilación", "Imprime basura"],
        answer="No imprime nada",
        explanation="Se está asignando 0, la condición siempre es falsa."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int v[4]={1,2,3,4};\nfor(int i=0,j=3;i&lt;4;i++,j--) cout &lt;&lt; v[i]+v[j];</code></pre>",
        options=["58", "4444", "1463", "48"],
        answer="4444",
        explanation="Pares: v[0]+v[3]=5, v[1]+v[2]=5, v[2]+v[1]=5, v[3]+v[0]=5 ⇒ imprime 5555."
    ),

    Exercise(
        type_="test",
        question="¿Salida?\n<pre><code>int v[3]={1,2,3};\nint i=0;\ncout &lt;&lt; v[i++] &lt;&lt; v[++i];</code></pre>",
        options=["12", "13", "23", "Error"],
        answer="13",
        explanation="v[i++] usa i=0 ⇒ 1, después i=1. Luego ++i=2 ⇒ v[2]=3."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>int v[5]={7,4,6,2,9};\nint pos=0;\nfor(int i=1;i&lt;5;i++) if(v[i]&lt;v[pos]) pos=i;\ncout &lt;&lt; pos;</code></pre>",
        options=["0", "1", "3", "4"],
        answer="3",
        explanation="El valor mínimo es 2, en la posición 3."
    ),
]

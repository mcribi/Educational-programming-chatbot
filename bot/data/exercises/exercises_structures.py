from src.exercise import Exercise

exercises_structures = [

    Exercise(
        type_="test",
        question="¿Qué es una estructura (struct) en C++?",
        options=[
            "Un tipo de bucle",
            "Un conjunto de variables agrupadas bajo un mismo nombre",
            "Un tipo de función especial",
            "Un archivo externo"
        ],
        answer="Un conjunto de variables agrupadas bajo un mismo nombre",
        explanation="Una estructura permite agrupar datos relacionados bajo un mismo identificador."
    ),

    Exercise(
        type_="test",
        question="¿Qué palabra clave se utiliza para definir una estructura en C++?",
        options=["class", "struct", "typedef", "union"],
        answer="struct",
        explanation="La palabra clave <code>struct</code> se usa para definir una estructura."
    ),

    Exercise(
        type_="test",
        question="Si definimos <pre><code>struct Persona { string nombre; int edad; };</code></pre> ¿cómo accedemos a la edad de una variable p de tipo Persona?",
        options=["p->edad", "p.edad", "edad.p", "Persona.edad"],
        answer="p.edad",
        explanation="Con el operador punto accedemos a los miembros de una estructura."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime este código?\n<pre><code>struct Punto { int x; int y; };\nint main(){ Punto p = {2, 5}; cout &lt;&lt; p.x + p.y; }</code></pre>",
        options=["2", "5", "7", "Error de compilación"],
        answer="7",
        explanation="Se inicializa con x=2, y=5, y se imprime la suma 2+5=7."
    ),

    Exercise(
        type_="test",
        question="¿Qué significa la instrucción <code>typedef struct { int x; int y; } Punto;</code>?",
        options=[
            "Crea un sinónimo de int",
            "Crea una estructura anónima y la llama Punto",
            "Crea un bucle de tipo struct",
            "Declara una clase llamada Punto"
        ],
        answer="Crea una estructura anónima y la llama Punto",
        explanation="Con typedef podemos dar un nombre corto a una estructura."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre si pasamos una estructura como parámetro por valor a una función?",
        options=[
            "La función trabaja con una copia de la estructura",
            "La función modifica directamente el original",
            "El compilador genera un error",
            "No se puede pasar estructuras a funciones"
        ],
        answer="La función trabaja con una copia de la estructura",
        explanation="Al pasarse por valor se crea una copia; para modificar el original se usa referencia o puntero."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>struct P { int x; };\nvoid cambia(P p){ p.x = 10; }\nint main(){ P a={5}; cambia(a); cout &lt;&lt; a.x; }</code></pre>",
        options=["5", "10", "Error de compilación", "Nada"],
        answer="5",
        explanation="Se pasa por valor, los cambios no afectan al original."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>struct P { int x; };\nvoid cambia(P &amp;p){ p.x = 10; }\nint main(){ P a={5}; cambia(a); cout &lt;&lt; a.x; }</code></pre>",
        options=["5", "10", "Error", "Nada"],
        answer="10",
        explanation="El paso por referencia permite modificar la variable original."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>struct Fecha { int dia; int mes; };\nstruct Persona { string nombre; Fecha f; };\nint main(){ Persona p = {\"Ana\", {1, 9}}; cout &lt;&lt; p.f.mes; }</code></pre>",
        options=["1", "9", "Error", "Ana"],
        answer="9",
        explanation="Se accede al miembro f.mes de la estructura anidada."
    ),

    Exercise(
        type_="test",
        question="Una estructura puede contener variables de distintos tipos de datos.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Es precisamente una de las ventajas de las estructuras."
    ),

    Exercise(
        type_="test",
        question="Los miembros de una estructura se acceden con el operador punto (.) cuando se trata de una variable, y con -> cuando se usa un puntero.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="El acceso depende de si trabajamos con variables normales o punteros."
    ),

    Exercise(
        type_="test",
        question="Una estructura puede contener otra estructura en su definición.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Esto se llama anidamiento de estructuras."
    ),
    
    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>struct P { int x; };\n"
            "void inc(P p){ p.x++; }\n"
            "int main(){ P a{3}; inc(a); cout &lt;&lt; a.x; }</code></pre>"
        ),
        options=["3", "4", "0", "Error de compilación"],
        answer="3",
        explanation="Se pasa por valor (copia). El a original no cambia."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>struct P { int x; };\n"
            "void inc(P &amp;p){ p.x++; }\n"
            "int main(){ P a{3}; inc(a); cout &lt;&lt; a.x; }</code></pre>"
        ),
        options=["3", "4", "0", "Error de compilación"],
        answer="4",
        explanation="La referencia permite modificar el original."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>struct P { int x; };\n"
            "int main(){ P a{1}; P* ptr = &amp;a; ptr-&gt;x = 9; cout &lt;&lt; a.x; }</code></pre>"
        ),
        options=["1", "9", "0", "Error de compilación"],
        answer="9",
        explanation="Con punteros se accede con <code>-&gt;</code> y se modifica el original."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida?\n"
            "<pre><code>struct V { int x; };\n"
            "struct W { V v; };\n"
            "int main(){ W w{{2}}; cout &lt;&lt; w.v.x; }</code></pre>"
        ),
        options=["0", "1", "2", "Error"],
        answer="2",
        explanation="Inicialización anidada: w.v.x = 2."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>struct P { int x; };\n"
            "P make(int v){ return P{v*2}; }\n"
            "int main(){ cout &lt;&lt; make(3).x; }</code></pre>"
        ),
        options=["3", "6", "9", "Error"],
        answer="6",
        explanation="La función retorna un P con x = 3*2."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Resultado?\n"
            "<pre><code>struct P{ int x; };\n"
            "int main(){ P a[3]={{1},{2},{3}}; int s=0; for(int i=0;i&lt;3;i++) s+=a[i].x; cout &lt;&lt; s; }</code></pre>"
        ),
        options=["3", "5", "6", "9"],
        answer="6",
        explanation="1+2+3 = 6."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida?\n"
            "<pre><code>struct P{ int x; };\n"
            "void set(P* p){ p-&gt;x = 5; }\n"
            "int main(){ P a{1}; set(&amp;a); cout &lt;&lt; a.x; }</code></pre>"
        ),
        options=["1", "5", "0", "Error"],
        answer="5",
        explanation="Se modifica el miembro a través del puntero."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Compila y qué pasaría?\n"
            "<pre><code>struct P{ int x; };\n"
            "void f(const P&amp; p){ /* p.x = 10; */ cout &lt;&lt; p.x; }\n"
            "int main(){ P a{7}; f(a); }</code></pre>"
        ),
        options=["No compila por la línea comentada", "Compila e imprime 7", "No compila por el const", "Se imprime 10"],
        answer="Compila e imprime 7",
        explanation="La asignación está comentada. Con const-ref no podríamos modificar; imprimir sí."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>struct Persona{ string nombre; int edad; };\n"
            "int main(){ Persona p{}; cout &lt;&lt; p.edad; }</code></pre>"
        ),
        options=["Indeterminado", "0", "1", "Error"],
        answer="0",
        explanation="Con <code>{}</code>, los miembros se inicializan a valor por defecto: int→0, string→vacía."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida?\n"
            "<pre><code>struct P{ int x; int y; };\n"
            "int main(){ P a{1,2}; P b; b=a; cout &lt;&lt; b.x &lt;&lt; b.y; }</code></pre>"
        ),
        options=["12", "21", "11", "22"],
        answer="12",
        explanation="La asignación copia miembro a miembro: b = a ⇒ (1,2)."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>struct Fecha{ int dia; int mes; };\n"
            "struct Persona{ string nombre; Fecha f; };\n"
            "int main(){ Persona per = {\"Ana\", {3, 11}}; Persona* p=&amp;per; cout &lt;&lt; p-&gt;f.mes; }</code></pre>"
        ),
        options=["3", "11", "Error", "Ana"],
        answer="11",
        explanation="Con puntero: <code>p-&gt;f.mes</code> accede al miembro anidado."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Salida exacta?\n"
            "<pre><code>struct R{ int a; int b; };\n"
            "R dup(int x){ return R{x, x*2}; }\n"
            "int main(){ cout &lt;&lt; dup(4).a &lt;&lt; \":\" &lt;&lt; dup(4).b; }</code></pre>"
        ),
        options=["4:8", "8:4", "4:4", "8:8"],
        answer="4:8",
        explanation="dup(4) produce {4,8}. Se imprimen a y b con ':' entre medias."
    ),

    Exercise(
        type_="test",
        question=(
            "¿Qué imprime?\n"
            "<pre><code>struct P{ int x; };\n"
            "int main(){ P v[2]={{1},{5}}; P&amp; r = v[1]; r.x += 2; cout &lt;&lt; v[1].x; }</code></pre>"
        ),
        options=["1", "3", "5", "7"],
        answer="7",
        explanation="r es una referencia al segundo elemento: 5+2 = 7."
    ),

    Exercise(
        type_="test",
        question=(
            "Razonar llamadas y salida:\n"
            "<pre><code>struct P{ int x; };\n"
            "int show(P p){ cout &lt;&lt; p.x; return p.x; }\n"
            "P make(int k){ return P{k+1}; }\n"
            "int main(){ cout &lt;&lt; show( make(2) ); }</code></pre>"
        ),
        options=["23", "32", "3", "2"],
        answer="33",
        explanation="make(2) crea {3}; show imprime 3 y retorna 3; luego main imprime ese 3 ⇒ '33'."
    ),

]

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

    Exercise(
        type_="code",
        question="Define un struct Persona { string nombre; long long edad; }. Lee el nombre (línea completa) y la edad, y muestra: 'Edad de <nombre>: <edad>'.",
        tests_json={
            "sample": [{"input": "Ada Lovelace\n36\n", "output": "Edad de Ada Lovelace: 36"}],
            "hidden": [
                {"input": "Alan Turing\n41\n", "output": "Edad de Alan Turing: 41"},
                {"input": "Grace Hopper\n85\n", "output": "Edad de Grace Hopper: 85"}
            ]
        },
        hint="Primero getline para capturar el nombre con espacios y después lee la edad con cin. La salida es una sola línea (el checker tolera un salto final si lo pones).",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'struct Persona{ string nombre; long long edad; };\n'
            'int main(){ Persona p; getline(cin,p.nombre); cin>>p.edad; cout<<\"Edad de \"<<p.nombre<<\": \"<<p.edad; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Define struct Punto { long long x; long long y; }. Lee x e y y muestra 'Punto(x,y)'.",
        tests_json={
            "sample": [{"input": "2 5\n", "output": "Punto(2,5)"}],
            "hidden": [
                {"input": "0 0\n", "output": "Punto(0,0)"},
                {"input": "-3 10\n", "output": "Punto(-3,10)"}
            ]
        },
        hint="Solo formatea exactamente como 'Punto(x,y)' (sin espacios). Una única línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Punto{ long long x,y; };\n'
            'int main(){ Punto p; cin>>p.x>>p.y; cout<<\"Punto(\"<<p.x<<\",\"<<p.y<<\")\"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Con struct Punto { long long x; long long y; }, lee dos puntos y muestra su distancia Manhattan |x1-x2|+|y1-y2|.",
        tests_json={
            "sample": [{"input": "2 5\n-1 1\n", "output": "7"}],
            "hidden": [
                {"input": "0 0\n0 0\n", "output": "0"},
                {"input": "-3 10\n5 -2\n", "output": "20"}
            ]
        },
        hint="Implementa una función AbsLL si quieres evitar librerías: abs(x) = x<0 ? -x : x.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Punto{ long long x,y; };\n'
            'long long AbsLL(long long v){ return v<0? -v: v; }\n'
            'int main(){ Punto a,b; cin>>a.x>>a.y>>b.x>>b.y; long long d=AbsLL(a.x-b.x)+AbsLL(a.y-b.y); cout<<d; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Define struct Rect { long long ancho; long long alto; }. Lee ancho y alto y muestra el área (ancho*alto).",
        tests_json={
            "sample": [{"input": "3 4\n", "output": "12"}],
            "hidden": [
                {"input": "7 1\n", "output": "7"},
                {"input": "0 5\n", "output": "0"}
            ]
        },
        hint="Operación directa con enteros grandes.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Rect{ long long ancho,alto; };\n'
            'int main(){ Rect r; cin>>r.ancho>>r.alto; cout<<r.ancho*r.alto; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Define struct Fecha { long long d; long long m; long long a; }. Lee día, mes y año, y muestra 'd/m/a'.",
        tests_json={
            "sample": [{"input": "1 9 2025\n", "output": "1/9/2025"}],
            "hidden": [
                {"input": "31 12 1999\n", "output": "31/12/1999"},
                {"input": "10 1 2000\n", "output": "10/1/2000"}
            ]
        },
        hint="Imprime sin ceros a la izquierda (salida simple con '/').",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Fecha{ long long d,m,a; };\n'
            'int main(){ Fecha f; cin>>f.d>>f.m>>f.a; cout<<f.d<<\"/\"<<f.m<<\"/\"<<f.a; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Con struct Persona { string nombre; long long edad; }, lee nombre (línea) y edad. Implementa void Cumple(Persona& p) que incremente su edad. Muestra la nueva edad.",
        tests_json={
            "sample": [{"input": "Ana\n29\n", "output": "30"}],
            "hidden": [
                {"input": "Luis\n0\n", "output": "1"},
                {"input": "Sofía\n99\n", "output": "100"}
            ]
        },
        hint="Primero getline para el nombre; luego lee la edad. Llama a Cumple(p) y muestra p.edad.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'struct Persona{ string nombre; long long edad; };\n'
            'void Cumple(Persona& p){ p.edad++; }\n'
            'int main(){ Persona p; getline(cin,p.nombre); cin>>p.edad; Cumple(p); cout<<p.edad; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Con struct Punto { long long x; long long y; }, lee dos puntos y cámbialos de sitio con void Swap(Punto& a, Punto& b). Muestra 'x1 y1 x2 y2' tras el intercambio.",
        tests_json={
            "sample": [{"input": "1 2  7 9\n", "output": "7 9 1 2"}],
            "hidden": [
                {"input": "0 0  0 0\n", "output": "0 0 0 0"},
                {"input": "-3 10  5 -2\n", "output": "5 -2 -3 10"}
            ]
        },
        hint="Usa una variable temporal en Swap. Imprime en una sola línea separando con espacios.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Punto{ long long x,y; };\n'
            'void Swap(Punto& a,Punto& b){ Punto t=a; a=b; b=t; }\n'
            'int main(){ Punto a,b; cin>>a.x>>a.y>>b.x>>b.y; Swap(a,b); cout<<a.x<<\" \"<<a.y<<\" \"<<b.x<<\" \"<<b.y; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="struct Producto { string nombre; long long precio; }. Lee 3 productos (nombre SIN espacios y precio). Muestra 'Mas barato: <nombre> <precio>'.",
        tests_json={
            "sample": [{"input": "pan 120\nleche 95\nhuevos 300\n", "output": "Mas barato: leche 95"}],
            "hidden": [
                {"input": "a 10\nb 10\nc 11\n", "output": "Mas barato: a 10"},
                {"input": "movil 399\nfunda 15\ncable 9\n", "output": "Mas barato: cable 9"}
            ]
        },
        hint="Si hay empate, elige el primero que aparece. Una sola línea.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'struct Producto{ string nombre; long long precio; };\n'
            'int main(){ Producto best; cin>>best.nombre>>best.precio; for(int i=1;i<3;i++){ Producto p; cin>>p.nombre>>p.precio; if(p.precio<best.precio) best=p; } cout<<\"Mas barato: \"<<best.nombre<<\" \"<<best.precio; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="struct Frac { long long num; long long den; }. Lee num y den (den≠0), reduce la fracción dividiendo por su MCD y muestra 'num/den' reducida (signo solo en el numerador).",
        tests_json={
            "sample": [{"input": "6 8\n", "output": "3/4"}],
            "hidden": [
                {"input": "-4 6\n", "output": "-2/3"},
                {"input": "10 -20\n", "output": "-1/2"}
            ]
        },
        hint="Usa Euclides para el MCD. Normaliza el signo para que el denominador sea positivo.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Frac{ long long num, den; };\n'
            'long long AbsLL(long long x){ return x<0? -x: x; }\n'
            'long long MCD(long long a,long long b){ a=AbsLL(a); b=AbsLL(b); while(b){ long long r=a%b; a=b; b=r; } return a; }\n'
            'int main(){ Frac f; cin>>f.num>>f.den; long long g=MCD(f.num,f.den); f.num/=g; f.den/=g; if(f.den<0){ f.den=-f.den; f.num=-f.num; } cout<<f.num<<\"/\"<<f.den; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="struct Tiempo { long long h,m,s; }. Lee h m s (con m o s posiblemente >=60 o <0) y normaliza para imprimir 'h m s' con 0 ≤ m,s < 60.",
        tests_json={
            "sample": [{"input": "1 120 75\n", "output": "2 1 15"}],
            "hidden": [
                {"input": "0 59 61\n", "output": "1 0 1"},
                {"input": "2 -1 0\n", "output": "1 59 0"}
            ]
        },
        hint="Ajusta segundos a minutos y minutos a horas (puede haber negativos). Haz las transferencias con divisiones y módulos cuidando los signos.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Tiempo{ long long h,m,s; };\n'
            'int main(){ Tiempo t; cin>>t.h>>t.m>>t.s;\n'
            '  // Normalizar segundos\n'
            '  t.m += t.s/60; t.s %= 60; if(t.s<0){ t.s+=60; t.m--; }\n'
            '  // Normalizar minutos\n'
            '  t.h += t.m/60; t.m %= 60; if(t.m<0){ t.m+=60; t.h--; }\n'
            '  cout<<t.h<<\" \"<<t.m<<\" \"<<t.s; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Con Punto { long long x; long long y; }, lee x y dx dy. Aplica el desplazamiento (x+=dx, y+=dy) y muestra 'x y'.",
        tests_json={
            "sample": [{"input": "3 4  1 -2\n", "output": "4 2"}],
            "hidden": [
                {"input": "0 0  0 0\n", "output": "0 0"},
                {"input": "-5 7  5 3\n", "output": "0 10"}
            ]
        },
        hint="Puedes implementar void Mueve(Punto& p, long long dx, long long dy).",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'struct Punto{ long long x,y; };\n'
            'void Mueve(Punto& p, long long dx, long long dy){ p.x+=dx; p.y+=dy; }\n'
            'int main(){ Punto p; long long dx,dy; cin>>p.x>>p.y>>dx>>dy; Mueve(p,dx,dy); cout<<p.x<<\" \"<<p.y; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Crea Fecha { long long d,m,a; } y Persona { string nombre; Fecha nac; }. Lee nombre (línea), luego d m a. Muestra '<nombre> (<d>/<m>/<a>)'.",
        tests_json={
            "sample": [{"input": "Ana María\n1 9 2000\n", "output": "Ana María (1/9/2000)"}],
            "hidden": [
                {"input": "Alan\n23 6 1912\n", "output": "Alan (23/6/1912)"},
                {"input": "Ada Lovelace\n10 12 1815\n", "output": "Ada Lovelace (10/12/1815)"}
            ]
        },
        hint="Lee el nombre con getline y después la fecha con cin. Una sola línea de salida.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'struct Fecha{ long long d,m,a; };\n'
            'struct Persona{ string nombre; Fecha nac; };\n'
            'int main(){ Persona p; getline(cin,p.nombre); cin>>p.nac.d>>p.nac.m>>p.nac.a; cout<<p.nombre<<\" (\"<<p.nac.d<<\"/\"<<p.nac.m<<\"/\"<<p.nac.a<<\")\"; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee N y luego N personas (nombre SIN espacios y edad). Muestra cuántas son mayores o iguales a 18.",
        tests_json={
            "sample": [{"input": "3\nana 17\nluis 18\npepe 20\n", "output": "2"}],
            "hidden": [
                {"input": "1\nsolo 17\n", "output": "0"},
                {"input": "4\nx 18\ny 18\nz 17\nw 30\n", "output": "3"}
            ]
        },
        hint="Define struct Persona { string nombre; long long edad; } y ve contando sin necesidad de guardar todas.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'struct Persona{ string nombre; long long edad; };\n'
            'int main(){ int N; if(!(cin>>N)) return 0; int cnt=0; for(int i=0;i<N;i++){ Persona p; cin>>p.nombre>>p.edad; if(p.edad>=18) cnt++; } cout<<cnt; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Lee 3 personas (nombre SIN espacios y edad) y ordénalas por edad ascendente. Muestra solo los nombres en orden: 'n1 n2 n3'.",
        tests_json={
            "sample": [{"input": "c 30\na 10\nb 20\n", "output": "a b c"}],
            "hidden": [
                {"input": "ana 5\nana2 5\nana3 6\n", "output": "ana ana2 ana3"},
                {"input": "x 100\ny 1\nz 100\n", "output": "y x z"}
            ]
        },
        hint="struct Persona { string nombre; long long edad; }. Haz swaps simples (if) para ordenar 3 elementos. Establece criterio estable en empates (mantén el orden de entrada).",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'struct Persona{ string nombre; long long edad; };\n'
            'void swapP(Persona& a, Persona& b){ Persona t=a; a=b; b=t; }\n'
            'bool menor(const Persona& a,const Persona& b){ if(a.edad!=b.edad) return a.edad<b.edad; return false; }\n'
            'int main(){ Persona a,b,c; cin>>a.nombre>>a.edad>>b.nombre>>b.edad>>c.nombre>>c.edad; \n'
            '  if(!menor(a,b)) swapP(a,b); if(!menor(b,c)) swapP(b,c); if(!menor(a,b)) swapP(a,b);\n'
            '  cout<<a.nombre<<\" \"<<b.nombre<<\" \"<<c.nombre; }\n'
        ),
        checker="ignore_trailing_whitespace",
        time_limit_ms=1000, memory_limit_mb=64,
    ),

]

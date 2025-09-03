from src.exercise import Exercise

exercises_class = [

    Exercise(
        type_="test",
        question="¿Qué es una clase en C++?",
        options=[
            "Un tipo especial de bucle",
            "Una plantilla que define atributos y métodos de objetos",
            "Una estructura reservada solo para funciones",
            "Un archivo externo de cabecera"
        ],
        answer="Una plantilla que define atributos y métodos de objetos",
        explanation="La clase es un modelo que agrupa variables (atributos) y funciones (métodos)."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la diferencia principal entre struct y class en C++?",
        options=[
            "struct no existe en C++",
            "En struct los miembros son públicos por defecto, en class son privados",
            "class no puede tener métodos, struct sí",
            "Son idénticos en todo"
        ],
        answer="En struct los miembros son públicos por defecto, en class son privados",
        explanation="Esa es la diferencia por defecto; ambos pueden usarse casi igual."
    ),

    Exercise(
        type_="test",
        question="¿Qué palabra clave se usa para crear un objeto de una clase?",
        options=["make", "object", "new", "El nombre de la clase como tipo"],
        answer="El nombre de la clase como tipo",
        explanation="Ejemplo: <code>MiClase obj;</code> crea un objeto de tipo MiClase."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime este código?\n<pre><code>class Punto {\n  public: int x;\n};\nint main(){ Punto p; p.x=5; cout &lt;&lt; p.x; }</code></pre>",
        options=["0", "5", "Error", "Basura"],
        answer="5",
        explanation="Se crea un objeto, se asigna x=5 y luego se imprime."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre si un atributo es private?",
        options=[
            "Solo puede ser accedido dentro de la clase",
            "Se accede siempre con ->",
            "Puede ser accedido libremente desde main",
            "Se inicializa siempre a 0"
        ],
        answer="Solo puede ser accedido dentro de la clase",
        explanation="La encapsulación impide acceso directo externo a miembros privados."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class Punto {\n  public:\n    int x;\n    int getDoble(){ return x*2; }\n};\nint main(){ Punto p; p.x=3; cout &lt;&lt; p.getDoble(); }</code></pre>",
        options=["3", "6", "9", "Error"],
        answer="6",
        explanation="Se llama al método getDoble() que devuelve 2*3=6."
    ),

    Exercise(
        type_="test",
        question="¿Qué es un constructor?",
        options=[
            "Una función normal con return",
            "Un método especial que inicializa objetos de la clase",
            "Un puntero a objeto",
            "Una librería estándar"
        ],
        answer="Un método especial que inicializa objetos de la clase",
        explanation="El constructor se llama automáticamente al crear un objeto."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class Punto{\n  public:\n    int x;\n    Punto(){ x=7; }\n};\nint main(){ Punto p; cout &lt;&lt; p.x; }</code></pre>",
        options=["0", "7", "Error", "Basura"],
        answer="7",
        explanation="El constructor asigna x=7 automáticamente."
    ),

    Exercise(
        type_="test",
        question="¿Para qué sirve el puntero this?",
        options=[
            "Apunta al objeto actual dentro de sus métodos",
            "Apunta siempre al primer objeto creado",
            "Es obligatorio en todas las funciones",
            "Sirve para acceder a atributos estáticos"
        ],
        answer="Apunta al objeto actual dentro de sus métodos",
        explanation="this se usa para distinguir el objeto que está ejecutando el método."
    ),

    Exercise(
        type_="test",
        question="¿Qué ventaja tiene declarar métodos como public y atributos como private?",
        options=[
            "Que el compilador genera menos código",
            "Que se garantiza el encapsulamiento y el control de acceso",
            "Que los objetos se crean más rápido",
            "No hay diferencia, es solo estilo"
        ],
        answer="Que se garantiza el encapsulamiento y el control de acceso",
        explanation="Es la práctica recomendada: ocultar atributos y exponer métodos controlados."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class Contador {\n  int valor;\n  public:\n    Contador(){ valor=0; }\n    void inc(){ valor++; }\n    int get(){ return valor; }\n};\nint main(){ Contador c; c.inc(); c.inc(); cout &lt;&lt; c.get(); }</code></pre>",
        options=["0", "1", "2", "Error"],
        answer="2",
        explanation="Se inicializa en 0 y luego se incrementa dos veces."
    ),

    Exercise(
        type_="test",
        question="Una clase puede tener varios constructores siempre que tengan distinta lista de parámetros.",
        options=["Verdadero", "Falso"],
        answer="Verdadero",
        explanation="Esto se llama sobrecarga de constructores."
    ),

    Exercise(
        type_="test",
        question="Un método private puede ser llamado desde main directamente.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Los métodos private solo pueden usarse dentro de la clase o amigos."
    ),

    Exercise(
        type_="test",
        question="Un objeto en C++ siempre se crea con new.",
        options=["Verdadero", "Falso"],
        answer="Falso",
        explanation="Se pueden crear en pila: <code>MiClase obj;</code> sin usar new."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class Punto {\n  int x;\npublic:\n  Punto(int v){ x=v; }\n  int get(){ return x; }\n};\nint main(){ Punto p(5); cout &lt;&lt; p.get(); }</code></pre>",
        options=["0", "5", "Error", "Basura"],
        answer="5",
        explanation="El constructor con parámetro inicializa x con 5."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class Punto {\n  int x;\npublic:\n  Punto(){ x=1; }\n  Punto(int v){ x=v; }\n  int get(){ return x; }\n};\nint main(){ Punto a; Punto b(7); cout &lt;&lt; a.get() &lt;&lt; b.get(); }</code></pre>",
        options=["17", "71", "77", "11"],
        answer="17",
        explanation="a usa el constructor por defecto (x=1), b usa el constructor con parámetro (x=7)."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class Contador{\n  int v;\npublic:\n  Contador(){ v=0; }\n  Contador&amp; inc(){ v++; return *this; }\n  int get(){ return v; }\n};\nint main(){ Contador c; c.inc().inc(); cout &lt;&lt; c.get(); }</code></pre>",
        options=["0", "1", "2", "Error"],
        answer="2",
        explanation="El método inc devuelve una referencia al objeto actual, permitiendo encadenar llamadas."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class C{\n  int x;\npublic:\n  C(int v){ x=v; }\n  int get(){ return x; }\n};\nint main(){ C* p=new C(9); cout &lt;&lt; p-&gt;get(); delete p; }</code></pre>",
        options=["9", "0", "Error", "Basura"],
        answer="9",
        explanation="Se crea dinámicamente con new y se accede con ->. Devuelve 9."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre al destruir un objeto en C++?",
        options=[
            "Siempre se libera memoria automáticamente",
            "Se llama al destructor, liberando recursos si está definido",
            "Se pierde la referencia pero la memoria queda reservada",
            "El compilador ignora la destrucción"
        ],
        answer="Se llama al destructor, liberando recursos si está definido",
        explanation="El destructor se ejecuta al salir de ámbito o al hacer delete."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class A{\n  static int c;\npublic:\n  A(){ c++; }\n  static int get(){ return c; }\n};\nint A::c=0;\nint main(){ A a1; A a2; cout &lt;&lt; A::get(); }</code></pre>",
        options=["0", "1", "2", "Error"],
        answer="2",
        explanation="c es estático: compartido entre todos los objetos. Dos objetos incrementan c=2."
    ),

    Exercise(
        type_="test",
        question="¿Qué significa declarar un método como const?\n<pre><code>int get() const;</code></pre>",
        options=[
            "El método no puede modificar atributos del objeto",
            "El método devuelve un valor constante",
            "El método es inmutable para siempre",
            "El método solo puede llamarse en objetos globales"
        ],
        answer="El método no puede modificar atributos del objeto",
        explanation="Los métodos const garantizan no alterar el estado del objeto."
    ),

    Exercise(
        type_="test",
        question="¿Qué ocurre al pasar un objeto por valor a una función?",
        options=[
            "Se pasa una referencia al mismo objeto",
            "Se crea una copia del objeto usando el constructor de copia",
            "Se pasa siempre como puntero",
            "Provoca error de compilación"
        ],
        answer="Se crea una copia del objeto usando el constructor de copia",
        explanation="Los objetos se copian por defecto al pasarse por valor."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class A{ public: int x=1; };\nclass B: public A{ public: int y=2; };\nint main(){ B b; cout &lt;&lt; b.x+b.y; }</code></pre>",
        options=["1", "2", "3", "Error"],
        answer="3",
        explanation="b hereda x=1 de A y tiene y=2 en B. Total=3."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class A{ public: virtual void f(){ cout &lt;&lt; \"A\"; } };\nclass B: public A{ public: void f(){ cout &lt;&lt; \"B\"; } };\nint main(){ A* p=new B(); p-&gt;f(); }</code></pre>",
        options=["A", "B", "Error", "Nada"],
        answer="B",
        explanation="Gracias a virtual, se ejecuta la versión sobrescrita en B."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime?\n<pre><code>class A{ public: int v=5; };\nclass B: public A{ public: int v=7; };\nint main(){ B b; cout &lt;&lt; b.v; }</code></pre>",
        options=["5", "7", "Error", "Basura"],
        answer="7",
        explanation="El atributo v de B oculta al de A."
    ),

    Exercise(
        type_="test",
        question="¿Por qué se recomienda que las clases base con métodos virtuales tengan un destructor virtual?",
        options=[
            "Porque así el compilador genera menos código",
            "Porque asegura que al borrar un objeto derivado vía puntero a base se llame al destructor correcto",
            "Porque obliga a que las clases derivadas definan destructor",
            "No tiene ninguna utilidad práctica"
        ],
        answer="Porque asegura que al borrar un objeto derivado vía puntero a base se llame al destructor correcto",
        explanation="Evita fugas de memoria y asegura liberación completa de recursos."
    ),
    Exercise(
        type_="code",
        question="Define una clase Punto con miembros públicos int x,y. Lee x e y y muestra la suma x+y.",
        tests_json={
            "sample": [{"input": "2 5\n", "output": "7"}],
            "hidden": [
                {"input": "0 0\n", "output": "0"},
                {"input": "-3 10\n", "output": "7"}
            ]
        },
        hint="Declara class Punto { public: int x,y; }; Crea un objeto, asígnale x e y y muestra x+y en UNA línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class Punto{ public: int x,y; };\n'
            'int main(){ Punto p; cin>>p.x>>p.y; cout<<(p.x+p.y); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Contador con atributo privado v. Constructor a 0, método inc() y get(). Lee n e incrementa n veces; muestra el valor.",
        tests_json={
            "sample": [{"input": "5\n", "output": "5"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "100\n", "output": "100"}
            ]
        },
        hint="Encapsula v como private. inc() no recibe parámetros. get() devuelve el valor.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class Contador{ int v; public: Contador():v(0){} void inc(){++v;} int get() const {return v;} };\n'
            'int main(){ int n; if(!(cin>>n)) return 0; Contador c; while(n--) c.inc(); cout<<c.get(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Rectangulo (ancho, alto privados). Constructor (w,h), métodos area() y perimetro(). Lee w h y muestra área y perímetro en dos líneas.",
        tests_json={
            "sample": [{"input": "3 4\n", "output": "12\n14"}],
            "hidden": [
                {"input": "7 1\n", "output": "7\n16"},
                {"input": "0 5\n", "output": "0\n10"}
            ]
        },
        hint="Usa long long para evitar overflow. Formato: primera línea área, segunda perímetro. Sin espacios extra al final de cada línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class Rectangulo{ long long w,h; public: Rectangulo(long long W,long long H):w(W),h(H){} '
            'long long area() const {return w*h;} long long perimetro() const {return 2*(w+h);} };\n'
            'int main(){ long long w,h; cin>>w>>h; Rectangulo r(w,h); cout<<r.area()<<\"\\n\"<<r.perimetro(); }\n'
        ),
        checker="ignore_trailing_newlines", time_limit_ms=1000, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Circulo (radio double). Métodos area() y longitud(). Lee r y muestra área y longitud con 6 decimales en dos líneas.",
        tests_json={
            "sample": [{"input": "1\n", "output": "3.141593\n6.283185"}],
            "hidden": [
                {"input": "0\n", "output": "0.000000\n0.000000"},
                {"input": "2.5\n", "output": "19.634955\n15.707963"}
            ]
        },
        hint="Usa const double PI=3.141592653589793; y iomanip (fixed, setprecision(6)).",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'class Circulo{ double r; public: explicit Circulo(double R):r(R){} '
            'double area() const { const double PI=3.141592653589793; return PI*r*r; } '
            'double longitud() const { const double PI=3.141592653589793; return 2*PI*r; } };\n'
            'int main(){ double r; cin>>r; Circulo c(r); cout.setf(ios::fixed); '
            'cout<<setprecision(6)<<c.area()<<\"\\n\"<<setprecision(6)<<c.longitud(); }\n'
        ),
        checker="ignore_trailing_newlines", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Persona con nombre (string) y edad (int), privados. Lee línea completa para nombre y luego edad. Muestra: 'Nombre: <nombre>, Edad: <edad>'.",
        tests_json={
            "sample": [{"input": "Ada Lovelace\n36\n", "output": "Nombre: Ada Lovelace, Edad: 36"}],
            "hidden": [
                {"input": "Alan Turing\n41\n", "output": "Nombre: Alan Turing, Edad: 41"},
                {"input": "Grace Hopper\n85\n", "output": "Nombre: Grace Hopper, Edad: 85"}
            ]
        },
        hint="Primero getline para el nombre (con espacios), luego la edad con cin. Formato exacto con coma y espacio.",
        solution_code=(
            '#include <iostream>\n#include <string>\nusing namespace std;\n'
            'class Persona{ string n; int e; public: void set(const string& name,int age){n=name;e=age;} '
            'string nombre() const {return n;} int edad() const {return e;} };\n'
            'int main(){ ios::sync_with_stdio(false); cin.tie(nullptr); string nombre; getline(cin,nombre); int edad; cin>>edad; '
            'Persona p; p.set(nombre,edad); cout<<\"Nombre: \"<<p.nombre()<<\", Edad: \"<<p.edad(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Cuenta con saldo (long long). Lee saldo inicial, ingreso y retirada. Si la retirada deja saldo negativo, imprime 'ERROR'; si no, imprime el saldo final.",
        tests_json={
            "sample": [{"input": "100\n50\n70\n", "output": "80"}],
            "hidden": [
                {"input": "0\n0\n0\n", "output": "0"},
                {"input": "10\n5\n20\n", "output": "ERROR"}
            ]
        },
        hint="Métodos depositar(x) y retirar(y). Si retirar no es posible, no modifiques el saldo y muestra 'ERROR'.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class Cuenta{ long long s; public: explicit Cuenta(long long S):s(S){} '
            'void depositar(long long x){ s+=x; } bool retirar(long long y){ if(s<y) return false; s-=y; return true; } '
            'long long saldo() const { return s; } };\n'
            'int main(){ long long s,i,r; cin>>s>>i>>r; Cuenta c(s); c.depositar(i); '
            'if(!c.retirar(r)) cout<<\"ERROR\"; else cout<<c.saldo(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Fraccion(n,d) con método simplificar(). Lee n y d (enteros, d≠0) y muestra la fracción irreducible en formato 'a/b' con el signo sólo en el numerador.",
        tests_json={
            "sample": [{"input": "8 12\n", "output": "2/3"}],
            "hidden": [
                {"input": "-2 4\n", "output": "-1/2"},
                {"input": "3 -6\n", "output": "-1/2"},
                {"input": "-2 -4\n", "output": "1/2"},
                {"input": "0 5\n", "output": "0/1"}
            ]
        },
        hint="Implementa gcd iterativo (evita std::gcd si prefieres). Normaliza signo (denominador positivo) y 0/d → 0/1.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'long long gcdll(long long a,long long b){ if(a<0) a=-a; if(b<0) b=-b; while(b){ long long t=a%b; a=b; b=t; } return a? a:1; }\n'
            'class Fraccion{ long long n,d; public: Fraccion(long long N,long long D):n(N),d(D){} '
            'void simplificar(){ if(n==0){ d=1; return; } long long g=gcdll(n,d); n/=g; d/=g; if(d<0){ d=-d; n=-n; } } '
            'void print() const { cout<<n<<\"/\"<<d; } };\n'
            'int main(){ long long n,d; cin>>n>>d; Fraccion f(n,d); f.simplificar(); f.print(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1500, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Vector3(double x,y,z) con método norma(). Lee x y z y muestra la norma con 6 decimales.",
        tests_json={
            "sample": [{"input": "1 2 2\n", "output": "3.000000"}],
            "hidden": [
                {"input": "0 0 0\n", "output": "0.000000"},
                {"input": "3 4 12\n", "output": "13.000000"}
            ]
        },
        hint="norma = sqrt(x*x + y*y + z*z). Usa fixed y setprecision(6).",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\n#include <cmath>\nusing namespace std;\n'
            'class Vector3{ double x,y,z; public: Vector3(double X,double Y,double Z):x(X),y(Y),z(Z){} '
            'double norma() const { return sqrt(x*x+y*y+z*z); } };\n'
            'int main(){ double x,y,z; cin>>x>>y>>z; Vector3 v(x,y,z); cout.setf(ios::fixed); cout<<setprecision(6)<<v.norma(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=1200, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Rango [a,b] con método bool contiene(int x) const. Lee a, b, x y muestra 'SI' si x está en [a,b], si no 'NO'.",
        tests_json={
            "sample": [{"input": "3 7 5\n", "output": "SI"}],
            "hidden": [
                {"input": "3 7 8\n", "output": "NO"},
                {"input": "-5 -1 -5\n", "output": "SI"}
            ]
        },
        hint="Asume a <= b. Imprime exactamente 'SI' o 'NO' en UNA línea.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class Rango{ long long a,b; public: Rango(long long A,long long B):a(A),b(B){} '
            'bool contiene(long long x) const { return a<=x && x<=b; } };\n'
            'int main(){ long long a,b,x; cin>>a>>b>>x; Rango r(a,b); cout<<(r.contiene(x)?\"SI\":\"NO\"); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=800, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Acum con valor entero inicial 0. Métodos add(int) y get(). add devuelve referencia a *this para encadenar. Lee a,b,c y muestra el acumulado tras add(a).add(b).add(c).",
        tests_json={
            "sample": [{"input": "3 4 5\n", "output": "12"}],
            "hidden": [
                {"input": "0 0 0\n", "output": "0"},
                {"input": "-1 2 -3\n", "output": "-2"}
            ]
        },
        hint="Firma: Acum& add(int k){ v+=k; return *this; } get() const devuelve v.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class Acum{ long long v; public: Acum():v(0){} Acum& add(long long k){ v+=k; return *this; } long long get() const {return v;} };\n'
            'int main(){ long long a,b,c; cin>>a>>b>>c; Acum ac; ac.add(a).add(b).add(c); cout<<ac.get(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=800, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase A con contador estático de instancias (se incrementa en el constructor). Lee n, crea n objetos (por ejemplo dentro de un bucle) y muestra A::get().",
        tests_json={
            "sample": [{"input": "5\n", "output": "5"}],
            "hidden": [
                {"input": "0\n", "output": "0"},
                {"input": "13\n", "output": "13"}
            ]
        },
        hint="static int c; en la clase + definición fuera: int A::c=0;. Un método estático get() devuelve c.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class A{ static int c; public: A(){ ++c; } static int get(){ return c; } }; int A::c=0;\n'
            'int main(){ int n; cin>>n; for(int i=0;i<n;i++){ A tmp; } cout<<A::get(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=800, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Punto(double x,y) con método distancia() const al origen. Lee x y y muestra la distancia con 6 decimales.",
        tests_json={
            "sample": [{"input": "3 4\n", "output": "5.000000"}],
            "hidden": [
                {"input": "0 0\n", "output": "0.000000"},
                {"input": "-6 8\n", "output": "10.000000"}
            ]
        },
        hint="distancia = sqrt(x*x + y*y). Usa fixed y setprecision(6).",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\n#include <cmath>\nusing namespace std;\n'
            'class Punto{ double x,y; public: Punto(double X,double Y):x(X),y(Y){} double distancia() const { return sqrt(x*x+y*y); } };\n'
            'int main(){ double x,y; cin>>x>>y; Punto p(x,y); cout.setf(ios::fixed); cout<<setprecision(6)<<p.distancia(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=800, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Par con dos enteros privados a,b. Métodos set(a,b), swap(), getA(), getB(). Lee a b, intercambia y muestra los valores finales en UNA línea separados por un espacio.",
        tests_json={
            "sample": [{"input": "7 9\n", "output": "9 7"}],
            "hidden": [
                {"input": "0 0\n", "output": "0 0"},
                {"input": "-3 10\n", "output": "10 -3"}
            ]
        },
        hint="Implementa swap manualmente (variable temporal) o con std::swap.",
        solution_code=(
            '#include <iostream>\nusing namespace std;\n'
            'class Par{ long long a,b; public: void set(long long A,long long B){a=A;b=B;} void swapv(){ long long t=a; a=b; b=t; } '
            'long long getA() const {return a;} long long getB() const {return b;} };\n'
            'int main(){ long long a,b; cin>>a>>b; Par p; p.set(a,b); p.swapv(); cout<<p.getA()<<\" \"<<p.getB(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=800, memory_limit_mb=64,
    ),

    Exercise(
        type_="code",
        question="Clase Termometro con Celsius (double). Método getFahrenheit(). Lee C y muestra F con 2 decimales.",
        tests_json={
            "sample": [{"input": "0\n", "output": "32.00"}],
            "hidden": [
                {"input": "100\n", "output": "212.00"},
                {"input": "-40\n", "output": "-40.00"}
            ]
        },
        hint="F = C*9/5 + 32. Formatea con fixed y setprecision(2).",
        solution_code=(
            '#include <iostream>\n#include <iomanip>\nusing namespace std;\n'
            'class Termometro{ double c; public: explicit Termometro(double C):c(C){} double getFahrenheit() const { return c*9.0/5.0+32.0; } };\n'
            'int main(){ double c; cin>>c; Termometro t(c); cout.setf(ios::fixed); cout<<setprecision(2)<<t.getFahrenheit(); }\n'
        ),
        checker="ignore_trailing_whitespace", time_limit_ms=800, memory_limit_mb=64,
    ),

]

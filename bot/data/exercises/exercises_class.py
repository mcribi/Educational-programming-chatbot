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

]

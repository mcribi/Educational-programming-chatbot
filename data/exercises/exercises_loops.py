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
        question="¿Qué hace el siguiente código?\n<pre><code>for (int i = 0; i < 3; i++) cout << i;</code></pre>",
        options=["Imprime 0 1 2", "Imprime 1 2 3", "Imprime 0 1 2 3", "No imprime nada"],
        answer="Imprime 0 1 2",
        explanation="Imprime los valores desde 0 hasta 2. El bucle se detiene cuando i vale 3."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es el error en este código?\n<pre><code>while (i < 10);\n{\n    cout << i;\n}</code></pre>",
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
        question="¿Qué imprime el siguiente código?\n<pre><code>int i = 1;\nwhile (i < 4) {\n    cout << i;\n    i++;\n}</code></pre>",
        options=["1 2 3", "1 2 3 4", "0 1 2", "Nada"],
        answer="1 2 3",
        explanation="El bucle se repite mientras i < 4, por lo que imprime 1, 2 y 3."
    ),

    Exercise(
        type_="test",
        question="¿Qué imprime este código?\n<pre><code>int j = 5;\ndo {\n    cout << j;\n    j++;\n} while (j < 5);</code></pre>",
        options=["5", "Nada", "5 6", "Error de compilación"],
        answer="5",
        explanation="El cuerpo se ejecuta una vez antes de comprobar la condición."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor final tiene la variable suma?\n<pre><code>int suma = 0;\nfor (int i = 1; i <= 3; i++) {\n    suma += i;\n}</code></pre>",
        options=["3", "6", "0", "9"],
        answer="6",
        explanation="1 + 2 + 3 = 6"
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este fragmento?\n<pre><code>for (int i = 1; i <= 5; i++) {\n    if (i % 2 == 0)\n        cout << i;\n}</code></pre>",
        options=["Imprime 1 2 3 4 5", "Imprime 2 4", "Imprime 1 3 5", "No imprime nada"],
        answer="Imprime 2 4",
        explanation="Imprime solo los números pares entre 1 y 5."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor final tiene la variable x?\n<pre><code>int x = 1;\nwhile (x < 100) {\n    x *= 2;\n}</code></pre>",
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
        question="¿Qué valor tendrá i al terminar?\n<pre><code>int i;\nfor (i = 0; i < 5; i++);</code></pre>",
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
        question="El siguiente bucle imprime solo 3 veces:\n<pre><code>for (int i = 1; i <= 3; i++)</code></pre>",
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
        question="¿Qué imprime este código?\n<pre><code>for (int i = 2; i <= 6; i += 2) {\n    cout << i;\n}</code></pre>",
        options=["2 3 4 5 6", "2 4 6", "1 2 3", "2 4 6 8"],
        answer="2 4 6",
        explanation="Incrementa de 2 en 2: imprime 2, 4 y 6."
    ),

    Exercise(
        type_="test",
        question="¿Qué valor final tendrá suma?\n<pre><code>int suma = 0;\nfor (int i = 0; i < 4; i++) {\n    suma += i;\n}</code></pre>",
        options=["4", "6", "10", "3"],
        answer="6",
        explanation="0 + 1 + 2 + 3 = 6"
    ),

    Exercise(
        type_="test",
        question="¿Qué hará este código?\n<pre><code>int x = 10;\nwhile (x > 0) {\n    cout << x;\n    x--;\n}</code></pre>",
        options=["Imprime del 0 al 10", "Imprime del 1 al 10", "Imprime del 10 al 1", "No imprime nada"],
        answer="Imprime del 10 al 1",
        explanation="El contador va decreciendo desde 10 hasta 1."
    ),

    Exercise(
        type_="test",
        question="¿Qué hace este código?\n<pre><code>int x = 5;\ndo {\n    x--;\n    cout << x;\n} while (x > 0);</code></pre>",
        options=["Imprime 5 4 3 2 1", "Imprime 4 3 2 1 0", "Imprime 5 4 3 2 1 0", "Error de compilación"],
        answer="Imprime 4 3 2 1 0",
        explanation="La variable se reduce antes de imprimir."
    ),

    Exercise(
        type_="test",
        question="¿Cuál es la salida del siguiente código?\n<pre><code>int total = 1;\nfor (int i = 1; i <= 3; i++) {\n    total *= i;\n}\ncout << total;</code></pre>",
        options=["3", "6", "9", "12"],
        answer="6",
        explanation="1*1 = 1, luego *2 = 2, luego *3 = 6. Resultado: 6"
    )

]

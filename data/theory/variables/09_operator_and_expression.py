from src.lesson import Lesson

lesson = Lesson(
    title="Operadores y expresiones en C++",
    content=(
        "Una <b>expresión</b> combina valores, variables y <b>operadores</b> para obtener un resultado.\n"
        "Ejemplo:\n"
        "<code>3 + 5</code> da 8\n"
        "<code>edad * 2</code> si edad vale 10, da 20\n\n"

        "<b>Tipos de operadores:</b>\n\n"

        "<b>Aritméticos</b> (operaciones matemáticas):\n"
        "• <code>+</code>: suma\n"
        "• <code>-</code>: resta\n"
        "• <code>*</code>: multiplicación\n"
        "• <code>/</code>: división\n"
        "• <code>%</code>: módulo (resto de una división entera)\n\n"

        "<b>Relacionales</b> (comparan valores):\n"
        "• <code>==</code>: igual que\n"
        "• <code>!=</code>: distinto de\n"
        "• <code>&lt;</code>: menor que\n"
        "• <code>&gt;</code>: mayor que\n"
        "• <code>&lt;=</code>: menor o igual que\n"
        "• <code>&gt;=</code>: mayor o igual que\n\n"

        "<b>Lógicos</b> (trabajan con valores booleanos):\n"
        "• <code>&&</code>: y lógico (ambas condiciones verdaderas)\n"
        "• <code>||</code>: o lógico (al menos una verdadera)\n"
        "• <code>!</code>: negación (invierte true/false)\n\n"

        "<b>Otros útiles:</b>\n"
        "• <code>++</code>: incremento (suma 1)\n"
        "• <code>--</code>: decremento (resta 1)\n"
        "• <code>=</code>: asignación (guardar valor)\n\n"

        "<b>Ejemplos de expresiones:</b>\n"
        "<code>int x = 10 + 5;</code>  // x vale 15\n"
        "<code>bool es_mayor = x &gt; 18;</code>  // resultado: false\n"
        "<code>int resto = 17 % 4;</code>  // resultado: 1\n\n"

        "<b>Importante:</b> El tipo de los datos afecta al resultado. "
        "<code>5 / 2</code> da <code>2</code> si ambos son <code>int</code>, pero da <code>2.5</code> si uno es <code>double</code>."
    )
)

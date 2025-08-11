from src.lesson import Lesson

lesson = Lesson(
    title="Operando con tipos numéricos distintos",
    content=(
        "Cuando combinas tipos diferentes (como <code>int</code> y <code>double</code>) en una operación, "
        "el compilador convierte automáticamente al tipo más grande.\n\n"
        "Ejemplo:\n"
        "<code>int unidades = 2;</code>\n"
        "<code>double precio = 3.5;</code>\n"
        "<code>double total = unidades * precio;</code> // unidades se convierte a double\n\n"
        "⚠️ Pero cuidado: si todos los operandos son enteros, se usa división entera.\n"
        "<code>media = (10 + 5) / 2;</code>  // Resultado: 7 (no 7.5)"
    )
)

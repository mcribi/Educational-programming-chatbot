from src.lesson import Lesson

lesson = Lesson(
    title="Ejemplos con matrices",
    content=(
        "🔹 <b>Ejemplo 1: Suma de dos matrices</b>\n"
        "<pre><code>int A[2][2] = {{1,2},{3,4}};\n"
        "int B[2][2] = {{5,6},{7,8}};\n"
        "int C[2][2];\n\n"
        "for (int i=0; i<2; i++)\n"
        "  for (int j=0; j<2; j++)\n"
        "    C[i][j] = A[i][j] + B[i][j];</code></pre>\n\n"
        "🔹 <b>Ejemplo 2: Nota media de alumnos</b>\n"
        "<pre><code>const int ALUMNOS = 3, NOTAS = 2;\n"
        "double notas[ALUMNOS][NOTAS] = {{5,7},{8,6},{9,10}};\n\n"
        "for (int i=0; i<ALUMNOS; i++) {\n"
        "  double suma = 0;\n"
        "  for (int j=0; j<NOTAS; j++) suma += notas[i][j];\n"
        "  cout << \"Media del alumno \" << i << \": \" << suma/NOTAS;\n"
        "}</code></pre>"
    )
)

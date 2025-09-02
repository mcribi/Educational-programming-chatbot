from src.lesson import Lesson

lesson = Lesson(
    title="Gestión de componentes en matrices",
    content=(
        "A veces reservamos una matriz grande, pero solo usamos parte de ella.\n\n"
        "📌 Estrategias:\n"
        "• Usar todas las posiciones (ej. crucigrama fijo 5x6).\n"
        "• Usar solo algunas filas o columnas (con variables que indiquen cuántas están en uso).\n"
        "• Usar un bloque rectangular dentro de la matriz.\n"
        "• Usar filas de distinto tamaño (ej. texto con líneas de diferentes longitudes).\n\n"
        "👉 Esto permite flexibilidad sin cambiar el tamaño reservado."
    )
)

from rich.table import Table
from rich import print

# Inicializar la tabla
tabla = Table(title="Ranking de Películas")

# Agregar columnas
tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
tabla.add_column("Título", style="magenta")
tabla.add_column("Rating", justify="center", style="green")

# Agregar filas
tabla.add_row("01", "Matrix", "9.1")
tabla.add_row("02", "Inception", "9.0")
tabla.add_row("03", "Interstellar", "8.6")

# Mostrar en consola
print(tabla)
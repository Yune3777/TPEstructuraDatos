from rich.panel import Panel
from rich import print

# Crear un panel simple
print(Panel("Bienvenido al sistema de gestión de catálogo.", title="CineBot v1.0"))

# Panel personalizado con colores y bordes redondeados
panel = Panel(
    "[green]Conexión establecida correctamente con la base de datos.[/green]",
    title="Estado del Sistema",
    border_style="cyan"
)
print(panel)
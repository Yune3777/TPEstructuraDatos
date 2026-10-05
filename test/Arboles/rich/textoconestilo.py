from rich.panel import Panel
from rich import print
from rich.table import Table

print("[bold yellow]Advertencia:[/bold yellow] Verifique los datos.")

print(Panel("Proceso finalizado", title="Info"))


t = Table()


t.add_column("Nombre")


t.add_row("Matrix")


print(t)
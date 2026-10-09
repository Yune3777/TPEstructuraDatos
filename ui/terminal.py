from servicios.catalogo import Catalogo
from rich.panel import Panel
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.align import Align

class Terminal:
    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo

    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = Prompt.ask("[bold white on green] Opción [/bold white on green]").strip()
            if opcion == "1":
                self._buscar()
            elif opcion == "2":
                self._cancion_aleatoria()
            elif opcion == "3":
                self._filtrar()
            elif opcion == "0":
                print("Gracias! Vuelvas prontos!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
            print()
            

    def _mostrar_menu(self) -> None:
        print(Panel(Align.center("OÍD MORTALES"), title="Versión 1.0", title_align="right"))
        
        print("1. Buscar canción por [bold green]Nombre[/bold green]")
        print("2. Canción [bold green]Aleatoria[/bold green]")
        print("3. Explorar por [bold green]Género[/bold green]")
        print("4. Recomendaciones por [bold green]similitud[/bold green]")
        print("5. Top 10 por [bold green]Año[/bold green]")
        print("0. [bold green]Salir[/bold green]")
        
        print("\n" + "--*" * 15 + "\n")
        

    def _buscar(self) -> None:
        nombre = input("Nombre de la canción: ").strip()
        resultado = self._catalogo.buscar(nombre)
        if resultado:
            print(
    f"La canción [bold green]{resultado.nombre}[/bold green] fue interpretada por "f"[bold green]{resultado.artista}[/bold green] en el idioma {resultado.idioma} y es del año {resultado.año}.")
        else:
            print(f"No encontramos '{nombre}'.")

    def _cancion_aleatoria(self) -> None:
        cancion = self._catalogo.cancion_aleatoria()
        print(f"La canción elegida es: [bold green]{cancion.nombre}[/bold green] que está interpretada por {cancion.artista} y es del año {cancion.año}.")

    def _filtrar(self) -> None:
        genero = input("Género: ").strip()
        resultados = self._catalogo.filtrar(genero)
        if resultados:
            for cancion in resultados:
                print(f"- {cancion.nombre} (interpretada por {cancion.artista})")
        else:
            print(f"No hay canciones del género '{genero}'.")
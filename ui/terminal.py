import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from servicios.catalogo import Catalogo
from rich.panel import Panel
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.align import Align

class Terminal:
    def __init__(self, catalogo: Catalogo,arbol) -> None:
        self._catalogo = catalogo

    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = Prompt.ask("[bold white on hot_pink3] INGRESAR OPCIÓN: [/bold white on hot_pink3]").strip()
            if opcion == "1":
                self._buscar()
            elif opcion == "2":
                self._manga_aleatorio()
            elif opcion == "3":
                self._filtrar()
            elif opcion == "0":
                print("\n [bold dark_orange3]Gracias![bold dark_orange3] [bold indian_red]Vuelvas[/bold indian_red] [bold hot_pink3]prontos![/bold hot_pink3]\n")
                break
            else:
                print("\n\n ⚠️  Opción inválida! Intente nuevamente ⚠️")
            print()
            

    def _mostrar_menu(self) -> None:
        print(Panel(Align.center("[bold indian_red]▀▄▀▄▀▄▀▄▀▄▀▄  MANPY  ▄▀▄▀▄▀▄▀▄▀▄▀[/bold indian_red]"), title="Versión 3.0", title_align="right",border_style="indian_red"))
        

        print("[bold dark_orange3][ 1 ]  [/bold dark_orange3] Buscar manga por [bold dark_orange3]Nombre[/bold dark_orange3]")
        print("[bold dark_orange3][ 2 ]  [/bold dark_orange3] Manga [bold dark_orange3]Aleatoria[/bold dark_orange3]")
        print("[bold indian_red][ 3 ]  [/bold indian_red] Explorar por [bold indian_red]Género[/bold indian_red]")
        print("[bold indian_red][ 4 ]  [/bold indian_red] Recomendaciones por [bold indian_red]similitud[/bold indian_red]")
        print("[bold hot_pink3][ 5 ]   Top 10[/bold hot_pink3]")
        print("[bold hot_pink3][ 0 ]   Salir[/bold hot_pink3]")
        
        print("\n" + "[bold indian_red]✦ ✦ [/bold indian_red]" * 15 + "\n")
        

    def _buscar(self) -> None:
        nombre = input("Nombre del manga: ").strip()
        resultado = self._catalogo.buscar(nombre)
        if resultado:
            print(
    f"El manga [bold green]{resultado.nombre}[/bold green] tiene como su artista a "f"[bold dodger_blue2]{resultado.artista}[/bold dodger_blue2], corresponde al género [bold deep_pink4]{resultado.genero}[/bold deep_pink4] y fue publicado en el año {resultado.año}.")
        else:
            print(f"No encontramos '{nombre}'.")

    def _manga_aleatorio(self) -> None:
        manga = self._catalogo.manga_aleatorio()
        print(f"El manga elegido es: [bold green]{manga.nombre}[/bold green], su artistas es {manga.artista} y su año de publicación es {manga.año}.")

    def _filtrar(self) -> None:
        genero = input("Género: ").strip()
        resultados = self._catalogo.filtrar(genero)
        if resultados:
            for manga in resultados:
                print(f"- [bold green]{manga.nombre}[/bold green] ([bold blue]{manga.artista}[/bold blue])")
        else:
            print(f"No hay mangas del género '{genero}'.")
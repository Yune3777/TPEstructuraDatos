import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from servicios.opciones_menu import OpcMenu
from rich.panel import Panel
from rich import print
from rich.prompt import Prompt
from rich.align import Align
from rich.console import Console



class Terminal:
    def __init__(self, catalogo, servicios, estructuras):
        self._catalogo = catalogo
        self.recomendador = servicios.get("recomendador")
        self.top_mangas = servicios.get("heap_max")
        self.arbol_general = estructuras.get("arbol_general")
        self.arbol_avl = estructuras.get("arbol_avl")

    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = Prompt.ask("[bold white on hot_pink3]\n\n\n INGRESAR OPCIÓN: [/bold white on hot_pink3]").strip()
            
            if opcion == "1":
                OpcMenu._buscar(self.arbol_avl)
            elif opcion == "2":
                OpcMenu._manga_aleatorio(self._catalogo)
            elif opcion == "3":
                OpcMenu._filtrar(self._catalogo)
            elif opcion == "4":
                OpcMenu._recomendar_manga(self.recomendador, self._catalogo, self.arbol_avl)
            elif opcion == "5":
                OpcMenu._top_5_rating(self._catalogo)
            elif opcion == "0":
                print("\n [bold dark_orange3]Gracias![bold dark_orange3] [bold indian_red]Vuelvas[/bold indian_red] [bold hot_pink3]prontos![/bold hot_pink3]\n")
                break
            else:
                print("\n\n ⚠️  Opción inválida! Intente nuevamente ⚠️")
            print()
            
    def _mostrar_menu(self) -> None:
        console = Console()
        console.clear()

        ARTE_SUPERIOR = r"""
 ██████   ██████   █████████   ██████   █████ ███████████  █████ █████
▒▒██████ ██████   ███▒▒▒▒▒███ ▒▒██████ ▒▒███ ▒▒███▒▒▒▒▒███▒▒███ ▒▒███ 
 ▒███▒█████▒███  ▒███    ▒███  ▒███▒███ ▒███  ▒███    ▒███ ▒▒███ ███  
 ▒███▒▒███ ▒███  ▒███████████  ▒███▒▒███▒███  ▒██████████   ▒▒█████   
 ▒███ ▒▒▒  ▒███  ▒███▒▒▒▒▒███  ▒███ ▒▒██████  ▒███▒▒▒▒▒▒     ▒▒███    
 ▒███      ▒███  ▒███    ▒███  ▒███  ▒▒█████  ▒███            ▒███    
 █████     █████ █████   █████ █████  ▒▒█████ █████           █████   
▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒ ▒▒▒▒▒           ▒▒▒▒▒    
"""
        console.print("\n\n")
        console.print(Panel(Align.center("\n[bold indian_red]" + ARTE_SUPERIOR + "[/bold indian_red]"), style="bold indian_red"))

        #print(Panel(Align.center("\n[bold indian_red]▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄  MANPY  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀[/bold indian_red]\n"), title="Versión 3.0", title_align="right",border_style="indian_red"))
        
        todas_las_opciones_menu = (
            
        "\n[bold dark_orange3][ 1 ]  [/bold dark_orange3] Buscar manga por [bold dark_orange3]Nombre[/bold dark_orange3]"
        "\n[bold dark_orange3][ 2 ]  [/bold dark_orange3] Manga [bold dark_orange3]Aleatorio[/bold dark_orange3]"
        "\n[bold indian_red][ 3 ]  [/bold indian_red] Explorar por [bold indian_red]Género[/bold indian_red]"
        "\n[bold indian_red][ 4 ]  [/bold indian_red] Recomendaciones por [bold indian_red]similitud[/bold indian_red]"
        "\n[bold hot_pink3][ 5 ]  [/bold hot_pink3] [bold hot_pink3]Top 5[/bold hot_pink3]"
        "\n[bold hot_pink3][ 0 ]   Salir[/bold hot_pink3]\n"
        )
        panel = Panel(
            Align.center(todas_las_opciones_menu),
            title="Menú",
            border_style="indian_red",
            width=60,
            )

        print(Align.center(panel))
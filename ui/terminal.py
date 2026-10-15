import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from servicios.catalogo import Catalogo
from rich.panel import Panel
from rich import print
from rich.prompt import Prompt
from rich.align import Align

class Terminal:
    def __init__(self, catalogo: Catalogo,arbol) -> None:
        self._catalogo = catalogo
        self.arbol = arbol

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
        print(Panel(Align.center("\n[bold indian_red]▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄  MANPY  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀[/bold indian_red]\n"), title="Versión 3.0", title_align="right",border_style="indian_red"))
        

        print(Align.center("\n\n[bold dark_orange3][ 1 ]  [/bold dark_orange3] Buscar manga por [bold dark_orange3]Nombre[/bold dark_orange3]"))
        print(Align.center("\n[bold dark_orange3][ 2 ]  [/bold dark_orange3] Manga [bold dark_orange3]Aleatoria[/bold dark_orange3]"))
        print(Align.center("\n[bold indian_red][ 3 ]  [/bold indian_red] Explorar por [bold indian_red]Género[/bold indian_red]"))
        print(Align.center("\n[bold indian_red][ 4 ]  [/bold indian_red] Recomendaciones por [bold indian_red]similitud[/bold indian_red]"))
        print(Align.center("\n[bold hot_pink3][ 5 ]   Top 10[/bold hot_pink3]"))
        print(Align.center("\n[bold hot_pink3][ 0 ]   Salir[/bold hot_pink3]"))
        
        print("\n" + "[bold indian_red]✦ ✦ [/bold indian_red]" * 60 + "\n")
        

    def _buscar(self) -> None:
        nombre = input("\n" "Nombre del manga: ").strip()
        resultados = self.arbol.buscar_palabra(nombre, lambda e: e.nombre.lower())
        if resultados:
            for resultado in resultados:
                print(Align.center("\n"
    f"El manga [bold deep_pink3]{resultado.nombre}[/bold deep_pink3] tiene como su artista a "f"[bold bold deep_pink4]{resultado.artista}[/bold  deep_pink4], corresponde al género [bold hot_pink3]{resultado.genero}[/bold hot_pink3] y fue publicado en el año [bold light_pink3]{resultado.año}[/bold light_pink3]."))
        else:
            print(Align.center(f"No encontramos '{nombre}'."))



    def _manga_aleatorio(self) -> None:
        manga = self._catalogo.manga_aleatorio()
        print(Align.center("\n" f"El manga elegido es: [bold deep_pink3]{manga.nombre}[/bold deep_pink3] del género [bold red]{manga.genero}[/bold red]. Su artistas es [bold hot_pink3]{manga.artista}[/bold hot_pink3] y se publicó en el año [bold plum3]{manga.año}[/bold plum3].""\n"))



    def _filtrar(self) -> None:
        genero = input("Género: ").strip()
        resultados = self._catalogo.filtrar(genero)
        if resultados:
            for manga in resultados:
                print(Align.center("\n" f"- [bold deep_pink3]{manga.nombre}[/bold deep_pink3] ([bold hot_pink3]{manga.artista}[/bold hot_pink3])""\n"))
        else:
            print(Align.center("\n" f"No hay mangas del género '{genero}'." "\n"))
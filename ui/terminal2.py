import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from servicios.catalogo import Catalogo
from rich.panel import Panel
from estructuras.avl import AVL
from rich import print
from rich.align import Align

class Terminal:
    def __init__(self, catalogo: Catalogo,arbol) -> None:
        self._catalogo = catalogo
        self.arbol = arbol

    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = input("INGRESAR OPCIÓN:").strip()
            if opcion == "1":
                self._buscar()
            elif opcion == "2":
                self._manga_aleatorio()
            elif opcion == "3":
                self._filtrar()
            elif opcion == "0":
                print("\n Gracias! Vuelvas prontos! \n")
                break
            else:
                print("\n\n Opción inválida! Intente nuevamente")
            print()
            

    def _mostrar_menu(self) -> None:
        print(Panel(Align.center("\n" + "▀▄"*26 + "  MANPY  " + "▄▀"*26 + "\n"), title="Versión 3.0", title_align="right",border_style="indian_red"))
        

        print("\n")
        print("[ 1 ]   Buscar manga por Nombre  \n")
        print("[ 2 ]   Manga Aleatorio  \n")
        print("[ 3 ]   Explorar por Género \n")
        print("[ 4 ]   Recomendaciones por similitud \n")
        print("[ 5 ]   Top 10 \n")
        print("[ 0 ]   Salir")
        
        print("\n \n \n" + "♦ ♦ " * 30 + "\n \n \n")
        

    def _buscar(self) -> None:
        nombre = input("\n" "Nombre del manga: ").strip()
        resultados = self.arbol.buscar_palabra(nombre, lambda e: e.nombre.lower())
        if resultados:
            for resultado in resultados:
                print(Align.center("\n"
        f"El manga {resultado.nombre} tiene como su artista a "f"{resultado.artista}, corresponde al género {resultado.genero} y fue publicado en el año {resultado.año}."))
        else:
            print(Align.center(f"No encontramos '{nombre}'."))



    def _manga_aleatorio(self) -> None:
        manga = self._catalogo.manga_aleatorio()
        print(Align.center("\n" f"El manga elegido es: {manga.nombre} del género {manga.genero}, su artistas es {manga.artista} y se publicó en el año {manga.año}.""\n"))



    def _filtrar(self) -> None:
        genero = input("\n Género: ").strip()
        resultados = self._catalogo.filtrar(genero)
        if resultados:
            for manga in resultados:
                print(Align.center("\n" f"- {manga.nombre} ({manga.artista})""\n"))
        else:
            print(Align.center("\n" f"No hay mangas del género '{genero}'." "\n"))
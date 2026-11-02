import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from estructuras.avl import ArbolAvl
from rich import print
from rich.align import Align

class OpcMenu:

    # OPCION 1) NOMBRE
    @staticmethod
    def _buscar(arbol_avl) -> None:
        nombre = input("\n" "Nombre del manga: ").strip()
        resultados = arbol_avl.buscar_palabra(nombre, lambda e: e.nombre.lower())
        if resultados:
            for resultado in resultados:
                print(Align.center("\n"
    f"El manga [bold deep_pink3]{resultado.nombre}[/bold deep_pink3] tiene como su artista a "f"[bold bold deep_pink4]{resultado.artista}[/bold  deep_pink4], corresponde al género [bold hot_pink3]{resultado.genero}[/bold hot_pink3] y fue publicado en el año [bold light_pink3]{resultado.año}[/bold light_pink3]."))
        else:
            print(Align.center(f"No encontramos '{nombre}'."))


    # OPCION 2) RANDOM
    @staticmethod
    def _manga_aleatorio(catalogo) -> None:
        manga = catalogo.manga_aleatorio()
        print(Align.center("\n" f"El manga elegido es: [bold deep_pink3]{manga.nombre}[/bold deep_pink3] del género [bold red]{manga.genero}[/bold red]. Su artistas es [bold hot_pink3]{manga.artista}[/bold hot_pink3] y se publicó en el año [bold plum3]{manga.año}[/bold plum3].""\n"))


    # OPCION 3) GÉNERO
    @staticmethod
    def _filtrar(catalogo) -> None:
        genero = input("Género: ").strip()
        resultados = catalogo.filtrar(genero)
        if resultados:
            for manga in resultados:
                print(Align.center("\n" f"- [bold deep_pink3]{manga.nombre}[/bold deep_pink3] ([bold hot_pink3]{manga.artista}[/bold hot_pink3])""\n"))
        else:
            print(Align.center("\n" f"No hay mangas del género '{genero}'." "\n"))


    # OPCION 4) RECOMENDADOR
    @staticmethod
    def _recomendar_manga(recomendador, catalogo,arbol_avl):
        nombre_manga = input("Ingresá el nombre de un manga para hacer una recomendación: ").strip()
        palabra_nombre = arbol_avl.buscar_palabra(nombre_manga, lambda e: e.nombre.lower())
        if not palabra_nombre:
            print("No encontré un manga con ese nombre. Volvé a intentarlo.")
            return
        
        manga_encontrado = palabra_nombre[0]
        mangas = catalogo.listar()
        
        try:
            indice_inicio = mangas.index(manga_encontrado)
        except ValueError:        
            print("No encontré el índice del manga en el catálogo. Volvé a intentarlo.")
            return
        
        recomendaciones = recomendador.recomendar_con_bfs(inicio=indice_inicio, limite=5)
        
        if not recomendaciones:
            print("No puedo recomendarte nada. Lo siento.")
        else:
            print(f"\nMangas recomendados basados en '{manga_encontrado.nombre}':")
            for i, manga in enumerate(recomendaciones, 1):
                print(f"{i}. {manga.nombre} (Género: {manga.genero} - Año: {manga.año})")

    # OPCION 5) TOP 5
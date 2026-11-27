import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from estructuras.avl import ArbolAvl
from rich import print
from rich.prompt import Prompt
from rich.align import Align
from estructuras.heap_max import MaxHeap
from servicios.top_mangas import TopMangas

class OpcMenu:

    # OPCION 1) NOMBRE
    @staticmethod
    def _buscar(arbol_avl) -> None:
        nombre = input("\n" "Nombre del manga: ").strip()
        resultados = arbol_avl.buscar_palabra(nombre, lambda e: e.nombre.lower())
        if resultados:
            for resultado in resultados:
                print(("\n"
    f"El manga [bold dark_orange3]{resultado.nombre}[/bold dark_orange3] tiene como su artista a "f"[bold indian_red]{resultado.artista}[/bold indian_red], corresponde al género [bold hot_pink3]{resultado.genero}[/bold hot_pink3] y fue publicado en el año [bold light_pink3]{resultado.año}[/bold light_pink3]."))
        else:
            print((f"No encontramos '{nombre}'."))


    # OPCION 2) RANDOM
    @staticmethod
    def _manga_aleatorio(catalogo) -> None:
        manga = catalogo.manga_aleatorio()
        print(("\n" f"El manga elegido es: [bold dark_orange3]{manga.nombre}[/bold dark_orange3] del género [bold indian_red]{manga.genero}[/bold indian_red]. Su artistas es [bold hot_pink3]{manga.artista}[/bold hot_pink3] y se publicó en el año [bold light_pink3]{manga.año}[/bold light_pink3].""\n"))


    # OPCION 3) GÉNERO
    @staticmethod
    def _filtrar(catalogo) -> None:
        genero = input("Género: ").strip()
        resultados = catalogo.filtrar(genero)
        if resultados:
            for manga in resultados:
                print(("\n" f"- [bold indian_red]Nombre: [/bold indian_red] {manga.nombre} - [bold hot_pink3]Artista: [/bold hot_pink3] {manga.artista} - [bold light_pink3]Otros géneros:[/bold light_pink3] {manga.genero}""\n"))
        else:
            print(("\n" f"No hay mangas del género '{genero}'." "\n"))


    # OPCION 4) RECOMENDADOR
    @staticmethod
    def _recomendar_manga(recomendador, catalogo,arbol_avl):
        nombre_manga = input("→ Ingresá el nombre de un manga para hacer una recomendación: ").strip()
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
            print(f"\n Mangas recomendados basados en [bold indian_red]{manga_encontrado.nombre}[/bold indian_red]:\n")
            for i, manga in enumerate(recomendaciones, 1):
                print(f"{i}. [bold indian_red]{manga.nombre}[/bold indian_red] ( {manga.genero} ) -[bold hot_pink3] Artista: [/bold hot_pink3]{manga.artista} ([bold light_pink3]{manga.año})[/bold light_pink3]")

    # OPCION 5) TOP 5
    
    @staticmethod
    def _top_5_rating(catalogo) -> None:

        print(("\n[bold hot_pink3]TU TOP 5:[/bold hot_pink3]"))
        print(("[bold light_pink3]1.[/bold light_pink3] Por año"))
        print(("[bold light_pink3]2.[/bold light_pink3] Por género\n"))

        sub_opcion = Prompt.ask("[bold indian_red] → Ingresá 1 o 2 [/bold indian_red]").strip()

        if sub_opcion == "1":
            año = int(Prompt.ask("[bold indian_red] → Ingresá el año [/bold indian_red]").strip())
            candidatos = [m for m in catalogo.listar() if m.año == año]
            titulo = f"TOP 5 (Año {año}):"

        elif sub_opcion == "2":
            print(("\n[bold indian_red]GÉNEROS PRINCIPALES:[/bold indian_red]"))
            print(("[bold hot_pink3]1.[/bold hot_pink3] Shonen"))
            print(("[bold hot_pink3]2.[/bold hot_pink3] Shojo"))
            print(("[bold hot_pink3]3.[/bold hot_pink3] Seinen"))
            print(("[bold hot_pink3]4.[/bold hot_pink3] Josei\n"))

            op_genero = Prompt.ask("[bold indian_red] → Ingresá un número del 1 al 4 [/bold indian_red]").strip()
            generos = {"1": "Shonen", "2": "Shojo", "3": "Seinen", "4": "Josei"}

            if op_genero not in generos:
                print(("\n[bold hot_pink3]⚠️  Opción inválida! Intente nuevamente ⚠️[/bold hot_pink3]"))
                return

            genero_elegido = generos[op_genero]
            candidatos = [m for m in catalogo.listar() if genero_elegido.lower() in m.genero.lower()]
            titulo = f"\nTOP 5 (Género {genero_elegido}):"

        else:
            print(("\n[bold hot_pink3]⚠️  Opción inválida! Intente nuevamente ⚠️[/bold hot_pink3]"))
            return

        if len(candidatos) == 0:
            print(("\n[bold dark_orange3]No se encontraron mangas para esa opción.[/bold dark_orange3]"))
            return

        heap = MaxHeap()
        for i, manga in enumerate(candidatos):
            heap.insert((manga.rating, manga.nombre.lower(), i, manga))

        top_5 = []
        while len(heap.heap) > 0 and len(top_5) < 5:
            _, _, _, manga = heap.extract_max()
            top_5.append(manga)
            top_5.sort(key=lambda m: (-m.rating, m.nombre.lower()))

        print((f"[bold hot_pink3]{titulo}[/bold hot_pink3]"))
        for pos, manga in enumerate(top_5, start=1):
            print((f"[bold dark_orange3]{pos}.[/bold dark_orange3] [bold]{manga.nombre}[/bold] - Rating: [bold hot_pink3]{manga.rating}[/bold hot_pink3]"))
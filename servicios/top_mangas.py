from estructuras.heap_max import MaxHeap

class TopMangas:
    
    @staticmethod
    def mostrar_top_5(catalogo) -> None:
        print("\n--- TOP 5 ---")
        print("1. Por año")
        print("2. Por gran género")
        opcion = input("Elegí 1 o 2: ").strip()
        GRANDES_GENEROS = [
                "Shonen",
                "Seinen",
                "Shojo",
                "Josei",
                ]
        
        candidatos = []
        mangas = catalogo.listar()
        filtro_texto = ""

        if opcion == "1":
            año_input = int(input("Ingresá un número de año (ej: 1994): ").strip())
            filtro_texto = f"Año {año_input}"

            for manga in mangas:
                if manga.año == año_input:
                    candidatos.append(manga)

        elif opcion == "2":
            print("\nElegí un Género para tu TOP 5:")
            print("1. Shonen")
            print("2. Shojo")
            print("3. Seinen")
            print("4. Josei")

            op_genero = input("Ingresá un número del 1 al 4: ").strip()

            if op_genero == "1":
                genero_elegido = "Shonen"
            elif op_genero == "2":
                genero_elegido = "Shojo"
            elif op_genero == "3":
                genero_elegido = "Seinen"
            elif op_genero == "4":
                genero_elegido = "Josei"
            else:
                print("Opción de género inválida.")
                return

            filtro_texto = f"Género {genero_elegido}"

            for manga in mangas:
                if genero_elegido.lower() in manga.genero.lower():
                    candidatos.append(manga)

        else:
            print("Opción inválida.")
            return

        if len(candidatos) == 0:
            print(f"No hay mangas para {filtro_texto}.")
            return

        heap = MaxHeap()
        for i, manga in enumerate(candidatos):
            heap.insert((manga.rating, manga.nombre.lower(), i, manga))

        top_5 = []
        while len(heap.heap) > 0 and len(top_5) < 5:
            _, _, _, manga = heap.extract_max()
            top_5.append(manga)

        top_5.sort(key=lambda m: (-m.rating, m.nombre.lower()))

        print(f"\nTOP 5 ({filtro_texto}):")
        for puesto, manga in enumerate(top_5, start=1):
            print(f"{puesto}. {manga.nombre} - Rating: {manga.rating} - {manga.genero} ({manga.año})")
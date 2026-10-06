from servicios.catalogo import Catalogo

class Terminal:
    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo

    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = input("Opción: ").strip()
            if opcion == "1":
                self._buscar()
            elif opcion == "2":
                self._listar()
            elif opcion == "3":
                self._filtrar()
            elif opcion == "0":
                print("¡Hasta la próxima!")
                break
            else:
                print("Opción inválida.")
            print()
            

    def _mostrar_menu(self) -> None:
        print("=" * 40)
        print(" OÍD MORTALES — TERMINAL (v1)")
        print("=" * 40)
        print("1. Buscar canción por nombre")
        print("2. Listar todas las canciones")
        print("3. Filtrar por género")
        print("0. Salir")
        print("-" * 40)

    def _buscar(self) -> None:
        nombre = input("Nombre de la canción: ").strip()
        resultado = self._catalogo.buscar(nombre)
        if resultado:
            print(f"Encontrada: {resultado}")
        else:
            print(f"No encontramos '{nombre}'.")

    def _listar(self) -> None:
        for cancion in self._catalogo.listar():
            print(f"- {cancion}")

    def _filtrar(self) -> None:
        genero = input("Género: ").strip()
        resultados = self._catalogo.filtrar(genero)
        if resultados:
            for cancion in resultados:
                print(f"- {cancion}")
        else:
            print(f"No hay canciones del género '{genero}'.")
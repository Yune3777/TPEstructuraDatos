from servicios.catalogo import Catalogo
from ui.terminal import Terminal
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral

def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/dataset_mangas_1000.json")

    arbol_avl = AVL()
    for elemento in catalogo.listar():
        arbol_avl.insertar(elemento, clave= lambda e: e.nombre.lower())

    arbol_general = ArbolGeneral()
    arbol_general.cargar_generos()

    terminal = Terminal(catalogo, arbol_avl)
    terminal.iniciar()




if __name__ == "__main__":
    main()
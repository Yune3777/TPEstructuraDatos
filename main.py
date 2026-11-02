from servicios.catalogo import Catalogo
from ui.terminal import Terminal
from estructuras.avl import ArbolAvl
from estructuras.arbol_general import ArbolGeneral
from servicios.recomendador import AdminGrafos

def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/dataset_mangas_1000.json")

    arbol_avl = ArbolAvl()
    for elemento in catalogo.listar():
        arbol_avl.insertar(elemento, clave= lambda e: e.nombre.lower())

    arbol_general = ArbolGeneral()
    arbol_general.cargar_generos()

    recomendador = AdminGrafos(catalogo)

    servicios = {
        "recomendador" : recomendador,
        #"top_mangas" : top_mangas,
    }
    estructuras = {
        "arbol_general" : arbol_general,
        "arbol_avl" : arbol_avl,
    }

    terminal = Terminal(catalogo, servicios, estructuras)
    terminal.iniciar()




if __name__ == "__main__":
    main()
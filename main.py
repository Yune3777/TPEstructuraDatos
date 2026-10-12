from servicios.catalogo import Catalogo
from ui.terminal import Terminal
from estructuras.arbol_binario import ArbolBST

def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/dataset_mangas_10.json")
    
    arbol = ArbolBST()
    for elemento in catalogo.listar():
            arbol.insertar(elemento, clave= lambda e: e.nombre.lower())
            
    terminal = Terminal(catalogo, arbol)
    terminal.iniciar()

if __name__ == "__main__":
    main()


    
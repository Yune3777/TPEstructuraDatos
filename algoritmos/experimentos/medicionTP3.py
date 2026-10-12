import time
import timeit
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from servicios.catalogo import Catalogo
from estructuras.arbol_binario import ArbolBST

def main() -> None:
    tamaños = (10, 100, 1000, 10000)
    print("tamaño\tsecuencial_ms\tbinaria_ms\tarbol_ms")

    for n in tamaños:
        catalogo = Catalogo()
        catalogo.cargar_desde_json(f"datos/dataset_mangas_{n}.json")
        
    
        nombre_probe = f"Manga {n - 1}"
        lista_mangas = catalogo.listar()
        
        t_arbol = medir_arbol(lista_mangas, nombre_probe)

        catalogo.ordenar_por_nombre()
        t_sec = min(timeit.repeat(lambda: catalogo.buscar(nombre_probe), number=20, repeat=5)) / 20 * 1000
        t_bin = min(timeit.repeat(lambda: catalogo.buscar_binaria(nombre_probe), number=20, repeat=5)) / 20 * 1000
        
        print(f"{n}\t{t_sec:.4f}\t\t{t_bin:.4f}\t\t{t_arbol:.4f}")

def medir_arbol(lista, nombre):
    """Mide la búsqueda en árbol sobre la lista dada."""
    arbol = ArbolBST()
    for e in lista: 
        arbol.insertar(e, clave=lambda e: e.nombre.lower()) 
    inicio = time.time() 
    _ = arbol.buscar(nombre.lower(), clave= lambda e: e.nombre.lower()) 
    fin = time.time()
    return (fin - inicio) * 1000 # milisegundos


if __name__ == "__main__":
    main()
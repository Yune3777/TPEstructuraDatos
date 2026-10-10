import timeit
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from servicios.catalogo import Catalogo


def main() -> None:
    tamaños = (10, 100, 1000, 10000)
    print("tamaño\tsecuencial_ms\tbinaria_ms")

    for n in tamaños:
        catalogo = Catalogo()
        catalogo.cargar_desde_json(f"datos/genesongs_{n}.json")
        catalogo.ordenar_por_nombre()
    
        nombre_probe = f"Cancion {n - 1}"

        t_sec = min(timeit.repeat(lambda: catalogo.buscar(nombre_probe), number=20, repeat=5)) / 20 * 1000
        t_bin = min(timeit.repeat(lambda: catalogo.buscar_binaria(nombre_probe), number=20, repeat=5)) / 20 * 1000
        
        print(f"{n}\t{t_sec:.4f}\t\t{t_bin:.4f}")

if __name__ == "__main__":
    main()
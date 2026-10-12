import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from estructuras.arbol_binario import ArbolBST

class Elemento:

    def __init__(self, nombre, rating):
        self.nombre = nombre
        self.rating = rating
    
    def __repr__(self):
        return f"{self.nombre}(rating{self.rating})"
    
def main():
    arbol = ArbolBST()
    # Lo construimos SIN orden, para que el árbol ordene solo
    datos = [ Elemento("Erased", 8.52), 
        Elemento("Vagabond", 8.86), 
        Elemento("Claymore", 8.39), 
        Elemento("Berserk", 9.24), 
        Elemento("Rurouni Kenshin", 8.72),]
    
    for d in datos: 
        arbol.insertar(d, clave=lambda e: e.nombre.lower())
    
    print("Altura del árbol:", arbol.altura())
    
    print("\n--- inorder (ordenado alfabéticamente) ---")
    for e in arbol.inorder():
        print(" ", e)
    
    print("\n--- preorder ---")
    for e in arbol.preorder():
        print(" ", e.nombre)
    
    print("\n--- postorder ---")
    for e in arbol.postorder():
        print(" ", e.nombre)
    
    print("\n--- búsquedas ---") 
    encontrado = arbol.buscar("rurouni kenshin", clave=lambda e: e.nombre.lower())
    print("Buscar 'rurouni kenshin':", encontrado) 
    no_encontrado = arbol.buscar("zzz", clave=lambda e: e.nombre.lower())
    print("Buscar 'zzz':", no_encontrado)

if __name__ == "__main__":
    main()
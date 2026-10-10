class NodoArbol:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.informacion = dato


def arbol_vacio(raiz):
    return raiz == None

def insertar_nodo(raiz, dato): # devuelve un nodo de árbol
    if arbol_vacio(raiz):
        raiz = NodoArbol(dato)
    elif (raiz.informacion <= dato):
        raiz.derecha = insertar_nodo(raiz.derecha, dato)
    else:
        raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
    return raiz

def imprimir_arbol(raiz):
    if arbol_vacio(raiz):
        print(" - ")
    else:
        print(raiz.informacion)
        print(F"Visitando IZQUIERDA del nodo {raiz.informacion}")
        imprimir_arbol(raiz.izquierda)
        print(F"Visitando DERECHA del nodo {raiz.informacion}")
        imprimir_arbol(raiz.derecha)


class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho =None
        
class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato, clave):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato, clave)

    def _insertar_recursivo(self, nodo, dato, clave):
        if clave(dato) < clave(nodo.dato):
            if nodo.izquierdo is None: 
                nodo.izquierdo = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.izquierdo, dato, clave)
        else:
            if nodo.derecho is None: 
                nodo.derecho = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.derecho, dato, clave)

    def buscar(self, valor, clave):
        return self._buscar_recursivo(self.raiz, valor, clave)

    def _buscar_recursivo(self, nodo, valor, clave):
        if nodo is None:
            return None
        valor_nodo = clave(nodo.dato)
        if valor == valor_nodo:
            return nodo.dato
        if valor < valor_nodo:
            return self._buscar_recursivo(nodo.izquierdo, valor, clave)
        return self._buscar_recursivo(nodo.derecho, valor, clave)

    def inorder (self):
        return self._recorrer(self._inorder_recursivo, self.raiz)

    def preorder(self):
        return self._recorrer(self._preorder_recursivo, self.raiz)

    def postorder(self):
        return self._recorrer(self._postorder_recursivo, self.raiz)

    def _recorrer(self, funcion, nodo):
            resultado = []
            funcion(nodo, resultado)
            return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierdo, resultado) 
            resultado.append(nodo.dato)
            self._inorder_recursivo(nodo.derecho, resultado)

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None: 
            resultado.append(nodo.dato)
            self._preorder_recursivo(nodo.izquierdo, resultado)
            self._preorder_recursivo(nodo.derecho, resultado)


    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierdo, resultado)
            self._postorder_recursivo(nodo.derecho, resultado) 
            resultado.append(nodo.dato)


    def altura(self):
        """Profundidad máxima del árbol. Árbol vacío → 0."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursiva(nodo.izquierdo),
                       self._altura_recursiva(nodo.derecho))

    def esta_vacio(self):
        return self.raiz is None
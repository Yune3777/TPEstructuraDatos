class NodoAVL:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None


    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _factor_balance(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izquierdo),
                              self._altura(nodo.derecho))

    def _rotacion_izquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo

        y.izquierdo = z
        z.derecho = T2

        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y

    def _rotacion_derecha(self, z):
        y = z.izquierdo
        T2 = y.derecho

        y.derecho = z
        z.izquierdo = T2

        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y

    def _rotacion_izquierda_derecha(self, nodo):
        nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
        return self._rotacion_derecha(nodo)

    def _rotacion_derecha_izquierda(self, nodo):
        nodo.derecho = self._rotacion_derecha(nodo.derecho)
        return self._rotacion_izquierda(nodo)

    def insertar(self, dato, clave):
        self.raiz = self._insertar_recursivo(self.raiz, dato, clave)

    def _insertar_recursivo(self, nodo, dato, clave):
        if nodo is None:
            return NodoAVL(dato)

        if clave(dato) < clave(nodo.dato):
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, dato, clave)
        elif clave(dato) > clave(nodo.dato):
            nodo.derecho = self._insertar_recursivo(nodo.derecho, dato, clave)
        else:
            return nodo

        self._actualizar_altura(nodo)

        balance = self._factor_balance(nodo)

        if balance > 1 and clave(dato) < clave(nodo.izquierdo.dato):
            return self._rotacion_derecha(nodo)

        if balance < -1 and clave(dato) > clave(nodo.derecho.dato):
            return self._rotacion_izquierda(nodo)

        if balance > 1 and clave(dato) > clave(nodo.izquierdo.dato):
            return self._rotacion_izquierda_derecha(nodo)

        if balance < -1 and clave(dato) < clave(nodo.derecho.dato):
            return self._rotacion_derecha_izquierda(nodo)

        return nodo

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


    def buscar_palabra(self, subcadena, clave):
        resultados = []
        self.buscar_palabra_recursivo(self.raiz, subcadena.lower(),clave, resultados)
        return resultados

    def buscar_palabra_recursivo(self, nodo, subcadena, clave, resultados):
        if nodo is None:
            return
        self.buscar_palabra_recursivo(nodo.izquierdo, subcadena, clave, resultados)
        texto_nodo = clave(nodo.dato)
        if subcadena in texto_nodo:
            resultados.append(nodo.dato)
        self.buscar_palabra_recursivo(nodo.derecho, subcadena, clave, resultados)


    def inorder(self):
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorder_recursivo(nodo.derecho, resultado)

    def preorder(self):
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preorder_recursivo(nodo.izquierdo, resultado)
            self._preorder_recursivo(nodo.derecho, resultado)

    def postorder(self):
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierdo, resultado)
            self._postorder_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.dato)

    def altura(self):
        return self._altura(self.raiz)

    def esta_vacio(self):
        return self.raiz is None

    def __len__(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)

def comparar_bst_vs_avl(lista_datos, clave):
    import time

    try:
        from arbol_binario import ArbolBST
    except ImportError:
        try:
            from estructuras.arbol_binario import ArbolBST
        except ImportError:
            return {"error": "No se encontró arboles.py para comparar"}

    bst = ArbolBST()
    for d in lista_datos:
        bst.insertar(d, clave=clave)

    # --- AVL ---
    avl = AVL()
    for d in lista_datos:
        avl.insertar(d, clave=clave)

    # Medir tiempo de búsqueda en ambos
    valor_test = clave(lista_datos[0])

    inicio = time.time()
    for _ in range(1000):
        bst.buscar(valor_test, clave=clave)
    tiempo_bst = (time.time() - inicio) * 1000

    inicio = time.time()
    for _ in range(1000):
        avl.buscar(valor_test, clave=clave)
    tiempo_avl = (time.time() - inicio) * 1000

    return {
        "altura_bst": bst.altura(),
        "altura_avl": avl.altura(),
        "tiempo_bst_ms": tiempo_bst,
        "tiempo_avl_ms": tiempo_avl,
        "mejor_balance": avl.altura() < bst.altura(),
    }


if __name__ == "__main__":
    
    
    class Elemento:
        def __init__(self, nombre, valor):
            self.nombre = nombre
            self.valor = valor

        def __repr__(self):
            return f"{self.nombre}({self.valor})"

    datos = [
        Elemento("Berserk", 1),
        Elemento("Monster", 2),
        Elemento("Nausicaa", 3),
        Elemento("JoJo's Bizarre Adventure", 4),
        Elemento("Vinland Saga", 5),
        Elemento("Yokohama Kaidashi Kikou", 6),
        Elemento("20th Century Boys", 7),
        Elemento("Fullmetal Alchemist", 8),
        Elemento("Akira", 9),
        Elemento("Yotsuba&!", 10),
    ]

    # AVL
    avl = AVL()
    for d in datos:
        avl.insertar(d, clave=lambda x: x.nombre.lower())

    print("=== AVL con datos ordenados ===")
    print("Altura del AVL:", avl.altura())
    print("Cantidad de nodos:", len(avl))
    print()

    print("--- inorder ---")
    for e in avl.inorder():
        print(" ", e)

    print()
    print("--- preorder (muestra el balance) ---")
    for e in avl.preorder():
        print(" ", e)

    print()
    print("Buscar 'Yokohama Kaidashi Kikou':", avl.buscar("yokohama kaidashi kikou", clave=lambda x: x.nombre.lower()))
    print("Buscar 'Sailor Moon':", avl.buscar("sailor moon", clave=lambda x: x.nombre.lower()))

    # Comparar con BST
    print("\n=== Comparación BST vs AVL ===")
    resultado = comparar_bst_vs_avl(datos, clave=lambda x: x.nombre.lower())
    if "error" in resultado:
        print("  ", resultado["error"])
    else:
        print(f"  Altura BST: {resultado['altura_bst']}")
        print(f"  Altura AVL: {resultado['altura_avl']}")
        print(f"  BST es más alto que AVL: {resultado['mejor_balance']}")

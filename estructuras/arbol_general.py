class NodoGeneral:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def __repr__(self):
        return f"Nodo({self.dato})"

		
class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def insertar_raiz(self, dato):
        self.raiz = NodoGeneral(dato)
        return self.raiz
		
    def agregar_hijo(self, nodo_padre, dato):
        if nodo_padre is None and self.raiz is None:
            raise ValueError("El árbol no tiene raíz. Use insertar_raiz primero.")

        nuevo_nodo = NodoGeneral(dato)
        nodo_padre.hijos.append(nuevo_nodo)
        return nuevo_nodo

    def buscar(self, valor):
        if self.raiz is None:
            return None

        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            if actual.dato == valor:
                return actual
            cola.extend(actual.hijos)
        return None

    def buscar_recursivo(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return None
        if nodo.dato == valor:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_recursivo(valor, hijo)
            if resultado is not None:
                return resultado
        return None
	
    def amplitud(self):
        if self.raiz is None:
            return []
        
        resultado = []
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            resultado.append(actual.dato)
            cola.extend(actual.hijos)
        return resultado

    def profundidad_preorder(self, nodo=None, resultado=None):
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado

        resultado.append(nodo.dato)
        for hijo in nodo.hijos:
            self.profundidad_preorder(hijo, resultado)
        return resultado

    def profundidad_postorder(self, nodo=None, resultado=None):
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado

        for hijo in nodo.hijos:
            self.profundidad_postorder(hijo, resultado)
        resultado.append(nodo.dato)
        return resultado

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)

    def cantidad_nodos(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        return 1 + sum(self.cantidad_nodos(hijo) for hijo in nodo.hijos)

    def es_vacio(self):
        return self.raiz is None

    def listar_hijos(self, nodo):
        return [hijo.dato for hijo in nodo.hijos]

    def obtener_niveles(self):
        if self.raiz is None:
            return []

        niveles = []
        nivel_actual = [self.raiz]
        while nivel_actual:
            niveles.append([n.dato for n in nivel_actual])
            siguiente = []
            for nodo in nivel_actual:
                siguiente.extend(nodo.hijos)
            nivel_actual = siguiente
        return niveles

    def __repr__(self):
        if self.raiz is None:
            return "Árbol General vacío"
        return f"Árbol General (raíz: {self.raiz.dato}, altura: {self.altura()})"

    def cargar_generos(self):
        nodo_categ=self.insertar_raiz("Mangas")
        self.agregar_hijo(nodo_categ, "Seinen")
        self.agregar_hijo(nodo_categ, "Shojo")
        self.agregar_hijo(nodo_categ, "Shonen")
        self.agregar_hijo(nodo_categ, "Josei")
        return nodo_categ
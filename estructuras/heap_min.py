class MinHeap:
    def __init__(self):
        self._elementos = []

    def esta_vacio (self):
        return len(self._elementos) == 0

    def __len__(self):
        return len(self._elementos)

    def consultar_minimo(self):
        if self.esta_vacio():
            raise IndexError("El heap está vacío")
        return self._elementos[0]

    def insertar(self, valor):
        self._elementos.append(valor)
        self._subir(len(self._elementos) - 1)

    def extraer_minimo(self):
        if self.esta_vacio():
            raise IndexError("El heap está vacío")

        minimo = self._elementos[0]
        ultimo = self._elementos.pop()

        if not self.esta_vacio():
            self._elementos[0] = ultimo
            self._bajar(0)

        return minimo

    def _subir(self, indice):
        while indice > 0:
            padre = (indice -1) // 2

            if self._elementos[padre]<= self._elementos[indice]:
                break

            self._intercambiar(padre,indice)
            indice = padre

    def _bajar(self, indice):
        cantidad = len(self._elementos)

        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            menor = indice

            if(izquierdo<cantidad and self._elementos[izquierdo] < self._elementos)[menor]:
                menor=izquierdo
            if(derecho<cantidad and self._elementos[derecho] < self._elementos)[menor]:
                menor = derecho
            if menor == indice:
                break

            self._intercambiar(indice,menor)
            indice = menor

    def _intercambiar(self,i,j):
        self._elementos[i], self._elementos[j] = self._elementos[j], self._elementos[i]
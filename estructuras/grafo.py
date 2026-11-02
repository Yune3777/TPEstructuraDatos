class GrafoMatriz:
    def __init__(self, n, dirigido = False):
        self.n = n
        self.dirigido = dirigido
        self.matriz = [[0] * n for _ in range (n)]

    def agregar_arista (self, u, v, peso=1):
        self.matriz[u][v] = peso
        if not self.dirigido:
            self.matriz[v][u] = peso

    def eliminar_arista (self, u, v):
        self.matriz[u][v] = 0
        if not self.dirigido:
            self.matriz[v][u] = 0

    def hay_arista(self, u, v):
        return self.matriz[u][v] !=0

    def vecinos(self, u):
        return [v for v in range(self.n) if self.matriz[u][v !=0]]

    def mostrar(self):
        for fila in self.matriz:
            print(fila)


class GrafoLista:
    def __init__(self, n, dirigido = False):
        self.n = n
        self.dirigido = dirigido
        self.adj = {i: {} for i in range (n)}

    def agregar_arista (self, u, v, peso=1):
        self.adj[u][v] = peso
        if not self.dirigido:
            self.adj[u][v] = peso
            
    def eliminar_arista(self, u, v):
        self.adj[u].pop(v, None)
        if not self.dirigido:
            self.adj[v].pop (u, None)

    def hay_arista(self, u, v):
        return v in self.adj[u]

    def vecinos(self,u):
        return list(self.adj[u])

    def mostrar(self):
        for u, vecinos in self.adj.items():
            print(f'{u} -> {list(vecinos.items())}')

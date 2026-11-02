    # Recursivo: la pila de llamadas hace de pila
def dfs(grafo, inicio, vistos=None):
    if vistos is None:
        vistos = set()
    vistos.add(inicio)
    orden = [inicio]
    for w in grafo[inicio]:
        if w not in vistos:
            orden += dfs(grafo, w, vistos)
    return orden

# Iterativo: pila explícita, vecinos en orden inverso
def dfs_iter(grafo, inicio):
    pila = [inicio]
    vistos = set()
    orden = []
    while pila:
        v = pila.pop()
        if v in vistos:
            continue
        vistos.add(v)
        orden.append(v)
        for w in reversed(grafo[v]):
            if w not in vistos:
                pila.append(w)
    return orden
from collections import deque

def bfs_camino(grafo, inicio, destino):
    padre = {inicio: None}
    cola = deque([inicio])
    while cola:
        v = cola.popleft()
        if v == destino:
            break
        for w in grafo[v]:
            if w not in padre:      # "padre" tambien puedo ponerle "visitados"
                padre[w] = v
                cola.append(w)
    if destino not in padre:
        return None, []            # no hay camino
    camino = []
    v = destino
    while v is not None:
        camino.append(v)
        v = padre[v]
    return camino[::-1], padre

def bfs_recomendaciones(grafo, inicio, limite=5):
    recomendados = []
    visitados = {inicio}
    cola = deque([inicio])
    
    while cola and len(recomendados) < limite:
        v = cola.popleft()

        for w in grafo.adj[v]:
            if w != inicio and w not in visitados:
                visitados.add(w)
                cola.append(w)
                recomendados.append(w)
                if len(recomendados) >= limite:
                    break
    return recomendados
from estructuras.grafo import GrafoLista
from algoritmos.bfs import bfs_camino
from algoritmos.bfs import bfs_recomendaciones
from algoritmos.dfs import dfs_iter

class AdminGrafos:
    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.lista_mangas = self.catalogo.listar()
        self.grafo = self._armar_red()

    def _armar_red(self):
        n = len(self.lista_mangas)
        grafo_manga = GrafoLista(n, dirigido=False)
        for i in range (n):
            for j in range(i + 1, n):
                m1 = self.lista_mangas[i]
                m2 = self.lista_mangas[j]
                
                if m1.genero == m2.genero:
                    grafo_manga.agregar_arista(i,j)
                elif m1.artista == m2.artista:
                    grafo_manga.agregar_arista(i,j)
                elif m1.año == m2.año:
                    grafo_manga.agregar_arista(i,j)

        return grafo_manga

    def recomendar_con_bfs(self, inicio, limite=5):
        indices_recomendados = bfs_recomendaciones(self.grafo, inicio, limite*15)
        mangas_recomendados = [self.lista_mangas[idx] for idx in indices_recomendados]
        manga_base = self.lista_mangas[inicio]
        
        def prioridad(manga_recomendado):
            comparte_artista = manga_base.artista.strip().lower() == manga_recomendado.artista.strip().lower()
            comparte_año = manga_base.año == manga_recomendado.año
            comparte_genero = any(g.strip().lower() in manga_recomendado.genero.lower() for g in manga_base.genero.split('/'))
            return (not comparte_artista, not comparte_año, not comparte_genero)
        mangas_recomendados.sort(key=prioridad)
        return mangas_recomendados[:limite]
            
    

    def recomendar_con_dfs(self, inicio):
        orden = dfs_iter(self.grafo.adj, inicio)
        return [self.lista_mangas[idx] for idx in orden]
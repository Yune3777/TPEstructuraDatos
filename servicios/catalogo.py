import json
import sys
import os
import random
import bisect
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelos.manga import Manga


class Catalogo:
    def __init__(self) -> None:
        self._elementos: list[Manga] = []
    
    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, 'r', encoding='utf-8') as mangas:
            catalogo = json.load(mangas)
        for item in catalogo["mangas"]:
            self._elementos.append(
                Manga(item["nombre"], item["genero"], item["artista"], item["rating"], item["año"])
            )
                

    def ordenar_por_nombre(self) -> None:
        self._elementos.sort(key=lambda p: p.nombre.lower())

    def buscar_binaria(self, nombre: str):
        claves = [p.nombre.lower() for p in self._elementos]
        indice = bisect.bisect_left(claves, nombre.lower())
        if indice < len(claves) and claves[indice] == nombre.lower():
            return self._elementos[indice]
        return None
    
    def buscar(self, nombre: str) -> Manga | None:
        for manga in self._elementos:
            if manga.nombre.lower() == nombre.lower():
                return manga
        return None



    def manga_aleatorio(self) -> Manga:
        return random.choice(self._elementos)

    def listar(self) -> list[Manga]:
        return list(self._elementos)
    
    def filtrar(self, genero: str) -> list[Manga]:
        return [
            manga for manga in self._elementos
            if genero.lower() in manga.genero.lower()
        ]
    
    def __len__(self) -> int:
        return len(self._elementos)


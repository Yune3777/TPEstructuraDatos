import json
import sys
import os
import random
import bisect
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelos.cancion import Cancion


class Catalogo:
    def __init__(self) -> None:
        self._elementos: list[Cancion] = []
    
    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, 'r', encoding='utf-8') as canciones:
            catalogo = json.load(canciones)
        for item in catalogo["temas"]:
            self._elementos.append(
                Cancion(item["nombre"], item["genero"], item["artista"], item["rating"], item["año"], item["idioma"])
            )
                

    def ordenar_por_nombre(self) -> None:
        self._elementos.sort(key=lambda p: p.nombre.lower())

    def buscar_binaria(self, nombre: str):
        claves = [p.nombre.lower() for p in self._elementos]
        indice = bisect.bisect_left(claves, nombre.lower())
        if indice < len(claves) and claves[indice] == nombre.lower():
            return self._elementos[indice]
        return None
    
    def buscar(self, nombre: str) -> Cancion | None:
        for cancion in self._elementos:
            if cancion.nombre.lower() == nombre.lower():
                return cancion
        return None



    def cancion_aleatoria(self) -> Cancion:
        return random.choice(self._elementos)

    def listar(self) -> list[Cancion]:
        return list(self._elementos)
    
    def filtrar(self, genero: str) -> list[Cancion]:
        return [
            cancion for cancion in self._elementos
            if cancion.genero.lower() == genero.lower()
        ]
    
    def __len__(self) -> int:
        return len(self._elementos)


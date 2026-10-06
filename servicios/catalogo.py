import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelos.cancion import Cancion


class Catalogo:
    def __init__(self) -> None:
        self._elementos: list[Cancion] = []
    
    def cargar_desde_json(self, ruta: str) -> None:
        with open('datos/canciones_90s_10.json', 'r', encoding='utf-8') as canciones:
            catalogo = json.load(canciones) # Carga el contenido en un diccionario o lista
        for item in catalogo["temas"]:
            self._elementos.append(
                Cancion(item["nombre"], item["genero"], item["artista"], item["idioma"], item["año"])
            )
                
    
    def buscar(self, nombre: str) -> Cancion | None:
        for cancion in self._elementos:
            if cancion.nombre.lower() == nombre.lower():
                return cancion
        return None

    def listar(self) -> list[Cancion]:
        return list(self._elementos)
    
    def filtrar(self, genero: str) -> list[Cancion]:
        return [
            cancion for cancion in self._elementos
            if cancion.genero.lower() == genero.lower()
        ]
    
    def __len__(self) -> int:
        return len(self._elementos)


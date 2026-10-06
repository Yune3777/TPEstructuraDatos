class Cancion:

    def __init__(self, nombre: str, genero: str, artista: str, idioma: str, año: int):
        self._nombre = nombre
        self._genero = genero
        self._artista = artista
        self._idioma = idioma
        self._año = año
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def genero(self) -> str:
        return self._genero
    
    @property
    def artista(self) -> str:
        return self._artista
    
    @property
    def idioma(self) -> str:
        return self._idioma
    
    @property
    def año(self) -> int:
        return self._año

    
    def __repr__(self) -> str:
        return f"{self._nombre} ({self._genero}) ({self.artista}) ({self.idioma}) ({self.año})"
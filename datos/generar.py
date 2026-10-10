import json
import random

GENEROS = ["Rock", "Pop", "Grunge", "Electronica", "Dance", "Alternativo"]
ARTISTAS = ["Oasis", "Nirvana", "Madonna", "Red Hot Chili Peppers", "Radiohead", "Blur"]
IDIOMAS = ["Inglés", "Español"]
RATINGS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
AÑOS = list(range(1990, 1999))
NOMBRE = ["Say You'll Be There", "Wannabe", "Spice Up Your Life", "Stop", "Viva Forever", "Goodbye", "Holler", "Let Love Lead the Way", "Tell Me Why", "Never Give Up on the Good Times"]

def generar(n: int) -> None:
    temas = [
        {
            "nombre": random.choice(NOMBRE),
            "genero": random.choice(GENEROS),
            "artista": random.choice(ARTISTAS),
            "rating": round(random.uniform(1.0, 10.0), 1),
            "año": random.randint(1990, 1999),
            "idioma": random.choice(IDIOMAS)
        }
        for i in range(n)
    ]
    ruta = f"datos/genesongs_{n}.json"
    data_guardar = {"temas": temas}     
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(data_guardar, archivo, ensure_ascii=False, indent=2)

    print(ruta)

for n in (10, 100, 1000, 10000):
    generar(n)
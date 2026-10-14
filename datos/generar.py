import json
import random

GENEROS = ["Seinen","Shojo","Shonen", "Josei"]
ARTISTAS = ["Hayao Miyazaki","Hirohiko Araki", "Kentaro Miura", "Naoki Urasawa","Makoto Yukimura","Hitoshi Ashinano"]

def generar(n: int) -> None:
    mangas = [
    {
    "nombre": f"Manga {i}",
    "genero": random.choice(GENEROS),
    "artista": random.choice(ARTISTAS),
    "año": round(random.randint(1984, 2026)),
    "rating": round(random.uniform(1.0, 10.0), 1),}

    for i in range(n)
    ]
    
    ruta = f"datos/dataset_mangas_{n}.json"
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(mangas, archivo, ensure_ascii=False, indent=2)
    print(ruta)
    
for n in (10000, 50000):
    generar(n)
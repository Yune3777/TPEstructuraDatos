import json

# Carga el archivo base de 1000 elementos
with open('datos/dataset_mangas_1000.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Crear el archivo de 10 elementos
with open('mangas_10.json', 'w', encoding='utf-8') as f:
    json.dump(data[:10], f, ensure_ascii=False, indent=2)

# 2. Crear el archivo de 100 elementos
with open('mangas_100.json', 'w', encoding='utf-8') as f:
    json.dump(data[:100], f, ensure_ascii=False, indent=2)

# 3. Crear el archivo de 10,000 elementos (repitiendo 10 veces)
with open('mangas_10000.json', 'w', encoding='utf-8') as f:
    json.dump(data * 10, f, ensure_ascii=False, indent=2)

print("¡Los tres archivos (mangas_10.json, mangas_100.json y mangas_10000.json) se han generado con éxito!")
# 🌸 MANPY 🌸 


## Descripción del proyecto

Sistema de búsqueda y recomendación de mangas.

## Dominio elegido y justificación

- **Dominio elegido:** Se eligió el tema de mangas (historietas japonesas).
- **Justificación:** Se cuenta con gran cantidad de base de datos en internet que a su vez son gratuitas o que se pueden obtener por medio de APIs.

---

## Problema que resuelve

Una vez que el usuario termina un manga puede seguir leyendo otro que esté relacionado con el mismo género, o el mismo artista o si quiere estar al día con los mangas más rankeados en la actualidad.

##  Usuario objetivo

El usuario es una persona de unos 20 a 40 años, con gustos por la lectura. Prefieren historias profundas que no terminen en un solo capítulo. Suelen seguir al mismo autor. Eligen un género o géneros similares para seguir con el próximo manga.


## Requisitos
```bash
- Python 3.10 o superior.
- Librería `Rich` (especificada en el `requirements.md`).
```

## Pruebas
```bash
python -m unittest discover tests
```

## Instrucciones de ejecucion

1. Abrir la terminal en la carpeta del proyecto
2. Ejecutar el archivo principal con el siguiente comando:
```bash
python main.py
```

## Descripción detallada de las funcionalidades implementadas

### ️ Menú principal

```bash

- Búsqueda por Manga: introducir el nombre del manga para obtener todos los datos de él.
- Manga Aleatorio: se recomienda un manga aleatorio cualquiera.
- Explorar por Género: se escribe el género y devuelve mangas de ese género.
- Recomendaciones por similitud: introducir el nombre de un manga y devuelven mangas similares en cuanto a género o artista.
- Top 10: muestra el top 10 de los mejores mangas.

```

### Ejemplo de uso

```text
========================================
MANPY - TERMINAL
========================================
1. Búsqueda por Manga
2. Manga Aleatorio
3. Explorar por Género
4. Recomendaciones por similitud
5. Top 10
0. Salir
----------------------------------------
Opción: 1
El manga elegido fue: Dragon Ball y a continuación te cuento más sobre él...
"Dragon Ball" su artista es "Akira Toriyama". Su género es "Acción, fantasía" y se estrenó en el año 1984.
```

## Estructura del proyecto

```
├───algoritmos
│   ├───experimentos
│    │   ├──generador_graficos.py
│   │   ├──medicionTP2.py
│   │   ├──medicionTP3.py
│   │   ├──medicionTP4y5.py
│   │   ├──medicionTP6.py
│   │   ├──midetimeit.py
│   │   └───test unittest.py
│   ├── bfs.py
│   ├── busqueda.py
│   ├── busquedabinaria.py
│   ├── caminos.py
│   ├── dfs.py
│   └── probar_bst.py
│       
├───datos
│   ├── dataset_mangas_10.json
│   ├── dataset_mangas_100.json
│   └── dataset_mangas_10000.json
│       
├───docs
│   ├── Capturas
│   │   ├──Prueba de Grafos
│   │   │   ├──Paso01.PNG
│   │   │   ├──Paso02.PNG
│   │   │   └──Paso03.PNG
│   │   ├──diagrama de clases 01.png
│   │   ├──diagrama de clases 02.png
│   │   ├──diagrama de clases 03.png
│   │   ├──diagramde flujo 03.png
│   │   ├──experimento-tp2.png
│   │   ├──experimento-tp3.png
│   │   ├──experimento-tp4y5.png
│   │   ├──experimento-tp6.png
│   │   ├──tp1-menu-principal.png
│   │   ├──tp1-menu-principal3_Visual.png
│   │   └──tp1-menu-principal3_Powershell.png
│   ├──analisis_tp3.md
│   ├──analisis_tp4 y 5.md
│   ├──analisis_tp6.md
│   ├──casos_de_usos.md
│   ├──diagrama_clases.md
│   ├──diagrama_secuencia.md
│   ├──gestion_proyecto00.md
│   ├──Reportes.md
│   ├──requerimientos.md
│   ├──requerimientos.txt
│   └───tp2-experimentos.md
│       
├───estructuras
│   ├── arbol_binario.py
│   ├── arbol_general.py
│   ├── avl.py
│   ├── grafo.py
│   ├── heap_max.py
│   └── heap_min.py
│       
├───modelos
│   ├── manga.py
│   └── usuarios.py
│       
├───servicios
│   ├── carga_dataset.py
│   ├── catalogo.py
│   ├── opciones_menu.py
│   ├── recomendador.py
│   └── top_mangas.py
│       
├───ui
│    └───terminal.py
│
├───.gitignore
├───main.py
└── README.md


```
---
## 🌸 Integrante
* *Daiana Calderón*

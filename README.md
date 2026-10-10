# 🎧 OÍD MORTALES 🎧 


## 📝 Descripción del proyecto

Sistema de recomendación de música de los 90' que permite buscar, ordenar y descubrir canciones a partir de uno dado.

## 🎯 Dominio elegido y justificación

- **Dominio elegido:** Se eligió el tema de música de los 90'.
- **Justificación:** Al combinar una base de datos como lo es MusicBrainz, que tiene base de datos es 100% pública y descargables, y Spotify, que cuenta con filtros como año, géneros específicos, etc., sumado los charts de Billboards para poder ver los temas más rankeados, se puede llegar a la cantidad de 10.000 canciones pudiendo generar un dataset con los datos necesarios para poder usarlo en el proyecto.

---

## 🛠️ Problema que resuelve

En los 90' estaba la posibilidad de encontrar música o bandas extranjeras por recomendación del boca a boca. Hoy en día el acceso a esa música es más fácil pero con tanta información uno no sabe por dónde empezar, así que lo mejor es comenzar asociando lo que ya se conoce e ir expandiendo los horizontes, por ejemplo, con recomendaciones por género, por similitud en estilos entre artistas, etc.

## 🙋🏻‍♀️🙋🏻‍♂️ Usuario objetivo
El Usuario es lo que hoy consideran *"Millenials"*, que creció escuchando estas bandas y no las cambia a pesar de conocer otras nuevas, ya sea por nostalgia o por fanatismo. Es el que se queja cada vez que escucha lo que los jóvenes de hoy escuchan agregando la frase "la mejor época era la de los 90'". Es el que escribe "Nirvana" en el buscador de Youtube y espera que el logaritmo lo lleve a temas icónicos de esa década encontrando siempre los mismos temas. No se cansa de escucharlos pero le gustaría descubrir nuevos temas con la estética de esa época.


## ⚙️ Requisitos
```bash
- Python 3.10 o superior.
- Librería `Rich` (especificada en el `requirements.md`).
```


## 🚀 Instrucciones de ejecucion

1. Abrir la terminal en la carpeta del proyecto
2. Ejecutar el archivo principal con el siguiente comando:
```bash
python main.py
```

## ✨ Descripción detallada de las funcionalidades implementadas

### ️ Menú principal

```bash

- Búsqueda por Canción: introducir el nombre de la canción para obtener todos los datos de ella.
- Canción Aleatoria: se recomienda una canción aleatoria cualquiera.
- Explorar por Género: elegir el género y devuelve canciones de ese género.
- Recomendaciones por similitud: introducir el nombre de una canción y devuelven canciones similares en cuanto a género o artista.
- Top 10 por año: muestra el top 10 de las mejores canciones de cada año.

```

### Ejemplo de uso

```text
========================================
OÍD MORTALES - TERMINAL
========================================
1. Búsqueda por Canción
2. Canción Aleatoria
3. Explorar por Género
4. Recomendaciones por similitud
5. Top 10 por Año
0. Salir
----------------------------------------
Opción: 1
La canción elegida fue: Zombie y a continuación te cuento más sobre ella...
"Zombie" fue interpretada por "The Cranberries" en el idioma Inglés. Su género es Rock alternativo y es del año 1994.
```

## 📁 Estructura del proyecto

```
├───main.py
│   
├───algoritmos
│   ├── bfs.py
│   ├── busqueda.py
│   ├── caminos.py
│   └── dfs.py
│       
├───datos
│   ├── canciones_90s_10.json
│   ├── canciones_90s_100.json
│   └── canciones_90s_10000.json
│       
├───docs
│   ├── Diagrama de flujo.png
│   ├── README.md
│   └── Reportes.md
│       
├───estructuras
│   ├── arboles.py
│   ├── arbol_binario.py
│   ├── avl.py
│   ├── grafo.py
│   └── heap.py
│       
├───modelos
│   └── usuarios.py
│       
├───servicios
│   └── recomendador.py
│       
└───test
    └───Arboles
        ├── basearbol.py
        └── clasenodo.py
            

```
---
## 🤝 Integrantes
* *Antonela Bruno*
* *Daiana Calderón*

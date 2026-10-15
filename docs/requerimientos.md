# REQUERIMIENTOS - MANPY 

## 1. Alcance
El sistema permite un catálogo interactivo en consola para administrar mangas (historietas japonesas). Está pensada para personas de mediana edad, lectoras, que gustan de historias profundas y que suelen seguir el trabajo de los mismos artistas o eligen mangas con los mismos géneros.

## 2. Requisitos Funcionales (RF)
* **RF-01:** El sistema debe permitir la búsqueda de mangas por nombre.
* **RF-02:** El sistema debe listar el catálogo completo.

## 3. Requisitos No Funcionales (RNF)
| ID | Requerimiento | Verificación |
|---|---|---|
| RNF01 | La búsqueda por nombre debe ser logarítmica sobre el total de los elementos, en este caso mangas. | TP3+ (BST) |
| RNF02 | El sistema debe soportar al menos 10.000 mangas sin degradar la respuesta perceptiblemente | TP2 (experimentos) |
| RNF03 | La interfaz debe ser usable por alguien que no conoce la implementación | Demo |
| RNF04 | El proyecto debe ejecutarse con Python 3.10+ sin instalaciones extra | README |

## 4. Criterios de aceptación (ejemplo)
> **RF03 — Top 10**
> - Se muestran exactamente 10 resultados (o todos los que existan si son menos).
> - Orden descendente por rating, desempate alfabético.
> - Debería responder en menos de 1 segundo con 10.000 elementos.

## 5. Dependencias del Entorno
El proyecto requiere Python 3.10+ y las librerías listadas en `requirements.txt`.

## 6. Fuera de alcance
- Perfiles de usuario.
- Guardar preferencias.
- Crear listas de favoritos, leídos, pendientes o para leer en un futuro.
- Carga de imagenes ilustrativas.

## 7. Observaciones
Se tenía pensado hacer un bot de Telegram pero no creo poder hacerlo por el tiempo justo con el que cuento.
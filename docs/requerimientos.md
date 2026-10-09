# REQUERIMIENTOS - OÍD MORTALES 

## 1. Alcance
El sistema permite un catálogo interactivo en consola para administrar canciones de la década de los 90' y que está pensado para un usuario nacido entre los 80's y 90' que hayan crecido escuchando esta música y quieran seguir descubriendo temas de esa época.

## 2. Requisitos Funcionales (RF)
* **RF-01:** El sistema debe permitir la búsqueda de canciones por nombre.
* **RF-02:** El sistema debe listar el catálogo completo.

## 3. Requisitos No Funcionales (RNF)
| ID | Requerimiento | Verificación |
|---|---|---|
| RNF01 | La búsqueda por nombre debe ser logarítmica sobre el total de [elementos] | TP3+ (BST) |
| RNF02 | El sistema debe soportar al menos 10.000 [elementos] sin degradar la respuesta perceptiblemente | TP2 (experimentos) |
| RNF03 | La interfaz debe ser usable por alguien que no conoce la implementación | Demo |
| RNF04 | El proyecto debe ejecutarse con Python 3.10+ sin instalaciones extra | README |

## 4. Criterios de aceptación (ejemplo)
> **RF03 — Top 10**
> - Se muestran exactamente 10 resultados (o todos los que existan si son
menos).
> - Orden descendente por rating, desempate alfabético.
> - Responde en menos de 1 segundo con 10.000 elementos.

## 5. Dependencias del Entorno
El proyecto requiere Python 3.10+ y las librerías listadas en `requirements.txt`.

## 6. Fuera de alcance
- Autenticación o perfiles de usuario.
- Persistencia de preferencias.
- [Todo lo que no comprometás: escribirlo ahorra malentendidos]

## 7. Observaciones
[Decisiones del equipo que un revisor deba conocer: por qué tal estructura, qué
se descartó y por qué.]
# Gestión del proyecto
- Tablero: https://trello.com/b/0R9d1Ug0/oid-mortales-tp
- Metodología: Scrum simplificado — un sprint por TP con duración de 5 días. 
- Columnas: Pendientes - En proceso - Revisar - Hecho - Fuentes para consultar - Herramientas para TP

## Sprint TP00 (Lanzamiento)
- [x] Definir dominio y justificarlo
- [x] Buscar y crear dataset reales
- [x] Revisar que tenga la suficiente cantidad de datos máximos (10000)
- [x] Definir categorías con la que vamos a trabajar.
- [x] Revisar que las bases de datos cuenten con las categorías que vamos a trabajar
- [x] Crear base de datos con 10 elementos para usar en pruebas de los códigos
- [x] Crear base de datos con 50 elementos
- [x] Escribir propuesta de 1 página
- [x] Bocetar diagrama de clases inicial
- [x] Armar repositorio y README
- [-] Crear base de datos con 10.000 elementos

### Retro TP00
- La base de datos con 10.000 elementos está costando porque tengo cuenta gratuita con la IA y se limita las posibilidades de creación de un dataset fiel, real y completo sin errores.

## Sprint TP01
- [x] Encapsular las clases del dominio
- [x] Carga de datos desde JSON
- [x] Creación de la interfaz de terminal
- [x] Crear la operación de Buscar
- [x] Crear la operación de Listar
- [x] Crear la operación de Filtrar
- [x] Crear el catálogo
- [x] Crear el main
- [x] Crear el diagramde clases
- [x] Crear casos de usos
- [x] Actualizar README

### Retro TP00
- El menú es muy básico y sé que se puede mejorar usando la librería de Rich.

## Sprint TP02
- [x] Elegir dos operaciones críticas para las pruebas
- [x] Elegir dos estrategias distintas para compararlas con diferenes cantidades de elementos
- [x] Analizar cuál conviene más en cada situación
- [x] Usar BigO para las notaciones
- [x] Usar el generador para crear listas de diferentes tamaños
- [x] Crear la búsqueda binaria
- [x] Medir con `timeit`
- [x] Crear tabla con ls resultados
- [x] Instalar el entorno virtual para usar `matplotlib`
- [x] Crear gráficos de las pruebas
- [x] Anotar todas las conclusiones en un archivo `.md`


### Retro TP02
- Recordar usar el .gitignore para archivos y carpetas que sean para hacer pruebas.

## Sprint TP03
- [x] Creación del árbol binario
- [x] Acomodar el "Buscar" al árbol binario (antes era búsqueda lineal)
- [x] Hacer el testeo de comparacón entre árbol secuencial y árbol binario
- [x] Crear la documentación con las conclusiones a la que llegamos después de la comparación
- [x] Subir todo al repo

### Retro TP03
- Para evitar tener problemas de conflictos con ramas cuando se esté trabajando en GitHub hay que recordar de SIEMPRE hacer un pull primero y después el push.

## Sprint TP04
- [x] Incorporación de AVL y árbol general
- [x] Adaptar el AVL a la búsqueda por título
- [x] Adaptar el árbol general a la opción de "Buscar por Género"
- [x] Analizar la complejidad entre los dos

### Retro TP00
- En una de las pruebas surgió un problema: los mangas suelen recordarse generalmente por una palabra de todo su nombre (Ej.: a Neon Genesis Evangelion se lo recurda como Evangelion) por lo que se creó una función para buscar una palabra dentro del nombre. Así encontraríamos todos los posibles títulos entre los que estarían el que buscamos.
- El problema es que esta búsqueda tiene que recorrer todos los nodos, volviendo a una búsqueda lineal y desaprovechando los beneficios del AVL.
- Quizás, con alguna herramienta que veamos en próximas clases se pueda solucionar este problema. Por el momento quedará con una función de "for".


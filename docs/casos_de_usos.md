## Caso de uso: Buscar canción por título

- ***Actor:*** Usuario

- ***Precondición:*** El catálogo de canciones está cargado desde el archivo JSON.

- ***Flujo principal:*** 
    - El usuario selecciona la opción "Buscar canción por nombre" en el menú principal.
    - El sistema solicita el "nombre" de la canción a buscar.
    - El usuario ingresa el nombre de la canción.
    - El sistema busca la canción en el catálogo (sin distinguir mayúsculas/minúsculas ni acentos).
    - El sistema muestra los detalles de la canción encontrada (nombre, artista, año, género e idioma).

- ***Flujo alternativo:*** Si la canción no se encuentra en el catálogo, el sistema muestra un mensaje que dice que la canción no se encuentra en la lista.


## Caso de uso: Canción aleatoria
- ***Actor:*** Usuario

- ***Precondición:*** El catálogo de canciones está cargado desde el archivo JSON.

- ***Flujo principal:*** 
    - El usuario selecciona la opción "Canción Aleatoria".
    - El sistema recupera la lista completa de canciones registradas en el catálogo.
    - El sistema muestra una canción canción aleatoria mostrando nombre, artista, año, género e idioma.

- ***Flujo alternativo:*** Si el catálogo está vacío, el sistema muestra un mensaje de que no hay canciones disponibles para mostrar.


## Caso de uso: Explorar por Género
- ***Actor:*** Usuario

- ***Precondición:*** El catálogo de canciones está cargado desde el archivo JSON.

- ***Flujo principal:*** 
    - El usuario selecciona la opción "Explorar por género" en el menú principal.
    - El sistema busca el género musical que pide el usuario (ej. Rock argentino, Pop).
    - El usuario ingresa el género.
    - El sistema filtra las canciones que coincidan con dicho género (sin distinguir mayúsculas/minúsculas).
    - El sistema muestra la lista con el nombre de todas las canciones pertenecientes al género solicitado.

- ***Flujo alternativo:*** Si no existen canciones pertenecientes a ese género el sistema muestra un mensaje de que no existe ese género en la lista.
## Caso de uso: Buscar manga por título

- ***Actor:*** Usuario

- ***Precondición:*** El catálogo de mangas está cargado desde el archivo JSON.

- ***Flujo principal:*** 
    - El usuario selecciona la opción "Buscar manga por nombre" en el menú principal.
    - El sistema solicita el "nombre" del manga a buscar.
    - El usuario ingresa el nombre del manga.
    - El sistema busca el manga en el catálogo (sin distinguir mayúsculas/minúsculas ni acentos).
    - El sistema muestra los detalles del manga encontrado (nombre, artista, género y año).

- ***Flujo alternativo:*** Si el manga no se encuentra en el catálogo, el sistema muestra un mensaje que dice que el manga no se encuentra en la lista.


## Caso de uso: Manga aleatorio
- ***Actor:*** Usuario

- ***Precondición:*** El catálogo de mangas está cargado desde el archivo JSON.

- ***Flujo principal:*** 
    - El usuario selecciona la opción "Manga Aleatorio".
    - El sistema recupera la lista completa de mangas registrados en el catálogo.
    - El sistema muestra un manga aleatorio mostrando nombre, artista, año y género.

- ***Flujo alternativo:*** Si el catálogo está vacío, el sistema muestra un mensaje de que no hay mangas disponibles para mostrar.


## Caso de uso: Explorar por Género
- ***Actor:*** Usuario

- ***Precondición:*** El catálogo de mangas está cargado desde el archivo JSON.

- ***Flujo principal:*** 
    - El usuario selecciona la opción "Explorar por género" en el menú principal.
    - El sistema busca el género musical que pide el usuario (ej. Rock argentino, Pop).
    - El usuario ingresa el género.
    - El sistema filtra los mangas que coincidan con dicho género (sin distinguir mayúsculas/minúsculas).
    - El sistema muestra la lista con el nombre de todas los mangas pertenecientes al género solicitado.

- ***Flujo alternativo:*** Si no existen mangas pertenecientes a ese género el sistema muestra un mensaje de que no existe ese género en la lista.
classDiagram
    class OidMortales {
        - List~Cancion~ canciones
        + buscarPorCancion(titulo: String) List~Cancion~
        + obtenerCancionAleatoria() Cancion
        + obtenerTop10PorAnio(anio: int) List~Cancion~
        + obtenerRecomendacionesPorSimilitud(cancion: Cancion) List~Cancion~
    }

    class Cancion {
        - String titulo
        - int anio
    }

    OidMortales "1" *-- "*" Cancion : contiene





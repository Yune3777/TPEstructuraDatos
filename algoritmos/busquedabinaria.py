def binaria(lista, buscado): #Método de búsqueda binaria
    posicion = -1
    primero = 0
    ultimo = len(lista) - 1
    while (primero <= ultimo and posicion == -1):
        medio = (primero + ultimo) // 2
        if (lista[medio] == buscado):
            posicion = medio
        else:
            if buscado < lista[medio]:
                ultimo = medio - 1
            else:
                primero = medio + 1
    return posicion
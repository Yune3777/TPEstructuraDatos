import timeit
def medir(func, titulo, number=20, repeat=5) -> float:#Devuelve el MEJOR tiempo por llamada en ms (evita ruido de la máquina)
    tiempos = timeit.repeat(lambda: func(titulo), number=number, repeat=repeat)
    mejor = min(tiempos) / number
    return mejor * 1000 # a milisegundos
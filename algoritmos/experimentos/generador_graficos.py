import matplotlib.pyplot as plt

#Datos para crear el gráfico
cant_datos = [10, 100, 1000, 10000] #cantidad de datos en búsqueda secuencial
bs_ms = [0.0010, 0.0088, 0.0892, 1.0093 ] #busqueda secuencial en milisegundos
bb_ms = [0.0008 , 0.0061, 0.0618, 0.7352 ] #búsqueda binaria en milisegundos

fig,ax = plt.subplots(figsize=(10,6))#creo la figura y el eje
ax.grid(linestyle='--',linewidth=0.5,color='gray',zorder=-10)#agrego la grilla
ax.plot(cant_datos, bs_ms, 'tab:green', label='Búsqueda Secuencial')#pongo las variables que van a ir en el eje x y en el eje y, respectivamente.
ax.plot(cant_datos, bb_ms, 'tab:blue', label='Búsqueda Binaria')

plt.xlabel('Cantidad de Datos')
plt.ylabel('Tiempo (ms)')
plt.title('Comparación de Tiempos de Búsqueda')
plt.legend()
plt.show()# Con esto muestro la gráfica
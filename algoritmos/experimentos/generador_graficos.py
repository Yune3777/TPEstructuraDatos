import matplotlib.pyplot as plt

#Datos para crear el gráfico
cant_datos = [10, 100, 1000, 10000] #cantidad de datos en búsqueda secuencial
bs_ms = [0.0009, 0.0086, 0.0944, 1.0391 ] #busqueda secuencial en milisegundos
bb_ms = [0.0008 , 0.0070, 0.0752, 0.8473 ] #búsqueda binaria en milisegundos
ab_ms = [0.0036, 0.0041, 0.0038, 0.0081 ] #búsqueda usando árbol binario en milisegundos
avl_ms = [0.0031, 0.0026, 0.0033, 0.0057 ] #búsqueda usando AVL

fig,ax = plt.subplots(figsize=(10,6))#creo la figura y el eje
ax.grid(linestyle='--',linewidth=0.5,color='gray',zorder=-10)#agrego la grilla
ax.plot(cant_datos, bs_ms, 'tab:green', label='Búsqueda Secuencial')#pongo las variables que van a ir en el eje x y en el eje y, respectivamente.
ax.plot(cant_datos, bb_ms, 'tab:blue', label='Búsqueda Binaria')
ax.plot(cant_datos, ab_ms, 'tab:red', label='Búsqueda Árbol Binario')
ax.plot(cant_datos, avl_ms, 'tab:purple', label='Búsqueda AVL')

plt.xlabel('Cantidad de Datos')
plt.ylabel('Tiempo (ms)')
plt.title('Comparación de Tiempos de Búsqueda')
plt.legend()
plt.show()# Con esto muestro la gráfica
# En este caso se vera con mas detalle la libreria NUMPY
import numpy as np

matriz=np.random.randint(4,15,6)
print "Matriz aleatoria:\n",matriz
matriz=matriz.reshape(2,3)
print "Forma de matriz (2,3)\n",matriz
# podemos ejecutar la suma de los accesos de una matriz
# por ejemplo sumaremos los elementos de las listas internas de cada matriz
print "suma por fila\n",matriz.sum(axis=1) # aca veremos la suma por lista que hace referencia a la suma de elementos por fila
print "suma por columnas \n",matriz.sum(axis=0) # donde nos suma la columna completa por cada matriz





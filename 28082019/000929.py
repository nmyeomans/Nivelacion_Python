# En este caso se vera con mas detalle la libreria NUMPY
import numpy as np
# Para formar matrices multidimensionales , se pueden usar listas en el interior de un array
matriz=np.array([(1.,3.,5.,7.),(2.,4.,6.,8.)])    # En este caso se crea una matriz bidimensional
print "Matriz bidimensional: \n", matriz
# cabe destacar si ejecutamos matriz=np.array(1,2,3) nos lanzara un error
# por otra parte se puede interactuar con la matriz , donde podemos hacer cambios directamente en ella
# por ejemplo sumaremos 5 y lo multiplicaremos por 2
matriz+=5
matriz*=2
print "Matriz modificada: \n", matriz  # podemos ver que los valores cambian respecto de la operacion y son guardados 
# para imprimir zeros utilizamos np.zeros
matriz=np.zeros((3,4))   # estamos ordenando a crear una matriz de 3 listas con 4 elementos cada una
print "Matriz con np.zeros:\n",matriz
print "Tipo de dato:", matriz.dtype

# tambien se puede crear una matriz llena de unos 
matriz=np.ones((3,5))    # estamos ordenando a crear una matriz de 3 listas con 5 elementos
print "Matriz con np.ones: \n",matriz
# ademas , podemos hacer matrices unidimensionales de solo unos
matriz=np.ones(8)
print "Unidimensional\n", matriz
# Tenemos la opcion de crear tipo de dato especifico en un array 
matriz=np.array([3,4,5],dtype=np.int16)
print "Matriz unidimensional con tipo de dato: \n",matriz, matriz.dtype
print "Memoria de cada elemento en bytes:",matriz.itemsize
# Podemos crear una matriz con valores aleatorios mediante np.random.random
matriz=np.random.random((2,2))
print "Matriz aleatorioa:\n",matriz
# podemos ajustar la precision de puntos 
np.set_printoptions(precision=2,suppress=True) #ajustamos la presicion para dos decimales
print "Precision ajustada a 2:\n" ,matriz
# podemos crear una matriz unidimensional con parametros int
matriz=np.random.randint(0,50,5)
print "Matriz aleatorio de parametros int:\n",matriz
# nos entrega la suma, el min, el max, el promedio, la varianza y otros  de los parametros
print " La suma de todos es:",matriz.sum() 
print " El valor minimos de la matriz es:",matriz.min()
print " El valor maximo de la matriz es:",matriz.max()
print " Promedio entre parametros:", matriz.mean()
print " Varianza entre parametros:", matriz.var()
print " Desviacion estandar:",matriz.std()



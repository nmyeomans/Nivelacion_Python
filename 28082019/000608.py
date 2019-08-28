# En este caso se vera con mas detalle la libreria NUMPY
import numpy as np

matriz=np.array([2,3,4])  # esto nos entrega una matriz con 3 elementos en el 
print " Matriz mediante comando array:"
print matriz
# otra forma de crear una matriz es utilizando la funcion de rango
matriz=np.arange(1,50,4) # esto nos entrega una matriz con parametros entre 1 y  12 con pasos de 2  
print " Matriz mediante comando arange:"
print matriz
matriz=np.linspace(1,100,8)  # este comando es mas rapido y podemos determinar el parametro inicial y final, ademas de el numero de elementos en el interior
print " Matriz mediante comando linspace:"
print matriz    # matriz espaciada uniformemente
# podemos modificar nuestra matriz y bidimensionarla
print "Matriz bidimensionada"
matriz=matriz.reshape(4,2)
print matriz
# ahora podemos ver los numeros de elemetons y las filas y columnas con  size y shape respectivamente
print " numero de elementos:", matriz.size
print " numero de (filas, columnas):", matriz.shape
print " tipo de dato: ", matriz.dtype
print " memoria de cada elemento en bytes:" ,matriz.itemsize   # nos indica cuanta memoria en bytes de cada elemento de la matriz 

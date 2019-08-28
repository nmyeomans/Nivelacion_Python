# En esta ocasion usaremos la libreria numpy
# Primero importamos numpy 
import numpy as np
# En este caso usaremos el comando linspace que crea un arreglo (uno , dos , tres)
# uno es el punto de inicio
# dos el punto final
# tres el numero de elementos que quieres
a=np.linspace(1,10,5)
b=np.linspace(2,20,5)
print " Arreglo con valores entre 1 y 10 con 5 elementos:"
print a
print " Arreglo con valores entre 2 y 20 con 5 elementos:"
print b

# para crear una matriz especificamente en numoy podemos utilizar listas
# por ejemplo definir una lista dentro de un array
lista=[2,4,6,8,10]
lista2=[[1,3,5,7,9], lista]
matriz=np.array([lista])
matriz2=np.array([lista2])
# podemos hacer una matriz a partir de dos listas
print "Matrices a partir de una lista y dos respectivamente:"
print matriz
print matriz2
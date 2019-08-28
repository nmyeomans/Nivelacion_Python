# En esta ocasion usaremos la libreria numpy
# Primero importamos numpy 
import numpy as np
matriz=np.zeros(20)        # En otras palabras estamos generando un vector con numero flotantes 0.0
print "\n Matriz con comando np.zeros"
print matriz
# Podemos modificar el orden de esta matriz 
print "\n Matriz"
matriz.shape=(20,1)
print matriz
 
# Por otra parte haremos una matriz llena de 1 
matriz2=np.ones(15)
print "\n Matriz con comando np.ones"
print matriz2
# ademas podemos ver el tipo de parametro que tenemos dentro de la matriz 
print type(matriz2[0])

# ademas tenemos otra forma de crear una matriz para rellenar
matriz3=np.empty(10)
print "\n Matriz con comando np.empty"
print matriz3
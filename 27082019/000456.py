# En esta ocasion usaremos la libreria numpy
# Primero importamos numpy 
import numpy as np
# Podemos generar matrices aleatorias de forma rapida
np.random.seed()
a=np.random.randint(25, size=10) # crea una matriz con valores enteros aleatorios entre 0 y 25
print a    # tiene un largo de 10 digitos 

# por otra parte podemos ver la posicion a la que se encuentra o tomar una serie de parametros 
print " Posicion 0 y final del arreglo :"
print a[0], "y",a[-1]
print  "valores desde la posicion 0 a la 2:"
print a[0:3]    # cabe destacar que inicia en sero , pero llega hasta n-1 , donde n es 3

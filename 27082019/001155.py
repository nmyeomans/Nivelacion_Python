# Para este caso veremos que los array son iterables entre si 
# Ademas, se puede iterar en si mismo , aumentando valores internos
import matplotlib.pyplot as plt    # Importamos matplotlib para poder graficar
import numpy as np
from skimage import io
foto= io.imread('playa.png')       # Abrimos la imagen 
x=np.array([1,2,3,4,5])             # Array de largo L
y=np.array([6,7,8,9,10])            #Array de largo L
#Iteracion entre los array
suma= x+y
print 'suma:',suma
multiplicacion=x*y
print 'multiplicacion:',multiplicacion
suma_agregada=x+100
print "suma agregada:", suma_agregada
producto_punto= x @ y
print 'Nos entrega el producto punto:',producto_punto    # nos entrega el producto punto 
plt.imshow(foto[:,:,0].T)       # Nos entrega la matriz transpuesta

z=np.array([2,1,6,4,5])
np.sort(z)




 
# en este caso leeremos una imagen
# importamos skimage
from skimage import io
import matplotlib.pyplot as plt    # importamos matplotlib para poder graficar
import numpy as np
foto= io.imread('playa.png')       # abrimos la imagen 
print foto.shape       # nos muestra la forma de la imagen
print type(foto)
plt.imshow(foto)            #se imprime la imagen en orden
plt.imshow(foto[::-1])      #imprime la imagen invertida por filas solamente
plt.imshow(foto[:,::-1])    # nos imprime la imagen invirtiendo las columnas
plt.imshow(foto[10:100,100:150]) # cortamos la imagen es un rango
plt.imshow(foto[::2,::2])   # reduce la imagen por la mitad

foto_sin=np.sin(foto) 
print foto

#En esta ocasion trabajamos con la imagen importada en distintas aplicaciones
from skimage import io
import matplotlib.pyplot as plt    # importamos matplotlib para poder graficar
import numpy as np
foto= io.imread('playa.png')       # abrimos la imagen 
valores=np.array([1,2,3,4,5,6,7,8,9])    # creamos un array como parametro 
print valores<2         #Imprime True o False si se cumple o no la condicion 
print valores>2
print valores[valores<2] # Imprime los valores que cumplen la condicion
print valores[valores>=2] # Imprime los valores que cumplen la condicion 

foto_masked=np.where(foto>50,255,0) # se encarga de modificar el umbral
plt.imshow(foto_masked)

a_array=np.array([1,2,3,4,5])
y_array=np.array([6,7,8,9,10])



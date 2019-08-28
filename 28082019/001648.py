# En este caso se vera con mas detalle la libreria NUMPY
import numpy as np
# vamos abrir y recorrer un archivo , de tal forma que se generara una matriz
# este archivo fue extraido a partir de la pagina https://github.com/joeyajames/Python/tree/master/Numpy
# el archivo corresponde a data.txt
archivo_datos=np.loadtxt("data.txt",dtype=np.uint8,delimiter=",",skiprows=1)
print archivo_datos
matriz=np.arange(20)
# ahora  desordenaremos la matriz
print np.random.shuffle(matriz)
for i in range (3):
    print " valor random de la matriz:", np.random.choice(matriz)
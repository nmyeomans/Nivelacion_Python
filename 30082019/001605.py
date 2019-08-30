from matplotlib import pyplot as plt
import numpy as np
# haremos un codigo continuo , dado que todo esta directamente relacionado
print "HoraMinutoSegundo: 001605"
plt.style.use("fivethirtyeight")
#print plt.style.available
# En este caso veremos como realizar graficas mediante matplotlib
# creamos una lista como numpy
edades_x=np.arange(20,31,1) # edades
salario_y=np.array([384960,420000,467520,493200,532000,560000,623160,649280,673170,687480,737520])  # Salarios

print edades_x
print salario_y
# luego graficamos de la forma (x,y) por eje respectivamente
plt.plot(edades_x,salario_y,color="k", marker=".", label="Salario Santiago")
#Podemos ver que en un grafico podemos cambiar el color de una curva, marcar los puntos , hacer una leyenda entre otros.
#Creamos una lista con salarios en el Norte
salario_y2=np.array([453720,488760,538500,572870,630160,659980,700030,700000,714960,753700,836400])
plt.plot(edades_x,salario_y2,color="#444444",linestyle="--", marker=".",label="Salario Norte")
# podemos generar un color especifico de un tipo , por ejemplo #444444  , es posible encontrar mas colores en la red
# Podemos crear otra lista con salarios en el sur
salario_y3=np.array([553720,588760,638500,672870,650160,699980,790030,806000,894990,959700,939400])
plt.plot(edades_x,salario_y3,color="r",linestyle="--", marker=".",label="Salario Sur")
plt.xlabel("Edad ")
plt.ylabel("Salarios ($)")
plt.title("Salarios ($) por edades en region")

#plt.legend(["Salario Santiago","Salarios Norte"])
# en vez de hacer lo anterior , al aplicar label en el pyplot directamente, podemos solo importar legend
plt.legend()
plt.tight_layout()

#minuto 003021#

# para poder guardar una imagen, podemos usar el comando savefig
plt.savefig("Grafico.png")
plt.show()

import numpy as np
# en esta ocasion haremos un codigo consecutivo , como el video es tan largo recomiendo ver el ultimo codigo que adjuntara todos los demas
print "\nHoraMinutosSegundos: 000646"
# primero veremos que los valores de una lista al sumar las listas no se podra sumar termino a termino
# para sumar termino a termino deberemos hacer un ciclo
x=[1,3,5,7,9]
y=[2,4,6,8,10]

suma=[]
for a,b in zip(x,y):
    suma.append(a+b)  # lo que hace el ciclo es asignar el valor de cada parametro de la lista a a,b y luego los sumamos y guardamos en otra lista
print suma

lista=list(range(1000000))
#%timeit sum(lista), vemos la cantidad de loops y su velocidad
array=np.array(lista)
#%timeit sum(lista), vemos la cantidad de loops y su velocidad, es mas arrapido el arreglo array
# ahora haremos nuestros parametros en forma de matriz 
x=np.array([1,3,5,7,9])
y=np.array([2,4,6,8,10])
print x
print y
print x+y
print x/y
print x*y

#001530#
print "\nHoraMinutosSegundos: 001530"
# las matrices en numpy son homogeneas para el tipo de parametro a trabajar , tanto int como floats
print x.ndim   # nos entrega la dimension de la matriz 
print x.shape  # nos entrega el numero de parametros 
# el comando type nos ayudara a saber el tipo de dato que estamos usando , ya sea una matriz, lista, tupla , entre otros parametros
# ejemplo
print type(x)
print type(x[0])
# se pueden ejecutar diversas funciones respecto al array , por ejemplo: sin, cos, exp, log, entre otras
print np.log(x)
print np.cos(y)
print np.log(x*y)
print np.exp(y**2)
# Se puede ver la definicion de un comando numpy y la consola nos entrega el tipo de funcion que es  por ejemplo
print np.sum

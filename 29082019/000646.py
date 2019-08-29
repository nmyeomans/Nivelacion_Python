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

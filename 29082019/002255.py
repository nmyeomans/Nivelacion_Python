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

#002255#
print "\nHoraMinutosSegundos: 002255"
# numpy como dijimos anteriormente trabaja asociando homogeneidad entre sus parametros , por ende si se asigna un parametro en una posicion de tipo flotante cuando el array es del tipo int , este automaticamente sera truncado a int
x=np.array([2,4,6,8,10])
y=np.array([50,25,0+2j,40])
z=np.array([1.0,2,3,4])
print x.dtype,y.dtype,z.dtype # nos entrega el tipo de dato de cada arreglo
# por otra parte podemos definir el tipo de dato que queremos para nuestro arreglo 
x=np.array([2,4,6,8,10], dtype="int64")
y=np.array([1,2,3,4,5], dtype="float64")
print x.dtype
print y.dtype
# en este caso crearemos una matriz a mano
matriz=np.array([[1,2,3,4,5],[6,7,8,9,10]]) # aqui tendremos dos filas para la matriz
print matriz
print matriz.ndim # me entrega la dimension de la matriz
print matriz.shape # numero de filas y numero de parametros por fila
print matriz.T   # traspone la matriz
for i in range (len (matriz)):
    for j in range (len(matriz[i])):
        print matriz[i,j] # nos imprime todos los parametros de la matriz por posicion
        
a=np.array([1,2,3,4,5,6,7])
print a[:-2] # podemos ver en estos casos que el archivo recorrera desde el inicio hasta el ante penultimo dato, por ende nos entregara esos valores recorridos
print a[::]# entrega todos los parametros
print a[-2:] # entrega desde la posicion ante penultima hasta el final

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


# 004222
print "\nHoraMinutosSegundos: 004222"
print " ejercicio"
matriz=np.arange(25).reshape(5,5) # matriz que es reordenada en 5 filas y 5 columnas
print matriz
print " extraccion:"
rojo=matriz[:,1::2]
amarillo=matriz[4]# otras alternativas eran matriz[-1], matriz[-1,:]
azul=matriz[1::2,:3:2]
print rojo
print amarillo
print azul
# ademas puedo remplazar parametros, por ejemplo cambiare los parametros i,j  de algunos de la matriz
matriz[-1,-2]=matriz[0,0]
print matriz # vemos que ambos parametros quedan iguales.
# si quisiera cambiar todos los parametros de la ultima columna se debe hacer lo siguiente
matriz[:,-1]=1  # cambian todos los parametros de la ultima columna por unos
 # existen comandos para ver el ID de cada matriz , ademas de ver si los datos de una matriz son propios o atribuidos de otro lado
print " id de los colores definidos como arreglo"
print id(rojo)
print id(amarillo)
print id(azul)
print id(matriz)
print red.flags # vemos particularidades de la matriz red y principalmente si sus datos son propios o fueron extraidos de otro lado
print matriz.flags

#005622#
print "\nHoraMinutosSegundos: 005622"
# En esta ocasion veremos como podemos seleccionar parametros de un arreglo

a=np.arange(0,200,20)# estamos creando un arreglo con parametros de 20 en 20 en un rango de 0 hasta 200
print a
# podemos llamar a los parametros del arreglo a partir de una lista
lista=[1,3,5,-2,-1]
valores=a[lista]
print valores
# ademas podemos crear un arreglo de forma manual donde podemos dar el tipo de dato bool, lo que hace es convertir todos los ceros en falsos y los unos y todo en verdadero
mask=np.array([0,1,1,0,0,1,0,0],dtype=bool)
print mask

x=np.array([2,-4,-5,2,3,6,8,-2])
print x
# podemos escribir o modificar los valores negativos de un arreglo . como ademas iterar.
negativos=x<0
print x[negativos]   # nos imprime los negativos
# podemos hacer la condicion directamente en los corchetes y ademas podemos modificar y no querer valores negativos en la matriz
x[x<0]=0
print x    # nos entrega la matriz con 0 en los valore que eran negativos 

# podemos ver un pegueÃ±o ejemplo donde iremos cambiando estas condiciones y demostrar como funcionan:
x=np.arange(0,10,1)

lista=[0,1,2,3,4]
for i in range (len(lista)):
    print x[lista]  # me entrega los valores en cada posicion segun la lista
    if i<2:
        print x[i]  # nos entrega el valor i
        print x[x>i] # nos entrega los valores mayores que i
    elif i>2:
        x[i]=1000   # en la posicion i se cambiara el valor por 1000
        print x
# operadores binarios: and , or , not , xor  
#  & (and)  | (or) ~ (not)
# ^{xor}
# por ejemplo veremos si se cumple la siguiente condicion
x=np.array([1,2,3,4,5,6,7,8,9,10])
print  (x<9)&(x>5) 
print np.nonzero([x<0])


# Podemos ver que dentro del ciclo for ademas de hacer operaciones , podemos hacer condiciones del tipo if 
suma=0
for i in range(1,10):
    if i%2==0:              #el porcentaje(%) en python nos entrega el resto de todo valor 
        suma+=i
        print i             # podemos ver que nos entrega todos los multiplos de 2
print "La suma de todos es "
print suma
print "\n"
 
# TAREA del video
# calcular la suma de todos los multiplos de tres y cinco que hay en un rango de 100
print " Tarea propuesta en el video"
# Generamos las listas y la suma inicial vacias y en cero respectivamente
suma_3=0
lista_3=[]
suma_5=0
lista_5=[]
for i in range(1,100):
    # se generan una condicion dentro de otra para los numeros que son multiplos de ambos
    if i%3==0:              # evaluamos si el numero es multiplo de 3
        suma_3+=i
        lista_3.append(i)
        if i%5==0:           # evaluamos si el numero es multiplo de 5
            lista_5.append(i)
    elif i%5==0:             # evaluamos si el numero es multiplo de 5
        suma_5+=i
        lista_5.append(i)
        if i%3==0:           # evaluamos si el numero es multiplo de 3
            lista_3.append(i)
print " Suma de los multiplos de 3  : ", suma_3
print " Los multiplos de 3 : " , lista_3
print " Suma de los multiplos de 5  : ", suma_5
print " Los multiplos de  5: " , lista_5


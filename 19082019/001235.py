# Se crean parametros con el objetivo de ser evaluado en las condiciones
# Se utiliza raw_input para preguntar al usuario los parametros que quiere evaluar(no sale en el video)
# El comando if es utilizado para evaluar una condicion , si esta se cumple se ingresa directamente( en este ejemplo nos imprime)
# Luego el comando elif de la misma forma que if evalua una condicion, se evalua si o solo si if no se cumple
# Posteriormente para else se ejecuta si y solo si las condiciones anteriores no se cumplen 
print (" En este caso se trabajara con numeros enteros \n")
a=raw_input("valor entre 0 y 100 (entero) que le asigna al parametro a:")
b=raw_input("valor entre 0 y 100 (entero) que le asigna al parametro b:")

if a<b:
    print ("El parametro a es menor que b")
elif a==b:
    print ("Los parametros son iguales")
else:
    print ("El parametro a es mayor que b")
# por otra parte generamos otros parametros con el fin de evaluar si son pares o impares
# Se utiliza int para ver si es o no 
c=raw_input("valor entre 0 y 100 (entero) que le asigna al parametro c:")
d=raw_input("valor entre 0 y 100 (entero) que le asigna al parametro d:")
if int(c)%2==0 and int(d)%2==0:
    print ("Ambos parametros son pares")
elif int(c)%2==0 and int(d)%2!=0:
    print ("Solo el parametro c es par")
elif int(c)%2!=0 and int(d)%2==0:
    print ("Solo el parametro d es par")
else:
    print ("Ambos parametros son impares")
    

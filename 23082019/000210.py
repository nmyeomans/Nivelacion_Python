#En este caso ocuparemos while 
# Erincipalmente while se encarga de iterar en funcion a una condicion inicial planteada
# En este caso introductorio de como funciona while veremos como ejecutar lo hecho en for a partir de un cicli while
# En primer lugar generamos una suma y un contador inicial
suma=0
contador=1
while contador<10:     # El contador se evalua en una condicion , si se cumple continua
    suma+=contador
    contador+=1         # Sumamos al contador , para volver a entrar al ciclo , de no sumar el ciclo podria repetirse infinitas veces
print "suma del 1 al 9:"
print suma              # Podemos ver que suma todos los valores entre 1 y 10 

# Otro ejemplo, pero con multiplicacion
multiplicacion=1
contador2=1
while contador2<=5:
    multiplicacion*=contador2
    contador2+=1
print "multiplicacion del 1 al 5:"
print multiplicacion
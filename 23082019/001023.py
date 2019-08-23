# En este caso veremos como salir de un ciclo for o while mediante una condicion interna
# Ademas utilizaremos el True y break
# partiremos con el caso for para salir del ciclo cuando un numero de la lista sea negativo
Lista=[10,8,4,2,1,-1,-3,-5,-7,-9]
print Lista
suma_pos=0
for numero in Lista:
    if numero <0:                  # condicion para numeros negativos
        break                      #  break nos saca del ciclo de forma automatica
    suma_pos+=numero
print " Caso for "
print "Suma parametros positivos de la lista:"
print suma_pos
# utilizando la misma lista anterior para el caso while tenemos:
suma2_pos=0
i=0
while True:                     # Entramos automaticamente al ciclo , sea cual sea el numero
    suma2_pos+=Lista[i]
    i+=1
    if Lista[i]<0:             # generamos la condicion negativa, se cumple y salimos del ciclo
        break
print " Caso While "
print "Suma parametros positivos de la lista:"
print suma2_pos
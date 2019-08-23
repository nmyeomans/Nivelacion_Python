# En este caso veremos cuando es conveniente usar el ciclo while a diferencia de for
# cuando tenemos listas con numero positivos y negativos por ejemplo , como while usa una condicion es mas conveniente 
# ejemplo
Lista=[10,7,5,3,2,1,-1,-3,-5,-8,-9]
print Lista
suma_pos=0
i=0
while Lista[i]>=0:          # Ponemos la condicion positiva para que podamos entrar al ciclo
    suma_pos+=Lista[i]      # guardamos el parametro positivo de la lista
    i+=1
print "Suma de los parametros positivos de la lista"
print suma_pos

# Existe el caso en el que podemos tener una lista con todos sus numeros positivos lo cual nos arrojaria error
# El error seria por que nuestro contador i nos indicara la posicion en la lista y como la lista es de n dijitos sus posiciones llegan hasta n-1 digitos
# Por lo tanto llamaremos al dijito de la lista de la posicion n el cual no existe, por eso se puede crear una doble condicion

Lista2=[10,9,8,6,4,2,1]                  # Lista de numeros positivos
print Lista2
suma=0
j=0
while j<len(Lista2) and Lista2[j]>=0:    # cabe destacar que debemos colocar como primera condicion la del contador, ya que va leyendo de izquierda a derecha 
    suma+=Lista[j]
    j+=1
print "Suma de los parametros de la segunda lista:"
print suma
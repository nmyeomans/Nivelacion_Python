# En este capitulo cosideramos listas , donde podemos guardar parametros
# generamos una lista la cual guardara parametros y se eliminaran parametros
# utilizando comandos como .append() y .pop() respectivamente

lista=[1,2,3]
print lista
lista.append(4)
lista.append("Nicolas")
lista.append([7,"nicolas"])
print lista
lista.pop() # este parametro nos elimina el ultimo valor guardado y asi puede ir eliminando los ultimos
print lista
lista.pop()
print lista
# Ademas podemos seleccionar parametros por posicion de la lista
# las listas estan ordenadas en posicion partiendo desde el 0 
# por ejemplo imprimiremos la posicion 0 y 2
print " Ahora imprimiremos los parametros de la lista , en este caso el 0 y 2: \n"  # \n es para saltar linea
print lista[0]
print lista[2]
# Para realizar iteracciones podemos usar el comando for
# En primera instancia podemos ver que a partir de una lista se pueden recorrer sus parametros
# para recorrer los parametros de forma secuenciada utilizamos el comando for

goleador=["Hans","Nicolas","Matias"]
# En vez de ir utilizando print continuamente para indicar cada uno , utilizamos for

for persona in goleador:    # al indicar persona in goleador , estamos asignando de a un parametro de la lista
    print persona       # nos imprime uno a uno los parametros de la lista
    
# podemos ver que dentro del ciclo for puede imprimir mas de una vez el nombre hasta completar el ciclo
# ejemplo
print "\n" 
for persona in goleador:
    print persona
    print persona
    # podemos ver que nos imprimira 2 veces por cada parametro de la lista

# Para crear operaciones de numeros grandes es mas sencillo utilizar (range)
# con (range) lo que hacemos es generar un rango de valor los cuales sirven para crear una lista de tal rango o operar directamente con for
# por ejemplo

lista=list(range(1,25))    # lo que hago es generar una lista con (list) con valores en un rango de 1 a 25, sin considerar el 25
print lista                 # tendremos una lista con valores del 1 hasta el 24
# en el caso de que no quiera usar listas puedo hacer esa suma de forma directa

print "\n"
suma=0
for i in range(1,25):      # sumaremos valores del 1 al 24
     suma=suma+i 
print suma
    
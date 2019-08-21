# En esta ocasion vamos a cambiar de lugar los parametros de una lista 
# para eso vamos a generar variables seleccionando un parametro especifico de la lista 
# la forma siguiente es mas larga de lo normal pero es utilil para cambiar de orden en una lista
goleador=["Hans", "Nicolas", "Matias"]
ordenar=goleador[0]         # asignamos una varible con el parametro de la lista de la posicion respectiva
goleador[0]=goleador[1]     #luego modificamos reemplazando el primer parametro de la lista con el segundo 
goleador[1]=ordenar         #luego el segundo parametro de la lista guardara el primero
print goleador
# podemos ver que la consola nos imprime el cambio de sujeto en este caso
 # otra forma mas eficiente es hacerlo con comas , designando un orden a cada variable de la lista 
goleador[1],goleador[2]=goleador[2],goleador[1]
print goleador
# podemos ver que es mas eficiente esta forma de asignacion para cada parametro de la lista 

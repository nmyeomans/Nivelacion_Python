# En esta caso se utiliza def para crear una funcion 
# donde ingresamos un parametro el cual se evalua y retorna un resultado
# ej utilizaremos la funcion cuadratica, donde sabemos que es de la forma ax**2+bx+c, la cual retornara las soluciones 


def fun_cuadratica(a,b,c):
    xmas=(-b+((b**2)-4*a*c)**(1/2))/(2*a)       #los parametros se evaluan en la funcion con +
    xmenos=(-b-((b**2)-4*a*c)**(1/2))/(2*a)     #los parametros se evaluan en la funcion con -
    print "las soluciones son : "
    return  xmas, xmenos
# definimos una variable como una funcion de parametros definidos
a= fun_cuadratica(1,2,4)
b= fun_cuadratica(2,2,2)
# con esto podemos ver que en primer lugar la variable creada entrega directamente todo tipo de impresion dentro de su funcion 
# luego al imprimir , nos damos cuenta que solo nos da el retorno de las soluciones en este caso
print a
print b
# Podemos ver finalmente que al tener una variable asignada como una funcion, automaticamente se recorre todo tipo de re asignacion , impresiones entre otras.

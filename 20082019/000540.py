# En esta caso se utiliza def para crear una funcion 
# donde ingresamos un parametro el cual se evalua y retorna un resultado
def fun_1(x):           #La variable entra a la funcion y se evalua 
    return x*10+x**3-x  # con el return la funcion entrega el valor o parametro alterado
# definimos variables que son equivalentes a la funcion evaluada en un parametro
valor_1=fun_1(3)
valor_2=fun_1(5)
valor_3=fun_1(2)
# luego para poder ver esos parametros evaluados en la funcion utilizamos un print para que nos retorne el parametro alterado
print valor_1
print valor_2
print valor_3


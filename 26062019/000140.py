# En esta ocasion veremos diccionarios
# Lo que hacemos con los diccionarios es definir , asignar, guardar parametros de una forma diferente
# Podemos ver a continuacion el caso en el que definiremos las edades de personas, con el objetivo de modelar el comportamiento de los diccionarios
#{"Nicolas":22, "Matias":17, "Hans":27}
Edades={}               # En este caso creanos el diccionario
Edades["Nicolas"]=22    # Asignamos al String la edad correspondiente como un int 
Edades["Matias"]=17     #    ""
Edades["Hans"]=27       #    ""
# Podemos ver que al imprimir , tendremos la edad de la persona
print "Edades de Nicolas, Matias y Hans. Respectivamente"
print Edades["Nicolas"]
print Edades["Matias"]
print Edades["Hans"]
# Ademas, al igual que en las listas podemos cambiar la definicion que le damos a un parametro 
# por ejemplo ahora Matias tendra 10 
Edades["Matias"]=10
print "Edad cambiada de Matias"
print Edades["Matias"]
# Ademas de guardar valor para string podemos usar int respecto de int 
print "El valor 10 en nuestro diccionario entrega:"
Edades[10]=1
print Edades[10]

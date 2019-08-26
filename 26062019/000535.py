# En este caso veremos como iterar con for un diccionario
# A partir del mismo diccionario anterior , correremos cada item del diccionario
Edades={}               # En este caso creanos el diccionario
Edades["Nicolas"]=22    # Asignamos al String la edad correspondiente como un int 
Edades["Matias"]=17     #    ""
Edades["Hans"]=27       #    ""

for concepto,definicion in Edades.items():      # guardamos en concepto y definicion el valor de cada parametro del diccionario segun definicion
    print "Concepto:"
    print concepto
    print "Definicion:"
    print definicion

# Podemos ver que nos permite entregar de forma mas practica el diccionario completo
# Tambien , se pueden agregar listas para separar cada termino y guardarlo por concepto y definicion, podemos relacionarlo mas a lo que ya hemos visto mediante este curso

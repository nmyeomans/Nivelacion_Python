# usaremos el mismo ejemplo del video if else , para evaluar este caso como una funcion
# se dejaron parametros como la edad , masa , peso maximo , repeticiones con el objetivo de ser evaluados
# al ser evaluados estos nos diagnosticaran mediante la funcion el nivel en que nos encontramos en forma fisica 
# cabe destacar que esta funcion se hace para el tren superior
def evaluacion(nombre,edad,masa,peso_max,repeticiones): 
    print nombre
    print edad
    x1=2.5*repeticiones
    x2=100.-x1
    x3=x2/100.
    RM_estimado=float((peso_max/x3)/masa)
    if edad<=20:
        if RM_estimado>=1.76:
            return"Nivel Superior"
        elif RM_estimado>=1.34:
            return "Nivel Excelente" 
        elif RM_estimado>=1.19:
            return  "Nivel Bueno"  
        elif RM_estimado>=1.06:
            return "Nivel Justo"
        else:
            return "Nivel Pobre"
    elif edad>=20 and edad>=29:
        if RM_estimado>=1.63:
            return "Nivel Superior"
        elif RM_estimado>=1.32:
            return  "Nivel Excelente" 
        elif RM_estimado>=1.14:
            return "Nivel Bueno"  
        elif RM_estimado>=0.99:
            return "Nivel Justo"
        else:
            return "Nivel Pobre"
    elif edad>=30 and edad>=39:
        if RM_estimado>=1.35:
            return "Nivel Superior"
        elif RM_estimado>=1.12:
            return "Nivel Excelente" 
        elif RM_estimado>=0.98:
            return "Nivel Bueno"  
        elif RM_estimado>=0.88:
            return "Nivel Justo"
        else:
            return "Nivel Pobre"
    elif edad>=40 and edad>=49:
        if RM_estimado>=1.2:
            return "Nivel Superior"
        elif RM_estimado>=1.0:
            return "Nivel Excelente" 
        elif RM_estimado>=0.88:
            return "Nivel Bueno"  
        elif RM_estimado>=0.8:
            return "Nivel Justo"
        else:
            return "Nivel Pobre"
    elif edad>=50 and edad>=59:
        if RM_estimado>=1.05:
            return "Nivel Superior"
        elif RM_estimado>=0.9:
            return "Nivel Excelente" 
        elif RM_estimado>=0.79:
            return "Nivel Bueno"  
        elif RM_estimado>=0.71:
            return "Nivel Justo"
        else:
            return "Nivel Pobre"
    else:
        if RM_estimado>=0.94:
            return "Nivel Superior"
        elif RM_estimado>=0.82:
            return "Nivel Excelente" 
        elif RM_estimado>=0.72:
            return "Nivel Bueno"  
        elif RM_estimado>=0.66:
            return "Nivel Justo"
        else:
            return "Nivel Pobre"
print " Evaluacion de RM tren superior "
nombre="Nicolas"
edad=22
masa=78
peso_max=50
repeticiones=4

nombre2="Hans"
edad2=27
masa2=99
peso_max2=70
repeticiones2=5

usuario1=evaluacion(nombre,edad,masa,peso_max,repeticiones)
usuario2=evaluacion(nombre2,edad2,masa2,peso_max2,repeticiones2)
#Lo mismo que en los casos anteriores, se recorre la funcion al ser asignada en una variable , sin retornar
# para retornar la evaluacion imprimimos la variable creada , en este caso (Usuario(N°))
print usuario1
print usuario2

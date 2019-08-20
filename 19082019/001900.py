# El objetivo de este programa es representar el nivel en el que se encuentra una persona en base a su repeticion maxima
# la repeticion maxima consiste en el maximo peso que una persona puede levantar en un numero de repeticiones apto
# apto se hace referencia a mayor a 3 repeticiones como minimo
# para esto se generar parametros donde se obtendra informacion relevante para el calculo de la repeticion maxima
# En esta ocasion solo se evalua el tren superior del cuerpo
# se utilizaron condiciones if , elif, else
# el float se utilizo principalmente para poder trabajar y comparar con los valores de la tabla de niveles


print " Evaluacion de RM tren superior "

edad=raw_input("Edad: ")
masa=float(raw_input("Peso de la persona en (kg):"))
peso_max=float(raw_input("Maximo peso levantado en (kg): "))
repeticiones=float(raw_input("Numero de repeticiones de peso max:"))
x1=2.5*repeticiones
print x1
x2=100.-x1
x3=x2/100.
print x3
RM_estimado=float((peso_max/x3)/masa)

print RM_estimado
if edad<=20:
    if RM_estimado>=1.76:
        print "Nivel Superior"
    elif RM_estimado>=1.34:
        print "Nivel Excelente" 
    elif RM_estimado>=1.19:
        print "Nivel Bueno"  
    elif RM_estimado>=1.06:
        print "Nivel Justo"
    else:
        print "Nivel Pobre"
elif edad>=20 and edad>=29:
    if RM_estimado>=1.63:
        print "Nivel Superior"
    elif RM_estimado>=1.32:
        print "Nivel Excelente" 
    elif RM_estimado>=1.14:
        print "Nivel Bueno"  
    elif RM_estimado>=0.99:
        print "Nivel Justo"
    else:
        print "Nivel Pobre"
elif edad>=30 and edad>=39:
    if RM_estimado>=1.35:
        print "Nivel Superior"
    elif RM_estimado>=1.12:
        print "Nivel Excelente" 
    elif RM_estimado>=0.98:
        print "Nivel Bueno"  
    elif RM_estimado>=0.88:
        print "Nivel Justo"
    else:
        print "Nivel Pobre"
elif edad>=40 and edad>=49:
    if RM_estimado>=1.2:
        print "Nivel Superior"
    elif RM_estimado>=1.0:
        print "Nivel Excelente" 
    elif RM_estimado>=0.88:
        print "Nivel Bueno"  
    elif RM_estimado>=0.8:
        print "Nivel Justo"
    else:
        print "Nivel Pobre"
elif edad>=50 and edad>=59:
    if RM_estimado>=1.05:
        print "Nivel Superior"
    elif RM_estimado>=0.9:
        print "Nivel Excelente" 
    elif RM_estimado>=0.79:
        print "Nivel Bueno"  
    elif RM_estimado>=0.71:
        print "Nivel Justo"
    else:
        print "Nivel Pobre"
else:
    if RM_estimado>=0.94:
        print "Nivel Superior"
    elif RM_estimado>=0.82:
        print "Nivel Excelente" 
    elif RM_estimado>=0.72:
        print "Nivel Bueno"  
    elif RM_estimado>=0.66:
        print "Nivel Justo"
    else:
        print "Nivel Pobre"
# crearemos una funcion llamada convertir , que pasara de millas a kilometros como el desafio propuesto en el video

def convertir(millas):
    km=1.6*millas
    return km
# en primer lugar damos ejemplos
print "ejemplos:"   
milla1=convertir(20)
milla2=convertir(350)
print milla1
print milla2
# luego preguntamos al usuario el numero de millas que desea pasar a km
valor=float(raw_input("Numero de millas que se pasaran a km:"))
milla3=convertir(valor)
print milla3


#Ej. 7. Pedir el nivel del agua en metros de una cisterna.

#ENTRADA DE DATOS
nivel = int(input("Escribir nivel: "))


if (nivel < 0):
    print("FUGA EN CISTERNA")

elif (nivel == 0):
    print("ENCENDER BOMBA DE AGUA")

elif (nivel > 0 and nivel <= 2):
    print ("ACELERAR BOMBA DE AGUA")

elif (nivel > 2 and nivel <= 4):
    print ("BOMBA TRABAJANDO")

elif (nivel > 4 and nivel < 6):
    print ("DESACELERAR BOMBA")

elif (nivel == 6):
    print ("APAGAR BOMBA")

elif (nivel > 6):
    print ("DESBORDAMIENTO DE AGUA EN CISTERNA")
    
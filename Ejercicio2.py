#Ej. 2. Calcular el área y perímetro de un círculo.

import math


#ENTRADA DE DATOS
radio = float(input("Escribir el tamaño de radio: "))
radio_cuadrado = pow(radio, 2)

#PROCESOS
área = math.pi * radio_cuadrado
perímetro = 2 * math.pi * radio

#SALIDA DE DATOS
print("El área del círculo es de:", round(área, 4))
print("El perímetro del círculo es de:", round(perímetro, 4))
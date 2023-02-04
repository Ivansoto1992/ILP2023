#Ej. 5. Obtener valores para: a, b y c. Calcular la fórmula general.

import math

#ENTRADA DE DATOS
elemento_a = float(input("Ingresar un número: "))
elemento_b = float(input("Ingresar un número: "))
elemento_c = float(input("Ingresar un número: "))

#PROCESOS
elemento_b_cuadrada = pow(elemento_b, 2)
#raíz = math.sqrt(elemento_b_cuadrada - (4 * elemento_a * elemento_c))
raíz = pow(elemento_b_cuadrada - (4 * elemento_a * elemento_c), 1/2)


#SALIDA DE DATOS
print("La variable X1 es:", (((-elemento_b - raíz) / 2 * elemento_a)))
print("La variable X2 es:", (((-elemento_b + raíz) / 2 * elemento_a)))

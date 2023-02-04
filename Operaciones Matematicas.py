#Operaciones Matematicas

#importar una libreria de funciones matematicas 
import math as m


#entrada de datos 
#Declarar o crear dos variables 
numero_1 = 10
numero_2 = 2

#Constante
Gravedad_Tierra = 9.8
PI = 3.1416


#Procesos (Operaciones o calculos Matematicos y/o Logicos)
suma = numero_1 + numero_2
resta = numero_1 - numero_2
suma = 0 
multiplicar = numero_1 * numero_2
division = numero_2 / numero_2


potencia_1 = numero_1 ** numero_2
potencia_2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2, 3)


#Salida de Datos
print("La suma es igual a", suma)
print("La resta es igual a", resta)
print('La suma es igual a' + str (suma))


#concatenar (union de 2 o mas textos)
#Casteo: Conversion de un tipo de dato en otro tipo de dato

print(f"La suma es igual a {suma}") #d: formateo de interpolacion de texto 

#constante=valor que se mantiene fijo o no cambia su valor

#Syntax= elemento que puede cambiar su valor 
#nombre_variable= valor 

print("La potencia 1 =", round(potencia_1, 2))
print("La potencia 2 =", round(potencia_2, 4))

raiz_cuadrada_1 = m.sqrt(9)
raiz_cuadrada_2 = (9,1/2)
raiz_cubica = (27, 1/3)
cubo = pow(numero_2, 3)

modulo_residuo =  9 % 2 
modulo_residuo2 = 20 % 6

print("redondear la suma de constantes = ", round(Gravedad_Tierra + PI, 2))

print("El modulo o residuo =", modulo_residuo)

numero_1 = float (input("Escribe un numero: "))
numero_2 = int 







#Ejercicios 






#Ej. 1. Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

#ENTRADA DE DATOS
calificación_1 = float(input("Escribir calificación 1: "))
calificación_2 = float(input("Escribir calificación 2: "))
calificación_3 = float(input("Escribir calificación 3: "))

#PROCESOS
suma = calificación_1 + calificación_2 + calificación_3
promedio = suma / 3

#SALIDA DE DATOS
print("El promedio de calificaciones es:", round(promedio, 2))



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






#Ej. 3. Determinar la edad de una persona conociendo el año actual y el año de nacimiento.

#ENTRADA DE DATOS
año_de_nacimiento = int(input("Escribir año de nacimiento: "))
año_actual = int(input("Escribir año actual: "))

#PROCESOS
Edad = año_actual - año_de_nacimiento

#SALIDA DE DATOS
print("La edad de la persona es de:", Edad, "años")





#Ej. 4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

#ENTRADA DE DATOS
grados_celcius = float(input("Escribir temperatura: "))


#PROCESOS
grados_fahrenheit = (grados_celcius * 1.8) + 32
grados_kelvin = grados_celcius + 273.15

#SALIDA DE DATOS
print("La temperatura es de:", grados_celcius, "°C")
print("La temperatura es de:", round(grados_fahrenheit, 2), "°F")
print("La temperatura es de:", grados_kelvin, "K")





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




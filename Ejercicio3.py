#Ej. 3. Determinar la edad de una persona conociendo el año actual y el año de nacimiento.

#ENTRADA DE DATOS
año_de_nacimiento = int(input("Escribir año de nacimiento: "))
año_actual = int(input("Escribir año actual: "))

#PROCESOS
Edad = año_actual - año_de_nacimiento

#SALIDA DE DATOS
print("La edad de la persona es de:", Edad, "años")
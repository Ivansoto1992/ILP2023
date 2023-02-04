#Ejercicio 4
#ENTRADA DE DATOS
# Pedir la cantidad de grados y convertirlos a °C, °F y K.

#entrada 
GRADOSCELCIUS=float(input("cantidad grados: "))
GRADOS=float(input("cantidad grados: "))

#proceso
grados_f = (GRADOSCELCIUS*1.8)+32
grados_k= GRADOSCELCIUS+273.15
grados_f_c = (GRADOS*1.8)+32
grados_k_c= GRADOS-273.15
grados_c_k= GRADOS+273.15
grados_f_k=(9*(GRADOS-32))/9+273.15
grados_k_f=(9*(GRADOS-273.15))/5+32
grados_c_f=(9*GRADOS)/5+32




#salida
print("los grados son:",GRADOSCELCIUS, "°c")
print("los grados son:", grados_f, "°f")
print("los grados son:", grados_k, "°k")
print("los grados son: ", round(grados_f_c,2))
print("los grados son: ", round(grados_k_c,2))
print("los grados son: ",round(grados_c_k,2))
print("los grados son: ", round(grados_f_k,2))
print("los grados son: ", round(grados_k_f,2))
print("los grados son: ", round(grados_c_f,2))


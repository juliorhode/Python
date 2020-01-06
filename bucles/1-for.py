
#Sintaxis: for variable in elemento_recorrer
# Los elementos a recorrer puede ser una lista, tupla, cadena, range

# Tipo range nos permite utilizar el for de python con conteo numerico
for i in ["Primavera","Verano",426]:
	# i = "Primavera"
	# i = "Verano"
	# i = "Otono"
	# i = "Invierno"
	# print("hola", end=" ")
	print("Hola")

contador = 0
miEmail = input("Introduce el email: ")
for i in miEmail:
    if (i == "@" or i == "."):
    	contador = contador + 1

if contador == 2:
    print("Email correcto")
else:
	print("Email incorrecto")

print("Manejo del Range")
for i in range(5):
	print(i)

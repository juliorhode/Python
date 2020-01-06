for i in range(5):
	# concatenar texto con valores de variables
	# f indica que vamos a utilizar una notacion especial
	# {variable}
	print(f"valor de la variable {i}")
	# print(i)
for i in range(5,10):
	print(i)

for i in range(5,50,5):
	print(f"Valor: {i}")


valido = False 
email = input("Introduce tu email: ")
for i in range( len(email)):
	if email[i] == "@":
		valido = True

if valido == True:
	print("Email Correcto")
else:
	print("Email incorrecto") 
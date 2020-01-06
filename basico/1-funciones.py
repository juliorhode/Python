# Declaracion de la funcion
def mensaje():
	# Cuerpo de la funcion
	print("Estamos en curso de python")
	print("Estamos con funciones")
	print("Ay vamos")

print("Ejecutando la funcion")
print("----------------------")

# Llamada de la funcion
mensaje()

# Declaracion de la funcion
def suma():
	# Cuerpo de la funcion
	num1 = 5
	num2 = 7
	print(num1 + num2)

# Llamada de la funcion
suma()

# Declaracion de la funcion
def operacion(numero1, numero2):
	# Cuerpo de la funcion
	print(numero1 + numero2)

# Llamada de la funcion
operacion(2, 2)
operacion(35, 5)

# Declaracion de la funcion
def operacion2(num1, num2):
	# Cuerpo de la funcion
	resultado = num1 + num2
	return resultado

# Llamada de la funcion
print(operacion2(5,5))

# Llamada de la funcion
reultado_funcion = operacion2(5,5)
print(reultado_funcion)

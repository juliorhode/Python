edad = -7
# Concatenacion de operadores de comparacion. El lee esto de izquierda a derecha
if 0 < edad < 100:
	print("Edad es corecta")
else:
	print("Edad incorrecta")


salarioPresidente = int(input("Salario Presidente: "))
print("El salario del Presidentes es: " + str(salarioPresidente))

salarioJefe= int(input("Salario Jefe: "))
print("El salario del Jefe es: " + str(salarioJefe))

salarioAdministrativo = int(input("Salario Administrativo: "))
print("El salario del Administrativo es: " + str(salarioAdministrativo))

if salarioAdministrativo < salarioJefe < salarioPresidente:
	print("Todo funciona bien")
else:
	print("Algo falla")
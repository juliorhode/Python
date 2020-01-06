print("Programa de evaluacion de notas de alumnos")

# Introducir valores por teclado
nota_alumno = input("Nota del Alumno: ")

# Para poder introducir datos por consola, debemos entrar en 
# tools -- sublimeREPL -- Python -- Python-RUN current file
def evaluacion(nota):
	valoracion = "aprobado"
	# > mayor que
	# < menor que
	# == igual que
	# >= mayor igual que
	# <= menor igual que
	# != diferente de
	if nota < 5:
		valoracion = "reprobado"
		
	return valoracion

print(evaluacion(int(nota_alumno))) # Transformamos con int() a numerico lo que r
# ecibimos

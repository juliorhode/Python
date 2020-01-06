# El alumno debe escoger una asignatura dentro del listado

# Me da error al escribir el String normal, tuve que escribir 
# mi texto dentro de comilla
print("Asignaturas optativas:")
print("Informatica - Prueba de Software - Testing")
opcion = input("Introduce la asignatura escogida entre comillas: ")
asignatura = opcion.lower()
if asignatura in ("informatica", "prueba de software", "testing"):
	print("Asignatura elegida: " + asignatura)
else:
 	print("La asignatura escogida no esta contemplada")
print("Verificacion de acceso")

edadUsuario = int(input("Introduce tu edad: "))

if edadUsuario < 18:
	print("No puedes pasar")
elif edadUsuario > 100:
	print("Edad incorrecta")
else:
	print("Puedes pasar")

nota = int(input("Introduce tu nota: "))
if nota < 5:
	print("Insuficiente")
elif nota < 6:
	print("Suficiente")
elif nota < 7:
	print("Bien")
elif nota < 9:
	print("Notable")
else:
	print("Sobresaliente")


print("El programa ha finalizado")
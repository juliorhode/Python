# Estas son las condiciones para recibir beca
# distancia > 40km
# numero hermanos > 2
# salario familiar <= 20000

print("Programa de becas")

distanciaEscuela = int(input("Introduce distancia en km: "))
print(distanciaEscuela)

numeroHermanos = int(input("Introduce cantidad de hermanos: "))
print(numeroHermanos)

salarioFamiliar = int(input("Introduce salario familiar: "))
print(salarioFamiliar)

if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")
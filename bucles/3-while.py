

i = 1

while i <= 10:
    print("Ejecucion " + str(i))
    i = i + 1

print("Termino la ejecucion")

edad = int( input("Introduce la edad: "))
while edad < 5 or edad > 100:
    print("Haz introducido una edad no permitida. Vuleve a intentarlo")
    edad = int( input("Introduce la edad: "))
print("Puedes pasar. Gracias por tu edad")
print("Edad: " + str(edad))

# Con esto importamos la clase math
import math
print("Programa de calculo de raiz cuadra")
numero = int( input("Ingrese un numero: "))
intentos = 0
while numero < 0:
    print("No se puede hallar la raiz de un numero negativo")
    if intentos == 2:
        print("Haz utilizado muchos intentos.")
        print("El programa ha finalizado")
        break;
    numero = int( input("Ingrese un numero: "))
    if numero < 0:
        intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))

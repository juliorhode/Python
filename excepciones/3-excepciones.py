# Lanzamiento de excepciones intencionales

# ----------------- Inicio de la funcion -----------------
def evaluaEdad(edad):
    if edad < 0:
        # raise tipo_excepcion()
        raise TypeError("No se permiten edades negativas")
    elif edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate..."
# ----------------- Fin de la funcion -----------------

print(evaluaEdad(18))

# ----------------- Inicio de la funcion -----------------
import math
def calculaRaiz(num):
    if num < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num)
# ----------------- Fin de la funcion -----------------

op1 = (int(input("Introduce un numero: ")))
try:
    print(calculaRaiz(op1))
# Con as le damos un alias a la excepcion
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
print("Programa finalizado")

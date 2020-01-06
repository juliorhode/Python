# Los generadores son estructuras que extraen valores de una funcion y se almacenan en objetos iterables.
# Estos valores se almacenan uno en uno.
# Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente.
# Esta caracteristica es conocida como "suspension de estado".

# Ventajas:
# 1) Son mas eficientes que las funciones tradicionales
# 2) Muy utiles con listas de valores infinitos
# 3) Bajo determinados escenarios, sera muy util que un enerador devuelva los valores uno a uno

# Sintaxis:
# def nombre_funcion():
#     yield variable

# Vamos a generar numeros pares con una funcion tradicinal
def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num * 2)
        num = num + 1
    return miLista

print(generaPares(10))

# Vamos a generar numeros pares con un generador
def generaParesGenerador(limite):
    num = 1

    while num < limite:
        yield num * 2
        num = num + 1
devuelvePares = generaParesGenerador(10)

# Devuelve valor y entre llamada y llamada esta en estado de suspension
print(next(devuelvePares))
print("Aqui va mas codigo.......")
print(next(devuelvePares))
print("Aqui va mas codigo.......")
print(next(devuelvePares))

# yield from
# Simplifica el codigo de los generadores en el caso de utilizar bucles anidados dentro del generador (for dentro de otro)

# Vamos a crear un programa que nos devuelva una serie de ciudades

# Con el * dentro de parametros de la funcion, le indicamos que va a recibir un numero indeterminado de elementos y
# estos los acomoda en forma de tupla
def devulevleCiudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            # yield subElemento
        yield from elemento
        # yield elemento

ciudadesDevueltas = devulevleCiudades("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
miTupla = ("Julio", 14,2,1990,14)
print(miTupla[1])
print(miTupla[3])

# Construimos una lista desde la tupla
miLista = list(miTupla)
print(miLista)
print(miTupla)

# Convertir de lista a tupla
miTupla2 = tuple(miLista)
print(miTupla2)

# Verificamos si existe un elemento en la tupla
print("Julio" in miTupla)

# Nos cuenta cuantos elementos existe el que buscamos
print(miTupla.count(14))

# Nos indica la cantidad de elementos
print(len(miTupla))

# Tupla unitaria (con un unico elemento)
miTupla3 = ("Hola",)
print(miTupla3)
print(len(miTupla3))


# Desepaquetado de tupla
miTupla4 = ("Julio", 14,2,1990)
nombre,dia,mes,agno = miTupla4
print(nombre)
print(mes)
print(agno)
print(dia)

# Empaquetado de tupla
miTupla5 = "Adrianno", 27,9,2010
print(miTupla5)
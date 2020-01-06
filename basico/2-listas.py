miLista = ["Julio", "Cesar", "Ferrer", "Rhode"]
print(miLista)
# Mostramos los elementos desde el indice indicado
print(miLista[2:])

# Agregamos al final
miLista.append("Adrianno")
# Agregamos en una posicion especifica
miLista.insert(2,"Alejandro")

# Mostramos toda la lista
print(miLista[:])

# Extendemos los elementos de la lista
miLista.extend([1,2,3])

print(miLista[:])

# Devuelve el indice del elemento
print(miLista.index("Alejandro"))

# Buscar un elemento de la lista y devuelve un booleano
print("Rhode" in miLista)

# Eliminar un elemento de la lista
miLista.remove(1)
miLista.remove(2)
print(miLista[:])

# Eliminamos el ultimo elemento de la lista
miLista.pop()
print(miLista[:])

miLista2 = ["Julio", "Rafael"]
print(miLista2)

# Unir listas
miLista3 = miLista + miLista2
print(miLista3)

# Repetir la lista tantas veces se le indique
miLista4 = [1,2,3]*3
print(miLista4)
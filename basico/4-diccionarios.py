# SyntaxError: Non-ASCII character '\xc3'..... Para solucionar esto, se coloca lo siuiente:
#encoding=utf-8

print("hola")
miDiccionario={"Alemania":"Berlin","Venezuela":"Caracas","Espana":"Madrid"}
# Acceder a un elemento
print(miDiccionario["Venezuela"])
print(miDiccionario["Espana"])
print(miDiccionario)

miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

# Corregir un elemento
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

# Eliminar un elemento
del miDiccionario["Espana"]
print(miDiccionario)

miDiccionario2 = {"Nombre":"Julio", "Edad":40}
print(miDiccionario2)

miTupla = ["Francia", "Italia", "Alemania"]
miDiccionario3 = {miTupla[0]:"Paris", miTupla[1]:"Roma", miTupla[2]:"Berlin"}
print(miDiccionario3)
print(miDiccionario3["Francia"])

miDiccionario4 = {23:"Jordan", "Nombre":"Michael","Anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccionario4)
print(miDiccionario4["Anillos"])

# Diccionario dentro otro diccionario con tupla
miDiccionario5 = {23:"Jordan", "Nombre":"Michael","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario5)
print(miDiccionario5["Anillos"])

# Dvuelve las claves del diccionario
print(miDiccionario.keys())

# Devuelve los valores del dicionario
print(miDiccionario.values())

# Tamaño del diccionario
print(len(miDiccionario))



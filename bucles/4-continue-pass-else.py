for letra in "Python":
    if letra == "h":
        continue
    print("Viendo la letra: " + letra)


nombre = "Curso de Python"

contador = 0
for i in nombre:
    if i == " ":
        continue
    contador += 1

print("Cantidad de caracteres: " + str(len(nombre)))
print("Cantidad de caracteres sin espacios en blanco: " + str(contador))

email = input("Introduce tu email: ")
for i in email:
    if i == "@":
        arroba = True
        break; # Aqui sale del bucle

# Este pertenece al for y se ejecuta cuando ya no tenga mas nada que recorrer el bucle
else:
    arroba = False

print(arroba)
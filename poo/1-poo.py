class Coche():
    #Constructor de la clase
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        #Encapsulacion de variable para que no sea accesible desde el exterior de la clase
        self.__ruedas = 4
        self.enMarcha = False

    # self = esto es lo mismo que this. Lo que pasa es que en java estaba implicito pero aqui
    # en python hay que colocarlo

    #Metodo
    def arrancar(self,arrancamos):
        # pass no hace nada, es para que no haya fallo si se deja la funcion vacia
        # pass
        self.enMarcha = arrancamos

        if(self.enMarcha==True):
            verificar = self.__chequeo()

        if(self.enMarcha and verificar):
            return "El coche esta en marcha."
        elif(self.enMarcha and verificar==False):
            return "Algo ha ido mal con el chequeo. No se puede arrancar"
        else:
            return "El coche esta detenido."

    # Metodo
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis,
              " y un largo de ", self.largoChasis)

    #Metodo encapsulado
    def __chequeo(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

# Instanciamos la clase. Aqui no se usa el new para instanciar
miCoche = Coche()
#print("El largo del coche es:", miCoche.largoChasis)
#print("El ancho del coche es:", miCoche.anchoChasis)
#print("El coche tiene ", miCoche.ruedas, " ruedas.")
print(miCoche.arrancar(True)) # Al invocar el metodo, el self que recibe es: miCoche.enMarha = True
miCoche.estado()


print("---------- A continuacion creamos el segundo objeto ----------")
miCoche2 = Coche()
#print("El largo del coche es:", miCoche2.largoChasis)
#print("El ancho del coche es:", miCoche2.anchoChasis)
print(miCoche2.arrancar(False))
miCoche2.__ruedas = 2 #Como esta encapsulada, no se genera el cambio
miCoche2.estado()


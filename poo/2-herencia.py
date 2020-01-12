# Clase
class Vehiculos():
    # Constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    # Metodo
    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha,
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

# Herencia
class Furgoneta(Vehiculos):
    # Metodo
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

# Herencia
class Moto(Vehiculos):
    haceCaballito =""
    #Tiene por herencia los metodos de Vehiculo, mas el propio
    #Metodo
    def caballito(self):
        self.haceCaballito ="Voy haciendo caballito"

    #Sobreescritura de Metodo
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha,
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.haceCaballito)

class VehiculoElectrico(Vehiculos):
    def __init__(self, marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100

    def cargaEnergia(self):
        self.cargando = True

#Herencia Multiple
class BicicletaElectrica(VehiculoElectrico,Vehiculos):
    pass

# --------------------------------------------------------------------------------------------------------------
miMoto = Moto("Kawasaki", "ZX6R")
miMoto.caballito()
miMoto.estado()
print("\n--------------------------------------------------------\n")
miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print("\n--------------------------------------------------------\n")
#El constructor que toma de primero va de acuerdo al orden de la herencia que se haga al crear la clase,
# en pocas, se le da mas preferencia de izquierda a derecha y dara preferencia a ese constructor

# Esto dara error: TypeError: __init__() takes 1 positional argument but 3 were given
miBici = BicicletaElectrica("Shogun","HR100")

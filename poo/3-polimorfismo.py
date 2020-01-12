class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 10 ruedas")


#miVehiculo = Moto()
#miVehiculo.desplazamiento()

#miVehiculo2 = Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3 = Camion()
#miVehiculo3.desplazamiento()

def desplazaVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
# Al llamar al metodo desplazaVehiculo() y pasarle como parametro el objeto creado miVehiculo que es de tipo
# camion, viaja y se almacena en vehiculo del metodo desplazaVehiculo(). Como el objeto es de tipo camion,
# va a llamar el metodo desplazamiento() de la clase Camion
desplazaVehiculo(miVehiculo)

miVehiculo2 = Moto()
desplazaVehiculo(miVehiculo2)
miVehiculo3 = Coche()
desplazaVehiculo(miVehiculo3)

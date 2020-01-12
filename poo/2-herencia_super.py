class Persona():
    #Constructor
    def __init__(self,nombre, apellido, edad):
        self.nombre     = nombre
        self.apellido   = apellido
        self.edad       = edad
    #Metodo
    def descripcion(self):
        print("Nombre: ",self.nombre, "\nApellido: ", self.apellido, "\nEdad: ", self.edad)

class Empleado(Persona):
    #Constructor
    def __init__(self, salario, antiguedad,nombre,apellido,edad):
        super().__init__(nombre,apellido,edad)
        self.salario    = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        #Ejecuta el metodo del padre
        super().descripcion()
        print("Salario: ",self.salario,"\nAntiguedad: ",self.antiguedad)

#Principio de sustitucion:
# Es siempre un/a --> Un empleado siempre es una Persona = SI. Una persona siempre es un empleado = NO
# --------------------------------------------------------------------------------------------------------------
persona1  = Persona("Julio","Rhode",40)
persona1.descripcion()
print("\n--------------------------------------------------------\n")
empleado1 = Empleado(1500,21,"Julio","Rhode",40)
empleado1.descripcion()
print("empleado1 es de la clase Empleado: ",isinstance(empleado1,Empleado))
print("empleado1 es de la clase Persona: ",isinstance(empleado1,Persona))
print("persona1 es de la clase Empleado: ",isinstance(persona1,Empleado))
print("persona1 es de la clase Persona: ",isinstance(persona1,Persona))

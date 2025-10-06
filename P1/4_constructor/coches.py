import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase

    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):    
        self.marca=marca
        self.color=color
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas
    #Crear los metodos get y set para cada atributo estos metodos son importantes y necesarios en todas las clases que el programador creee para poder interactuar con los valores de los atributos a traves de estos metodos digamos que son la manera mas adecuada para solicitar un valor (get) o para modificar un valor (set) a un atributo en particular de la clase a traves de un objeto
    #En teoria se debe de crear un metodo get y set para cada atributo de la clase
    #Los metodos get y set siempre regresan un valor es decir el valor de la propiedad a traves del return
    #Por otro lado los metodos set no regresan ningun valor pero si reciben un parametro que es el valor que se le va a asignar a la propiedad

    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
    #2da. Forma
    @property
    def marca2(self):
        return self.marca
    @marca2.setter
    def marca2(self,marca):
        self.marca=marca

    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    def getModelo(self):
        return self.modelo
    def setModelo(self,modelo):
        self.modelo=modelo
    def getVelocidad(self):
        return self.velocidad
    def setVelocidad(self,velocidad):
        self.velocidad=velocidad
    def getCaballaje(self):
        return self.caballaje
    def setCaballaje(self,caballaje):
        self.caballaje=caballaje
    def getPlazas(self):
        return self.plazas
    def setPlazas(self,plazas):
        self.plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase
coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)
coche1.num_serie="akwjffawd"
coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"
print(coche4.marca2)

print(f"Datos del Vehiculo:\nMarca: {coche1.getMarca()}\nColor: {coche1.getColor()}\nModelo: {coche1.getModelo()}\nVelocidad: {coche1.getVelocidad()}\nCaballaje: {coche1.getCaballaje()}\nPlazas: {coche1.getPlazas()}\nNumero de serie: {coche1.num_serie}\n")
print(f"Datos del Vehiculo:\nMarca: {coche2.getMarca()}\nColor: {coche2.getColor()}\nModelo: {coche2.getModelo()}\nVelocidad: {coche2.getVelocidad()}\nCaballaje: {coche2.getCaballaje()}\nPlazas: {coche2.getPlazas()}")

print(coche3.marca2)
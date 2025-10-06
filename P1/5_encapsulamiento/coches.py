import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase

    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):    
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas
    #Crear los metodos get y set para cada atributo estos metodos son importantes y necesarios en todas las clases que el programador creee para poder interactuar con los valores de los atributos a traves de estos metodos digamos que son la manera mas adecuada para solicitar un valor (get) o para modificar un valor (set) a un atributo en particular de la clase a traves de un objeto
    #En teoria se debe de crear un metodo get y set para cada atributo de la clase
    #Los metodos get y set siempre regresan un valor es decir el valor de la propiedad a traves del return
    #Por otro lado los metodos set no regresan ningun valor pero si reciben un parametro que es el valor que se le va a asignar a la propiedad

    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca=marca
    #2da. Forma
    @property
    def marca2(self):
        return self.__marca
    @marca2.setter
    def marca2(self,marca):
        self.__marca=marca

    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color=color
    def getModelo(self):
        return self.__modelo
    def setModelo(self,modelo):
        self.__modelo=modelo
    def getVelocidad(self):
        return self.__velocidad
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad
    def getCaballaje(self):
        return self.__caballaje
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje
    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,plazas):
        self.__plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      return "Estas hacelerando"

    def frenar(self):
      return "Estas frenando"

#Fin definir clase

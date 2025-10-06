import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase

    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):    
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
    #Crear los metodos get y set para cada atributo estos metodos son importantes y necesarios en todas las clases que el programador creee para poder interactuar con los valores de los atributos a traves de estos metodos digamos que son la manera mas adecuada para solicitar un valor (get) o para modificar un valor (set) a un atributo en particular de la clase a traves de un objeto
    #En teoria se debe de crear un metodo get y set para cada atributo de la clase
    #Los metodos get y set siempre regresan un valor es decir el valor de la propiedad a traves del return
    #Por otro lado los metodos set no regresan ningun valor pero si reciben un parametro que es el valor que se le va a asignar a la propiedad

    #2da. Forma
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad
    @property
    def caballaje(self):
        return self._caballaje
    @caballaje.setter
    def caballaje(self,caballaje):
        self._caballaje=caballaje
    @property
    def plazas(self):
        return self._plazas
    @plazas.setter
    def plazas(self,plazas):
        self._plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      return "Estas acelerando el coche"

    def frenar(self):
      return "Estas frenando el coche"

#Fin definir clase

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga
        

    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga
    def acelerar(self):
        return "Estas acelerando el camion"
    def frenar(self):
        return "Estas frenando el camion"
    
    @property
    def eje(self):
        return self.__eje
    @eje.setter
    def eje(self,eje):
        self.__eje=eje

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    @capacidadCarga.setter
    def capacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga


class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

    def transportar(self,num_pasajeros):
        self.num_pasajeros=num_pasajeros
        return self.num_pasajeros
    def acelerar(self):
        return "Estas acelerando la camioneta"
    def frenar(self):
        return "Estas frenando la camioneta"
    
    @property
    def traccion(self):
        return self.__traccion
    @traccion.setter
    def traccion(self,traccion):
        self.__traccion=traccion

    @property
    def cerrada(self):
        return self.__cerrada
    @cerrada.setter
    def cerrada(self,cerrada):
        self.__cerrada=cerrada
import os
os.system("cls")

class clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio
    
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self,tamanio):
        self.tamanio=tamanio

    def __getAtributo_Privado(self):
        return self.__atributo_privado
    def getAtributo_Privado2(self):
        self.__getAtributo_Privado()
    def setAtributo_Privado(self,atributo_privado):
        self.__atributo_privado=atributo_privado

#Usar los atributos y metodos de acuerdo a su encapsulamiento
objeto=clase("Rojo","Grande")
print(f"Mi objeto tinene los siguientes atributos: {objeto.color} y {objeto.tamanio}")


print(f"Soy el contenido del atributo publico: {objeto.atributo_publico}")
print(f"Soy el contenido del atributo protegido: {objeto._atributo_protegido}")
print(f"Soy el contenido del atributo privado: {objeto.getAtributo_Privado2()}")
objeto.setAtributo_Privado("Se ha cambiado el valor de atributo privado")
print(f"Soy el contenido del atributo privado: {objeto.getAtributo_Privado2()}")
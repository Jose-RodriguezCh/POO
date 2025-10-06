'''
CONDICIONES

1. NO hay meotodo constructor
2. TODOS LOS ATRIBUTOS SEAN PUBLICOS
3. Metodo acelerar y frenar no hacen nada
'''
import os
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase
coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

coche2=Coches()
coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"Datos del Vehiculo:\nMarca: {coche1.marca}\nColor: {coche1.color}\nModelo: {coche1.modelo}\nVelocidad: {coche1.velocidad}\nCaballaje: {coche1.caballaje}\nPlazas: {coche1.plazas}\n")
print(f"Datos del Vehiculo:\nMarca: {coche2.marca}\ncolor: {coche2.color}\nModelo: {coche2.modelo}\nVelocidad: {coche2.velocidad}\nCaballaje: {coche2.caballaje}\nPlazas: {coche2.plazas}")
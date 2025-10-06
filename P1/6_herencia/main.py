from coches import *
import os
os.system("cls")

#Solicitar los datos que posteriormente seran los atributos de los objetos

'''num_coches=input("¿Cuantos coches o vehiculos tienes?")
for i in range(0,num_coches):
    print(f"\n\t...Datos del automovil #{i+1}...")
    marca=input("Ingresa la marca del auto: ").upper()
    color=input("Ingresa el color del auto: ").upper()
    modelo=input("Ingresa el modelo del auto: ").upper()
    velocidad=int(input("Ingresa la velocidad del auto: "))
    potencia=int(input("Ingresa la potencia del auto: "))
    plazas=int(input("Ingresa el numero de plazas del auto: "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n")

'''
coche=Coches("VW","Blanco","2020",220,180,4)
print(coche._color,coche.acelerar())

camion=Camiones("VW","Blanco a parciado","2020",220,180,4,2,2500)
print(camion._color,camion.acelerar())

camioneta=Camionetas("VW","Azul","2020",220,180,4,"Delantera",True)
print(camioneta._color,camioneta.acelerar())



'''coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda")
coche1.num_serie="akwjffawd"
coche4=Coches("","","",0,0,0)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")
print(f"\nDatos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")()

print(coche3.marca2)'''
'''
Elaborar un programa que calcule el area de un rectangulo
-Implementar el paradigma estructurado
-Implementar el paradigma orientado a objetos
'''
import os
os.system("cls")

#Estructurado
def CalcularArea(b,h):
    area=b*h
    return area

b=float(input("Ingresa la base del rectangulo: "))
h=float(input("Ingresa la altura del rectangulo: "))
area=CalcularArea(b,h)
print(f"El area del rectangulo es: {area}")

#Orientado a Objetos
class Reactangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura

rect=Reactangulo(5,3)
print(rect.area())
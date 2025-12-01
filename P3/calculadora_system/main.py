'''
    Crear una calculadora:
    1.- Dos campos de texto
    2.- 4 botones para las operaciones
    3.- Mostrar el resultado en una alerta
    4.- Programado de forma oo
    4.- Considerar el MVC
'''
from view import interfaz
from tkinter import *

class App:
    def __init__(self,ventana):
        #Ejecutar la ventana
        view=interfaz.vista(ventana)
    # @staticmethod
    # def main(ventana):
    #     view=interfaz.vista(ventana)
        
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    # App.main(ventana)
    ventana.mainloop()
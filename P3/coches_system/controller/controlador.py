from tkinter import messagebox
from view import view1

class controlador:
    #Autos
    @staticmethod
    def insertar_autos(marca,color,modelo,velocidad,caballaje,plazas):
        resultado=""#Pendiente
        controlador.respuesta_sql(resultado)
    
    @staticmethod
    def consultar_autos():
        resultado=""#Pendiente
        return resultado
    
    @staticmethod
    def consultar_id_autos(id):
        resultado=""#Pendiente
        return resultado

    @staticmethod
    def actualizar_autos(id,marca,color,modelo,velocidad,caballaje,plazas):
        resultado=""#Pendiente
        controlador.respuesta_sql(resultado)
    
    @staticmethod
    def eliminar_autos(id):
        resultado=""#Pendiente
        controlador.respuesta_sql(resultado)

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(message="Accion realizada con exito")
        else:
            messagebox.showinfo(message="ERROR realizado con exito")
from tkinter import messagebox
from view import view1
from model import cochesBD as coches

class controlador:
    #Autos
    @staticmethod
    def insertar_autos(marca,color,modelo,velocidad,caballaje,plazas):
        resultado=coches.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        controlador.respuesta_sql(resultado)
    
    @staticmethod
    def consultar_autos():
        resultado=coches.Autos.consultar()
        return resultado
    
    @staticmethod
    def consultar_id_autos(id):
        resultado=coches.Autos.consultar_id(id)
        return resultado

    @staticmethod
    def actualizar_autos(id,marca,color,modelo,velocidad,caballaje,plazas):
        resultado=coches.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
        controlador.respuesta_sql(resultado)
    
    @staticmethod
    def eliminar_autos(id):
        resultado=coches.Autos.elminiar(id)
        controlador.respuesta_sql(resultado)

    #Camoinetas
    @staticmethod
    def insertar_camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        cerrada=cerrada.upper()
        if cerrada=="SI":
            res=True
            resultado=coches.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,res)
            controlador.respuesta_sql(resultado)
        elif cerrada=="NO":
            res=False
            resultado=coches.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,res)
            controlador.respuesta_sql(resultado)
        else:
            messagebox.showinfo(message="ERROR, solo se acepta si o no")
    
    @staticmethod
    def consultar_camionetas():
        resultado=coches.Camionetas.consultar()
        return resultado
    
    @staticmethod
    def consultar_id_camionetas(id):
        resultado=coches.Camionetas.consultar_id(id)
        return resultado

    @staticmethod
    def actualizar_camionetas(id,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        cerrada=cerrada.upper()
        if cerrada=="SI":
            res=True
            resultado=coches.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,res,id)
            controlador.respuesta_sql(resultado)
        elif cerrada=="NO":
            res=False
            resultado=coches.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,res,id)
            controlador.respuesta_sql(resultado)
        else:
            messagebox.showinfo(message="ERROR, solo se acepta si o no")

    
    @staticmethod
    def eliminar_camionetas(id):
        resultado=coches.Camionetas.elminiar(id)
        controlador.respuesta_sql(resultado)


    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(message="Accion realizada con exito")
        else:
            messagebox.showinfo(message="ERROR")
from tkinter import messagebox
from model import usuario,nota
from view import view1

class controlador:
    @staticmethod
    def registro(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon='info',message=f"{nombre} {apellidos} Se registro correctamente con el email: {email}",title="Usuarios")
        else:
            messagebox.showinfo(icon='info',message=f"** Por favor intentarlo de nuevo, no fue posible insertar el registro **",title="Usuarios")
    
    @staticmethod
    def inicio_sesion(ventana,email,contrasenia):
        registro=usuario.Usuario.iniciar_sesion(email,contrasenia)
        if registro:
            messagebox.showinfo(icon='info',message=f"{registro[1]} {registro[2]} Has iniciado sesion correctamente",title="Usuarios")
            view1.view.menuNotas(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showinfo(icon='info',message=f"** Email y/o contraseña incorrecta, volver a intentarlo **",title="Usuarios")
    
    @staticmethod
    def crearNota(id,titulo,descripcion):
        resultado=nota.Nota.crear(id,titulo,descripcion)
        controlador.respuesta_sql(resultado)
    
    @staticmethod
    def mostrarNota(id):
        resultado=nota.Nota.mostrar(id)
        return resultado
    
    @staticmethod
    def buscar_nota(id,id_user):
        resultado=nota.Nota.buscar_id(id,id_user)
        return resultado
    
    @staticmethod
    def actualizarNota(id,titulo,descripcion):
        resultado=nota.Nota.actualizar(id,titulo,descripcion)
        controlador.respuesta_sql(resultado)

    @staticmethod
    def eliminarNota(id):
        resultado=nota.Nota.eliminar(id)
        controlador.respuesta_sql(resultado)
    
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(message="Accion realizada con exito")
        else:
            messagebox.showinfo(message="ERROR realizado con exito")
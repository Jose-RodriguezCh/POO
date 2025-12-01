from tkinter import *
from tkinter import messagebox
from controller import controlador1

class view:
    def __init__(self,ventana):
        ventana.title("Gestion de notas")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.interfazPrincipal(ventana)
    
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def interfazPrincipal(ventana):
        view.borrarPantalla(ventana)
        Label(ventana,text=".:: Menu Principal ::.",justify=CENTER).pack(pady=5,padx=10)
        btn_registro=Button(ventana,text="1.- Registro",command=lambda:view.interfazRegistro(ventana),justify=CENTER)
        btn_registro.pack(pady=10)
        btn_login=Button(ventana,text="2.- Login",command=lambda:view.interfazLogin(ventana),justify=CENTER)
        btn_login.pack(pady=10)
        btn_salir=Button(ventana,text="3.- Salir",command=ventana.quit,justify=CENTER)
        btn_salir.pack(pady=1)

    @staticmethod
    def interfazRegistro(ventana):
        view.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Registro en el sistema ::.\n",justify=CENTER).pack(pady=10)
        
        lbl_nombre=Label(ventana,text="¿Cual es tu nombre?",justify=CENTER)
        lbl_nombre.pack(pady=10)
        txt_nombre=Entry(ventana)
        txt_nombre.focus()
        txt_nombre.pack(pady=10)

        lbl_apellidos=Label(ventana,text="¿Cual son tus apellidos?",justify=CENTER)
        lbl_apellidos.pack(pady=10)
        txt_apellidos=Entry(ventana)
        txt_apellidos.pack(pady=10)

        lbl_email=Label(ventana,text="Ingresa tu email",justify=CENTER)
        lbl_email.pack(pady=10)
        txt_email=Entry(ventana)
        txt_email.pack(pady=10)

        lbl_contrasenia=Label(ventana,text="Ingresa tu contraseña",justify=CENTER)
        lbl_contrasenia.pack(pady=10)
        txt_contrasenia=Entry(ventana)
        txt_contrasenia.pack(pady=10)
        
        btn_registrar=Button(ventana,text="Registrar",command=lambda:(controlador1.controlador.registro(txt_nombre.get(),txt_apellidos.get(),txt_email.get(),txt_contrasenia.get()),view.interfazLogin(ventana)),justify=CENTER)
        btn_registrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda:view.interfazPrincipal(ventana),justify=CENTER)
        btn_volver.pack(pady=1)
    
    @staticmethod
    def interfazLogin(ventana):
        view.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: inicio de Sesion ::.\n",justify=CENTER).pack(pady=10)

        lbl_email=Label(ventana,text="Ingresa tu email",justify=CENTER)
        lbl_email.pack(pady=10)
        txt_email=Entry(ventana)
        txt_email.focus()
        txt_email.pack(pady=10)

        lbl_contrasenia=Label(ventana,text="Ingresa tu contraseña",justify=CENTER)
        lbl_contrasenia.pack(pady=10)
        txt_contrasenia=Entry(ventana)
        txt_contrasenia.pack(pady=10)
        
        btn_entrar=Button(ventana,text="Entrar",command=lambda:controlador1.controlador.inicio_sesion(ventana,txt_email.get(),txt_contrasenia.get()),justify=CENTER)
        btn_entrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda:view.interfazPrincipal(ventana),justify=CENTER)
        btn_volver.pack(pady=1)

    @staticmethod
    def menuNotas(ventana,usuario_id,nombre,apellidos):
        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos
        
        view.borrarPantalla(ventana)
        Label(ventana,text=f".:: Bienvenido {nombre} {apellidos}, has iniciado sesion ::.",justify=CENTER).pack(pady=5,padx=10)
        btn_crear=Button(ventana,text="1.- Crear",command=lambda:view.crearNota(ventana),justify=CENTER)
        btn_crear.pack(pady=10)
        btn_mostrar=Button(ventana,text="2.- Mostrar",command=lambda:view.mostrarNota(ventana),justify=CENTER)
        btn_mostrar.pack(pady=10)
        btn_cambiar=Button(ventana,text="3.- Cambiar",command=lambda:view.buscar_id(ventana,"cambiar"),justify=CENTER)
        btn_cambiar.pack(pady=1)
        btn_eliminar=Button(ventana,text="4.- Eliminar",command=lambda:view.buscar_id(ventana,"borrar"),justify=CENTER)
        btn_eliminar.pack(pady=10)
        btn_regresar=Button(ventana,text="5.- Regresar",command=lambda:view.interfazPrincipal(ventana),justify=CENTER)
        btn_regresar.pack(pady=10)
    
    @staticmethod
    def crearNota(ventana):
        view.borrarPantalla(ventana)
        Label(ventana,text=".:: Crear Nota ::.\n",justify=CENTER).pack(pady=10)

        lbl_titulo=Label(ventana,text="Titulo:",justify=CENTER)
        lbl_titulo.pack(pady=10)
        titulo=StringVar()
        txt_titulo=Entry(ventana,textvariable=titulo,justify=RIGHT)
        txt_titulo.focus()
        txt_titulo.pack(pady=10)

        lbl_descripcion=Label(ventana,text="Descripcion:",justify=CENTER)
        lbl_descripcion.pack(pady=10)
        desc=StringVar()
        txt_descripcion=Entry(ventana,textvariable=desc,justify=RIGHT)
        txt_descripcion.pack(pady=10)
        
        btn_guardar=Button(ventana,text="Guardar",command=lambda:controlador1.controlador.crearNota(id_user,titulo.get(),desc.get()),justify=CENTER)
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda:view.menuNotas(ventana,id_user,nom_user,ape_user),justify=CENTER)
        btn_volver.pack(pady=1)

    @staticmethod
    def mostrarNota(ventana):
        view.borrarPantalla(ventana)
        registros=controlador1.controlador.mostrarNota(id_user)
        if len(registros)>0:
            filas=""
            Label(ventana,text="Tus notas son:\n",justify=CENTER).pack(pady=10)
            for fila in registros:
                filas+=f"ID: {fila[0]} \nTitulo: {fila[2]}\nDescripcion: {fila[3]}\nFecha: {fila[4]}\n\n"
        else:
            filas="...¡No existen notas para este usuario!..."

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)

        
        #Consulta y un for
        # lbl_titulo=Label(ventana,text="Titulo:",justify=CENTER)
        # lbl_titulo.pack(pady=10)
        # txt_titulo=Entry(ventana)
        # txt_titulo.focus()
        # txt_titulo.pack(pady=10)

        # lbl_descripcion=Label(ventana,text="Descripcion:",justify=CENTER)
        # lbl_descripcion.pack(pady=10)
        # txt_descripcion=Entry(ventana)
        # txt_descripcion.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",command=lambda:view.menuNotas(ventana,id_user,nom_user,ape_user),justify=CENTER)
        btn_volver.pack(pady=1)
    
    @staticmethod
    def buscar_id(ventana,tipo):
        view.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Buscar una Nota::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text=f"ID de la Nota a buscar: ")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana,text="Buscar",command=lambda:view.cambiar_id(ventana,id.get())).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana,text="Buscar",command=lambda:view.eliminar_id(ventana,id.get())).pack(pady=5)

    @staticmethod
    def cambiar_id(ventana,id_):
        registro=controlador1.controlador.buscar_nota(id_,id_user)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta nota en la BD ...")
        else:
            view.borrarPantalla(ventana)

            lbl_titulo=Label(ventana,text=f".::Cambiar una nota::.")
            lbl_titulo.pack(pady=10)

            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            Label(ventana,text="Titulo: ").pack(pady=5)
            titulo=StringVar()
            txt_titulo=Entry(ventana,textvariable=titulo,justify=RIGHT)
            titulo.set(registro[2])
            txt_titulo.pack(pady=5)

            Label(ventana,text="Descripcion: ").pack(pady=5)
            desc=StringVar()
            lbl_desc=Entry(ventana,textvariable=desc,justify=RIGHT)
            desc.set(registro[3])
            lbl_desc.pack(pady=5)
                
            Button(ventana,text="Guardar",command=lambda:controlador1.controlador.actualizarNota(id_,titulo.get(),desc.get())).pack(pady=5)
            Button(ventana,text="Volver",command=lambda:view.menuNotas(ventana,id_user,nom_user,ape_user)).pack(pady=5)

    #Vista de eliminar pantalla
    @staticmethod
    def eliminar_id(ventana,id_):
        registro=controlador1.controlador.buscar_nota(id_,id_user)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta nota en la BD ...")
        else:
            view.borrarPantalla(ventana)

            lbl_titulo=Label(ventana,text=".::Borrar una nota::.")
            lbl_titulo.pack(pady=10)
            lbl_id=Label(ventana,text=f"\nID de la nota:\n")
            lbl_id.pack(pady=5)
            
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify=RIGHT,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:controlador1.controlador.eliminarNota(id_))
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="Volver",command=lambda:view.menuNotas(ventana,id_user,nom_user,ape_user))
            btn_volver.pack(pady=5)

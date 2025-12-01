from tkinter import messagebox
from tkinter import *
from controller import funciones
from model import operaciones

#Interfaz o view
class vista:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("500x500")
        ventana.resizable(False,False)
        self.interfaz_principal(ventana)

    @staticmethod
    def interfaz_principal(ventana):
        vista.borrrarPantalla(ventana)
        vista.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1,width=5,justify=RIGHT)
        txt_numero1.focus()
        txt_numero1.pack(side=TOP,anchor=CENTER)
        txt_numero2=Entry(ventana,textvariable=n2,width=5,justify=RIGHT)
        txt_numero2.pack(side=TOP,anchor=CENTER)

        btn_sumar=Button(ventana,text="+",command=lambda:funciones.funciones.respuesta_sql(funciones.funciones.operacion("+",n1.get(),n2.get())))
        btn_sumar.pack()
        btn_restar=Button(ventana,text="-",command=lambda:funciones.funciones.respuesta_sql(funciones.funciones.operacion("-",n1.get(),n2.get())))
        btn_restar.pack()
        btn_multiplicar=Button(ventana,text="X",command=lambda:funciones.funciones.respuesta_sql(funciones.funciones.operacion("X",n1.get(),n2.get())))
        btn_multiplicar.pack()
        btn_dividir=Button(ventana,text="/",command=lambda:funciones.funciones.respuesta_sql(funciones.funciones.operacion("/",n1.get(),n2.get())))
        btn_dividir.pack()
        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack()

        ventana.mainloop()
    
    #Menu de la app de operaciones
    @staticmethod
    def menuPrincipal(ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)
        
        operacionesMenu=Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Operaciones",menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda: vista.interfaz_principal(ventana))
        operacionesMenu.add_command(label="Consultar",command=lambda: vista.consultar(ventana))
        operacionesMenu.add_command(label="Cambiar",command=lambda: vista.buscar_id(ventana,"cambiar"))
        operacionesMenu.add_command(label="Borrar",command=lambda: vista.buscar_id(ventana,"borrar"))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="salir",command=ventana.quit)

    @staticmethod
    def consultar(ventana):
        vista.borrrarPantalla(ventana)
        vista.menuPrincipal(ventana)
        titulo=Label(ventana,text=".::Listado de las operaciones::.")
        titulo.pack(pady=10)
        cursor=operaciones.operaciones.consultar()
        if len(cursor)>0:
            l=1
            for i in cursor:
                op=Label(ventana,text=f"Operacion: {l} ID: {i[0]} Fecha de Creacion: {i[1]}\n Operacion: {i[2]}{i[4]}{i[3]} = {i[5]}")
                op.pack(pady=10)
                l+=1
        else:
            messagebox.showinfo(title="Error",message="No existen operaciones guardadas en la BD...",icon="info")
        
        btn_volver=Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def buscar_id(ventana,tipo):
        vista.borrrarPantalla(ventana)
        vista.menuPrincipal(ventana)

        lbl_titulo=Label(ventana,text=f".::Buscar una Operacion::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text=f"ID de la Operacion a buscar: ")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana,text="Buscar",command=lambda:vista.cambiar_id(ventana,id.get())).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana,text="Buscar",command=lambda:vista.eliminar_id(ventana,id.get())).pack(pady=5)

    @staticmethod
    def cambiar_id(ventana,id_):
        registro=operaciones.operaciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta operacion en la BD ...")
        else:
            vista.borrrarPantalla(ventana)
            vista.menuPrincipal(ventana)

            lbl_titulo=Label(ventana,text=f".::Cambiar una Operacion::.")
            lbl_titulo.pack(pady=10)

            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            Label(ventana,text="Número 1: ").pack(pady=5)
            n1=IntVar()
            numero1=Entry(ventana,textvariable=n1,justify=RIGHT,width=5)
            n1.set(registro[2])
            numero1.pack(pady=5)

            Label(ventana,text="Número 2: ").pack(pady=5)
            n2=IntVar()
            numero2=Entry(ventana,textvariable=n2,justify=RIGHT,width=5)
            n2.set(registro[3])
            numero2.pack(pady=5)

            Label(ventana,text="Signo: ").pack(pady=5)
            sig=StringVar()
            signo=Entry(ventana,justify=CENTER,textvariable=sig,width=5)
            sig.set(registro[4])
            signo.pack(pady=5)

            Label(ventana,text="Resultado: ").pack(pady=5)
            resul=DoubleVar()
            resultado=Entry(ventana,textvariable=resul,justify=RIGHT,width=5)
            resul.set(registro[5])
            resultado.pack(pady=5)
                
            Button(ventana,text="Guardar",command=lambda:operaciones.operaciones.actualizar(n1.get(),n2.get(),sig.get(),resul.get(),id_)).pack(pady=5)
            Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana)).pack(pady=5)

    #Vista de eliminar pantalla
    @staticmethod
    def eliminar_id(ventana,id_):
        registro=operaciones.operaciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta operacion en la BD ...")
        else:
            vista.borrrarPantalla(ventana)
            vista.menuPrincipal(ventana)

            lbl_titulo=Label(ventana,text=".::Borrar una operacion::.")
            lbl_titulo.pack(pady=10)
            lbl_id=Label(ventana,text=f"\nID de la operacion:\n")
            lbl_id.pack(pady=5)
            
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify=RIGHT,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:operaciones.operaciones.eliminar(id_))
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana))
            btn_volver.pack(pady=5)

    #Borrar Pantalla
    @staticmethod
    def borrrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
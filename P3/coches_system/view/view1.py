from tkinter import *
from tkinter import messagebox,ttk
import customtkinter as ctk

class view:
    def __init__(self,ventana):
        ventana.title("Coches_System")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)
    
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        view.borrarPantalla(ventana)
        Label(ventana,text=".:: Menu Principal ::.",justify=CENTER).pack(pady=5,padx=10)
        btn_autos=Button(ventana,text="1.- Autos",command=lambda:view.menu_acciones(ventana,"Autos"),justify=CENTER)
        btn_autos.pack(pady=10)
        btn_camionetas=Button(ventana,text="2.- Camionetas",command=lambda:view.menu_acciones(ventana,"Camionetas"),justify=CENTER)
        btn_camionetas.pack(pady=10)
        btn_camiones=Button(ventana,text="3.- Camiones",command=lambda:view.menu_acciones(ventana,"Camiones"),justify=CENTER)
        btn_camiones.pack(pady=10)
        btn_salir=Button(ventana,text="4.- Salir",command=ventana.quit,justify=CENTER)
        btn_salir.pack(pady=1)

    @staticmethod
    def menu_acciones(ventana,tipo):
        view.borrarPantalla(ventana)
        Label(ventana,text=f".:: Menu de {tipo} ::.",justify=CENTER).pack(pady=5,padx=10)
        if tipo=="Autos":
            insertar=lambda:view.insertar_autos(ventana)
            consultar=lambda:view.consultar_autos(ventana)
            actualizar=lambda:view.buscar_id_auto(ventana,"actualizar")
            eliminar=lambda:view.buscar_id_auto(ventana,"eliminar")
        elif tipo=="Camionetas":
            insertar=lambda:view.insertar_camionetas(ventana)
        elif tipo=="Camiones":
            insertar=lambda:view.insertar_camiones(ventana)


        btn_insertar=Button(ventana,text="1.- Insertar",command=insertar,justify=CENTER)
        btn_insertar.pack(pady=10)
        btn_consultar=Button(ventana,text="2.- Consultar",command=consultar,justify=CENTER)
        btn_consultar.pack(pady=10)
        btn_actualizar=Button(ventana,text="3.- Actualizar",command=actualizar,justify=CENTER)
        btn_actualizar.pack(pady=1)
        btn_eliminar=Button(ventana,text="4.- Eliminar",command=eliminar,justify=CENTER)
        btn_eliminar.pack(pady=10)
        btn_regresar=Button(ventana,text="5.- Regresar",command=lambda:view.menu_principal(ventana),justify=CENTER)
        btn_regresar.pack(pady=10)
    
    @staticmethod
    def insertar_autos(ventana):
        view.borrarPantalla(ventana)
        Label(ventana,text=".:: Datos del vehiculo ::.\n",justify=CENTER).pack(pady=10)

        lbl_marca=Label(ventana,text="Marca:",justify=CENTER)
        lbl_marca.pack(pady=10)
        marca=StringVar()
        txt_marca=Entry(ventana,textvariable=marca,justify=RIGHT)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Color:",justify=CENTER)
        lbl_color.pack(pady=10)
        color=StringVar()
        txt_color=Entry(ventana,textvariable=color,justify=RIGHT)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Modelo:",justify=CENTER)
        lbl_modelo.pack(pady=10)
        modelo=StringVar()
        txt_modelo=Entry(ventana,textvariable=modelo,justify=RIGHT)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Velocidad:",justify=CENTER)
        lbl_velocidad.pack(pady=10)
        velocidad=StringVar()
        txt_velocidad=Entry(ventana,textvariable=velocidad,justify=RIGHT)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(ventana,text="Caballaje:",justify=CENTER)
        lbl_caballaje.pack(pady=10)
        caballaje=StringVar()
        txt_caballaje=Entry(ventana,textvariable=caballaje,justify=RIGHT)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(ventana,text="Plazas:",justify=CENTER)
        lbl_plazas.pack(pady=10)
        plazas=StringVar()
        txt_plazas=Entry(ventana,textvariable=plazas,justify=RIGHT)
        txt_plazas.pack(pady=5)
        
        btn_guardar=Button(ventana,text="Guardar",command=lambda:"",justify=CENTER)
        btn_guardar.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:view.menu_acciones(ventana,"Autos"),justify=CENTER)
        btn_volver.pack(pady=5)

    @staticmethod
    def consultar_autos(ventana):
        view.borrarPantalla(ventana)
        Label(ventana,text=".:: Consulta de Autos ::.\n",justify=CENTER).pack(pady=10)
        registros=[
            ["1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2"]
        ]
        if len(registros)>0:
            columnas=("ID","Marca","Color","Modelo","Velocidad","Potencia","Plazas")
            tree_frame = ctk.CTkFrame(ventana, fg_color="transparent")
            tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))
            autos_tree=ttk.Treeview(tree_frame, columns=columnas, show="headings", height=10)
            
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=autos_tree.yview)
            scrollbarx= ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=autos_tree.xview)
            autos_tree.configure(yscroll=scrollbar.set,xscroll=scrollbarx.set)
            scrollbar.pack(side="right", fill="y")
            scrollbarx.pack(side=BOTTOM, fill="x")
            autos_tree.pack(side="left", fill=BOTH, expand=True)

            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview", background="#F0F0F0", foreground="black", rowheight=18, fieldbackground="#F0F0F0")
            style.configure("Treeview.Heading", background="#D1D5DB", foreground="black", font=("Arial", 12, "bold"))

            for col in columnas:
                autos_tree.heading(col, text=col)
                autos_tree.column(col, width=120, anchor="center")

            for item in registros:
                fila = (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
                autos_tree.insert("", END, values=fila)
        else:
            ctk.CTkLabel(ventana, text="No hay datos para mostrar", font=ctk.CTkFont(size=16)).pack(pady=20)
        
        btn_volver=Button(ventana,text="Volver",command=lambda:view.menu_acciones(ventana,"Autos"),justify=CENTER)
        btn_volver.pack(pady=1)
    
    @staticmethod
    def buscar_id_auto(ventana,tipo):
        view.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Buscar un Auto::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text=f"ID del auto a buscar: ")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="actualizar":
            Button(ventana,text="Buscar",command=lambda:view.cambiar_autos(ventana,id.get())).pack(pady=5)
        elif tipo=="eliminar":
            Button(ventana,text="Buscar",command=lambda:view.eliminar_autos(ventana,id.get())).pack(pady=5)

    @staticmethod
    def cambiar_autos(ventana,id_):
        registro=[
            ["1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2"]
        ]
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta nota en la BD ...")
        else:
            view.borrarPantalla(ventana)

            lbl_titulo=Label(ventana,text=f".::Cambiar un Auto::.")
            lbl_titulo.pack(pady=10)

            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5,state="readonly")
            id.set(registro[1][0])
            txt_id.focus()
            txt_id.pack(pady=5)

            Label(ventana,text="Marca: ").pack(pady=5)
            marca=StringVar()
            txt_marca=Entry(ventana,textvariable=marca,justify=RIGHT)
            marca.set("Pendiente")
            txt_marca.pack(pady=5)

            Label(ventana,text="Color: ").pack(pady=5)
            color=StringVar()
            lbl_color=Entry(ventana,textvariable=color,justify=RIGHT)
            color.set("Pendiente")
            lbl_color.pack(pady=5)
            
            Label(ventana,text="Modelo: ").pack(pady=5)
            modelo=StringVar()
            lbl_modelo=Entry(ventana,textvariable=modelo,justify=RIGHT)
            modelo.set("Pendiente")
            lbl_modelo.pack(pady=5)

            Label(ventana,text="Velocidad: ").pack(pady=5)
            velocidad=StringVar()
            lbl_velocidad=Entry(ventana,textvariable=velocidad,justify=RIGHT)
            velocidad.set("Pendiente")
            lbl_velocidad.pack(pady=5)

            Label(ventana,text="Potencia: ").pack(pady=5)
            potencia=StringVar()
            lbl_potencia=Entry(ventana,textvariable=potencia,justify=RIGHT)
            potencia.set("Pendiente")
            lbl_potencia.pack(pady=5)

            Label(ventana,text="Plazas: ").pack(pady=5)
            plazas=StringVar()
            lbl_plazas=Entry(ventana,textvariable=plazas,justify=RIGHT)
            plazas.set("Pendiente")
            lbl_plazas.pack(pady=5)
                
            Button(ventana,text="Guardar",command=lambda:"").pack(pady=5)
            Button(ventana,text="Volver",command=lambda:view.menu_acciones(ventana,"Autos")).pack(pady=5)

    #Vista de eliminar pantalla
    @staticmethod
    def eliminar_autos(ventana,id_):
        registro=[
            ["1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2"]
        ]
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta nota en la BD ...")
        else:
            view.borrarPantalla(ventana)

            lbl_titulo=Label(ventana,text=".::Borrar un Auto::.")
            lbl_titulo.pack(pady=10)
            lbl_id=Label(ventana,text=f"\nID del Auto:\n")
            lbl_id.pack(pady=5)
            
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify=RIGHT,state="readonly")
            id.set(registro[1][0])
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:"")
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="Volver",command=lambda:view.menu_acciones(ventana,"Autos"))
            btn_volver.pack(pady=5)

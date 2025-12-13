from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
import customtkinter as ctk
from view import usuarios as usu
from controller import controller

class inventario:
    def __init__(self, ventana):
        self.consultar(ventana)  # Ventana principal

    @staticmethod
    def borrrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menuPrincipal(ventana, menuBar):
        inventarioMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Inventario", menu=inventarioMenu)
        inventarioMenu.add_command(label="Agregar", command=lambda: "")
        inventarioMenu.add_command(label="Consultar", command=lambda: inventario.consultar(ventana))
        inventarioMenu.add_command(label="Cambiar", command=lambda: "")
        inventarioMenu.add_command(label="Borrar", command=lambda: "")
        inventarioMenu.add_separator()
        inventarioMenu.add_command(label="Salir", command=ventana.quit)

    @staticmethod
    def consultar(ventana):
        inventario.borrrarPantalla(ventana)

        # ===== TÍTULO PRINCIPAL =====
        titulo = ctk.CTkLabel(
            ventana,
            text="📊 Reporte General de Inventario",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#1B6CA8"
        )
        titulo.pack(pady=25)

        cursor = controller.productos.consultar()

        if len(cursor) > 0:
            contar = controller.inventario.consultar()

            # ===== CONTENEDOR PRINCIPAL =====
            frame_totales = ctk.CTkFrame(
                ventana, 
                fg_color="#F1FAFF",
                corner_radius=20
            )
            frame_totales.pack(fill="both", padx=40, pady=15)

            # ===== SUBTÍTULO =====
            subtitulo = ctk.CTkLabel(
                frame_totales,
                text="Resumen del inventario",
                font=ctk.CTkFont(size=22, weight="bold"),
                text_color="#145A8D"
            )
            subtitulo.pack(pady=15)

            # Tarjetas 1 a 3 (Inversión, Venta, Total de productos)
            for texto in [
                f"💰 Inversión Total\n\n${contar[0][0]} MXN",
                f"📈 Venta Total Estimada\n\n${contar[0][1]} MXN",
                f"📦 Total de productos registrados\n\n{round(contar[0][2])} artículos"
            ]:
                tarjeta = ctk.CTkFrame(frame_totales, fg_color="white", corner_radius=16)
                tarjeta.pack(fill="x", padx=25, pady=10)
                label = ctk.CTkLabel(
                    tarjeta,
                    text=texto,
                    font=ctk.CTkFont(size=20, weight="bold"),
                    text_color="#1B6CA8",
                    justify="left",
                    anchor="w"
                )
                label.pack(padx=20, pady=15, fill="x")

            # ==============================
            #        TARJETA 4 CON SCROLL
            # ==============================
            agotados = controller.inventario.consultar_agotado() or []
            res = f"⚠️ Productos cerca de agotarse\n\n"
            for i in agotados:
                res += f"• {i[0]} — {i[1]} unidades\n"

            tarjeta4 = ctk.CTkFrame(frame_totales, fg_color="white", corner_radius=16)
            tarjeta4.pack(fill="both", padx=25, pady=10, expand=True)

            # Usamos CTkScrollableFrame
            scroll_frame = ctk.CTkScrollableFrame(tarjeta4, fg_color="white")
            scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

            ag_label = ctk.CTkLabel(
                scroll_frame,
                text=res if res != "" else "Todos los productos tienen stock suficiente.",
                font=ctk.CTkFont(size=20, weight="bold"),
                text_color="#1B6CA8",
                justify="left",
                anchor="w",
                wraplength=600  # Ajusta según quieras que el texto haga wrap
            )
            ag_label.pack(fill="both", expand=True, pady=5)

        else:
            ctk.CTkLabel(
                ventana, 
                text="No hay productos registrados.",
                font=ctk.CTkFont(size=18, weight="bold"),
                text_color="#FF4B4B"
            ).pack(pady=20)
            # columnas = ("ID", "Nombre", "Telefono", "Direccion")

            # # Frame contenedor para Treeview y Scrollbar
            # tree_frame = ctk.CTkFrame(ventana, fg_color="transparent")
            # tree_frame.pack(fill=BOTH, expand=True, padx=20, pady=(0, 20))

            # proveedores_tree = ttk.Treeview(
            #     tree_frame,
            #     columns=columnas,
            #     show="headings",
            #     height=12
            # )

            # # Scrollbar
            # scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=proveedores_tree.yview)
            # proveedores_tree.configure(yscroll=scrollbar.set)
            # scrollbar.pack(side="right", fill="y")
            # proveedores_tree.pack(side="left", fill=BOTH, expand=True)

            # # Estilos
            # style = ttk.Style()
            # style.theme_use("default")
            # style.configure(
            #     "Treeview",
            #     background="#F0F0F0",
            #     foreground="black",
            #     rowheight=28,
            #     fieldbackground="#F0F0F0"
            # )
            # style.configure(
            #     "Treeview.Heading",
            #     background="#D1D5DB",
            #     foreground="black",
            #     font=("Arial", 12, "bold")
            # )

            # for col in columnas:
            #     proveedores_tree.heading(col, text=col)
            #     proveedores_tree.column(col, width=150, anchor="center")

            # # Insertar datos
            # for row in cursor:
            #     proveedores_tree.insert("", END, values=row)

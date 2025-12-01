from tkinter import messagebox
from model import operaciones
from view import interfaz

#Control App o Controller
class funciones:
    @staticmethod
    def operacion(signo,numero1,numero2):
        if signo=="+":
            ope=numero1+numero2
            tipo_ope="Suma"
        elif signo=="-":
            ope=numero1-numero2
            tipo_ope="Resta"
        elif signo=="X":
            ope=numero1*numero2
            tipo_ope="Multiplicacion"
        elif signo=="/":
            ope=numero1/numero2
            tipo_ope="Division"
        resultado=messagebox.askquestion(message=f"{numero1}{signo}{numero2} = {ope}\n\n¿Deseas guardar en la base de datos?",icon="question")
        if resultado=="yes":
            return operaciones.operaciones.insertar(numero1,numero2,signo,ope)
            
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta==True:
            messagebox.showinfo(message="Accion realizada con exito")
        else:
            messagebox.showinfo(message="ERROR")
from view import view1
from tkinter import *

class App:
    def __init__(self,ventana):
        view=view1.view(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()

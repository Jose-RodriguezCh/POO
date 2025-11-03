from model import usuario
from model import nota
import os
import getpass

class APP:
    def __init__(self):
        self.main()

    def borrarPantalla():
        os.system("cls")

    def esperarTecla():
        input(f"\n\t\tOprima une tecla para continuar... ")

    def registroUsuario():
        APP.borrarPantalla()
        print("\n \t ..:: Registro en el Sistema ::..")
        nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
        apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
        email=input("\t Ingresa tu email: ").lower().strip()
        password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
        #Agregar codigo
        resultado=usuario.usuarios.registrar(nombre,apellidos,email,password)
        if resultado:
            print(f"\n\t{nombre} {apellidos}, se registro correctamente, con el email {email}")
        else:
            print(f"\n\t...Por favor intentelo denuevo, no fue posible registrar al usuario")

    def loginUsuario():
        APP.borrarPantalla()
        print("\n \t ..:: Inicio de Sesión ::.. ")     
        email=input("\t Ingresa tu E-mail: ").lower().strip()
        password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
        #Agregar codigo 
        registro=usuario.usuarios.iniciar_sesion(email,password)
        if registro:
            APP.menu_notas(registro[0],registro[1],registro[2])
        else:
            print(f"\n\tE-mail y/o contraseña incorrectas, vuelva a intentarlo...")

    #Notas
    def crearNota(usuario_id):
        APP.borrarPantalla()
        print(f"\n \t .:: Crear Nota ::. ")
        titulo=input("\tTitulo: ")
        descripcion=input("\tDescripción: ")
        #Agregar codigo
        respuesta=nota.notas.crear(usuario_id,titulo,descripcion)
        if respuesta:
            print(f"\n\tSe creo la nota {titulo} exitosamente")
        else:
            print(f"\n\tNo fue posible crear la nota en este momento, vuelva a intentar ...")
    
    def imprimir_notas(lista_notas):
        print("\n\tMostrar las notas")
        print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
        print(f"-"*50)
        for i in lista_notas:
            print(f"{i[0]:<10}{i[2]:<15}{i[3]:<15}{i[4]}")  
        print(f"-"*50)

    def mostrarNota(usuario_id):
        APP.borrarPantalla()
        #Agregar codigo  
        lista_notas=nota.notas.mostrar(usuario_id)
        if len(lista_notas)>0:
            APP.imprimir_notas(lista_notas)
        else:
            print("\n\tNo existen notas de acuerdo a ese usuario")

    def cambiarNota(nombre,apellidos,usuario_id):
        APP.borrarPantalla()
        print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
        lista_notas=nota.notas.mostrar(usuario_id)
        if len(lista_notas)>0:
            APP.imprimir_notas(lista_notas)
            op=True
            while op:
                cambio=input("¿Deseas cambiar alguna lista? (Si/No): ").upper().strip()
                if cambio=="SI":
                    id = input("\t \t ID de la nota a actualizar: ")
                    res=False
                    for i in lista_notas:
                        if str(i[0])==id:
                            res=True
                    if res:
                        titulo = input("\t Nuevo título: ")
                        descripcion = input("\t Nueva descripción: ")
                        #Agregar codigo
                        respuesta=nota.notas.cambiar(id,titulo,descripcion)
                        if respuesta:
                            print(f"\n\tSe actualizo la nota {titulo} exitosamente")
                        else:
                            print(f"\n\tNo fue posible actualizar la nota en este momento, vuelva a intentar ...")  
                    else:
                        print(f"\n\tNo hay notas con el id {id} en el sistema, vuelva a intentarlo...")
                    op=False
                elif cambio=="NO":
                    op=False
                else:
                    print("No se selecciono una opcion valida, volver a intentarlo")
        else:
            print("\n\tNo existen notas de acuerdo a ese usuario")

    def eliminarNota(nombre,apellidos,usuario_id):
        APP.borrarPantalla()
        lista_notas=nota.notas.mostrar(usuario_id)
        if len(lista_notas)>0:
            APP.imprimir_notas(lista_notas)
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            op=True
            while op:
                res=input("¿Deseas borrar alguna nota? (Si/No)").upper().strip()
                if res=="SI":
                    id = input("\t \t ID de la nota a eliminar: ")
                    #Agregar codigo
                    respuesta=nota.notas.borrar(id)
                    if respuesta:
                        print(f"Se borro la nota {id} exitosamente")
                    elif respuesta==False:
                        print(f"No fue posible borrar la nota en este momento, vuelva a intentar ...")
                    op=False
                elif res=="NO":
                    op=False
                else:
                    print("No se selecciono una opcion valida")
        else:
            print("\n\tNo existen notas de acuerdo a ese usuario")

    def menu_notas(usuario_id,nombre,apellidos):
        while True:
            APP.borrarPantalla()
            print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
            print("\n \t .::  Menu Notas ::. \n\t1.- Crear \n\t2.- Mostrar \n\t3.- Cambiar \n\t4.- Eliminar \n\t5.- Salir """)
            opcion = input("\t\t Elige una opción: ").upper().strip()

            if opcion == '1' or opcion=="CREAR":
                APP.crearNota(usuario_id)
                APP.esperarTecla()    
            elif opcion == '2' or opcion=="MOSTRAR":
                APP.mostrarNota(usuario_id)
                APP.esperarTecla()
            elif opcion == '3' or opcion=="CAMBIAR":
                APP.cambiarNota(nombre,apellidos,usuario_id)
                APP.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                APP.eliminarNota(nombre,apellidos,usuario_id)
                APP.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                APP.esperarTecla()

    def main(self):
        opcion=True
        while opcion:
            APP.borrarPantalla()
            print("\n \t.:: Sistema de Gestión de Notas ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
            opcion=input("\t\t Elige una opción: ").upper().strip() 

            if opcion=="1" or opcion=="REGISTRO":
                APP.registroUsuario()
                APP.esperarTecla()
            elif opcion=="2" or opcion=="LOGIN": 
                APP.loginUsuario()
                APP.esperarTecla()  
            elif opcion=="3" or opcion=="SALIR": 
                print("Termino la Ejecución del Sistema")
                opcion=False
                APP.esperarTecla()  
            else:
                print("Opcion no valida")
                APP.esperarTecla() 

if __name__=="__main__":
    app=APP()



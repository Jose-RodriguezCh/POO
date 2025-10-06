import os
os.system("cls")

class Alumno:
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula
    
    def inscribirse(self):
        pass
    def estudiar(self):
        pass

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_matricula(self):
        return self.__matricula


class Profesor:
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor
    
    def impartir(self):
        pass
    def evaluar(self):
        pass

    def get_nombre(self):
        return self.__nombre
    
    def get_experiencia(self):
        return self.__experiencia
    
    def get_num_profesor(self):
        return self.__num_profesor
    

class Curso:
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos
    
    def asignar(self):
        pass

    def get_nombre(self):
        return self.__nombre
    
    def get_codigo(self):
        return self.__codigo
    
    def get_creditos(self):
        return self.__creditos

alumno1=Alumno("Luis","18","12345678")
alumno2=Alumno("Juan","19","87654321")
print(f"{alumno1.get_nombre()}\n{alumno1.get_edad()}\n{alumno1.get_matricula()}\n")
print(f"{alumno2.get_nombre()}\n{alumno2.get_edad()}\n{alumno2.get_matricula()}\n")

profesor1=Profesor("Eugenio","5 años","1234")
profesor2=Profesor("Francisco","10 años","0111")
print(f"{profesor1.get_nombre()}\n{profesor1.get_experiencia()}\n{profesor1.get_num_profesor()}\n")
print(f"{profesor2.get_nombre()}\n{profesor2.get_experiencia()}\n{profesor2.get_num_profesor()}\n")

curso1=Curso("Ingles","12345","100")
curso2=Curso("Algebra","54321","80")
print(f"{curso1.get_nombre()}\n{curso1.get_codigo()}\n{curso1.get_creditos()}\n")
print(f"{curso2.get_nombre()}\n{curso2.get_codigo()}\n{curso2.get_creditos()}\n")

#Asociacion 2
#alumno-curso: cursa
#profesor-alumno: imparte
#Multiplicidad
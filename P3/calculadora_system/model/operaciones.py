from conexionBD import conexion,cursor

class operaciones:
    @staticmethod
    def insertar(numero1,numero2,signo,resultado):
        try:
            sql="INSERT INTO operaciones VALUES (null,NOW(),%s,%s,%s,%s)"
            val=(numero1,numero2,signo,resultado)
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM operaciones")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(numero1,numero2,signo,resultado,id):
        try:
            cursor.execute("UPDATE operaciones SET fecha=NOW(),numero1=%s,numero2=%s,signo=%s,resultado=%s WHERE id=%s",(numero1,numero2,signo,resultado,id))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            res=[]
            cursor.execute("SELECT * FROM operaciones WHERE id=%s",(id,))
            res=cursor.fetchall()
            if len(res)>0:
                cursor.execute("DELETE FROM operaciones WHERE id=%s",(id,))
                conexion.commit()
                return True
            else:
                print(f"No se encontro una nota con el id {id}")
        except:
            return False
    
    @staticmethod
    def consultar_id(id):
        try:
            cursor.execute("SELECT * FROM operaciones where id=%s",(id,))
            return cursor.fetchone()
        except:
            return []
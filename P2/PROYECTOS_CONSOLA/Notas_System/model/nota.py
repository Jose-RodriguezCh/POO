from conexionBD import *

class notas:
    def crear(usuario_id,titulo,descripcion):
        try:
            sql="INSERT INTO notas (usuario_id,titulo,descripcion,fecha) VALUES (%s,%s,%s,NOW())"
            val=(usuario_id,titulo,descripcion)
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False

    def mostrar(usuario_id):
        try:
            sql="SELECT * FROM notas WHERE usuario_id=%s"
            val=(usuario_id,)
            cursor.execute(sql,val)
            return cursor.fetchall()
        except:
            return []
        
    def cambiar(id,titulo,descripcion):
        try:
            cursor.execute("UPDATE notas SET titulo=%s,descripcion=%s,fecha=NOW() WHERE id=%s",(titulo,descripcion,id))
            conexion.commit()
            return True
        except:
            return False

    def borrar(id):
        try:
            res=[]
            cursor.execute("SELECT * FROM notas WHERE id=%s",(id,))
            res=cursor.fetchall()
            if len(res)>0:
                cursor.execute("DELETE FROM notas WHERE id=%s",(id,))
                conexion.commit()
                return True
            else:
                print(f"No se encontro una nota con el id {id}")
        except:
            return False
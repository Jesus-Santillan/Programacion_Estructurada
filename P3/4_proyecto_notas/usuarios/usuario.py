from conexionBD import *
import datetime 

def registrar(nombre,apellido,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        sql="insert into usuarios (nombre,apellidos,email,password,fecha) values(%s,%s,%s,%s,%s)"
        val=(nombre,apellido,email,contrasena,fecha)
        cursor.execute(sql,val) 
        conexion.commit()   
        return True
    except:
        return False
def iniciar_secion(email,contraseña):
    try:
        sql="select * from usuarios where email=%s and password=%s"
        val=(email,contraseña)
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None
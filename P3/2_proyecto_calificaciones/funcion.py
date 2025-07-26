import os
import mysql.connector
from mysql.connector import Error 

def PausaBorra(tpausa):
    if(tpausa=='p'):
        os.system("pause")
    os.system("cls")
    
def conexion():
    try:
        conn = mysql.connector.connect(
            user='root', password='2373203', host='127.0.0.1', database='bd_calificaciones'
        )  
    except Error:
        print("Algo no se pudo completar para obtener los datos del sistema")
        print("Por favor contactar con un administrador ") 
        PausaBorra('p')
        conn=None
    return conn
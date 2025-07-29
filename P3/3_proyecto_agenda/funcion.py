import os
import mysql.connector
from mysql.connector import Error 

def pausa_borra(tpausa):
    if(tpausa=='p'):
        os.system("pause")
    os.system("cls")
    
def conexion():
    try:
        conn = mysql.connector.connect(
            user='root', password='2373203', host='127.0.0.1', database='bd_agenda'
        )  
    except Error:
        print("Algo no se pudo completar para obtener los datos del sistema")
        print("Por favor contactar con un administrador ") 
        pausa_borra('p')
        conn=None
    return conn
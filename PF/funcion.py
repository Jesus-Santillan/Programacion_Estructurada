import os
import re
import mysql.connector
from mysql.connector import Error 
def pausa_borra(tpausa):
    if(tpausa=='p'):
        os.system("pause")
    os.system("cls")
    
def conexion():
    try:
        conn = mysql.connector.connect(user='root', password='2373203', host='127.0.0.1', database='bd_libreria')
        resultado=f"\n\t\t\t\t\t     {'\033[0;92m'}{'\033[4;92m'}✅ Conexion a la base de datos realizada ✅ {'\033[0;0m'}"
    except Error as e:
        print(e)
        print("Algo no se pudo completar para obtener los datos del sistema")
        print("Por favor contactar con un administrador ") 
        pausa_borra('p')
        resultado=f"\n\t\t\t\t\t     {'\033[4;93m'}{'\033[0;93m'}⚠ Ocurrio algo inprevisto en la conexion a la DB... ⚠ {'\033[0;0m'}"
        conn=None
    return resultado,conn

def limpiar_n(nombre):
    caracteres_invalidos_windows = r'[<>:"/\\|?*]'
    caracteres_invalidos_linux = r'/'
    caracteres_invalidos = f'{caracteres_invalidos_windows}|{caracteres_invalidos_linux}'
    nombre_limpio = re.sub(caracteres_invalidos, '_', nombre)
    if os.name == 'nt': 
        nombres_reservados = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 
                              'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 
                              'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
        if nombre_limpio.upper() in nombres_reservados:
            nombre_limpio = '_' + nombre_limpio
    
    return nombre_limpio
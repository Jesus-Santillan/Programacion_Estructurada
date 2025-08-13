import sys
import os
from funcion import pausa_borra
cb="\033[97m"
os.system("color")
os.system("cls")

#Funcion para abrir otros archivos 
def abrir_archivo(file_path):
    try:
        os.system(f'python {file_path}')
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")#Como llego aquí :O
        pausa_borra('p')

cond=True
while cond==True :
    print(f"{'\033[3;96m'}   \t\t\t",f"".center(25,'-'),f"{cb} 💻 Sistema de administracion 📚 {'\033[96m'}",f"".center(25,'-'),f"\t\t\t   ")
    print(f"\n{cb}")
    print(f"\t\t\t\t\t  {'\033[93m'}‣ {cb}1)  Configuracion del sistema \n")
    print(f"\t\t\t\t\t  {'\033[94m'}‣ {cb}2)  Gestionar datos {cb}({'\033[36m'}manejar sistema{cb}) \n")
    print(f"\t\t\t\t\t  {'\033[92m'}‣ {cb}3)  Extra \n")
    print(f"\t\t\t\t\t  {'\033[0;31m'}‣ {cb}4)  Salir \n")
    print(f"{'\033[0;0m'}")
    try:
        opc_materia=int(input(f"\t\t\t\t\t {'\033[100m'}{'\033[37m'} Ingresa la opción a la que quieras ingresar (numero) ‣ "))
        print(f"{'\033[0;0m'}")
        pausa_borra('b')
        match opc_materia:
            case 1:
                pausa_borra('b')
                print(f"   \t\t",f"".center(25,'-'),"⁙",f" Configuracion del sistema ".center(23,' '),"⁙",f"".center(25,'-'),f"\t\t\t   ")
                abrir_archivo("proyecto_u2_libreria\conf_sistema.py")
            case 2:
                print(f"   \t\t",f"".center(25,'-'),"⁙",f" Gestionar datos ".center(23,' '),"⁙",f"".center(25,'-'),f"\t\t\t   ")
                print("\n")
                abrir_archivo("Proyecto_u2_libreria\conf_datos.py")
            case 3:
                pausa_borra('b')
                print(" ⁖ Extra ⁖ ")
                print("Santillan Fuentes Jesus Emilio")
                print("<nombre 2>")
                print("2-C TI PROG UTD")
            case 4:
                print(f"Muchas gracias ;> ....")
                sys.exit()
            case _:
                pausa_borra('b')
                print(f"‣ Porfavor ingresa opciones validas, opcion tecleada: {opc_materia}. Intentalo otra vez")                
    except ValueError:
        print(f"{'\033[0;0m'}")
        pausa_borra('b')
        print("‣ Ingresa números para seleccionar una opción. porfavor Intentalo otra vez")
    except KeyboardInterrupt:
        print(f"{'\033[0;0m'}")
        pausa_borra('b')
        print("No ingreses este tipo de cosas...") 
    pausa_borra('p')
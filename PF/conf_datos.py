from control_datos import *
from sis_ingreso import iniciar_sesion
from funcion import pausa_borra,conexion

(us,p,ingreso)=iniciar_sesion()
pausa_borra('b')
print(ingreso)
if ingreso==f"\n{'\033[0;92m'}{'\033[4;92m'}✅ Inicio de secion ADMIN exitoso ✅ {'\033[0;0m'}" or ingreso==f"\n{'\033[0;92m'}{'\033[4;92m'}✅ Inicio de secion exitoso ✅ {'\033[0;0m'}":
    pausa_borra('p')
    opc_sec=-1
    opcion_n=0
    (respuesta,temp)=conexion()
    if respuesta!=f"\n\t\t\t\t\t     {'\033[0;92m'}{'\033[4;92m'}✅ Conexion a la base de datos realizada ✅ {'\033[0;0m'}":
        print("\n"+respuesta+"\n")
        pausa_borra('p')
        
    while(opc_sec!=opcion_n):
        archivo=open("proyecto_u2_libreria\\datos_conFS.txt")
        opciones=archivo.readlines()
        archivo.close()
        opcion_n=menu(opciones)
        try:
            opc_sec=int(input(f"\t\t\t\t\t\t\tIngresa a la seccion que quieres utilizar ‣ "))
        except ValueError:
            pausa_borra('b')
            print("Ingresa caracteres validos ....")
            pausa_borra('p')
            continue
        except KeyboardInterrupt:
            pausa_borra('b')
            print("No ingreses este tipo de cosas...") 
            pausa_borra('p')
            
        if opc_sec>0 and opc_sec<opcion_n:
            pausa_borra('b')
            main_seccion(str(opciones[opcion_n+opc_sec-1]).strip(),str(opciones[opc_sec-1]).strip(),opc_sec,opcion_n,us,p)          
        elif opc_sec==opcion_n:
            pausa_borra('b')
            print("opcion salir activada ....")
        else:
            pausa_borra('b')
            print(f"Ingresa opciones validas del rango del 1 al {opcion_n}")
            pausa_borra('p')
    print("\n")
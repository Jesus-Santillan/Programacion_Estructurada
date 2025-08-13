from control_secc import *
from sis_ingreso import *
from funcion import pausa_borra
(us,p,ingreso)=iniciar_sesion()
pausa_borra('b')
print(f"{ingreso}")
print("")
if ingreso==f"\n{'\033[0;92m'}{'\033[4;92m'}✅ Inicio de secion ADMIN exitoso ✅ {'\033[0;0m'}" and p=="si":
    pausa_borra('p')
    opc_sec=0
    opcion_n=0
    (respuesta,temp)=conexion()
    print("\n"+respuesta+"\n")
    pausa_borra('p')
    while(opc_sec!=opcion_n+3):
        archivo=open("proyecto_u2_libreria\\datos_conFS.txt")
        opciones=archivo.readlines()
        archivo.close()
        opcion_n=menu(opciones)
        try:
            opc_sec=int(input(f"\t\t\t\t\t\t{'\033[0;37m'}Ingresa a la seccion que quieres utilizar {'\033[1;30m'}‣{'\033[0m'} "))
        except ValueError:
            pausa_borra('b')
            print("Ingresa caracteres validos (numeros como 1,2... )....")
            pausa_borra('p')
            continue
        except KeyboardInterrupt:
            pausa_borra('b')
            print("No ingreses este tipo de cosas...") 
            pausa_borra('p')
            
        if opc_sec>0 and opc_sec<opcion_n:
            pausa_borra('b')
            main_seccion(str(opciones[opcion_n+opc_sec-1]).strip(),str(opciones[opc_sec-1]).strip(),opc_sec,opcion_n)          
        elif opc_sec==opcion_n:
            pausa_borra('b')
            print(agregar_secc(opcion_n))
            pausa_borra('p')
        elif opc_sec==opcion_n+1: 
            pausa_borra('b') 
            print(eliminar_Tdsecc())
            pausa_borra('p')
        elif opc_sec==opcion_n+2:
            pausa_borra('b') 
            print(registrar(us))
            pausa_borra('p')
        elif opc_sec==opcion_n+3:
            pausa_borra('b')
            print("opcion salir activada ....")
        else:
            pausa_borra('b')
            print(f"Ingresa opciones validas del rango del 1 al {opcion_n+3}")
            pausa_borra('p')    
    print("\n")
elif ingreso==f"\n{'\033[0;92m'}{'\033[4;92m'}✅ Inicio de secion exitoso ✅ {'\033[0;0m'}" and p=="no": 
    print(f"🛑 {'\033[0;91m'}<{'\033[0;97m'} Sin embargo, el usuario no tiene los permisos necesarios para acceder a la seccion solicitada ❗{'\033[0;91m'}>{'\033[0;0m'}")
    print("    Contacte con un administrador...")
    print("")
    pausa_borra('p')    
    

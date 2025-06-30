
import os

'''
lista={
    ["Ruben",10.0,8.9,9.2],
    ["Andres",10.0,10.0,10.0],
    ["Maria",10.0,10.0,10.0]        
}
'''
def PausaBorra(tpausa):
    if(tpausa=='p'):
        os.system("pause")
    os.system("cls")
    
def menu_principal():
    print("🐱‍🐉 ---- Calificaciones ---- 🐱‍👓")
    print("")
    print(f"👉  1️⃣  Agregar")
    print(f"👉  2️⃣  Mostrar")
    print(f"👉  3️⃣  Calcular")
    print(f"👉  4️⃣  Salir")   
    print("")
    opc_materia=int(input(f"🗿 Ingresa la opción a la que quieras ingresar (numero) ‣ "))
    print("")
    PausaBorra('n') 
    return opc_materia
    
def agregar_calificaciones(l_datos):
    temp_ld=[]
    temp_ld=l_datos
    print(" \U0001F4BE Agregar calificaciones")
    nombre=input(f" \U0001F4DD Ingresa tu nombre completo por favor ‣ ").strip().lower()
    print("")
    verif=True
    while(verif==True):
        try:
            calif_1=float(input(f" \U0001F4DD Ingresa el valor numerico de la primer calificacion ‣ "))
            calif_2=float(input(f" \U0001F4DD Ingresa el valor numerico de la segunda calificacion ‣ "))
            calif_3=float(input(f" \U0001F4DD Ingresa el valor numerico de la tercera calificacion ‣ "))
            if(calif_1>=0 and calif_1<=10 and calif_2>=0 and calif_2<=10 and calif_3>=0 and calif_3<=10):
                temp_ld[0].append(nombre)
                temp_ld[1].append(calif_1)
                temp_ld[2].append(calif_2)
                temp_ld[3].append(calif_3)
                verif=False               
                print(" \u2705 <La operacion se realizo con exito> \u2705")
                print("")
            else:
                PausaBorra('n') 
                print("😑 Porfavor ingresa un numero entre el 1 al 10...") 
                print(" \u26A0 <No fue posible capturar los valores> \u26A0 ")
                print("♠ Ingresa nuevamente las calificaciones ♦")
                PausaBorra('p')   
        except ValueError:
            PausaBorra('n') 
            print("😑 Ingresa solo valores numericos para las calificaciones")
            print("\u26A0 <No fue posible capturar los valores> \u26A0 ")
            print("♥ Ingresa nuevamente las calificaciones ♣")
            PausaBorra('p')
    return temp_ld
           
def mostrar_calificaciones(l_datos):
    temp_ld=[[],[],[],[]]
    temp_ld=l_datos
    print("")
    print(" \U0001F4DD Mostrar calificaciones \U0001F50D") 
    print("")
    print(f"{'Nombre':<15}{'Calif 1':<10}{'Calif 2':<10}{'Calif 3':<10}{'Calif final':<10}")  
    print("_"*60) 
    cont_p=0
    for i in range(0,len(temp_ld[0])):
        print(f"{temp_ld[0][i]:<15}{temp_ld[1][i]:<10}{temp_ld[2][i]:<10}{temp_ld[3][i]:<10}{(temp_ld[1][i]+temp_ld[2][i]+temp_ld[3][i])/3}") 
        print("_"*60)
        cont_p=cont_p+(temp_ld[1][i]+temp_ld[2][i]+temp_ld[3][i])/3
    print("")      
    print("numero de alumnos: ",str(len(temp_ld)-1))
    print("El promedio total de los alumnos es de: ",str((cont_p)/len(temp_ld[0])))
        
def calcular_promedios(l_datos):
    temp_ld=[[],[],[],[]]
    temp_ld=l_datos
    print("")
    print(" \U0001F4DD Promedio de calificaciones \U0001F50D") 
    print("")
    print(f"{'Nombre':<15}{'promedio':<10}")  
    print("_"*40) 
    cont_p=0
    for i in range(0,len(temp_ld[0])):
        print(f"{temp_ld[0][i]:<15}{(temp_ld[1][i]+temp_ld[2][i]+temp_ld[3][i])/3}") 
        print("_"*40)
        cont_p=cont_p+(temp_ld[1][i]+temp_ld[2][i]+temp_ld[3][i])/3
    print("")      
    print("numero de alumnos: ",str(len(temp_ld)-1))
    try:
        print("El promedio total de los alumnos es de: ",str((cont_p)/len(temp_ld[0]))) 
    except ZeroDivisionError:
        print(" ⚠️ <No hay calificaciones registradas> ⚠️ ")   
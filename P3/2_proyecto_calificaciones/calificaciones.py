
from funcion import *

'''
lista={
    ["Ruben",10.0,8.9,9.2],
    ["Andres",10.0,10.0,10.0],
    ["Maria",10.0,10.0,10.0]        
}
'''
    
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
    global conn
    conn=conexion()
    return opc_materia
    
def agregar_calificaciones():
    print(" \U0001F4BE Agregar calificaciones")
    nombre_a=input(f" \U0001F4DD Ingresa tu nombre completo por favor ‣ ").strip().lower()
    print("")
    verif=True
    while(verif==True):
        try:
            calif_1=float(input(f" \U0001F4DD Ingresa el valor numerico de la primer calificacion ‣ "))
            calif_2=float(input(f" \U0001F4DD Ingresa el valor numerico de la segunda calificacion ‣ "))
            calif_3=float(input(f" \U0001F4DD Ingresa el valor numerico de la tercera calificacion ‣ "))
            if(calif_1>=0 and calif_1<=10 and calif_2>=0 and calif_2<=10 and calif_3>=0 and calif_3<=10):
                cursor = conn.cursor()
                sql =f'''INSERT INTO `calificaciones` (`nombre`, `calificacion 1`, `calificacion 2`, `calificacion 3`) VALUES ('{nombre_a}', '{calif_1}', '{calif_2}', '{calif_3}')'''
                cursor.execute(sql)
                conn.commit()   
                conn.close()
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
        except Error as e:
            PausaBorra('n') 
            print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
            print("\u26A0 <No fue posible capturar los valores> \u26A0 ")
            print("❕ Contacta con un administrador ❕")
            PausaBorra('p')
           
def mostrar_calificaciones():
    temp_ld=[]
    try:
        cursor = conn.cursor()
        sql =f'''SELECT * FROM `calificaciones`'''
        cursor.execute(sql)
        temp_ld=cursor.fetchall()
        conn.close()
    except Error as e:
        PausaBorra('n') 
        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
        print("\u26A0 <No fue posible capturar los valores> \u26A0 ")
        print("❕ Contacta con un administrador ❕")
        PausaBorra('p')   
    print("")
    print(" \U0001F4DD Mostrar calificaciones \U0001F50D") 
    print("")
    if temp_ld!=[]:
        print(f"{'Nombre':<15}{'Calif 1':<10}{'Calif 2':<10}{'Calif 3':<10}{'Calif final':<10}")  
        print("_"*60) 
        cont_p=0
        for i in range(0,len(temp_ld)):
            print(f"{temp_ld[i][0]:<15}{temp_ld[i][1]:<10}{temp_ld[i][2]:<10}{temp_ld[i][3]:<10}{(temp_ld[i][1]+temp_ld[i][2]+temp_ld[i][3])/3}") 
            print("_"*60)
            cont_p=cont_p+(temp_ld[i][1]+temp_ld[i][2]+temp_ld[i][3])/3
        print("")      
        print("numero de alumnos: ",str(len(temp_ld)))
        print("El promedio total de los alumnos es de: ",str((cont_p)/len(temp_ld)))
    else:
        PausaBorra('n')
        print(" ⚠️ <No hay calificaciones registradas> ⚠️ ") 
        PausaBorra('p')
                
def calcular_promedios():
    temp_ld=[]
    try:
        cursor = conn.cursor()
        sql =f'''SELECT * FROM `calificaciones`'''
        cursor.execute(sql)
        temp_ld=cursor.fetchall()
        conn.close()
    except Error as e:
        PausaBorra('n') 
        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
        print("\u26A0 <No fue posible capturar los valores> \u26A0 ")
        print("❕ Contacta con un administrador ❕")
        PausaBorra('p') 
    print("")
    print(" \U0001F4DD Promedio de calificaciones \U0001F50D") 
    print("")
    if temp_ld!=[]:
        print(f"{'Nombre':<15}{'Promedio':<10}")  
        print("_"*40) 
        cont_p=0
        for i in range(0,len(temp_ld)):
            print(f"{temp_ld[i][0]:<15}{(temp_ld[i][1]+temp_ld[i][2]+temp_ld[i][3])/3}") 
            print("_"*40)
            cont_p=cont_p+(temp_ld[i][1]+temp_ld[i][2]+temp_ld[i][3])/3
        print("")      
        print("numero de alumnos: ",str(len(temp_ld)))
        try:
            print("El promedio total de los alumnos es de: ",str((cont_p)/len(temp_ld)))
        except ZeroDivisionError:
            PausaBorra('n')
            print(" ⚠️ <No hay calificaciones registradas> ⚠️ ") 
            PausaBorra('p')  
    else:
        PausaBorra('n')
        print(" ⚠️ <No hay calificaciones registradas> ⚠️ ") 
        PausaBorra('p')   
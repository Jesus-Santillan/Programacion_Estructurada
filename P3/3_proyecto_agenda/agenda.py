import os
def menu():
    print(f"   \t\t",f"".center(25,'-'),"📗",f"  Sistema de gestion de agenda de contacto ".center(45,' '),"📘",f"".center(25,'-'),f"\t\t\t   ")
    print("")
    print(f"\t\t\t\t\t‣ 1️⃣  Agregar contacto \n")
    print(f"\t\t\t\t\t‣ 2️⃣  Mostrar todos los contactos \n")
    print(f"\t\t\t\t\t‣ 3️⃣  Buscar contacto por nombre \n")
    print(f"\t\t\t\t\t‣ 4️⃣  Eliminar un contacto \n")
    print(f"\t\t\t\t\t‣ 5️⃣  Eliminar todos los contactos \n")
    print(f"\t\t\t\t\t‣ 6️⃣  Modificar datos de un contacto \n")
    print(f"\t\t\t\t\t‣ 7️⃣  salir \n")
    opc=int(input(f"\t\t\t\t\t👉 Ingresa la opción a la que quieras ingresar (numero del 1-4 ) ‣ "))
    print("")
    return opc

def pausa_borra(tpausa):
    if(tpausa=='p'):
        os.system("pause")
    os.system("cls") 
pausa_borra('b') 

def agregar_contacto(agenda):
    print("")
    print(" ➕ Agregar contacto 🐔🐾 ")
    nombre=input(" 😶 Ingresa el nombre del contacto nuevo ‣ ").lower().strip()
    if nombre in agenda:
        print("El contacto espesificado ya existe...")
        pausa_borra('p') 
    else:
        tel=input(" 📱 Ingresa el numero de telefono de la persona ‣ ")
        email=input(" 📧 Ingresa el correo electronico de la persona ‣ ")
        direccion=input(" 🏡 Ingresa la direccion donde recide el contacto ‣ ")
        relacion=input(" 🗃 Ingresa la relacion que se tiene con esta persona ‣ ")
        agenda[nombre]=[tel,email,direccion,relacion]
        print("Accion realizada con exito")
    return agenda

def agregar_contacto(agenda):
    print("")
    print(" 📝 Agregar contacto 💠 ")
    nombre=input(" 😶 Ingresa el nombre del contacto ‣ ").lower().strip()
    if nombre in agenda:
        print("El contacto espesificado ya existe...")
        pausa_borra('p') 
    else:
        tel=input(" 📱 Ingresa el numero de telefono de la persona ‣ ")
        email=input(" 📧 Ingresa el correo electronico de la persona ‣ ")
        direccion=input(" 🏡 Ingresa la direccion donde recide el contacto ‣ ")
        relacion=input(" 🗃 Ingresa la relacion que se tiene con esta persona ‣ ")
        agenda[nombre]=[tel,email,direccion,relacion]
        print("Accion realizada con exito")
    return agenda

def mostrar_contacto(agenda):
    print("")
    print(" 💻 Mostrar contacto 👨‍💻📑 ")
    if len(agenda)!=0:
        print("_"*100)
        print(f"{'Nombre':<20}{'Telefono':<20}{'Email':<20}{'Direccion':<20}{'Relacion':<20}")
        print("_"*100)
        for i in agenda:
            print(f"{i:<20}{agenda[i][0]:<20}{agenda[i][1]:<20}{agenda[i][2]:<20}{agenda[i][3]:<20}") 
            print("_"*100) 
        print("")
    else:
        print("\n <No se encontro ningun contacto> \n")  
    '''
    nombres=list(agenda.keys())
    agenda=[list(agenda)]
    while(cont<len(agenda)):
        print(f"{'Nombre':<20}{'Telefono':<20}{'Email':<20}{'Relacion':<20}{'Relacion':<20}")
        print(f"{nombres[cont]:<20}{agenda[cont][0]:<20}{agenda[cont][1]:<20}{agenda[cont][2]:<20}{agenda[cont][3]:<20}")
        print("_"*60)
        cont+=1
    '''
    
def buscar_contacto(agenda):
    print("")
    print("  🔎👤 Buscar contacto  ")
    nombre=input(" 😶 Ingresa el nombre del contacto a buscar ").lower().strip()
    if not(nombre in agenda):
        print("El contacto espesificado no existe...")
        pausa_borra('p') 
    else:
        print("_"*100)
        print(f"{'Nombre':<20}{'Telefono':<20}{'Email':<20}{'Relacion':<20}{'Relacion':<20}")
        print(f"{nombre:<20}{agenda[nombre][0]:<20}{agenda[nombre][1]:<20}{agenda[nombre][2]:<20}{agenda[nombre][3]:<20}") 
        print("_"*100) 

def modificar_contacto(agenda):
    print("")
    print("  ✏ Modificar un contacto  ")
    nombre=input(" 😶 Ingresa el nombre del contacto a buscar ").lower().strip()
    print("")
    if not(nombre in agenda):
        print("El contacto espesificado no existe...")
    else:
        if len(agenda)!=0:
            print("")
            tel=input(" 📱 Ingresa el numero de telefono de la persona ‣ ")
            email=input(" 📧 Ingresa el correo electronico de la persona ‣ ")
            direccion=input(" 🏡 Ingresa la direccion donde recide el contacto ‣ ")
            relacion=input(" 🗃 Ingresa la relacion que se tiene con esta persona ‣ ")
            agenda[nombre]=[tel,email,direccion,relacion]
            print("<Accion realizada con exito>")
        else:
            print(" 🕳 No se encontro ninguna coincidencia")  
    return agenda

def eliminar_contacto(agenda):
    print("")
    print("  ✂👤 Eliminar un contacto  ")
    nombre=input(" 😶 Ingresa el nombre del contacto a buscar ").lower().strip()
    print("")
    if not(nombre in agenda):
        print("El contacto espesificado no existe...")
    else:
        if len(agenda)!=0:
            print("")
            eliminar_r=int(input(" 🔻 Estas seguro de que quieres eliminarlo... 1)si 2)no ‣ "))
            if eliminar_r==1:
                agenda.pop(nombre)
            elif eliminar_r==2:
                print("ok")
            else:
                print(" 🕳 Ingresa opciones de verdad :b")
        else:
            print(" 🕳 No se encontro ninguna coincidencia")  
    return agenda  
    
def eliminarT_contacto(agenda):
    print("")
    print("  🗑 Eliminar todos los contactos  ")
    eliminar_r=int(input(" 🔻 Estas seguro de que quieres eliminar TODOS los contactos... 1)si 2)no ‣ "))
    if eliminar_r==1:
        agenda.clear()
    elif eliminar_r==2:
        print("ok")
    else:
        print(" 🕳 Ingresa opciones de verdad :b") 
    return agenda   

def eliminarT_contacto(agenda):
    print("")
    print("  🗑 Eliminar todos los contactos  ")
    eliminar_r=int(input(" 🔻 Estas seguro de que quieres eliminar TODOS los contactos... 1)si 2)no ‣ "))
    if eliminar_r==1:
        agenda.clear()
    elif eliminar_r==2:
        print("ok")
    else:
        print(" 🕳 Ingresa opciones de verdad :b") 
    return agenda 
    
        
    
    
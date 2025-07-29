from funcion import pausa_borra,conexion,Error
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
    global conn
    conn=conexion()
    print("")
    return opc

def agregar_contacto():
    print("")
    print(" 📝 Agregar contacto 💠 ")
    nombre=input(" 😶 Ingresa el nombre del contacto ‣ ").lower().strip()
    cursor = conn.cursor()
    sql =f'''select * from agenda where nombre='{nombre}' '''
    cursor.execute(sql)
    agenda=cursor.fetchall()
    opc="1"
    if not(agenda==[] or agenda==None):
        print("El contacto espesificado ya existe...")
        opc=input("¿Deseas registrar a otro contacto con este mismo nombre? 1)Si 2)No ‣ ")
    if opc=="1":
        tel=input(" 📱 Ingresa el numero de telefono de la persona ‣ ")
        email=input(" 📧 Ingresa el correo electronico de la persona ‣ ")
        direccion=input(" 🏡 Ingresa la direccion donde recide el contacto ‣ ")
        relacion=input(" 🗃 Ingresa la relacion que se tiene con esta persona ‣ ")
        cursor = conn.cursor()
        sql2 =f'''insert into `agenda` (`nombre`, `telefono`, `email`, `direccion`, `relacion`) VALUES ('{nombre}', '{tel}', '{email}', '{direccion}', '{relacion}')'''
        cursor.execute(sql2)
        conn.commit()   
        conn.close()
        print(" \u2705 <La operacion se realizo con exito> \u2705")
    else:
        print("")
        print("La accion no fe realizada...")
        pausa_borra('p')

def mostrar_contacto():
    agenda=[]
    try:
        cursor = conn.cursor()
        sql =f'''select * from `agenda`'''
        cursor.execute(sql)
        agenda=cursor.fetchall()
        conn.close()
    except Error as e:
        pausa_borra('n') 
        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
        print("\u26A0 <No fue posible mostrar los valores> \u26A0 ")
        print("❕ Contacta con un administrador ❕")
        pausa_borra('p') 
    print("")
    print(" 💻 Mostrar contacto 👨‍💻📑 ")
    if agenda!=[]:
        print("_"*140)
        print(f"{'Nombre':<30}{'Telefono':<24}{'Email':<30}{'Direccion':<30}{'Relacion':<20}")
        print("_"*140)
        for i in range(0,len(agenda)):
            print(f"{agenda[i][1]:<30}{agenda[i][2]:<24}{agenda[i][3]:<30}{agenda[i][4]:<30}{agenda[i][5]:<20}") 
            print("_"*140) 
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
    
def buscar_contacto():
    print("")
    print("  🔎👤 Buscar contacto  ")
    nombre=input(" 😶 Ingresa el nombre del contacto a buscar ").lower().strip()
    agenda=[]
    try:
        cursor = conn.cursor()
        sql =f'''select * from agenda where nombre='{nombre}' '''
        cursor.execute(sql)
        agenda=cursor.fetchall()
        conn.close()
        if agenda==[] or agenda==None:
            pausa_borra('b')
            print("El contacto espesificado no existe...")
            pausa_borra('p')
        else:
            print("")
            print("_"*140)
            print(f"{'Nombre':<30}{'Telefono':<24}{'Email':<30}{'Direccion':<30}{'Relacion':<20}")
            print("_"*140)
            for i in range(0,len(agenda)):
                print(f"{agenda[i][1]:<30}{agenda[i][2]:<24}{agenda[i][3]:<30}{agenda[i][4]:<30}{agenda[i][5]:<20}") 
                print("_"*140) 
        print("") 
    except Error as e:
        pausa_borra('n') 
        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
        print("\u26A0 <No fue posible buscar los valores> \u26A0 ")
        print("❕ Contacta con un administrador ❕")
        pausa_borra('p')  

def modificar_contacto():
    print("")
    print("  ✏ Modificar un contacto  ")
    print("")
    cursor = conn.cursor()
    sql =f'''select * from `agenda`'''
    cursor.execute(sql)
    agenda=cursor.fetchall()
    print("")
    print(f"{'Nombre':<30}{'Telefono':<24}{'Email':<30}{'Direccion':<30}{'Relacion':<20}")
    print("_"*140)
    for i in range(0,len(agenda)):
        print(f"{agenda[i][1]:<30}{agenda[i][2]:<24}{agenda[i][3]:<30}{agenda[i][4]:<30}{agenda[i][5]:<20}") 
        print("_"*140) 
    print("")
    nombre=input(" 😶 Ingresa el nombre del contacto a buscar ").lower().strip()
    print("")
    agenda=[]
    try:
        cursor2 = conn.cursor()
        sql =f'''select * from agenda where nombre='{nombre}' '''
        cursor2.execute(sql)
        agenda=cursor2.fetchall()
    except Error as e:
        pausa_borra('n') 
        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
        print("\u26A0 <No fue posible encontrar los valores> \u26A0 ")
        print("❕ Contacta con un administrador ❕")
        pausa_borra('p') 
    if not(agenda==[] or agenda==None):
        print("")
        print(f"{'numero de contacto':<20}{'Nombre':<28}{'Telefono':<24}{'Email':<24}{'Direccion':<28}{'Relacion':<14}")
        print("_"*140) 
        for i in range(0,len(agenda)):
            print(f"{agenda[i][0]:<20}{agenda[i][1]:<28}{agenda[i][2]:<24}{agenda[i][3]:<24}{agenda[i][4]:<28}{agenda[i][5]:<14}") 
            print("_"*140)  
        print("")
        opc=input("Ingresa el numero de contacto (en la primer columna de la tabla) ‣ ")
        verif=False
        for i in range(0,len(agenda)):
            if int(opc)==agenda[i][0]:
                verif=True
                break
        if verif==True:    
            try:
                tel=input(" 📱 Ingresa el numero de telefono de la persona ‣ ")
                email=input(" 📧 Ingresa el correo electronico de la persona ‣ ")
                direccion=input(" 🏡 Ingresa la direccion donde recide el contacto ‣ ")
                relacion=input(" 🗃 Ingresa la relacion que se tiene con esta persona ‣ ")
                cursor3 = conn.cursor()
                sql ='''update `agenda`  set nombre=%s, telefono=%s,email=%s, direccion=%s, relacion=%s where id_contacto=%s'''
                valores=(nombre,tel,email,direccion,relacion,opc)
                cursor3.execute(sql,valores)
                conn.commit()   
                conn.close()
                print(" \u2705 <La operacion se realizo con exito> \u2705")
            except Error as e:
                pausa_borra('n') 
                print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
                print("\u26A0 <No fue posible eliminar los valores> \u26A0 ")
                print("❕ Contacta con un administrador ❕")
        else:
            pausa_borra('n') 
            print(f" no existe el numero de contacto: {opc}")
            print("\u26A0 <No fue posible eliminar los valores> \u26A0 ")
    else:
        print("")
        print("La accion no fe realizada...")
        print("El contacto no existe")
        pausa_borra('p') 

def eliminar_contacto():
    print("")
    print("  ✂👤 Eliminar un contacto  ")
    nombre=input(" 😶 Ingresa el nombre del contacto a buscar ").lower().strip()
    print("")
    agenda=[]
    try:
        cursor = conn.cursor()
        sql =f'''select * from agenda where nombre='{nombre}' '''
        cursor.execute(sql)
        agenda=cursor.fetchall()
        print("")
        print(f"{'numero de contacto':<20}{'Nombre':<28}{'Telefono':<24}{'Email':<24}{'Direccion':<28}{'Relacion':<14}")
        for i in range(0,len(agenda)):
            print(f"{agenda[i][0]:<20}{agenda[i][1]:<28}{agenda[i][2]:<24}{agenda[i][3]:<24}{agenda[i][4]:<28}{agenda[i][5]:<14}") 
            print("_"*140)  
        print("")
    except Error as e:
        pausa_borra('n') 
        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
        print("\u26A0 <No fue posible encontrar los valores> \u26A0 ")
        print("❕ Contacta con un administrador ❕")
        pausa_borra('p') 
    if agenda==[]:
        print("El contacto espesificado no existe...")
    else:
        if len(agenda)!=0:
            print("")
            eliminar_r=input(" 🔻 Estas seguro de que quieres eliminarlo... 1)si 2)no ‣ ")
            if eliminar_r=="1":
                print("")
                opc=input("Ingresa el numero de contacto (en la primer columna de la tabla) ‣ ")
                try:
                    sql2 =''' delete from agenda where id_contacto = %s '''
                    valor=(int(opc),)
                    cursor.execute(sql2,valor)  
                    conn.commit() 
                    print(" \u2705 <La operacion se realizo con exito> \u2705")
                except Error as e:
                    pausa_borra('n') 
                    print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
                    print("\u26A0 <No fue posible eliminar los valores> \u26A0 ")
                    print("❕ Contacta con un administrador ❕")                      
            elif eliminar_r=="2":
                pausa_borra('n')
                print("ok")
                pausa_borra('p') 
            else:
                pausa_borra('n')
                print(" 🕳 Ingresa opciones de verdad :b")
                pausa_borra('p') 
        else:
            pausa_borra('n')
            print(" 🕳 No se encontro ninguna coincidencia") 
            pausa_borra('p') 
    conn.close()
    return agenda  
      

def eliminarT_contacto():
    print("")
    print("  🗑 Eliminar todos los contactos  ")
    eliminar_r=input(" 🔻 Estas seguro de que quieres eliminar TODOS los contactos... 1)si 2)no ‣ ")
    if eliminar_r=="1":
        try:
            cursor = conn.cursor()
            sql =f'''truncate table agenda'''
            cursor.execute(sql)
            conn.close()
            print(" \u2705 <La operacion se realizo con exito> \u2705")
        except Error as e:
            pausa_borra('n') 
            print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
            print("\u26A0 <No fue posible mostrar los valores> \u26A0 ")
            print("❕ Contacta con un administrador ❕")
            pausa_borra('p')
    elif eliminar_r=="2":
        print("ok")
    else:
        print(" 🕳 Ingresa opciones de verdad :b")  
           
        
    
    
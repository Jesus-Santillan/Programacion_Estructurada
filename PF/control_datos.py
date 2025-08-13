from funcion import conexion,pausa_borra,Error
import openpyxl
from openpyxl import Workbook
import os
pausa_borra('b')

def menu(opciones):
    pausa_borra('b')
    global respuesta,conn
    (respuesta,conn)=conexion()
    pausa_borra('b')
    print(f"{'\033[94m'}   \t\t\t","".center(25,'-'),f"{'\033[1;97m'}⁙",f"{'\x1b[4;40m'}{'\x1b[1;100m'} 📘📕 Sistema de control de datos -biblioteca municipal- 📗 {'\033[0;97m'}{'\033[1;97m'}".center(23,' '),f"⁙{'\033[94m'}",f"".center(25,'-'),f"\t\t\t   ")
    print(f"{'\033[0;0m'}")
    opcion_n=1
    for linea in opciones: 
        if(str(linea).strip()=='----'):
            break    
        print(f"\t\t\t\t\t\t\t{'\033[0;93m'}‣ {'\033[1;97m'}{opcion_n}) {linea}")
        opcion_n+=1
    else:
        if len(opciones)==2:
            print("")
            print("\t\t\t\t\t\t\t‣ <No se han agregado secciones> \n")
    print(f"\t\t\t\t\t\t\t{'\033[0;96m'}‣ {'\033[1;97m'}{opcion_n}) Salir ")
    print(f"{'\033[0;0m'}")
    return opcion_n

def mostrar_Dsecc():
    pausa_borra('b')
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    datos=[]
    try:
        cursor = conn.cursor()
        sql =f'''select * from `{secc_nomb}`'''
        cursor.execute(sql)
        datos=cursor.fetchall()
        print("")
        if datos!=[]:
            cursor = conn.cursor()
            cursor.execute(f"show columns from `{secc_nomb}`") 
            caracteristicas=cursor.fetchall()
            t_max=" "
            for crt in caracteristicas:
                if len(str(crt[0]))>len(t_max):
                    t_max=crt[0]
            t_max=len(t_max)        
            for i in range(0,len(datos)):
                temp_Tmax=" "
                for j in datos[i]:
                    if len(str(j))>len(temp_Tmax):
                        temp_Tmax=j
                temp_Tmax=len(temp_Tmax)
                for k in range(0,len(caracteristicas)):
                    print(f"\t{'\033[0;37m'}+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+")
                    print(f"\t|{'\033[1;30m'}{'\033[1;104m'}{str(caracteristicas[k][0]).center(t_max+2,' ')}{'\033[0;0m'}{'\033[0;37m'}"+
                          f"|{'\033[0;0m'}{str(datos[i][k]).center(temp_Tmax+2,' ')}{'\033[0;37m'}|")
                print(f"\t+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+{'\033[0;0m'}")
                print("")  
            resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"
            print(f"{'\033[0;0m'}")
            opc_excel=input(" Deseas visualizar los datos por medio de excel 1)Si 2)No (Numero) ‣ ").strip()
            if opc_excel=="1":
                try:
                    if os.path.isfile(f"Proyecto_u2_libreria\\Visualizador.xlsx"):
                        os.remove('proyecto_u2_libreria\Visualizador.xlsx')
                        wb=Workbook()
                        wb.save('proyecto_u2_libreria\Visualizador.xlsx')   
                    exc=openpyxl.load_workbook('proyecto_u2_libreria\Visualizador.xlsx')
                    h_exc=exc.active 
                    c=[]
                    for crt in range(0,len(caracteristicas)):
                        c.append(caracteristicas[crt][0])
                    c=(c)
                    h_exc.append(c)
                    c=[]
                    for d in range(0,len(datos)):
                        for crt in range(0,len(caracteristicas)):
                            c.append(datos[d][crt])
                        c=(c)
                        h_exc.append(c)
                        c=[]          
                    exc.save('proyecto_u2_libreria\Visualizador.xlsx')
                    if os.path.isfile(f"Proyecto_u2_libreria\\Visualizador.xlsx"):
                        os.startfile("Proyecto_u2_libreria\\Visualizador.xlsx")
                    else:
                        pausa_borra('n') 
                        print(f"🟨 No se pudo crear el archivo")
                        pausa_borra('p')     
                except FileNotFoundError:
                    pausa_borra('n') 
                    print(f"🟨 El arrchivo no fue encontrado")
                    pausa_borra('p') 
                except FileNotFoundError:
                    pausa_borra('n') 
                    print(f"🟨 No se pudo encontrar el archivo")
                    pausa_borra('p')
                except KeyError:
                    pausa_borra('n') 
                    print(f"🟨 El nombre de la hoja ha cambiado, vuelvalo a cambiar por 'ver' ")
                    pausa_borra('p')       
            caracteristicas=None    
        else:
            print("\n <No se encontro ningun dato> \n") 
    except Error as e:
        pausa_borra('n') 
        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
        print("\u26A0 <No fue posible mostrar los valores> \u26A0 ")
        print("❕ Contacta con un administrador ❕")
        pausa_borra('p')   
    conn.close() 
    pausa_borra('p') 
    return resultado 

def añadir_Dsecc():
    pausa_borra('b')
    print(f" {'\033[0;93m'}➕ <{'\033[0;97m'}Añadir registro de datos{'\033[0;93m'}> 💬 {'\033[0;0m'}\n")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    cursor = conn.cursor()
    cursor.execute(f"show columns from `{secc_nomb}`") 
    caracteristicas=cursor.fetchall()
    cmp=[]
    tcmp=""
    com=","
    sig_s=" "
    print("")
    for crt in range(1,len(caracteristicas)):
        if(crt==len(caracteristicas)-1):
            com=""
            sig_s=sig_s+"%s "
        else:
            sig_s=sig_s+"%s,"
        try:
            temp_v=input(f"Ingresa los datos del campo: {caracteristicas[crt][0]} ‣ ")
        except ValueError:
            pausa_borra('b')
            print("Ingresa caracteres validos (numeros como 1,2... )....")
            pausa_borra('p')
        except KeyboardInterrupt:
            pausa_borra('b')
            print("No ingreses este tipo de cosas...") 
            pausa_borra('p')
        try:
            temp_v=int(temp_v)
        except:
            temp_v=temp_v 
            
        if temp_v=="":
            temp_v=None
                    
        cmp.append(temp_v)
        tcmp+=f"`{caracteristicas[crt][0]}`{com}"   
        print("")
               
        if(crt==len(caracteristicas)-1):
            try:
                cursor = conn.cursor()
                sql =f'''insert into `{secc_nomb}` ({tcmp}) VALUES ({sig_s})'''
                valores=(cmp)
                pausa_borra('p')
                cursor.execute(sql,valores)
                conn.commit()   
                conn.close()
                resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"   
            except Error as e:
                mensaje="1366 (HY000): Incorrect integer value:"
                mensaje_2="1062 (23000): Duplicate entry"
                mensaje_3="1048 (23000):"
                print(str(e)[0:len(mensaje)])
                t_camp=""
                if str(e)[0:len(mensaje)]==mensaje:
                    for i in str(e)[len(mensaje)+2:len(str(e))]:
                        if i!="'":
                            t_camp+=i    
                        else:
                            break
                    pausa_borra('b')
                    print(f"Ingresa los datos del campo segun sea en : {t_camp}")
                    print(f"Motivo referido :{e}")
                    print("Intentalo otra vez")
                    pausa_borra('p')
                    break 
                elif str(e)[0:len(mensaje_2)]==mensaje_2:
                    t_camp=""
                    for i in str(e)[len(mensaje_2)+2:len(str(e))]:
                        if i!="'":
                            t_camp+=i    
                        else:
                            break
                    pausa_borra('b')
                    print(f"Este campo no admite valores dupliados ({t_camp}), por favor ingrese otro dato...")
                    print(f"Motivo referido :{e}")
                    print("Intentalo otra vez")
                    pausa_borra('p')
                    break     
                elif str(e)[0:len(mensaje_3)]==mensaje_3:
                    t_camp=""
                    for i in str(e)[len(mensaje_3)+9:len(str(e))]:
                        if i!="'":
                            t_camp+=i    
                        else:
                            break
                    pausa_borra('b')
                    print(f"El campo {t_camp} necesita ser llenado necesariamente, por favor ingrese este dato...")
                    print(f"Motivo referido :{e}")
                    print("Intentalo otra vez")
                    pausa_borra('p')
                    break 
                elif str(e)!=None:
                    pausa_borra('b')
                    print(f"Algo inesperado paso...")
                    print(f"Motivo referido :{e}")
                    print("Intentalo otra vez")
                    pausa_borra('p')
                    break
                    
    else:
        if len(caracteristicas)<=1:
            print("<No se encontraron caracteristicas>")   
    return resultado 
   
def eliminar_datos():
    print(f" {'\033[0;90m'}🗄🗑 {'\033[0;91m'}<{'\033[0;97m'}eliminar Registro{'\033[0;91m'}> 📁 {'\033[0;0m'}\n")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    if mostrar_Dsecc()!=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}":
        pausa_borra('b')
        print("")
        try:
            (_,conn)=conexion()
            cursor = conn.cursor()
            pausa_borra('b')
            print("")
            print(" ^_+ Campos existentes a seleccionar")
            cursor.execute(f"show columns from `{secc_nomb}`") 
            caracteristicas=cursor.fetchall()   
            print("")
            for c in range(0,len(caracteristicas)):
                print(f"| {c+1}) {caracteristicas[c][0]}")    
            try:
                print("")
                crt_n=int(input("🔢 Ingresa el numero de la caracteristica con la que quieres buscar (el/los) registro a eliminar ‣ ").lower().strip())
                if crt_n+1>=1 and crt_n<=len(caracteristicas):
                    datos=[]
                    print("")
                    n_elm=input(" 🔎 Ingresa el dato a buscar para eliminar ‣ ").lower().strip()
                    try:
                        n_elm=int(n_elm)
                    except ValueError:
                        n_elm=n_elm
                    if n_elm=="":
                        n_elm=None
                    cursor = conn.cursor()
                    sql =f'''select * from `{secc_nomb}` where `{caracteristicas[crt_n-1][0]}`='''
                    sql=sql+"%s"
                    cursor.execute(sql,(n_elm,))
                    datos=cursor.fetchall()
                    t_max=" "
                    for crt in caracteristicas:
                        if len(str(crt[0]))>len(t_max):
                            t_max=crt[0]
                    t_max=len(t_max)        
                    for i in range(0,len(datos)):
                        temp_Tmax=" "
                        for j in datos[i]:
                            if len(str(j))>len(temp_Tmax):
                                temp_Tmax=j
                        temp_Tmax=len(temp_Tmax)
                        for k in range(0,len(caracteristicas)):
                            print(f"\t{'\033[0;37m'}+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+")
                            print(f"\t|{'\033[1;30m'}{'\033[1;104m'}{str(caracteristicas[k][0]).center(t_max+2,' ')}{'\033[0;0m'}{'\033[0;37m'}|{'\033[0;0m'}{str(datos[i][k]).center(temp_Tmax+2,' ')}{'\033[0;37m'}|")
                    print(f"\t+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+{'\033[0;0m'}")
                    if datos==[]:
                        pausa_borra('b')
                        print("No se encontro ninguna relacion con los datos a buscar...")
                        pausa_borra('p')
                    else:
                        if len(datos)!=0:
                            print("")
                            eliminar_r=input("🔻 Estas seguro de que quieres eliminarlo... 1)si 2)no ‣ ")
                            if eliminar_r=="1":
                                if len(datos)!=1:
                                    print("")
                                    opc=input("Ingresa el numero de contacto (en la primer columna de la tabla) ‣ ")
                                    try:
                                        sql2 =f"delete from `{secc_nomb}` where `{caracteristicas[0][0]}` ="
                                        sql2=sql2+"%s"
                                        valor=(int(opc),)
                                        cursor.execute(sql2,valor)  
                                        conn.commit() 
                                        resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"
                                    except Error as e:
                                        pausa_borra('n') 
                                        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
                                        print("\u26A0 <No fue posible eliminar los valores> \u26A0 ")
                                        print("❕ Contacta con un administrador ❕")      
                                else:
                                    try:
                                        sql2=f"delete from {secc_nomb} where {caracteristicas[crt_n-1][0]} ="
                                        sql2=sql2+"%s"
                                        valor=(n_elm,)
                                        cursor.execute(sql2,valor)  
                                        conn.commit() 
                                        resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"
                                    except Error as e:
                                        pausa_borra('n') 
                                        print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
                                        print("\u26A0 <No fue posible eliminar los valores> \u26A0 ")
                                        print("❕ Contacta con un administrador ❕")                    
                            elif eliminar_r=="2":
                                pausa_borra('n')
                                print("ok...")
                                resultado=f"\n{'\033[0;91m'}{'\033[4;91m'}⭕ Accion abortada ⭕ {'\033[0;0m'}"
                                pausa_borra('p') 
                            else:
                                pausa_borra('n')
                                print(" 🕳 Ingresa opciones validas :D")
                                pausa_borra('p')
                else:
                    pausa_borra('n')
                    print(" 🔸 Ingresa opciones validas :D")
                    pausa_borra('p')                
            except ValueError:
                pausa_borra('b')
                print("Ingresa caracteres validos (numeros como 1,2... )....")
                pausa_borra('p')
            except KeyboardInterrupt:
                pausa_borra('b')
                print("No ingreses este tipo de cosas...") 
                pausa_borra('p')           
        except Error as e:
            pausa_borra('b')
            print(f"🧱 Ocurrio algo inesperado, mensajer referido: {e}")
            print("Ocurrio algo inesperado, no pudieron ser cargados los datos....")
            pausa_borra('p')    
        conn.close()     
    return resultado

def eliminar_TDatos():
    pausa_borra('b')
    print(f" {'\033[0;90m'}🗑🔰 {'\033[1;91m'}<{'\033[0;97m'}eliminar (TODOS) los Registro{'\033[1;91m'}> 📁 {'\033[0;0m'}\n")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    eliminar_r=input(" 🔻 Estas seguro de que quieres eliminar TODOS los registros (datos) de la seccion... 1)si 2)no ‣ ")
    if eliminar_r=="1":
        try:
            cursor = conn.cursor()
            sql =f'''truncate table {secc_nomb}'''
            cursor.execute(sql)
            conn.close()
            resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"
        except Error as e:
            pausa_borra('n') 
            print(f"🟡 Ocurrio algo inesperado, mensajer referido: {e}")
            print("\u26A0 <No fue posible mostrar los valores> \u26A0 ")
            print("❕ Contacta con un administrador ❕")
            pausa_borra('p')
    elif eliminar_r=="2":
        pausa_borra('b')
        print("ok")
        resultado=f"\n{'\033[0;91m'}{'\033[4;91m'}⭕ Accion abortada ⭕ {'\033[0;0m'}"
        pausa_borra('p')
    else:
        pausa_borra('b')
        print(" Por favor, seleccione una opcion valida >:v") 
        pausa_borra('p') 
    conn.close()     
    return resultado

def modificar_Dsecc():
    print(f" {'\033[0;95m'}📝✏ <{'\033[0;97m'}Modificar datos{'\033[0;95m'}>  💻 {'\033[0;0m'}")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    if mostrar_Dsecc()!=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}":
        pausa_borra('b')
        print("")
        try:
            (_,conn)=conexion()
            cursor = conn.cursor()
            pausa_borra('b')
            print("")
            print(" ^_+ Campos existentes a seleccionar")
            cursor.execute(f"show columns from `{secc_nomb}`") 
            caracteristicas=cursor.fetchall()   
            print("")
            for c in range(0,len(caracteristicas)):
                print(f"| {c+1}) {caracteristicas[c][0]}")
        except Error as e:
            pausa_borra('b')
            print(f"🧱 Ocurrio algo inesperado, mensajer referido: {e}")
            print("Ocurrio algo inesperado, no pudieron ser cargados los datos....")
            pausa_borra('p')
        except Exception as e:
            print(e)
            pausa_borra('p')
        print("")
        try:
            crt_n=int(input("🔢 Ingresa el numero de la caracteristica con la que quieres buscar (el/los) registro a modificar ‣ ").strip())
        except ValueError:
            crt_n=-100
            pausa_borra('b')
            print("Ingresa caracteres validos (numeros como 1,2... )....")
            pausa_borra('p')
        except KeyboardInterrupt:
            crt_n=-200
            pausa_borra('b')
            print("No ingreses este tipo de cosas...") 
            pausa_borra('p')    
        if crt_n+1>=1 and crt_n-1<=len(caracteristicas):
            datos=[]
            print("")
            n_m=input(" 🔎 Ingresa el dato a buscar para modificar ‣ ").lower().strip()
            try:
                n_m=int(n_m)
            except ValueError:
                n_m=n_m
            if n_m=="":
                n_m=None
            try:
                cursor = conn.cursor()
                sql =f'''select * from `{secc_nomb}` where `{caracteristicas[crt_n-1][0]}`='''
                sql=sql+"%s"
                cursor.execute(sql,(n_m,))
                datos=cursor.fetchall()
                t_max=" "
                for crt in caracteristicas:
                    if len(str(crt[0]))>len(t_max):
                        t_max=crt[0]
                t_max=len(t_max)        
                for i in range(0,len(datos)):
                    temp_Tmax=" "
                    for j in datos[i]:
                        if len(str(j))>len(temp_Tmax):
                            temp_Tmax=j
                    temp_Tmax=len(temp_Tmax)
                    for k in range(0,len(caracteristicas)):
                        print(f"\t{'\033[0;37m'}+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+")
                        print(f"\t|{'\033[1;30m'}{'\033[1;104m'}{str(caracteristicas[k][0]).center(t_max+2,' ')}{'\033[0;0m'}{'\033[0;37m'}|{'\033[0;0m'}{str(datos[i][k]).center(temp_Tmax+2,' ')}{'\033[0;37m'}|")
                    print(f"\t+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+{'\033[0;0m'}")
                    print("")
            except Error as e:
                pausa_borra('b')
                print(f"🧱 Ocurrio algo inesperado, mensajer referido: {e}")
                print("Ocurrio algo inesperado, no pudieron ser cargados los datos....")
                pausa_borra('p')
                
            if datos==[]:
                pausa_borra('b')
                print("No se encontro ninguna relacion con los datos a buscar...")
                pausa_borra('p')
            else:
                if len(datos)!=0:
                    print("")
                    if len(datos)!=1:
                        print("")
                        try:
                            opc=input("Ingresa el numero de contacto (en la primer columna de la tabla) ‣ ")
                            sql =f'''select * from `{secc_nomb}` where `{caracteristicas[0][0]}`='''
                            sql=sql+"%s"
                            cursor.execute(sql,(opc,))
                            verif=cursor.fetchall()
                        except Error as e:
                            verif==[]
                            pausa_borra('b')
                            print(f"🧱 Ocurrio algo inesperado, mensajer referido: {e}")
                            print("Ocurrio algo inesperado, no pudieron ser cargados los datos....")
                        except ValueError:
                            pausa_borra('b')
                            print("Ingresa caracteres validos (numeros como 1,2... )....")
                            pausa_borra('p')   
                        except KeyboardInterrupt:
                            pausa_borra('b')
                            print("No ingreses este tipo de cosas...") 
                            pausa_borra('p')
                        if verif!=[]:
                            cmp=[]
                            tcmp=""
                            sig_s=" "
                            print("")
                            for crt in range(1,len(caracteristicas)):
                                if(crt==len(caracteristicas)-1):
                                    sig_s="%s "
                                else:
                                    sig_s="%s,"
                                try:
                                    temp_v=input(f"Ingresa los datos del campo: {caracteristicas[crt][0]} ‣ ")
                                except ValueError:
                                    pausa_borra('b')
                                    print("Ingresa caracteres validos (numeros como 1,2... )....")
                                    pausa_borra('p')
                                except KeyboardInterrupt:
                                    pausa_borra('b')
                                    print("No ingreses este tipo de cosas...") 
                                    pausa_borra('p') 
                                try:
                                    temp_v=int(temp_v)
                                except:
                                    temp_v=temp_v 
                                    
                                if temp_v=="":
                                    temp_v=None
                                            
                                cmp.append(temp_v)
                                tcmp+=f"`{caracteristicas[crt][0]}`="+sig_s  
                                print("")
                                    
                                if(crt==len(caracteristicas)-1):
                                    try:
                                        cmp.append(opc)
                                        cursor = conn.cursor()
                                        sql =f'''update `{secc_nomb}` set {tcmp} where `{caracteristicas[0][0]}`='''
                                        sql+="%s"
                                        valores=(cmp)
                                        pausa_borra('p')
                                        cursor.execute(sql,valores)
                                        conn.commit()   
                                        conn.close()
                                        resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"   
                                    except Error as e:
                                        mensaje="1366 (HY000): Incorrect integer value:"
                                        mensaje_2="1062 (23000): Duplicate entry"
                                        mensaje_3="1048 (23000):"
                                        print(str(e)[0:len(mensaje)])
                                        t_camp=""
                                        if str(e)[0:len(mensaje)]==mensaje:
                                            for i in str(e)[len(mensaje)+2:len(str(e))]:
                                                if i!="'":
                                                    t_camp+=i    
                                                else:
                                                    break
                                            pausa_borra('b')
                                            print(f"Ingresa los datos del campo segun sea en : {t_camp}")
                                            print(f"Motivo referido :{e}")
                                            print("Intentalo otra vez")
                                            pausa_borra('p')
                                            break 
                                        elif str(e)[0:len(mensaje_2)]==mensaje_2:
                                            t_camp=""
                                            for i in str(e)[len(mensaje_2)+2:len(str(e))]:
                                                if i!="'":
                                                    t_camp+=i    
                                                else:
                                                    break
                                            pausa_borra('b')
                                            print(f"Este campo no admite valores dupliados ({t_camp}), por favor ingrese otro dato...")
                                            print(f"Motivo referido :{e}")
                                            print("Intentalo otra vez")
                                            pausa_borra('p')
                                            break     
                                        elif str(e)[0:len(mensaje_3)]==mensaje_3:
                                            t_camp=""
                                            for i in str(e)[len(mensaje_3)+9:len(str(e))]:
                                                if i!="'":
                                                    t_camp+=i    
                                                else:
                                                    break
                                            pausa_borra('b')
                                            print(f"El campo {t_camp} necesita ser llenado necesariamente, por favor ingrese este dato...")
                                            print(f"Motivo referido :{e}")
                                            print("Intentalo otra vez")
                                            pausa_borra('p')
                                            break 
                                        elif str(e)!=None:
                                            pausa_borra('b')
                                            print(f"Algo inesperado paso...")
                                            print(f"Motivo referido :{e}")
                                            print("Intentalo otra vez")
                                            pausa_borra('p')
                                            break                                                   
                            else:
                                if len(caracteristicas)<=1:
                                    print("<No se encontraron caracteristicas>")  
                        else:
                            pausa_borra('b')
                            print(f"No fue posible encontrar una coincidencia, verifique los datos")
                            pausa_borra('p')   
                    else:
                        cmp=[]
                        tcmp=""
                        sig_s=" "
                        print("")
                        for crt in range(1,len(caracteristicas)):
                            if(crt==len(caracteristicas)-1):
                                sig_s="%s "
                            else:
                                sig_s="%s,"
                            try:
                                temp_v=input(f"Ingresa los datos del campo: {caracteristicas[crt][0]} ‣ ")
                            except ValueError:
                                pausa_borra('b')
                                print("Ingresa caracteres validos (numeros como 1,2... )....")
                                pausa_borra('p')
                            except KeyboardInterrupt:
                                pausa_borra('b')
                                print("No ingreses este tipo de cosas...") 
                                pausa_borra('p') 
                            try:
                                temp_v=int(temp_v)
                            except:
                                temp_v=temp_v 
                                
                            if temp_v=="":
                                temp_v=None
                                        
                            cmp.append(temp_v)
                            tcmp+=f"`{caracteristicas[crt][0]}`="+sig_s  
                            print("")
                                
                            if(crt==len(caracteristicas)-1):
                                try:
                                    cmp.append(n_m)
                                    cursor = conn.cursor()
                                    sql =f'''update `{secc_nomb}` set {tcmp} where `{caracteristicas[crt_n-1][0]}`='''
                                    sql+="%s"
                                    valores=(cmp)
                                    print(sql)
                                    pausa_borra('p')
                                    cursor.execute(sql,valores)
                                    conn.commit()   
                                    conn.close()
                                    resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"   
                                except Error as e:
                                    mensaje="1366 (HY000): Incorrect integer value:"
                                    mensaje_2="1062 (23000): Duplicate entry"
                                    mensaje_3="1048 (23000):"
                                    print(str(e)[0:len(mensaje)])
                                    t_camp=""
                                    if str(e)[0:len(mensaje)]==mensaje:
                                        for i in str(e)[len(mensaje)+2:len(str(e))]:
                                            if i!="'":
                                                t_camp+=i    
                                            else:
                                                break
                                        pausa_borra('b')
                                        print(f"Ingresa los datos del campo segun sea en : {t_camp}")
                                        print(f"Motivo referido :{e}")
                                        print("Intentalo otra vez")
                                        pausa_borra('p')
                                        break 
                                    elif str(e)[0:len(mensaje_2)]==mensaje_2:
                                        t_camp=""
                                        for i in str(e)[len(mensaje_2)+2:len(str(e))]:
                                            if i!="'":
                                                t_camp+=i    
                                            else:
                                                break
                                        pausa_borra('b')
                                        print(f"Este campo no admite valores dupliados ({t_camp}), por favor ingrese otro dato...")
                                        print(f"Motivo referido :{e}")
                                        print("Intentalo otra vez")
                                        pausa_borra('p')
                                        break     
                                    elif str(e)[0:len(mensaje_3)]==mensaje_3:
                                        t_camp=""
                                        for i in str(e)[len(mensaje_3)+9:len(str(e))]:
                                            if i!="'":
                                                t_camp+=i    
                                            else:
                                                break
                                        pausa_borra('b')
                                        print(f"El campo {t_camp} necesita ser llenado necesariamente, por favor ingrese este dato...")
                                        print(f"Motivo referido :{e}")
                                        print("Intentalo otra vez")
                                        pausa_borra('p')
                                        break 
                                    elif str(e)!=None:
                                        pausa_borra('b')
                                        print(f"Algo inesperado paso...")
                                        print(f"Motivo referido :{e}")
                                        print("Intentalo otra vez")
                                        pausa_borra('p')
                                        break                                                   
                        else:
                            if len(caracteristicas)<=1:
                                print("<No se encontraron caracteristicas>")                                         
        else:
            pausa_borra('n')
            print(" 🔸 Ingresa opciones validas :D")
            pausa_borra('p')                              
        conn.close()     
    return resultado    

def buscar_regD():
    pausa_borra('b')
    print(f"{'\033[0;34m'} 🔍 <{'\033[0;97m'}Buscar registro(s){'\033[0;97m'}>  {'\033[0;0m'}\n")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    try:
        (_,conn)=conexion()
        cursor = conn.cursor()
        pausa_borra('b')
        print("")
        print(" ^_^ Campos existentes a seleccionar")
        cursor.execute(f"show columns from `{secc_nomb}`") 
        caracteristicas=cursor.fetchall()   
        print("")
        for c in range(0,len(caracteristicas)):
            print(f"| {c+1}) {caracteristicas[c][0]}")
    except Error as e:
        pausa_borra('b')
        print(f"🧱 Ocurrio algo inesperado, mensajer referido: {e}")
        print("Ocurrio algo inesperado, no pudieron ser cargados los datos....")
        pausa_borra('p')
    try:
        crt_n=int(input("🔢 Ingresa el numero de la caracteristica con la que quieres buscar (el/los) registro a modificar ‣ ").strip())
    except ValueError:
        crt_n=-100
        pausa_borra('b')
        print("Ingresa caracteres validos (numeros como 1,2... )....")
        pausa_borra('p')
    except KeyboardInterrupt:
        crt_n=-200
        pausa_borra('b')
        print("No ingreses este tipo de cosas...") 
        pausa_borra('p')    
    if crt_n+1>=1 and crt_n-1<=len(caracteristicas):
        datos=[]
        print("")
        n_m=input(" 🔎 Ingresa el dato a buscar para modificar ‣ ").lower().strip()
        try:
            n_m=int(n_m)
        except ValueError:
            n_m=n_m
        if n_m=="":
            n_m=None
        try:
            cursor = conn.cursor()
            sql =f'''select * from `{secc_nomb}` where `{caracteristicas[crt_n-1][0]}`='''
            sql=sql+"%s"
            cursor.execute(sql,(n_m,))
            datos=cursor.fetchall()
            t_max=" "
            for crt in caracteristicas:
                if len(str(crt[0]))>len(t_max):
                    t_max=crt[0]
            t_max=len(t_max)        
            for i in range(0,len(datos)):
                temp_Tmax=" "
                for j in datos[i]:
                    if len(str(j))>len(temp_Tmax):
                        temp_Tmax=j
                temp_Tmax=len(temp_Tmax)
                for k in range(0,len(caracteristicas)):
                    print(f"\t{'\033[0;37m'}+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+")
                    print(f"\t|{'\033[1;30m'}{'\033[1;104m'}{str(caracteristicas[k][0]).center(t_max+2,' ')}{'\033[0;0m'}{'\033[0;37m'}|{'\033[0;0m'}{str(datos[i][k]).center(temp_Tmax+2,' ')}{'\033[0;37m'}|")
                print(f"\t+{'-'*(t_max+2)}-{'-'*(temp_Tmax+2)}+{'\033[0;0m'}")
                print("")
        except Error as e:
            pausa_borra('b')
            print(f"🧱 Ocurrio algo inesperado, mensajer referido: {e}")
            print("Ocurrio algo inesperado, no pudieron ser cargados los datos....")
            pausa_borra('p')
            
        if datos==[]:
            pausa_borra('b')
            print("No se encontro ninguna relacion con los datos a buscar...")
            pausa_borra('p')
        else:
            resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"
    return resultado 
        
def main_seccion(archivo_p,nomb_secc,n_seccion,n_relleno,usuario,permiso):
    global p_archivo
    p_archivo=archivo_p
    global secc_nomb
    secc_nomb=nomb_secc
    global num_secc
    num_secc=n_seccion
    global num_r
    num_r=n_relleno
    global resultado
    resultado=""
    opc=0
    if secc_nomb!="usuarios" or permiso=="si":
        print(f"   \t\t",f"".center(25,'-'),"⁙",f" {secc_nomb} ".center(23,' '),"⁙",f"".center(25,'-'),f"\t\t\t   ")
        print("\n")
        print(f"\t\t\t\t\t{'\033[0;90m'}‣{'\033[0;0m'} 1) Mostrar datos \n")
        print(f"\t\t\t\t\t{'\033[0;93m'}‣{'\033[0;0m'} 2) Añadir un registro (registrar datos en esta seccion) \n")
        print(f"\t\t\t\t\t{'\033[0;91m'}‣{'\033[0;0m'} 3) Eliminar registro (datos) \n")
        print(f"\t\t\t\t\t{'\033[1;91m'}‣{'\033[0;0m'} 4) Eliminar TODOS los registros de la seccion \n")
        print(f"\t\t\t\t\t{'\033[0;95m'}‣{'\033[0;0m'} 5) Modificar un registro (datos del registro) \n")
        print(f"\t\t\t\t\t{'\033[0;34m'}‣{'\033[0;0m'} 6) Buscar registro(s) \n")
        print(f"\t\t\t\t\t{'\033[0;37m'}‣{'\033[0;0m'} 7) Salir \n")
        try:
            opc=int(input("\t\t\t\t\tIngresa la opcion que quieras hacer ‣ "))
        except ValueError:
            pausa_borra('b')
            print("Ingesa la opcion deseada con numeros")
            pausa_borra('p') 
        except KeyboardInterrupt:
            pausa_borra('b')
            print("Evita teclear eso -_-")
            #opcion regresar
        #Opciones de la secion
                
        match opc:
            case 1:
                print(f"{'\033[0;90m'} 📖 Mostrar DATOS de {secc_nomb} 👨‍💻📑 {'\033[0;0m'}")
                print(mostrar_Dsecc())
                pausa_borra('p')
            case 2:
                print(añadir_Dsecc())
                pausa_borra('p')
            case 3:
                print(eliminar_datos())
                pausa_borra('p')
            case 4:
                print(eliminar_TDatos())
                pausa_borra('p')
            case 5:
                print(modificar_Dsecc())
                pausa_borra('p')
            case 6:
                print(buscar_regD())
                pausa_borra('p')
            case 7:
                print()
            case _:
                pausa_borra('b')
                print("Ingesa una opcion valida para hacer algo (del 1 al 7)")
                pausa_borra('p') 
        print(f"{'\033[0;0m'}",end="")
    else:
        pausa_borra('b')
        print(f"🛑 {'\033[0;91m'}<{'\033[0;97m'}Este usuario no tiene los permisos necesarios para acceder a esta seccion ❗{'\033[0;91m'}>{'\033[0;0m'}")
        print("   Contacte con un administrador...")
        pausa_borra('p')
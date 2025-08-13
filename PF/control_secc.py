import os
from funcion import *
from shutil import rmtree
bc='\033[0m'
def menu(opciones):
    global respuesta,conn
    (respuesta,conn)=conexion()
    pausa_borra('b')
    print(f"{'\033[33m'}   \t\t\t","".center(25,'-'),f"{'\033[1;97m'}⁙",f"{'\x1b[4;40m'}{'\x1b[1;100m'} Configuracion del sistema {'\033[0;97m'}{'\033[1;97m'}".center(23,' '),f"⁙{'\033[33m'}",f"".center(25,'-'),f"\t\t\t   ")
    print(f"{bc}")
    opcion_n=1
    for linea in opciones: 
        if(str(linea).strip()=='----'):
            break    
        print(f"\t\t\t\t\t\t{'\033[1;32m'}‣ {opcion_n}{'\033[0;32m'}{'\033[1;37m'}) {'\033[0;32m'}{linea}")
        opcion_n+=1
    else:
        if len(opciones)==2:
            print("")
            print("\t\t\t\t\t\t‣ <No se han agregado secciones> \n")
    print(f"\t\t\t\t\t\t{'\033[1;33m'}‣ {opcion_n}{'\033[0;33m'}{'\033[1;37m'}){'\033[0;33m'} Agregar una seccion \n")
    print(f"\t\t\t\t\t\t{'\033[1;94m'}‣ {opcion_n+1}{'\033[0;94m'}{'\033[1;37m'}){'\033[0;94m'} Eliminar todas las secciones \n")
    print(f"\t\t\t\t\t\t{'\033[1;36m'}‣ {opcion_n+2}{'\033[0;36m'}{'\033[1;37m'}){'\033[0;36m'} Registrar usuario \n")
    print(f"\t\t\t\t\t\t{'\033[1;31m'}‣ {opcion_n+3}{'\033[0;31m'}{'\033[1;37m'}){'\033[0;31m'} Salir ")
    print(f"{'\033[0;0m'}")
    return opcion_n
def cambiar_nombre():
    pausa_borra('b') 
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    print(f" 🔄 {'\033[0;33m'}<{'\033[0;97m'}Cambiar nombre{'\033[0;33m'}> 🔣 ({'\033[0;97m'}{secc_nomb}{'\033[0;33m'}) {'\033[0;0m'}\n")
    try:
        nombre_nv=str(input("Ingresa el nuevo nombre de la seccion  ‣ "))
        temp_nomb=nombre_nv 
        nombre_nv=limpiar_n(nombre_nv) 
        if temp_nomb!=nombre_nv:
            pausa_borra('b')
            print("El nombre: "+temp_nomb+" , se cambiara a el siguiente: "+nombre_nv)
            pausa_borra('p')
    except ValueError:
        pausa_borra('b') 
        print("Ingresa caracteres validos ....")  
    except KeyboardInterrupt:
        pausa_borra('b')
        print("No ingreses este tipo de cosas...") 
        
    if os.path.isfile(f"Proyecto_u2_libreria\\secciones\\{nombre_nv}.txt"):
        os.system("cls")
        print("<El nombre espesificado ya esxiste>") 
    else:      
        try:   
            if(os.path.exists("proyecto_u2_libreria\\secciones\\.txt")==True and os.path.exists(f"proyecto_u2_libreria\\secciones\\{nombre_nv}.txt")==False):
                os.system("cls")
                print("Algo paso al momento de cambiar el nombre")
                print("NO fue posible cambiar el nombre")    
                os.rename(f"proyecto_u2_libreria\\secciones\\{nombre_nv}.txt",p_archivo)   
                pausa_borra('p') 
            else:
                cursor = conn.cursor()
                sql=f"alter table `{secc_nomb}` rename to `{nombre_nv}`"
                cursor.execute(sql) 
                conn.close()
                resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"  
                archivo=open("proyecto_u2_libreria\\datos_conFS.txt","r")
                os.rename(p_archivo,f"proyecto_u2_libreria\\secciones\\{nombre_nv}.txt") 
                datos=archivo.readlines()
                archivo.close()
                archivo=open("proyecto_u2_libreria\\datos_conFS.txt","w")
                for i in range(0,len(datos)):
                    if(i==(num_secc-1)):                
                        archivo.write(f"{nombre_nv}\n")    
                    elif(i==(num_secc+num_r)-1):
                        archivo.write(f"proyecto_u2_libreria\\secciones\\{nombre_nv}.txt\n")   
                    else:
                        archivo.write(f"{datos[i]}")
                archivo.close()                
        except OSError:
            pausa_borra('b') 
            print("No utilize caracteres especiales o invalidos")
            print("Intente un nombre con solo letras y/o numeros")
        except Error as e:
            pausa_borra('b') 
            print("No se pudo cambiar el nombre de esta tabla") 
            print(f"Motivo referido: {'\033[0;94m'}{e}{'\033[0;0m'}")   
    return resultado  
     
def eliminar_secc():
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    print(f" ⬛ {'\033[0;90m'}🗑 {'\033[0;91m'}<{'\033[0;97m'}Eliminar seccion{'\033[0;91m'}> {'\033[0;0m'}\n")
    print("")    
    try:
        if os.path.isfile(p_archivo):
            opc=input("De verdad desea eliminar la seccion? (se eliminara junto a TODOS los datos) 1)Si 2)No ‣ ")
            if opc=="1":
                archivo=open("proyecto_u2_libreria\\datos_conFS.txt","r")
                datos=archivo.readlines()
                archivo.close()
                archivo=open("proyecto_u2_libreria\\datos_conFS.txt","w")
                for i in range(0,len(datos)):
                    if(i!=(num_secc-1) and i!=(num_secc+num_r)-1):                    
                        archivo.write(f"{datos[i]}")   
                archivo.close()
                os.remove(p_archivo)
                cursor = conn.cursor()
                cursor.execute(f"drop table if exists `{secc_nomb}`") 
                conn.close()
                resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"  
            else:
                resultado=f"\n{'\033[0;91m'}{'\033[4;91m'}⭕ Accion abortada ⭕ {'\033[0;0m'}"         
        else:            
            print("<El archivo espesificado no existe>")
            print("Error inesperado")
            pausa_borra('p') 
    except OSError:
        print("Error inesperado")
        pausa_borra('p')
    except Error as e:
        print("No se pudo eliminar la seccion")
        print(f"Motivo referido: {'\033[0;94m'}{e}{'\033[0;0m'}")
        pausa_borra('p')
    return resultado

def agregar_secc(num_rl):
    pausa_borra('b')
    print(f" ➕ 🔠 {'\033[0;33m'}<{'\033[0;97m'}Agregar seccion{'\033[0;33m'}> {'\033[0;0m'}\n")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}" 
    try:
        nombre_SecN=str(input("Ingresa el nuevo nombre de la seccion  ‣ ")) 
        temp_nomb=nombre_SecN 
        nombre_SecN=limpiar_n(nombre_SecN) 
        if temp_nomb!=nombre_SecN:
            pausa_borra('b')
            print("El nombre: "+temp_nomb+" , se cambiara a el siguiente: "+nombre_SecN)
            pausa_borra('p')
    except ValueError:
        pausa_borra('b')
        nombre_SecN=""
        print("Ingresa caracteres validos ....")  
    except KeyboardInterrupt:
        pausa_borra('b')
        print("Manuel deja de tocar mi codigo")  
        
    if os.path.isfile(f"Proyecto_u2_libreria\\secciones\\{nombre_SecN}.txt"):
        pausa_borra('b')
        print("<El nombre espesificado ya esxiste>")
    elif nombre_SecN!="":            
        print("")
        opc="1"
        verif=False
        temp_campo=""
        campos=[None,None,None,None]
        consulta=f"`id_{nombre_SecN}` int(11) primary key auto_increment ,"
        texto_def=f"`id_{nombre_SecN}` int(11) primary key auto_increment \n"
        while opc!="2" and opc!="3":
            try:
                temp_campo=input("Ingresa el nombre de una caracteristica ‣ ").strip()
                if(temp_campo!="" or temp_campo!=None):
                    campos[0]=temp_campo
                else:
                    pausa_borra('b')
                    print("Ingresa informacion en el campo por favor")
                    verif=True
                print("")
                print(f"{'\033[0;94m'}|{'\033[0;0m'} int  ")
                print(f"{'\033[0;94m'}|{'\033[0;0m'} float")
                print(f"{'\033[0;94m'}|{'\033[0;0m'} varchar")
                print(f"{'\033[0;94m'}|{'\033[0;0m'} <si se desean mas buscar los tipos de datos para mysql>")
                print("")
                temp_campo=input("Ingresa el tipo de dato que se utilizara ‣ ").lower().strip()
                if(temp_campo!="" or temp_campo!=None):
                    campos[1]=temp_campo
                else:
                    pausa_borra('b')
                    print("Ingresa informacion en el campo por favor")
                    verif=True
                print("")
                print("Ingresa 0 si el tipo de dato no necesita un tamaño")
                tamaño_d=int(input('Ingresa el tamaño maximo (en numero) que los datos utilizaran [2 ->(99) 4->(AAAA)] ‣ '))
                if tamaño_d!=0:
                    campos[1]=f"{campos[1]}({tamaño_d})"
                    
                temp_campo=input("Quieres que el campo necesite tener necesariamente un valor? 1)Si 2)No ‣ ").strip()
                if (temp_campo=="1"):
                    campos[2]=" not null "   
                elif (temp_campo=="2"):
                    campos[2]=""   
                else:
                    verif=True 
                
                temp_unico=input("Quieres que el campo necesite tener necesariamente un valor unico que no se repita? 1)Si 2)No ‣ ").strip()
                if (temp_unico=="1"):
                    campos[3]=" unique "   
                elif (temp_unico=="2"):
                    campos[3]=""   
                else:
                    verif=True     

                if verif==False:   
                    print("")
                    opc=input("Deseas agregar  otra caracteristica 1)Si 2)No 3)Canselar ‣ ").lower().strip()
                    consulta=consulta+f"`{campos[0]}` {campos[1]} {campos[2]} {campos[3]}"
                    texto_def=texto_def+f"`{campos[0]}` {campos[1]} {campos[2]} {campos[3]}\n"
                    print("\nAccion realizada")
                    print(f'''create table `{nombre_SecN}`({consulta})''')
                    print("\n")
                    if(opc=="2"):   
                        cursor = conn.cursor()
                        temp_c='''drop table if exists `%s` '''
                        cursor.execute(temp_c,(nombre_SecN,))
                        sql =f'''create table `{nombre_SecN}` ({consulta})'''
                        cursor.execute(sql)   
                        archivo=open(f"Proyecto_u2_libreria\\secciones\\{nombre_SecN}.txt", "x") 
                        archivo.close()
                        archivo_w=open(f"Proyecto_u2_libreria\\secciones\\{nombre_SecN}.txt", "w")
                        archivo_w.writelines(texto_def)
                        archivo_w.close()
                        archivo=open("proyecto_u2_libreria\\datos_conFS.txt","r")
                        datos=archivo.readlines()
                        archivo.close()
                        archivo=open("proyecto_u2_libreria\\datos_conFS.txt","w")
                        for i in range(0,len(datos)):
                            if(i==(num_rl-1)): 
                                archivo.write(f"{nombre_SecN}\n")
                                archivo.write(f"{datos[i]}")                      
                            else:
                                archivo.write(f"{datos[i]}")
                        archivo.write("")
                        archivo.close() 
                        archivo=open("proyecto_u2_libreria\\datos_conFS.txt","a")
                        archivo.write(f"proyecto_u2_libreria\\secciones\\{nombre_SecN}.txt \n")
                        archivo.close()  
                        conn.close() 
                        resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"            
                    elif(opc=="1"):                       
                        consulta=consulta+","  
                    elif(opc=="3"):
                        pausa_borra('b')
                        resultado=f"\n{'\033[0;91m'}{'\033[4;91m'}⭕ Accion abortada ⭕ {'\033[0;0m'}"
                        print("Ok")  
                    else:
                        pausa_borra('b')
                        print("Ingresa un valor aplicable (1/2) ")                                    
                else:
                    pausa_borra('b') 
                    print("Ingresa correctamente lo que se pide ") 
                    print("Intentalo de nuevo")
                    pausa_borra('p')
                    verif=False 
            except Error as e:
                pausa_borra('b')
                print("No se pudo realizar la accion")
                print("Intenta ingresar de forma correcta lo que se te pide o contacta con un administrador...")
                print(f"Motivo referido: {'\033[0;94m'}{e}{'\033[0;0m'}")
            except OSError:
                pausa_borra('b') 
                print("No utilize caracteres especiales o invalidos")
                print("Intente un nombre con solo letras y/o numeros") 
            except KeyboardInterrupt:
                pausa_borra('b')
                print("No ingreses este tipo de cosas") 
            except ValueError:
                pausa_borra('b')
                print("Ingresa solo valores numericos")
            pausa_borra('p')    
    return resultado                
                   
def eliminar_Tdsecc():
    pausa_borra('b')
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
    print(f"  {'\033[0;90m'}🗄🗑 {'\033[0;94m'}<{'\033[0;97m'}Eliminar TODAS las seccion{'\033[0;94m'}> {'\033[0;0m'}\n")
    print("<Eliminar todas las secciones> \n")
    print("")
    try:
        opc=input("Estas seguro que quieres eliminar TODAS (junto con TODOS los datos) las secciones (Si/No) ‣ ").strip().lower()
    except ValueError:
        pausa_borra('b')
        print("Ingresa caracteres validos ....")  
    except KeyboardInterrupt:
        pausa_borra('b')
        print("Evita teclear eso -_-")
        
    if(opc=="si"):
        try:
            cursor = conn.cursor()
            archivo=open("proyecto_u2_libreria\\datos_conFS.txt")
            opciones=archivo.readlines()
            archivo.close()
            for tabla in opciones: 
                if(str(tabla).strip()=='----'):
                    break    
                print("")
                print(tabla.strip())
                cursor.execute(f"drop table if exists `{tabla.strip()}`") 
            rmtree("proyecto_u2_libreria\\secciones/") 
            os.remove("proyecto_u2_libreria\\datos_conFS.txt")   
            os.mkdir("proyecto_u2_libreria\\secciones/")
            archivo=open("proyecto_u2_libreria\\datos_conFS.txt","a")
            archivo.write("----\n")
            archivo.close()
            conn.close()
            resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"
            pausa_borra('b')
        except OSError:
            pausa_borra('b')
            print("La accion no se pudo concretar inesperadamente")
            pausa_borra('p')
        except Error as e:
            pausa_borra('b')
            print("Algo inesperado ocurrio, mensaje referido: ")
            print(f"{'\033[0;94m'}{e}{'\033[0;0m'}")
            pausa_borra('p')    
        except ValueError:
            pausa_borra('b')
            print("Ingresa caracteres validos ....")  
        except KeyboardInterrupt:
            pausa_borra('b')
            print("Evita teclear eso -_-")
        
    elif(opc=="no"):
        pausa_borra('b')
        print("hasta la proxima :>")
        pausa_borra('p') 
        resultado=f"\n{'\033[0;91m'}{'\033[4;91m'}⭕ Accion abortada ⭕ {'\033[0;0m'}"
    else:
        pausa_borra('b')
        print("intenta una opcion si o no !!!")
        pausa_borra('p')  
    return resultado     

def mod_CSecc():
    salir=False
    resultado=None
    while salir!=True:
        pausa_borra('b')
        print("")
        archivo=open(p_archivo)
        opciones=archivo.readlines()
        archivo.close()
        print(f" 📝 {'\033[0;95m'}  🖍  <{'\033[0;97m'}Cararacteristicas de la seccion {'\033[0;95m'}> 🗒{'\033[0;0m'}\n")
        print("")
        print(f"{'\033[0;30m'}-".ljust(60,"-"))
        disc=False
        for linea in opciones:  
            if disc!=False:
                print(f"{'\033[0;30m'}|{'\033[0;0m'} {linea.strip()} ")
                print(f"{'\033[0;30m'}-".ljust(60,"-"))
            else:
                disc=True
        else:
            print(f"{'\033[0;0m'}")
            if len(opciones)==0:
                print("")
                print(" ‣ <No se han agregado secciones> \n")
        print("")
        print(f"‣ 1) {'\033[0;33m'}Agregar una caracteristica {'\033[0;0m'}\n")
        print(f"‣ 2) {'\033[0;36m'}Eliminar una caracteristica {'\033[0;0m'}\n")
        print(f"‣ 3) {'\033[0;92m'}Salir {'\033[0;0m'}")
        print("")
        try:        
            opc=int(input("Ingresa el numero de opcion  ‣ "))
            match opc:
                case 1:
                    pausa_borra('b')
                    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
                    opc=input("Ingresesa el nombre de la nueva caracteristica  ‣ ")
                    cursor = conn.cursor()
                    cursor.execute(f"show columns from `{secc_nomb}`") 
                    caracteristicas=cursor.fetchall()
                    entrar=True
                    for crt in range(0,len(caracteristicas)):
                        if caracteristicas[crt][0]==opc:
                            entrar=False  
                    caracteristicas=None
                    if entrar==True:  
                        print("")
                        print(f"{'\033[0;94m'}|{'\033[0;0m'} int  ")
                        print(f"{'\033[0;94m'}|{'\033[0;0m'} float")
                        print(f"{'\033[0;94m'}|{'\033[0;0m'} varchar")
                        print(f"{'\033[0;94m'}|{'\033[0;0m'} <si se desean mas buscar los tipos de datos para mysql>")
                        print(f"")
                        try:
                            temp_campo=input("Ingresa el tipo de dato que se utilizara ‣ ").lower().strip()
                            temp_campo=f"{temp_campo}({int(input('Ingresa el tamaño maximo (en numero) que los datos utilizaran ejemplo: [2 ->(99) 4->(AAAA)] ‣ '))})"
                            nvc=input("Quieres que el campo necesite tener necesariamente un valor? 1)Si 2)No ‣ ").strip()
                            if (nvc=="1"):
                                temp_campo=temp_campo+" not null "  
                            else:
                                print("\nNo se agregara esta opcion") 
                                pausa_borra('p')                                                            
                            nvu=input("Quieres que el campo necesite tener necesariamente un valor unico que no se repita? 1)Si 2)No ‣ ").strip()
                            if (nvu=="1"):
                                temp_campo=temp_campo+" unique "   
                            else:
                                print("\nNo se agregara esta opcion") 
                                pausa_borra('p')
                            archivo_w=open(p_archivo, "a")
                            archivo_w.write(f"`{opc}` {temp_campo}\n")
                            archivo_w.close()
                            cursor = conn.cursor()
                            cursor.execute(f"alter table `{secc_nomb}` add column `{opc}` {temp_campo} ") 
                            pausa_borra('b')
                            return f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"                           
                        except ValueError:
                            pausa_borra('b')
                            print("Por favor introdusca valores numericos")
                        except KeyboardInterrupt:
                            pausa_borra('b')
                            print("no hacer esto* ")
                    else:
                        pausa_borra('b')
                        print("Ingresa un nombre nuevo")
                case 2:
                    pausa_borra('b')
                    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ La accion no pudo ser concretada ⚠ {'\033[0;0m'}"
                    archivo=open(f"Proyecto_u2_libreria\\secciones\\{secc_nomb}.txt","w")
                    #Poner el verificador de caracteristicas antes de la pregunta!!!
                    print("")                  
                    cs=input("Ingresa la caracteristica que quieres eliminar ‣ ").strip().lower()
                    opc=input("De verdad quieres eliminar una opcion (Si/No) ‣ ").strip()
                    if(opc=="si"):
                        cont=0
                        d=False 
                        for i in opciones:
                            if d!=False:
                                for j in range(0,len(cs.strip())):
                                    if (i.lower())[j+1]==cs[j]:
                                        cont+=1
                                if cont==j+1:   
                                    cursor = conn.cursor()
                                    cursor.execute(f"alter table `{secc_nomb}` drop column `{cs}`") 
                                    conn.commit()
                                    conn.close()   
                                    #archivo.write("")
                                    return f"\n{'\033[0;92m'}{'\033[4;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}" 
                                else:
                                    archivo.write(i)                                   
                                cont=0
                            else:
                                archivo.write(i)
                                d=True
                        
                    elif(opc=="no"):
                        pausa_borra('b')
                        print(" esta bien... ") 
                        resultado=f"\n{'\033[0;91m'}{'\033[4;91m'}⭕ Accion abortada ⭕ {'\033[0;0m'}" 
                    else:
                        pausa_borra('b')
                        print(" Ingresa lo que se te pide (Si o No) ")
                    archivo.close()
                case 3:
                    conn.close()     
                    salir=True 
                    if resultado==None:     
                        resultado=""   
                    return resultado                    
                case _:
                    pausa_borra('b')
                    print("Ingresa opciones validas (1-3)")
            pausa_borra('p')
        except OSError:
            pausa_borra('b')
            print("La accion no se pudo concretar inesperadamente")
            pausa_borra('p')
        except Error as e:
            pausa_borra('b')
            print("Algo inesperado ocurrio, mensaje referido: ")
            print(f"{'\033[0;94m'}{e}{'\033[0;0m'}")
            pausa_borra('p')
        except ValueError:
            pausa_borra('b')
            print("Ingresa caracteres validos ....")  
        except KeyboardInterrupt:
            pausa_borra('b')
            print("Evita teclear eso -_-")
        finally:
            pausa_borra('b')
        
        
def main_seccion(archivo_p,nomb_secc,n_seccion,n_relleno):
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
    print(f"   \t\t",f"".center(25,'-'),"⁙",f" {secc_nomb} ".center(23,' '),"⁙",f"".center(25,'-'),f"\t\t\t   ")
    print("\n")
    print(f"\t\t\t\t\t{'\033[0;33m'}‣{'\033[0;0m'} 1) Modificar nombre de seccion \n")
    print(f"\t\t\t\t\t{'\033[0;95m'}‣{'\033[0;0m'} 2) Modificar las caracteristicas de la seccion \n")
    print(f"\t\t\t\t\t{'\033[0;91m'}‣{'\033[0;0m'} 3) Eliminar esta seccion \n")
    print(f"\t\t\t\t\t{'\033[0;92m'}‣{'\033[0;0m'} 4) Salir \n")
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
            print(cambiar_nombre())
            pausa_borra('p')
        case 2:
            print(mod_CSecc())
            pausa_borra('p')
        case 3:
            print(eliminar_secc())
            pausa_borra('p')
        case 4:
            print()
        case _:
            pausa_borra('b')
            print("Ingesa una opcion valida para hacer algo (del 1 al 3)")
            pausa_borra('p') 
    
    
import hashlib
from funcion import conexion,pausa_borra,Error
from getpass import getpass

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()
def registrar(usuario):
    (_,conn)=conexion()
    pausa_borra('b')
    print(f" ➕ 👤 {'\033[0;91m'}<Registro de usuario> 💬 {'\033[0;0m'}\n")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ No fue posible registrar al usuario ⚠ {'\033[0;0m'}"
    try:
        print("")
        n_usuario=input("Ingrese un nombre de usuario para utilizarlo en el sistema ‣ ")
        print("")
        cont=getpass("Ingresa la contraseña que sera usada (ingresa una contraseña segura y no la olvides o pierdas) ‣ ")
        print("")
        verif_cont=getpass("Ingresa la contraseña que sera usada (ingresa una contraseña segura y no la olvides o pierdas) ‣ ")
        print("")
        if cont==verif_cont:
            cursor = conn.cursor()
            p_admin=input("El usuario tendra permiso de administrar el sistema? 1)Si 2)No ‣ ")
            print("")
            verif=hash_password(getpass("Ingresa la contraseña de tu usuario (el usuario actual) para terminar la accion ‣ "))
            sql="select * from usuarios where usuario=%s and contraseña=%s"
            cursor.execute(sql,(usuario,verif))
            datos=cursor.fetchall()
            print("")
            if datos!=[] and datos!=None:    
                if p_admin=="1":
                    p_admin="si"
                else:
                    p_admin="no"
                print("")  
                cursor = conn.cursor()
                cont=hash_password(cont)
                sql="insert into usuarios (usuario,contraseña,permiso) values (%s,%s,%s)"
                val=(n_usuario,cont,p_admin)
                cursor.execute(sql,val)
                conn.commit()
                resultado="\n{'\033[4;92m'}{'\033[1;92m'}✅ La accion se realizo correctamente ✅ {'\033[0;0m'}"
                cont=None
            verif=None
            p_admin=None
            verif_cont=None    
        else:
            pausa_borra('b')
            print("Las contraseñas no coinciden, intentalo otra vez...")
            pausa_borra('p')  
    except Error as e:
        pausa_borra('b')
        print("No se pudo registrar el usuario actual...")
        print("Por favor intentelo otra vez o contacte a un administrador")
        print(f"Motivo referido: {'\033[0;94m'}{e}{'\033[0;0m'}")
        pausa_borra('p')  
    except ValueError:
        pausa_borra('b')
        print("Ingresa caracteres validos (numeros como 1,2... y sin caracteres especiales)....")
        pausa_borra('p')
    except KeyboardInterrupt:
        pausa_borra('b')
        print("No ingreses este tipo de cosas...") 
        pausa_borra('p')
    conn.close() 
    pausa_borra('b')
    return resultado

def iniciar_sesion():
    (_,conn)=conexion()
    pausa_borra('b')
    print(f" 🚪👤 {'\033[0;94m'}<{'\033[0;97m'}Inicio de secion usuario{'\033[0;94m'}>{'\033[0;97m'} 🕒🛎 {'\033[0;0m'}\n")
    resultado=f"\n{'\033[4;93m'}{'\033[0;93m'} ⚠ No se pudo iniciar secion correctamente ⚠ {'\033[0;0m'}"
    try:
        print("")
        usuario=input("Ingrese tu nombre de usuario ‣ ")
        print("")
        cont=hash_password(getpass("Ingresa tu contraseña ‣ "))
        print("")
        cursor = conn.cursor()
        sql="select * from `usuarios` where `usuario`=%s and `contraseña`=%s"
        cursor.execute(sql,(usuario,cont))
        datos=cursor.fetchall()
        print("")
        if datos!=[] and datos!=None:
            if datos[0][3]=="si":
                resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ Inicio de secion ADMIN exitoso ✅ {'\033[0;0m'}"
            else:
                resultado=f"\n{'\033[0;92m'}{'\033[4;92m'}✅ Inicio de secion exitoso ✅ {'\033[0;0m'}"    
            gr_perm=datos[0][3]
        else:
            gr_perm=0
            pausa_borra('b')
            print("El usuario y/o la contraseña no son correctos ...")
            print("Por favor intentelo otra vez o contacte a un administrador")
            pausa_borra('p') 
    except Error as e:
        pausa_borra('b')
        print("No se pudo inicar secion ...")
        print("Por favor intentelo otra vez o contacte a un administrador")
        print(f"Motivo referido: {'\033[0;94m'}{e}{'\033[0;0m'}")
        pausa_borra('p')  
    except ValueError:
        pausa_borra('b')
        print("Ingresa caracteres validos (numeros como 1,2... y sin caracteres especiales)....")
        pausa_borra('p')
    except KeyboardInterrupt:
        pausa_borra('b')
        print("No ingreses este tipo de cosas...") 
        pausa_borra('p')     
    conn.close() 
    return (usuario,gr_perm,resultado)
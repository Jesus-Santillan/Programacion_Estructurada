import os
#Dict u objeto para guardar los atributos de una pelicula

'''
peliculas={
    "nombre":"",
    "categoria":"",
    "clasificacion":"",
    "genero":"",
    "idioma":"",   
}
'''
pelicula={}

def PausaBorra(tpausa):
    if(tpausa=='p'):
        os.system("\t\t\t")
        os.system("pause")
    os.system("cls") 

def crearPeliculas():
    PausaBorra('n')
    print("---- crear una pelicula ----")
    #pelicula["nombre"]=input("Ingresa el nombre de la pelicula ‣ ").lower().strip()
    pelicula.update({"nombre":input("Ingresa el nombre de la pelicula ‣ ").lower().strip()})
    pelicula.update({"categoria":input("Ingresa la categoria a la que pertence la pelicula ‣ ").lower().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion de la pelicula ‣ ").lower().strip()})
    pelicula.update({"genero":input("Ingresa el genero al que pertenece la pelicula ‣ ").lower().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma en el que esta la pelicula ‣ ").lower().strip()})
    print(" \u2705 La operacion se realizo con exito \u2705")

def mostrar_peliculas():
    PausaBorra('n')
    print("---- crear una pelicula ----")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}") 

def borrar_peliculas():
    PausaBorra('n')
    print("---- borrar todas las peliculas ----") 
    opc=input(" ¿Deseas quitar o borrar todas las caracteristicas de la pelicula del sistema (Si/No)? ‣ ").lower().strip()
    if opc=="si":
        pelicula.clear()
        print(" \u2705 La operacion se realizo con exito \u2705 ")
        
def agregar_CPeliculas():
    PausaBorra('n')
    print("---- agregar caracteristicas a peliculas ----")  
    c_atrib=input("Ingresa el nombre de la carteristica de la pelicula ‣ ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la pelicula ‣ ").lower().strip()
    #pelicula.update({c_atrib:valor})    
    pelicula[c_atrib]=valor  
    print(" \u2705 La operacion se realizo con exito \u2705 ")
    
def modificar_CPeliculas():
    PausaBorra('n')
    print("---- modificar caracteristicas de las peliculas ----")
    '''
    if len(pelicula)>0:
        for i in pelicula:
            print(f"|{i}")
        print("")
        c_atrib=input("Ingresa la carteristica de la pelicula ‣ ").lower().strip()
        try:
            print("<",pelicula[c_atrib],">")
            newc_atrib=input("Ingresa el nuevo nombre de carteristica de la pelicula ‣ ").lower().strip()
            temp_atb=pelicula.pop(c_atrib)
            pelicula[newc_atrib]=temp_atb
        except KeyError:
            print("Caracteristica de pelicula no encontrada...")
    else:
        print("<No hay atributos registrados>")
    '''
    if len(pelicula)>0:
        cont=0
        for i in pelicula:
            print(f"|{i}")
            if input(" ¿Deseas modificar el nombre de esta caracteristica (Si/No)? ‣ ").lower().strip()=="si":
                c_atrib=i
                try:
                    print("<",pelicula[c_atrib],">")
                    newc_atrib=input("Ingresa el nuevo nombre de carteristica de la pelicula ‣ ").lower().strip()
                    temp_atb=pelicula.pop(c_atrib)
                    pelicula[newc_atrib]=temp_atb
                except KeyError:
                    print(" \u26A0 Caracteristica de pelicula no encontrada... \u26A0 ")
                    print("")
                PausaBorra("n")
            if(cont==len(pelicula)-1):
                break
            cont=cont+1    
        
    else:
        print(" \u26A0 <No hay atributos registrados> \u26A0 ") 
'''
def borrar_CPeliculas(): 
    PausaBorra('n')
    print("---- borrar caracteristicas de las peliculas ----")  
    opc=input(" ¿Deseas quitar o borrar todas las caracteristicas de la pelicula del sistema (Si/No)? ‣ ").lower().strip()
    if opc=="si" and len(pelicula)>0:
        pelicula.clear()
        print("La operacion se realizo con exito")
    elif len(pelicula)>0:
        print(" <no se encuentran atributos>")
    else:
        print("ok")
'''
        
def borrar_CPeliculas():
    PausaBorra('n')
    print(".:: borrar caracteristicas de las peliculas :..") 
    print("\n Valores actuales: \n") 
    
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}")
        print("")
        opc=input(" ¿Deseas borrar alguna caracteristica (Si/No)? ‣ ").lower().strip()
        if opc=="si": 
            c_atrib=input("Ingresa la carteristica que deseas quitar o borrar ‣ ").lower().strip()
            try:
                pelicula.pop(c_atrib)
                print(" \u2705 ::: ¡LA OPERACION SE REALIZO CON EXITO! ::: \u2705 ")
            except KeyError:
                print(" \u26A0 Caracteristica de pelicula no encontrada... \u26A0 ")
        else:
            print("ok")
    elif len(pelicula)<=0:
        print(" <no se encuentran atributos> ")
            

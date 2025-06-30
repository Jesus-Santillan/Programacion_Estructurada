import sys
import os
peliculas=[]

def PausaBorra(tpausa):
    if(tpausa=='p'):
        os.system("\t\t\t")
        os.system("pause")
    os.system("cls") 
    
def agregarPeliculas():
    PausaBorra('n')
    print("\t\t\t ⁖ Agregar pelicula ⁖")
    print("")
    peliculas.append(input("Ingresa el nombre de una pelicula ‣ ").lower().strip())
    print("")
    print("\t\t Operacion exitosa :D ")
    
def consultarPeliculas():
    PausaBorra('n')
    print("\t\t\t ⁖ Consultar peliculas ⁖")
    print("")
    for i in range(0,len(peliculas)):
        print(f"\t{i+1}.- {peliculas[i]}")
    else:
        if len(peliculas)==0:
            print("\t No hay peliculas en el sistema ")
        else:
            print("\t Operacion exitosa :D ")
            
def vaciarPeliculas():
    PausaBorra('n')
    print("\t\t\t ⁖ Vaciar o eliminar todas las peliculas ⁖")
    print("")    
    opc=input("¿Deseas borrar todas las peliculas peliculas?(Se eliminaran para siempre todas las peliculas) ‣ ").lower()
    if(opc=="si"):
        print("\t Operacion exitosa :D ")    
    elif(opc=="no"):
        print("\t Nos vemos despues :3")
    else:
        print("\t intenta ingresar opciones validas adios >:v")
 
def eliminarPeliculas():
    PausaBorra('n') 
    #mostrarPeliculas()
    print("")
    print("\n\t\t .:: Borrar peliculas ::.")
    print("")
    buscar_pel=input(" Ingresa el nombre de la pelicula que desaes buscar ‣ ").lower().strip()
    if not(buscar_pel in peliculas):
        print(" no se encontro una pelicula con este nombre :/")     
    else:
        encontro=0
        i=0
        while i<len(peliculas):
            if buscar_pel==peliculas[i]:
                opc=input(" ¿Deseas quitar o borrar la pelicula del sistema (Si/No)? ‣ ").lower().strip()
                if(opc=="si"):
                    print(f" La pelicula que se borro es {peliculas[i]} y estaba en la casilla: {i+1}")
                    peliculas.remove(peliculas[i])
                    print(f"\t\t\t ::: LA OPERACION SE REALIZO CON ÉXITO! :::")      
                    encontro+=1
                    i=-1
                else:
                    print("bye ;>")
            i+=1
        print(f" se borro {encontro} pelicula(s) con este titulo")        
def modificarPeliculas():
    PausaBorra('n') 
    mostrarPeliculas()
    print("")
    print("\t\t\t ⁖ Modificar una pelicula ⁖")
    print("")
    buscar_pel=input("\t Ingresa el nombre de una pelicula ‣ ").lower().strip()
    if not(buscar_pel in peliculas):
        print("\t no se encontro una pelicula con este nombre :/")     
    else:
        encontro=0
        i=0
        while i<len(peliculas):
            if buscar_pel==peliculas[i]:
                opc=input("¿Deseas actualizar-Modificar la pelicula? (Si/No) ‣ ").lower().strip()
                if(opc=="si"):
                    peliculas[i]=input("\t Introdusca el nuevo valor de la pelicula").lower().strip()
                    print("\t El nombre de la pelicula ha sido Modificado - actualizado ")       
                    encontro+=1
                    i=-1
            i+=1
        print(f"\t el numero de pelicula(s) encontradas y actualizadas es de: {encontro}") 
        
def buscarPeliculas():
    PausaBorra('n') 
    print("\t\t\t ⁖ Buscar una alguna pelicula ⁖")
    print("")
    buscar_pel=input("\t Ingresa el nombre de una pelicula ‣ ").lower().strip()
    if not(buscar_pel in peliculas):
        print("\t no se encontro una pelicula con este nombre :/")     
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if buscar_pel==peliculas[i]:
                print(f"pelicula encontrada: {buscar_pel} , pelicula numero {i+1}")
                encontro+=1
        print(f"\t numero de pelicula(s) encontradas: {encontro}")          
    
def mostrarPeliculas():
    con=-1
    while(con<=len(peliculas)):
        if(con==-1 or con==len(peliculas)):
            sub_con=0
            while(sub_con<=10):
                print("-",end="")
                sub_con=sub_con+1
            print("")
        else:
            print(f"| {peliculas[con]} ".format(20))
        con=con+1
    else:
        if(len(peliculas)==0):
            print("No se han agregado peliculas")    
        
            
         
     
     
    
    
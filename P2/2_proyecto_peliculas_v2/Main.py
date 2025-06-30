'''
Proyecto 1
Crear un proyecto que permita manejar(administrar) peliculas, colocar un menu de opciones 
para agregar, eliminar, modificar, consultar, buscar y vaciar peliculas
Notas: 
    1.-Utilizar funciones y mandar llamar desde otro archivo
    2.-Utilizar diccionarios para almacenar los atributos o caracteristicas (nombre,categoria,clasificacion,genero,idioma) de las peliculas
    3.-
'''



import peliculas
import sys
import os
#Funcion para abrir otros archivos
peliculas.PausaBorra('n') 
def abrir_archivo(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: El archivo '{file_path}' no existe.")#Como llego aquí :O
      os.system("cls")
      os.system("pause")   
cond=True
opc_materia=""
while cond==True:
   print(f"   \t\t",f"".center(25,'-'),f"---- Peliculas ----",f"".center(25,'-'),f"\t\t\t   ")
   print("\n")
   print(f"\t\t\t  ‣ 1)  Crear\n")
   print(f"\t\t\t  ‣ 2)  Borrar\n")
   print(f"\t\t\t  ‣ 3)  Mostrar\n")
   print(f"\t\t\t  ‣ 4)  Agregar caracteristicas\n")
   print(f"\t\t\t  ‣ 5)  Modificar caracteristicas\n")
   print(f"\t\t\t  ‣ 6)  Borrar caracteristicas\n")
   print(f"\t\t\t  ‣ 7)  Salir\n")
   try:
        opc_materia=int(input(f"\t\t\t  Ingresa la opción a la que quieras ingresar (numero) ‣ "))
        print("")
        peliculas.PausaBorra('n')

        match opc_materia:
            case 1:
                print(f" <crear>")
                print("")
                peliculas.crearPeliculas()
                peliculas.PausaBorra('p')
            case 2:
                print(f" <Borrar>")
                print("")
                peliculas.borrar_peliculas()
                peliculas.PausaBorra('p')
                print("")
            case 3:
                print(f" <Mostrar>")
                print("")
                peliculas.mostrar_peliculas()
                peliculas.PausaBorra('p')
            case 4:
                print(f" <Agregar Caracteristicas> ")
                print("")
                peliculas.agregar_CPeliculas()
                peliculas.PausaBorra('p')
            case 5:
                print(f" <Modificar Caracteristicas> ")
                print("")
                peliculas.modificar_CPeliculas()
                peliculas.PausaBorra('p')
            case 6:
                print(f" <Borrar caracteristicas>")
                peliculas.borrar_CPeliculas()
                peliculas.PausaBorra('p')   
            case 7:
                print("")
                print(f"Muchas gracias ;> ....")
                sys.exit()
            case _:
                peliculas.PausaBorra('n')
                print("")
                print(f" \u26A0 ‣ Porfavor ingresa opciones validas, opcion tecleada: {opc_materia} . Intentalo otra vez \u26A0 ")
                peliculas.PausaBorra('p')
                opc_materia=""                  
   except ValueError:
    peliculas.PausaBorra('n')
    print("")
    print(" \u26A0 ‣ Ingresa números para seleccionar una opción. porfavor Intentalo otra vez \u26A0 ")
    peliculas.PausaBorra('p')
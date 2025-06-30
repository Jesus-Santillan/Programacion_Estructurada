'''
Proyecto 1
Crear un proyecto que permita manejar(administrar) peliculas, colocar un menu de opciones 
para agregar, eliminar, modificar, consultar, buscar y vaciar peliculas
Notas: 
    1.-Utilizar funciones y mandar llamar desde otro archivo
    2.-Utilizar listas para almacenar los nombre de las peliculas
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
   print(f"\t\t\t  ‣ 1)  Agregar\n")
   print(f"\t\t\t  ‣ 2)  Eliminar o vaciar\n")
   print(f"\t\t\t  ‣ 3)  Modificar\n")
   print(f"\t\t\t  ‣ 4)  Consultar\n")
   print(f"\t\t\t  ‣ 5)  Salir\n")
   try:
        opc_materia=int(input(f"\t\t\t  Ingresa la opción a la que quieras ingresar (numero) ‣ "))
        print("")
        peliculas.PausaBorra('n')

        match opc_materia:
            case 1:
                print(f" <Agregar>")
                print("")
                peliculas.agregarPeliculas()
                peliculas.PausaBorra('p')
            case 2:
                print(f" <Eliminar>")
                print("")
                peliculas.eliminarPeliculas()
                peliculas.PausaBorra('p')
                print("")
                print(f" <vaciar>")
                peliculas.vaciarPeliculas()
                peliculas.PausaBorra('p')
            case 3:
                print(f" <Modificar>")
                print("")
                peliculas.modificarPeliculas()
                peliculas.PausaBorra('p')
            case 4:
                print(f" <Consultar> ")
                print("")
                peliculas.mostrarPeliculas()
                peliculas.consultarPeliculas()
                print(f" <buscar>")
                peliculas.buscarPeliculas()
                peliculas.PausaBorra('p')   
            case 5:
                print("")
                print(f"Muchas gracias ;> ....")
                sys.exit()
            case _:
                peliculas.PausaBorra('n')
                print("")
                print(f"‣ Porfavor ingresa opciones validas, opcion tecleada: {opc_materia} . Intentalo otra vez")
                peliculas.PausaBorra('p')
                opc_materia=""                  
   except ValueError:
    peliculas.PausaBorra('n')
    print("")
    print("‣ Ingresa números para seleccionar una opción. porfavor Intentalo otra vez")
    peliculas.PausaBorra('p')
'''
Crear un proyecto que permita gestionar(administrar) calificaciones,
colocar un menu de opciones para agregar, mostrar, y calcular el promedio de calificaciones

#Notas
#1.- Utilizar funciones y mandar a llamar desde otro archivo
#2.- Utilizar listas para almacenar el nombre y tres calificaciones de los alumnos
'''

import calificaciones
import sys
import os

def main():
    calificaciones.PausaBorra('n')   
    datos=[[],[],[],[]]
    cond=True
    opc_materia=""
    while cond:
        opc_materia=calificaciones.menu_principal()
        try:        
                match opc_materia:
                    case 1:
                        #print("")
                        #print(f" <crear>")
                        #print("")
                        datos=calificaciones.agregar_calificaciones(datos)
                        calificaciones.PausaBorra('p')
                    case 2:
                        #print("")
                        #print(f" <Borrar>")
                        #print("")
                        calificaciones.mostrar_calificaciones(datos)
                        calificaciones.PausaBorra('p')
                        #print("")
                    case 3:
                        #print("")
                        #print(" <Mostrar>")
                        #print("")
                        calificaciones.calcular_promedios(datos)
                        calificaciones.PausaBorra('p')  
                    case 4:
                        print("")
                        print(f" \U0001F6AA Muchas gracias ;> ....")
                        sys.exit()
                    case _:
                        #calificaciones.PausaBorra('n')
                        print("")
                        print(f" ⚠️ ‣ Porfavor ingresa opciones validas, opcion tecleada: {opc_materia} . Intentalo otra vez ")
                        #calificaciones.PausaBorra('p')
                        opc_materia=""                  
        except ValueError:
            calificaciones.PausaBorra('n')
            print("")
            print(" ⚠️ ‣ Ingresa números para seleccionar una opción. porfavor Intentalo otra vez")
            calificaciones.PausaBorra('p')
if __name__=="__main__":
    main()
import agenda
from funcion import pausa_borra
print("")
  
def main():
    opc=0
    while opc!=7:
        
        try:
            opc=agenda.menu()
            agenda.pausa_borra('b')  
            match opc:
                case 1:
                    agenda.agregar_contacto()
                    pausa_borra('p')                    
                case 2:
                    agenda.mostrar_contacto()
                    pausa_borra('p') 
                case 3:
                    agenda.buscar_contacto()
                    pausa_borra('p') 
                case 4:
                    agenda.eliminar_contacto()
                    pausa_borra('p') 
                case 5:
                    agenda.eliminarT_contacto()
                    pausa_borra('p') 
                case 6:
                    agenda.modificar_contacto()
                    pausa_borra('p')     
                case 7:
                    print(f"Muchas gracias ;> ....")
                    opc=4
                case _:
                        pausa_borra('b')  
                        print(f"‣ Porfavor ingresa opciones validas, opcion tecleada: {opc}. Intentalo otra vez")
                        pausa_borra('p')  
                   
        except ValueError:
            pausa_borra('b')   
            print("‣ Ingresa números para seleccionar una opción. porfavor Intentalo otra vez")
            pausa_borra('p')  
            
if __name__=="__main__":
    main()
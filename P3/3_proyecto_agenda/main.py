import agenda
print("")
  
def main():
    opc=0
    agenda_contacto={}
    while opc!=7:
        
        try:
            opc=agenda.menu()
            agenda.pausa_borra('b')  
            match opc:
                case 1:
                    agenda_contacto=agenda.agregar_contacto(agenda_contacto)
                    agenda.pausa_borra('p')                    
                case 2:
                    agenda.mostrar_contacto(agenda_contacto)
                    agenda.pausa_borra('p') 
                case 3:
                    agenda.buscar_contacto(agenda_contacto)
                    agenda.pausa_borra('p') 
                case 4:
                    agenda_contacto=agenda.eliminar_contacto(agenda_contacto)
                    agenda.pausa_borra('p') 
                case 5:
                    agenda_contacto=agenda.eliminarT_contacto(agenda_contacto)
                    agenda.pausa_borra('p') 
                case 6:
                    agenda_contacto=agenda.modificar_contacto(agenda_contacto)
                    agenda.pausa_borra('p')     
                case 7:
                    print(f"Muchas gracias ;> ....")
                    opc=4
                case _:
                        agenda.pausa_borra('b')  
                        print(f"‣ Porfavor ingresa opciones validas, opcion tecleada: {opc}. Intentalo otra vez")
                        agenda.pausa_borra('p')  
                   
        except ValueError:
            agenda.pausa_borra('b')   
            print("‣ Ingresa números para seleccionar una opción. porfavor Intentalo otra vez")
            agenda.pausa_borra('p')  
            
if __name__=="__main__":
    main()
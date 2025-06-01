from Paquete import modulos

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t\t.:: Agenda telefonica ::.\n\t\t Nombre: {nom}\n\t\tTelefono: {tel}")
modulos.espereTecla()
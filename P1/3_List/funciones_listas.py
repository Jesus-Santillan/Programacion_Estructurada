'''
List(Array)
son colecciones o conjuntos de datos/valores bajo un mismo nombre, para acceder a los valores
se hace con un indice numerico.
Nota: sus valores si son modificables
La lista es una colaccion ordenada y modificable. Permite miembros duplicados.

'''

import os
os.system("cls")

#Funciones mas comunes en las listas

paises=["Mexico","Brazil","España","Canada"]
numeros=[23,45,8,24,23,56]
varios=["hola",3.2426,"33",True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print("")
#Recorrer una lista e imprimir el contenido

#1er Forma
lista_i=""
for i in paises:
    print(i,end=" , ")
print("") 
print("")
lista_i=""
for i in paises:
    lista_i+=f"{i} , "
print(lista_i)        
#2da Forma
print("") 
lista_i=""
for i in range(0,len(paises)):
    lista_i+=f"{paises[i]} , "
print(lista_i)   
print("") 
lista_i=""
for i in range(0,len(paises)):
    print(paises[i],end=" , ")
print(lista_i)   
print("")
#Borramos pantalla

#Ordenar los elementos de la lista
print(paises)
print(numeros)
print(varios)
paises.sort()
print(paises)
numeros.sort()
print(numeros)
print("No se ordenan")

#Dar la vuelta a las listas
print("")
varios.reverse()
print(varios)
paises.reverse()
print(paises)
numeros.reverse()
print(numeros)
print("")

#Buscar un elemento dentro de una lista
print("España" in paises)
print("Espana" in paises)
print("")

#Insertar,añadir,agregar un elemento a una lista
print(paises)

#1er forma
paises.append("México")
print(paises)
paises.insert(1,"México")
print(paises)
paises.insert(6,"México")
print(paises)
print("")

#Borrar, eliminar, suprimir, quitar un elemento de la lista
print(paises)
paises.pop(0)
print(paises)
print("")
#2da Forma
paises.remove("México")
print(paises)
paises.sort()
print("")

#Obtener el indice o la posicion donde se encuentra un elemento
print(paises)
posicion=paises.index("Canada")
print("posicion ,",posicion)
paises.pop(posicion)
print(paises)
print("")

#Contar el numero de veces que un elemento se encuentra en una lista
print(numeros)
cuantas=numeros.count(45)
print(cuantas)
numeros.append(45)
cuantas=numeros.count(45)
print(cuantas)
cuantas=numeros.count(2333)
print(cuantas)
print("")
#Unir el contenido de una list a en otra

numero2=[100,200]
print(numero2)
print("")

#Crear un programa que una las listas numeros 1 y 2 e imprima el contenido de listas resultante en forma descendente
numeros.extend(numero2)
print(numeros)
numeros.sort()
numeros.reverse()
print(numeros)
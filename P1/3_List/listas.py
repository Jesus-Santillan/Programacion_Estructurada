import os

#Ejemplo 1 crear una lista de numeros e imprimir el contenido

numeros=[0,40,8,412,15,2]
print(numeros)
print("")
numeros_un=""
for i in numeros:
    numeros_un+=f"{i},"
print(numeros_un) 

numeros_un=""
for i in range(0,len(numeros)):
    numeros_un+=f"{numeros[i]}," 
print(numeros_un)     
print("") 

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra.
agreg=input("Ingresas un palabra a buscar ‣ ")
palabras=["hola","como","estas","hola","denuevo","y","hola"]
palabra_e=False
i_n=0
posiciones=[0]
for i in palabras:
    if i==agreg:
        if palabra_e==False:
            palabra_e=True #Encontrado
        else:                 
            posiciones.append(palabras.index(i,posiciones[-1]+1))
            print("Coincidencia encontrada en index : ",palabras.index(i,posiciones[-1]))          
if(len(posiciones)==1):
    print("no encontrado")    
else:    
    posiciones.pop(0)    
    print(posiciones) 
print("") 
posiciones=[]
palabra_e=False
for i in range(0,len(palabras)):
    if palabras[i]==agreg:
        if palabra_e==False:
            palabra_e=True #Encontrado
            i_n+=1
        else:
            print("Coincidencia encontrada en index : ",i) 
            posiciones.append(i)
if(len(posiciones)!=0):
    print(posiciones) 
else:
    print("no Encontrado")  
print("") 
if agreg in palabras:
    print("Encontrado")
else:
    print("no encontrado")  
print("")        
#Ejemplo 3 Añadir elementos a la lista
lista_x=[]

datM=1
while(datM!=2):
    if(datM==1):
        agreg=input("Ingresas un elemento a  agregar ‣ ")
        try:
            agreg=int(agreg)
        except:
            print("",end="")#No se 
        lista_x.append(agreg)
    try:
        datM=int(input("Deseas agregar mas datos? 1)Si 2)No ‣ "))
    except ValueError:
        print("Ingresa valores numericos")
        datM=0
print(lista_x)   
os.system("pause")
print("")
    
#Ejemplo 4 Crear una lista multidimencional para almacenar los nombres y telefonos de unos contactos "agenda"

agenda=[["Carlos","6188888888"],["Carlos V","6185555555"],["Carlos VI","6186666666"]]
print("agenda")
for i in agenda:
    print(i)
print("")
for r in range(0,len(agenda)):
    for c in range(0,len(agenda[r])):
        print(agenda[r][c])  
print("")

lista="" 
for j in range(0,len(agenda)):
    for k in range(0,len(agenda[j])):
        lista+=f"{agenda[j][k]},"
        lista+="\n"     
print(lista)

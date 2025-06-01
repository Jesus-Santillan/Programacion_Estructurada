'''
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones
1.-Sin estructuras de control
2.-Sin funciones

'''
#Version 1
NUM=int(input("Ingresa un numero a multiplicar: "))
print("")
print(f"-----Tabla del {NUM}-----")
print(f"{NUM} x 1 = {NUM*1}")
print(f"{NUM} x 2 = {NUM*2}")
print(f"{NUM} x 3 = {NUM*3}")
print(f"{NUM} x 4 = {NUM*4}")
print(f"{NUM} x 5 = {NUM*5}")
print(f"{NUM} x 6 = {NUM*6}")
print(f"{NUM} x 7 = {NUM*7}")
print(f"{NUM} x 8 = {NUM*8}")
print(f"{NUM} x 9 = {NUM*9}")
print(f"{NUM} x 10 = {NUM*10}")

#Version 2
'''
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones
1.-Con estructuras de control
2.-Sin funciones

'''
NUM=int(input("Ingresa un numero a multiplicar: "))
print("")
print(f"-----Tabla del {NUM}-----")
i=int(1)
while(i<=10):
    print(f"{NUM} x {i} = {NUM*i}")
    i+=1

#Version 2
'''
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones
1.-Con estructuras de control
2.-Con funciones

'''
def multi(num):
    NUM=int(num)
    print("")   
    print(f"-----Tabla del {NUM}-----")
    i=1
    numeros=""
    while(i<=10):
        numeros+=f"{NUM} x {i} = {NUM*i} \n"
        i+=1
    return numeros
num_n=int(input("Ingresa un numero a multiplicar"))
m=multi(num_n)
print(m)
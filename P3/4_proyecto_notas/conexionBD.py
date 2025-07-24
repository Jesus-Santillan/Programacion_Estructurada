import mysql.connector

try:
    conexion=mysql.connector.connect( user='root', password='2373203', host='127.0.0.1', database='bd_notas')
    cursor=conexion.cursor(buffered=True)
except:
    print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...") 



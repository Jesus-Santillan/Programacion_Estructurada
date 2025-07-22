import mysql.connector
from mysql.connector import Error

#Dict u objeto los atributos (nombre,categoria,clasificacion,genero,idioma) 

# pelicula={
#            "nombre":"",
#            "categoria":"",
#            "clasificacion":"",
#            "genero":"",
#            "idioma":""
#          }

pelicula={}

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t... Oprima cualquier tecla para continuar ...") 

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="2373203",
      database="bd_peliculas"
    )
    return conexion
  except Error as e:
    print(f"El error que se presento es: {e}")
    return None

def crearPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
      print("\n\t\t.:: Crear Películas ::. \n")
      pelicula.update({"nombre":input("\nIngresa el nombre: ").upper().strip()})
    # pelicula["nombre"]=input("\nIngresa el nombre: ").upper().strip()
      pelicula.update({"categoria":input("\nIngresa la categoría: ").upper().strip()})
      pelicula.update({"clasificacion":input("\nIngresa la clasificación: ").upper().strip()})
      pelicula.update({"genero":input("\nIngresa el genero: ").upper().strip()})
      pelicula.update({"idioma":input("\nIngresa el idioma: ").upper().strip()})
      ##### Sql para BD
      cursor=conexionBD.cursor()
      sql="insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values ( %s, %s, %s, %s, %s)"
      val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")

def mostrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    cursor=conexionBD.cursor()
    sql="select * from peliculas"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
    else:
      print("\t ..:: No hay películas en el sistema ::. ")

def buscarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    nombre=input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
    else:
      print("\t ..:: Las películas a buscar no estan en el sistema ::. ")      

def borrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
    else:
      print("\t ..:: Las películas a buscar no estan en el sistema ::. ")
      
def modificarPeliculas():
  print("\n\t\t.:: Crear Películas ::. \n")
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
    nombre = input("Ingresa el nombre de la película a modificar: ").upper().strip()
    cursor = conexionBD.cursor()
    sql = "SELECT * FROM peliculas WHERE nombre = %s"
    val = (nombre,)
    cursor.execute(sql, val)
    registros = cursor.fetchall()
    if registros:
      print("Película encontrada:")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-" * 80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-" * 80)

      resp = input(f"¿Deseas modificar la película '{nombre}'? (Si/No): ").lower().strip()
      if resp == "si":      
        try:
          id_buscar=int(input("Ingresa el numero de columna id de la fila a modificar: "))
          nuevo_nombre = input("Nuevo nombre: ").upper().strip()
          nueva_categoria = input("Nueva categoría: ").capitalize().strip()
          nueva_clasificacion = input("Nueva clasificación: ").upper().strip()
          nuevo_genero = input("Nuevo género: ").capitalize().strip()
          nuevo_idioma = input("Nuevo idioma: ").capitalize().strip()

          sql = """
            UPDATE peliculas SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s
            WHERE id=%s
          """
          valores = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, id_buscar)
          cursor.execute(sql, valores)
          conexionBD.commit()
          print("\nPelícula modificada exitosamente.")
        except (ValueError,Error ):
          print("No se pudo encontrar el campo espesificado")
    else:
      print("\t ..:: La película no se encuentra en el sistema ::. ")
       


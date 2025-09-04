#Escribir un script de Python que se conecte a una base de datos SQLite. Si el archivo de la base de datos no existe, se creará
#automáticamente. Luego, el script debe crear una tabla llamada clientes con las columnas id (entero, clave primaria) y nombre (texto).

import sqlite3 
conexion=sqlite3.connect("bd3.db") 
try:
 conexion.execute("""create table cliente (id integer primary key autoincrement, nombre text)""")
 print("se creo la tabla cliente")
except:
 print("La tabla cliente ya existe")
conexion.close
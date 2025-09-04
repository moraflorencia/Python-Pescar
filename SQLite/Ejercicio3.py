#Escribir un nuevo script que se conecte a la base de datos mi_base_de_datos.db, seleccione todos los registros de la tabla clientes y 
# los imprima en la consola.

import sqlite3
conexion=sqlite3.connect("bd3.db")
cursor=conexion.execute("select id, nombre from cliente")
for fila in cursor: print (fila)
conexion.close()
#Escribir un script que pida al usuario que ingrese un ID de cliente. El script debe buscar y mostrar el nombre del cliente 
#correspondiente a ese ID. Si el ID no existe, debe mostrar un mensaje de error.

import sqlite3
conexion=sqlite3.connect("bd3.db")
id=int(input("Ingrese el id de un cliente:"))
cursor=conexion.execute("select id,nombre from cliente where id=?", (id, ))
fila=cursor.fetchone()
if fila!=None: print(fila)
else: print("No existe cliente con ese id.")
conexion.close()
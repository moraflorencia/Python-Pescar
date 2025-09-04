#Crear un script que le pida al usuario un ID y un nuevo nombre. El script debe actualizar el registro con el ID proporcionado con el 
# nuevo nombre. Confirma la actualización imprimiendo un mensaje.

import sqlite3
conexion=sqlite3.connect("bd3.db")
id=int(input("Ingrese el id de un cliente:"))
cursor=conexion.execute("select id,nombre from cliente where id=?", (id, ))
fila=cursor.fetchone()
if fila!=None: print(fila)
else: print("No existe cliente con ese id.")
conexion.close()
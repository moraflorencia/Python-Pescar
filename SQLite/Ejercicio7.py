#Escribir un script que realice las siguientes tareas en orden: 
# Conectarse a la base de datos.
# Insertar un nuevo cliente llamado "Juan".
# Imprimir todos los clientes  de la tabla para la verificar la insercion.
# Actualizar el nombre de "Juan" a "Juan Perez".
# Imprimir todos los clientes nuevamente para confirmar el cambio.
# Eliminar el registro de "Juan Perez".
# Imprimir todos los clientes una ultima vez para demostrar que ha sido eleminado.

import sqlite3
conexion=sqlite3.connect("bd3.db")
try: 
    conexion.execute("INSERT INTO cliente(nombre)values(?,?)",("Juan"))
    cursor = conexion.execute("SELECT id , nombre from cliente")
    for fila in cursor :
        print(fila)
    conexion.commit()

except:
    print("La tabla cliente ya existe")
conexion.close()
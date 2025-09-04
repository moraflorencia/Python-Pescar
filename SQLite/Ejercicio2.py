#Modificar el script del problema 1 para insertar tres registros en la tabla clientes. Cada registro debe tener un nombre de cliente
#diferente

import sqlite3
conexion=sqlite3.connect("bd3.db")
conexion.execute("insert into cliente(nombre) values (?)", ("Flor",))
conexion.execute("insert into cliente(nombre) values (?)", ("Juan",))
conexion.execute("insert into cliente(nombre) values (?)", ("Rocio",))

conexion.commit()
conexion.close()
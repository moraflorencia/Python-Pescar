#Escribir un script que le pida al usuario un ID de cliente. El script debe eliminar el registro correspondiente a 
# ese ID y confirmar que la eliminación fue exitosa.
#Connecto to database 
import sqlite3
conexion=sqlite3.connect("bd3.db")
id_cliente= int(input("Ingrese un ID de cliente: "))
try:
    #Delete the register 
    cursor=conexion.execute("DELETE FROM cliente WHERE id=?" , (id_cliente,))
    conexion.commit()   
    if cursor.rowcount>0:
        print("Se elimino correctamente")
    else:
        print("Ya esta eliminado")
     

except sqlite3.Error as e:
    print("Error con la base de datos" ,e)
conexion.close()
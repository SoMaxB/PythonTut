# Importaciones
import mysql.connector

# Conexión con el servidor
conexion = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "maisicuel",
    database= "american_rider"
)

# Creación del cursor
cursor = conexion.cursor()
'''
# Crear una nueva base de datos
try:
    cursor.execute("CREATE DATABASE pruebas2;")
    print("Base de datos creada correctamente.")
except:
    print("Ha ocurrido un error al crear la base de datos, si no está creada, intentelo de nuevo.")


# Eliminar una base de datos
try:
    cursor.execute("DROP DATABASE pruebas2;")
    print("Base de datos eliminada correctamente.")
except:
    print("Ha ocurrido un error al eliminar la base de datos, si no está eliminada, intentelo de nuevo.")
'''

# Crear tablas
try:
    cursor.execute("CREATE TABLE clientes"
                   "(id INT NOT NULL AUTO_INCREMENT, "
                   "nombre VARCHAR(32) NOT NULL, "
                   "apellidos VARCHAR(64) NOT NULL, "
                   "telefono VARCHAR(9) NOT NULL, "
                   "direccion VARCHAR(256),"
                   "PRIMARY KEY (id));")
    print("La tabla se creo correctamente.")
except:
    print("Ocurrio un error al crear la tabla. Intentelo de nuevo.")
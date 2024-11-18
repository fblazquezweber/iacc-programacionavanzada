import mysql.connector
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",       
        password="15456951",   
        database="agencia",
        port=3309
    )

try:
    conexion = conectar()
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos.")
except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")
finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")
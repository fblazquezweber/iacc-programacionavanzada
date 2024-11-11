import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="15456951",
            database="AgenciasEspacialesDB",
            port=3309
        )
        return conexion
    except Error as err:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {err}")
        return None
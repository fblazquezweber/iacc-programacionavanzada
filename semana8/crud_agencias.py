from conexion_bd import conectar
from tkinter import messagebox, Toplevel, Label

def agregar_agencia(id, nombre, pais, fecha):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO AgenciaEspacial (ID, Nombre, Pais, FechaCreacion) VALUES (%s, %s, %s, %s)"
            valores = (id, nombre, pais, fecha)
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo("Éxito", "Agencia espacial agregada correctamente.")
        except Exception as err:
            messagebox.showerror("Error", f"No se pudo agregar la agencia: {err}")
        finally:
            cursor.close()
            conexion.close()

def mostrar_agencias():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT * FROM AgenciaEspacial"
            cursor.execute(sql)
            registros = cursor.fetchall()
            ventana_mostrar = Toplevel()
            ventana_mostrar.title("Agencias Espaciales")
            for index, (id, nombre, pais, fecha) in enumerate(registros):
                texto = f"ID: {id}, Nombre: {nombre}, País: {pais}, Fecha de Creación: {fecha}"
                Label(ventana_mostrar, text=texto).pack()
        except Exception as err:
            messagebox.showerror("Error", f"No se pudo recuperar las agencias: {err}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_agencia(id, nombre, pais, fecha):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "UPDATE AgenciaEspacial SET Nombre=%s, Pais=%s, FechaCreacion=%s WHERE ID=%s"
            valores = (nombre, pais, fecha, id)
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo("Éxito", "Agencia espacial actualizada correctamente.")
        except Exception as err:
            messagebox.showerror("Error", f"No se pudo actualizar la agencia: {err}")
        finally:
            cursor.close()
            conexion.close()

def borrar_agencia(id):
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas borrar esta agencia?")
    if respuesta:
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "DELETE FROM AgenciaEspacial WHERE ID=%s"
                valor = (id,)
                cursor.execute(sql, valor)
                conexion.commit()
                messagebox.showinfo("Éxito", "Agencia espacial borrada correctamente.")
            except Exception as err:
                messagebox.showerror("Error", f"No se pudo borrar la agencia: {err}")
            finally:
                cursor.close()
                conexion.close()
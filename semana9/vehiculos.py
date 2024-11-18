from conexion import conectar

def agregar_vehiculo(marca, modelo, año, combustible):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO Vehiculos (Marca, Modelo, Año, Combustible)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (marca, modelo, año, combustible))
        conexion.commit()
        return f"Vehículo {marca} {modelo} agregado con éxito."
    except Exception as e:
        return f"Error al agregar vehículo: {e}"
    finally:
        conexion.close()

def mostrar_vehiculos():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Vehiculos")
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        return f"Error al mostrar vehículos: {e}"
    finally:
        conexion.close()

def actualizar_vehiculo(id_vehiculo, campo, nuevo_valor):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = f"UPDATE Vehiculos SET {campo} = %s WHERE ID = %s"
        cursor.execute(sql, (nuevo_valor, id_vehiculo))
        conexion.commit()
        return f"Vehículo con ID {id_vehiculo} actualizado correctamente."
    except Exception as e:
        return f"Error al actualizar vehículo: {e}"
    finally:
        conexion.close()

def generar_informe_combustible(tipo_combustible):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "SELECT * FROM Vehiculos WHERE Combustible = %s"
        cursor.execute(sql, (tipo_combustible,))
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        return f"Error al generar informe: {e}"
    finally:
        conexion.close()

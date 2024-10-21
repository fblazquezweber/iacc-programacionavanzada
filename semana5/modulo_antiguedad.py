from datetime import datetime

def calcular_antiguedad(fecha_ingreso):
    fecha_actual = datetime.now()
    fecha_ingreso = datetime.strptime(fecha_ingreso, "%d-%m-%Y")
    antiguedad = fecha_actual.year - fecha_ingreso.year
    if fecha_actual.month < fecha_ingreso.month or (fecha_actual.month == fecha_ingreso.month and fecha_actual.day < fecha_ingreso.day):
        antiguedad -= 1
    return antiguedad
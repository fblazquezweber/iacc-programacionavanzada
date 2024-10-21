from modulo_registro import agregar_empleado
from modulo_antiguedad import calcular_antiguedad
from modulo_beneficios import asignar_beneficios

# Diccionario para almacenar los empleados
empleados = {}

# Agrenado empleado
nombre = "Francisco Blazquezz"
salario = 70000
fecha_ingreso = "01-08-2018"
empleados = agregar_empleado(empleados, nombre, salario, fecha_ingreso)

# Antigüedad
antiguedad = calcular_antiguedad(empleados[nombre]['fecha_ingreso'])

# Beneficios
beneficios = asignar_beneficios(antiguedad)

print(f"Empleado: {nombre}")
print(f"Salario: ${empleados[nombre]['salario']}")
print(f"Antigüedad: {antiguedad} años")
print(f"Beneficios: {beneficios}")
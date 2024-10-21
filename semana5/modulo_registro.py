def agregar_empleado(empleados, nombre, salario, fecha_ingreso):
    empleados[nombre] = {'salario': salario, 'fecha_ingreso': fecha_ingreso}
    return empleados
import tkinter as tk
from tkinter import messagebox
from crud_agencias import agregar_agencia, mostrar_agencias, actualizar_agencia, borrar_agencia

def agregar():
    id = entry_id.get()
    nombre = entry_nombre.get()
    pais = entry_pais.get()
    fecha = entry_fecha.get()
    if id and nombre and pais and fecha:
        agregar_agencia(id, nombre, pais, fecha)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def actualizar():
    id = entry_id.get()
    nombre = entry_nombre.get()
    pais = entry_pais.get()
    fecha = entry_fecha.get()
    if id and nombre and pais and fecha:
        actualizar_agencia(id, nombre, pais, fecha)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def borrar():
    id = entry_id.get()
    if id:
        borrar_agencia(id)
    else:
        messagebox.showwarning("Advertencia", "El campo ID es obligatorio.")

#ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Agencias Espaciales")

tk.Label(ventana, text="ID:").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(ventana)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="País:").grid(row=2, column=0, padx=5, pady=5)
entry_pais = tk.Entry(ventana)
entry_pais.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Fecha de Creación (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
entry_fecha = tk.Entry(ventana)
entry_fecha.grid(row=3, column=1, padx=5, pady=5)

# Botones para operaciones CRUD
tk.Button(ventana, text="Agregar", command=agregar).grid(row=4, column=0, padx=5, pady=5)
tk.Button(ventana, text="Mostrar", command=mostrar_agencias).grid(row=4, column=1, padx=5, pady=5)
tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=5, column=0, padx=5, pady=5)
tk.Button(ventana, text="Borrar", command=borrar).grid(row=5, column=1, padx=5, pady=5)

ventana.mainloop()





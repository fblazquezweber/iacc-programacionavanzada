import tkinter as tk
from tkinter import messagebox, ttk
from vehiculos import agregar_vehiculo, mostrar_vehiculos, actualizar_vehiculo, generar_informe_combustible

def agregar_vehiculo_gui():
    def guardar():
        mensaje = agregar_vehiculo(entry_marca.get(), entry_modelo.get(), int(entry_año.get()), entry_combustible.get())
        messagebox.showinfo("Resultado", mensaje)

    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Vehículo")

    tk.Label(ventana_agregar, text="Marca:").grid(row=0, column=0)
    entry_marca = tk.Entry(ventana_agregar)
    entry_marca.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Modelo:").grid(row=1, column=0)
    entry_modelo = tk.Entry(ventana_agregar)
    entry_modelo.grid(row=1, column=1)

    tk.Label(ventana_agregar, text="Año:").grid(row=2, column=0)
    entry_año = tk.Entry(ventana_agregar)
    entry_año.grid(row=2, column=1)

    tk.Label(ventana_agregar, text="Combustible:").grid(row=3, column=0)
    entry_combustible = tk.Entry(ventana_agregar)
    entry_combustible.grid(row=3, column=1)

    tk.Button(ventana_agregar, text="Guardar", command=guardar).grid(row=4, columnspan=2)

def mostrar_vehiculos_gui():
    resultados = mostrar_vehiculos()
    ventana_mostrar = tk.Toplevel()
    ventana_mostrar.title("Mostrar Vehículos")

    tree = ttk.Treeview(ventana_mostrar, columns=("ID", "Marca", "Modelo", "Año", "Combustible", "Disponible"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Marca", text="Marca")
    tree.heading("Modelo", text="Modelo")
    tree.heading("Año", text="Año")
    tree.heading("Combustible", text="Combustible")
    tree.heading("Disponible", text="Disponible")

    for vehiculo in resultados:
        tree.insert("", "end", values=vehiculo)

    tree.pack()

def generar_informe_gui():
    def generar():
        resultados = generar_informe_combustible(entry_combustible.get())
        for vehiculo in resultados:
            tree.insert("", "end", values=vehiculo)

    ventana_informe = tk.Toplevel()
    ventana_informe.title("Informe por Combustible")

    tk.Label(ventana_informe, text="Combustible:").grid(row=0, column=0)
    entry_combustible = tk.Entry(ventana_informe)
    entry_combustible.grid(row=0, column=1)

    tk.Button(ventana_informe, text="Generar", command=generar).grid(row=1, columnspan=2)

    tree = ttk.Treeview(ventana_informe, columns=("ID", "Marca", "Modelo", "Año", "Combustible", "Disponible"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Marca", text="Marca")
    tree.heading("Modelo", text="Modelo")
    tree.heading("Año", text="Año")
    tree.heading("Combustible", text="Combustible")
    tree.heading("Disponible", text="Disponible")
    tree.pack()
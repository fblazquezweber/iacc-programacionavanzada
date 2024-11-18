from tkinter import Tk, Button
from interfaz import agregar_vehiculo_gui, mostrar_vehiculos_gui, generar_informe_gui

def main():
    ventana = Tk()
    ventana.geometry('300x200')
    ventana.title("Agencia de Alquiler de Vehículos")
    boton1 = Button(ventana, padx=22, pady=10, text="Agregar Vehículo", command=agregar_vehiculo_gui)
    boton1.pack(padx=10, pady=10)
    boton2 = Button(ventana,padx=20, pady=10, text="Mostrar Vehículos", command=mostrar_vehiculos_gui)
    boton2.pack(padx=10, pady=10)
    boton3 = Button(ventana, padx=25, pady=10, text="Generar Informe", command=generar_informe_gui)
    boton3.pack(padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
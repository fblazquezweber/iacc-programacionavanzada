import tkinter as tk
from tkinter import messagebox

class CentroEventosApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("CentroEventosArenasX - Gestión de Eventos")
        self.crear_widgets()
    
    def crear_widgets(self):
        self.crear_detalles_evento()
        self.crear_categoria_tipo()
        self.crear_estado_evento()
        self.crear_numero_asistentes()
        self.crear_descripcion_evento()
        self.crear_ubicacion_evento()
        self.crear_botones_accion()
    
    def crear_detalles_evento(self):
        self.frame_detalles = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_detalles.pack(fill="x")
        
        tk.Label(self.frame_detalles, text="Nombre del evento:").grid(row=0, column=0, sticky="e")
        self.entry_nombre = tk.Entry(self.frame_detalles)
        self.entry_nombre.grid(row=0, column=1)
        
        tk.Label(self.frame_detalles, text="Organizador:").grid(row=1, column=0, sticky="e")
        self.entry_organizador = tk.Entry(self.frame_detalles)
        self.entry_organizador.grid(row=1, column=1)
        
        tk.Label(self.frame_detalles, text="Fecha del evento:").grid(row=2, column=0, sticky="e")
        self.entry_fecha = tk.Entry(self.frame_detalles)
        self.entry_fecha.grid(row=2, column=1)
    
    def crear_categoria_tipo(self):
        self.frame_categoria = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_categoria.pack(fill="x")
        
        self.categoria = tk.StringVar()
        self.categoria.set(None)
        
        tk.Label(self.frame_categoria, text="Categoría:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(self.frame_categoria, text="Cultural", variable=self.categoria, value="Cultural").grid(row=1, column=0)
        tk.Radiobutton(self.frame_categoria, text="Deportivo", variable=self.categoria, value="Deportivo").grid(row=1, column=1)
        tk.Radiobutton(self.frame_categoria, text="Social", variable=self.categoria, value="Social").grid(row=1, column=2)
        
        tk.Label(self.frame_categoria, text="Tipo de evento:").grid(row=2, column=0, sticky="w")
        self.tipos = {
            "Conferencia": tk.BooleanVar(),
            "Concierto": tk.BooleanVar(),
            "Fiesta": tk.BooleanVar(),
            "Seminario": tk.BooleanVar(),
            "Taller": tk.BooleanVar()
        }
        columna = 0
        for texto, var in self.tipos.items():
            tk.Checkbutton(self.frame_categoria, text=texto, variable=var).grid(row=3, column=columna)
            columna += 1
    
    def crear_estado_evento(self):
        self.frame_estado = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_estado.pack(fill="x")
        self.estado = tk.StringVar()
        self.estado.set(None)
        
        tk.Label(self.frame_estado, text="Estado del evento:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(self.frame_estado, text="Programado", variable=self.estado, value="Programado").grid(row=1, column=0)
        tk.Radiobutton(self.frame_estado, text="Realizado", variable=self.estado, value="Realizado").grid(row=1, column=1)
    
    def crear_numero_asistentes(self):
        self.frame_asistentes = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_asistentes.pack(fill="x")
        
        tk.Label(self.frame_asistentes, text="Número de asistentes estimados:").grid(row=0, column=0, sticky="e")
        self.entry_asistentes = tk.Entry(self.frame_asistentes)
        self.entry_asistentes.grid(row=0, column=1)
    
    def crear_descripcion_evento(self):
        self.frame_descripcion = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_descripcion.pack(fill="x")
        
        tk.Label(self.frame_descripcion, text="Descripción del evento:").pack(anchor="w")
        self.text_descripcion = tk.Text(self.frame_descripcion, height=5)
        self.text_descripcion.pack(fill="x")
    
    def crear_ubicacion_evento(self):
        self.frame_ubicacion = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_ubicacion.pack(fill="x")
        
        tk.Label(self.frame_ubicacion, text="Ubicación del evento:").grid(row=0, column=0, sticky="e")
        opciones_ubicacion = ["Salón Principal", "Área al Aire Libre", "Auditorio", "Sala de Conferencias"]
        self.ubicacion = tk.StringVar()
        self.ubicacion.set(opciones_ubicacion[0])
        tk.OptionMenu(self.frame_ubicacion, self.ubicacion, *opciones_ubicacion).grid(row=0, column=1)
    
    def crear_botones_accion(self):
        self.frame_botones = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_botones.pack()
        
        tk.Button(self.frame_botones, text="Registrar Evento", command=self.registrar_evento).grid(row=0, column=0, padx=5)
        tk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_formulario).grid(row=0, column=1, padx=5)
    
    def registrar_evento(self):
        nombre_evento = self.entry_nombre.get()
        organizador = self.entry_organizador.get()
        fecha = self.entry_fecha.get()
        categoria_seleccionada = self.categoria.get()
        tipos_seleccionados = [tipo for tipo, var in self.tipos.items() if var.get()]
        estado_evento = self.estado.get()
        numero_asistentes = self.entry_asistentes.get()
        descripcion = self.text_descripcion.get("1.0", tk.END)
        ubicacion_seleccionada = self.ubicacion.get()
        
        detalles_evento = f""" Detalles del Evento:
        Nombre del evento: {nombre_evento}
        Organizador: {organizador}
        Fecha del evento: {fecha}
        Categoría: {categoria_seleccionada}
        Tipo de evento: {', '.join(tipos_seleccionados)}
        Estado del evento: {estado_evento}
        Número de asistentes estimados: {numero_asistentes}
        Ubicación del evento: {ubicacion_seleccionada}
        Descripción del evento: {descripcion} """
        print(detalles_evento)
        messagebox.showinfo("Registro Exitoso", "El evento ha sido registrado.")
    
    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_organizador.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.categoria.set(None)
        for var in self.tipos.values():
            var.set(False)
        self.estado.set(None)
        self.entry_asistentes.delete(0, tk.END)
        self.text_descripcion.delete("1.0", tk.END)
        self.ubicacion.set("Salón Principal")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CentroEventosApp(ventana)
    ventana.mainloop()
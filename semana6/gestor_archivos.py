import json

def cargar_o_crear_archivos(archivo_proveedores, archivo_articulos):
    for archivo in [archivo_proveedores, archivo_articulos]:
        try:
            with open(archivo, "r") as f:
                json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(archivo, "w") as f:
                json.dump([], f)


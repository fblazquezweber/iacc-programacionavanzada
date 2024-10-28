import json

def agregar_articulo(archivo_articulos):
    nombre = input("Ingrese el nombre del artículo: ")
    categoria = input("Ingrese la categoría del artículo: ")
    precio = float(input("Ingrese el precio del artículo: "))
    proveedor = input("Ingrese el nombre del proveedor asociado: ")

    nuevo_articulo = {"Nombre": nombre, "Categoría": categoria, "Precio": precio, "Proveedor": proveedor}
    
    with open(archivo_articulos, "r") as f:
        articulos = json.load(f)
    articulos.append(nuevo_articulo)
    
    with open(archivo_articulos, "w") as f:
        json.dump(articulos, f, indent=2)
    
    print("Artículo agregado con éxito.")

def agregar_proveedor(archivo_proveedores):
    nombre = input("Ingrese el nombre del proveedor: ")
    ubicacion = input("Ingrese la ubicación del proveedor: ")

    nuevo_proveedor = {"Nombre": nombre, "Ubicación": ubicacion}
    
    with open(archivo_proveedores, "r") as f:
        proveedores = json.load(f)
    proveedores.append(nuevo_proveedor)
    
    with open(archivo_proveedores, "w") as f:
        json.dump(proveedores, f, indent=2)
    
    print("Proveedor agregado con éxito.")

def mostrar_informacion(archivo_articulos, archivo_proveedores):
    with open(archivo_articulos, "r") as f:
        articulos = json.load(f)
    with open(archivo_proveedores, "r") as f:
        proveedores = json.load(f)

    print("\n---- Información de Artículos ----")
    for articulo in articulos:
        print(f"Nombre: {articulo['Nombre']}, Categoría: {articulo['Categoría']}, Precio: {articulo['Precio']}, Proveedor: {articulo['Proveedor']}")
    
    print("\n---- Información de Proveedores ----")
    for proveedor in proveedores:
        print(f"Nombre: {proveedor['Nombre']}, Ubicación: {proveedor['Ubicación']}")

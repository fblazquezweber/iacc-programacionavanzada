from gestor_archivos import cargar_o_crear_archivos
from gestor_datos import agregar_articulo, agregar_proveedor, mostrar_informacion
from menu import mostrar_menu

def main():
    archivo_proveedores = "proveedores.json"
    archivo_articulos = "articulos.json"
    cargar_o_crear_archivos(archivo_proveedores, archivo_articulos)

    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == "1":
            agregar_articulo(archivo_articulos)
        elif opcion == "2":
            agregar_proveedor(archivo_proveedores)
        elif opcion == "3":
            mostrar_informacion(archivo_articulos, archivo_proveedores)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
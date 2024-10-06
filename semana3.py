class Libreria:
    def __init__(self):
        self.cantidad = 0
        self.venta = 0

    def ingresoLibros(self, cantidad):
        if cantidad < 0:
            raise ValueError("Las cantidades no pueden ser negativas")
        else:
            self.cantidad += cantidad
            return self.cantidad

    def ventaLibros(self, venta):
        if venta < 0:
            raise ValueError("Las cantidades no pueden ser negativas")
        elif venta > self.cantidad:
            raise ValueError("la cantidad vendida no puede exceder la cantidad en inventario")
        else:
            self.venta += venta
            self.cantidad -= venta
            return self.venta
        
    def resumenDiario(self):
        print(f"El total de las ventas fue de {self.venta} libros")
        print(f"Quedan un total de {self.cantidad} libros disponibles")
    
    def menu(self):
        print("\nMenú de Opciones:")
        print("1. Ingresar libros al inventario")
        print("2. Ingresar una venta")
        print("3. Resumen diario")
        print("4. Salir del programa")


def main():
    libreria = Libreria()
    while True:
        libreria.menu()
        try:
            opcion = int(input("\nSelecciona una opción (1, 2, 3 o 4): "))
        except ValueError:
            print("Error: Debes ingresar un número entero (1, 2, 3 o 4).")
            continue

        try:
            if opcion == 1:
                cantidad = int(input("Ingresa la cantidad de libros para el inventario: "))
                libreria.ingresoLibros(cantidad)
                print(f"Se han ingresado {cantidad} libros al inventario.")
            elif opcion == 2:
                venta = int(input("Ingresa la cantidad de libros vendidos: "))
                libreria.ventaLibros(venta)
                print(f"Se han vendido {venta} libros.")
            elif opcion == 3:
                 libreria.resumenDiario()
            elif opcion == 4:
                print("Saliendo del programa. ¡Gracias!")
                break
            else:
                print("Opción no válida. Por favor, selecciona entre 1, 2, 3 o 4.")      
        except ValueError as e:
            print(f"Error ValueError:{e}")
        except Exception as e:
            print(f"Error inesperado:{e}")

if __name__ == "__main__":
    main()


    

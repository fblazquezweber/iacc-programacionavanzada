import math

class Tienda:
    def __init__(self):
        self.precioBase = 40
        self.precios = {
             1:{'nombre': 'pantalon', 'precio': self.precioBase + 20.00},
             2:{'nombre': 'camisa', 'precio': self.precioBase + 10.00},
             3:{'nombre': 'zapatos', 'precio': self.precioBase + 30.00}           
             }
     
    def menuArticulosDisponibles(self):
        print("Articulos disponibles")
        for numero, articulo in self.precios.items():
            print(f"{numero}. {articulo['nombre'].capitalize()}: ${articulo['precio']:.2f}")
          
    def descuentoMayorista(self, cantidad):
        if cantidad < 10:
            return 1
        elif 10<= cantidad <=20:
            return 0.85
        else:
            return 0.75

    def totalPago(self, cantidad, precio, descuento):
        total = cantidad*precio*descuento
        return total
    # Ejemplo de uso
    pago_total = totalPago(10, 50, 0.85)

    def seleccionarArticulo(self):
        total = 0
        while True:
            self.menuArticulosDisponibles()
            try:
                seleccion = int(input("Selecciona el artículo que quieres comprar (o '0' para salir): "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if seleccion == 0:
                break
            try:
                if seleccion in self.precios:
                    articulo_seleccionado = self.precios[seleccion]
                    cantidad = int(input(f"¿Cuántos {articulo_seleccionado['nombre']}s quieres comprar?: "))
                    descuento = self.descuentoMayorista(cantidad)
                    total_pago = self.totalPago(cantidad, articulo_seleccionado['precio'], descuento)
                    total += total_pago
                    print(f"Total por {cantidad} {articulo_seleccionado['nombre']}s: ${total_pago:.2f}")
                else:
                    print("Artículo no válido.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

class Geometria:
    def areaSuperficieLateralCilindro(self):
        try:
            radio = float(input("Introduce el radio de la base del cilindro: "))
            altura = float(input("Introduce la altura del cilindro: "))
            if radio <= 0 or altura <= 0:
                print("Error: Tanto el radio como la altura deben ser mayores que 0.")
                return
            pi = math.pi
            area_lateral = 2 * pi * radio * altura
            print(f"El área lateral del cilindro es: {area_lateral:.2f} unidades cuadradas")
        except ValueError:
            print("Error: Debes ingresar valores numéricos válidos.")

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Calcular descuento por compra mayorista")
    print("2. Calcular área de la superficie lateral de un cilindro")
    print("3. Salir del programa")

def main():
    tienda = Tienda()
    geometria = Geometria()
    while True:
        mostrar_menu()

        try:
            opcion = int(input("\nSelecciona una opción (1, 2 o 3): "))
        except ValueError:
            print("Error: Debes ingresar un número entero (1, 2 o 3).")
            continue
        
        if opcion == 1:
            tienda.seleccionarArticulo()  # Llamamos directamente a la función que calcula el total en la clase
        elif opcion == 2:
            geometria.areaSuperficieLateralCilindro()  # Llamamos directamente a la función que calcula el área del cilindro
        elif opcion == 3:
            print("Saliendo del programa. ¡Gracias!")
            break
        else:
            print("Error: Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()
inventario = {}

def agregar_sabor(nombre, precio, stock):
    if nombre in inventario:
        print(f"El sabor '{nombre}' ya existe en el inventario.")
    else:
        inventario[nombre] = {'precio': precio, 'stock': stock}
        print(f"Sabor '{nombre}' agregado con éxito.")

def actualizar_sabor(nombre, precio=None, stock=None):
    if nombre in inventario:
        if precio is not None:
            inventario[nombre]['precio'] = precio
            print(f"Precio de '{nombre}' actualizado a ${precio}.")
        if stock is not None:
            inventario[nombre]['stock'] = stock
            print(f"Stock de '{nombre}' actualizado a {stock} unidades.")
    else:
        print(f"El sabor '{nombre}' no se encuentra en el inventario.")

def mostrar_inventario():
    if inventario:
        print("\nInventario actual:")
        for sabor, detalles in inventario.items():
            print(f"Sabor: {sabor}")
            print(f"  Precio: ${detalles['precio']}")
            print(f"  Stock: {detalles['stock']} unidades\n")
    else:
        print("El inventario está vacío.")

if __name__ == "__main__":
    # Agregar sabores de prueba
    agregar_sabor('Chocolate', 2.5, 100)
    agregar_sabor('Vainilla', 2.0, 80)
    agregar_sabor('Fresa', 3.0, 70)

    mostrar_inventario()
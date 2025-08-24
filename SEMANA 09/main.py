# main.py
from producto import Producto
from inventario import Inventario

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID del producto (único): ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Entrada inválida para cantidad o precio.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad_input = input("Nueva cantidad (deja vacío para no cambiar): ")
            precio_input = input("Nuevo precio (deja vacío para no cambiar): ")

            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre_busqueda = input("Nombre a buscar: ")
            resultados = inventario.buscar_productos_por_nombre(nombre_busqueda)
            if resultados:
                print(f"Productos que coinciden con '{nombre_busqueda}':")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Por favor, selecciona nuevamente.")

if __name__ == "__main__":
    menu()

import json
import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()
        if not self.productos:
            # Si no hay productos cargados, precargamos algunos productos de ejemplo
            self.precargar_productos_ejemplo()
            self.guardar_en_archivo()

    def precargar_productos_ejemplo(self):
        productos_ejemplo = [
            Producto("P001", "Lápiz", 100, 0.5),
            Producto("P002", "Cuaderno", 50, 2.0),
            Producto("P003", "Borrador", 75, 0.75),
        ]
        self.productos.extend(productos_ejemplo)
        print("Inventario inicial precargado con productos de ejemplo.")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            print(f"Archivo {self.archivo} no encontrado, se creará uno nuevo al guardar.")
            return
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.productos = [Producto.from_dict(prod) for prod in datos]
                print(f"{len(self.productos)} productos cargados desde {self.archivo}.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.archivo} está corrupto o no tiene formato JSON válido.")
        except PermissionError:
            print(f"Error: Sin permisos para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump([p.to_dict() for p in self.productos], f, ensure_ascii=False, indent=4)
            print(f"Inventario guardado exitosamente en {self.archivo}.")
        except PermissionError:
            print(f"Error: Sin permisos para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return False
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido exitosamente.")
        return True

    def eliminar_producto(self, id_producto):
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id_producto:
                del self.productos[i]
                self.guardar_en_archivo()
                print("Producto eliminado exitosamente.")
                return True
        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado exitosamente.")
                return True
        print("Producto no encontrado.")
        return False

    def buscar_productos_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("Inventario actual:")
        for producto in self.productos:
            print(producto)


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
                id_producto = input("ID del producto (único): ").strip()
                nombre = input("Nombre del producto: ").strip()
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Entrada inválida para cantidad o precio.")
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ").strip()
            cantidad_input = input("Nueva cantidad (deja vacío para no cambiar): ").strip()
            precio_input = input("Nuevo precio (deja vacío para no cambiar): ").strip()
            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre_busqueda = input("Nombre a buscar: ").strip()
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

# inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Asegura que el ID sea único
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return False
        self.productos.append(producto)
        print("Producto añadido exitosamente.")
        return True

    def eliminar_producto(self, id_producto):
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id_producto:
                del self.productos[i]
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
        for producto in self.productos:
            print(producto)

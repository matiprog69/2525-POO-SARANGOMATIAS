# tienda.py
# Sistema de ventas sencillo usando POO

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def vender(self, cliente, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.reducir_stock(cantidad):
                    total = producto.precio * cantidad
                    print(f"{cliente.nombre} compró {cantidad} x {producto.nombre}. Total: ${total}")
                else:
                    print(f"No hay suficiente stock de {producto.nombre}.")
                return
        print(f"Producto {nombre_producto} no encontrado.")

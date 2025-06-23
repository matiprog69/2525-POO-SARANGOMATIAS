# transporte.py
# Sistema de transporte sencillo con POO

class Ruta:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino


class Bus:
    def __init__(self, placa, capacidad):
        self.placa = placa
        self.capacidad = capacidad
        self.ruta = None
        self.ocupados = 0

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def subir_pasajero(self):
        if self.ocupados < self.capacidad:
            self.ocupados += 1
            return True
        return False


class Pasajero:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
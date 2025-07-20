# hotel.py
# Este programa simula un sistema de reservas de hotel utilizando POO.

class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero      # número de la habitación
        self.tipo = tipo          # tipo: sencilla, doble, suite
        self.disponible = True    # estado de la habitación

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        self.disponible = True


class Cliente:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, tipo, cliente):
        for hab in self.habitaciones:
            if hab.tipo == tipo and hab.disponible:
                hab.reservar()
                print(f"{cliente.nombre} ha reservado la habitación {hab.numero}.")
                return hab
        print(f"No hay habitaciones disponibles de tipo '{tipo}'.")
        return None
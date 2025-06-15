class ClimaDiario:
    def __init__(self):
        # Lista privada para almacenar temperaturas diarias
        self.__temperaturas = []

    def ingresar_temperatura(self, temp):
        # Método para agregar una temperatura diaria
        self.__temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        # Método para calcular el promedio de las temperaturas almacenadas
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def obtener_temperaturas(self):
        # Método para obtener la lista de temperaturas (encapsulamiento)
        return self.__temperaturas.copy()


def main():
    clima = ClimaDiario()
    print("Ingrese las temperaturas diarias para 7 días:")
    for i in range(1, 8):
        temp = float(input(f"Día {i}: "))
        clima.ingresar_temperatura(temp)

    promedio = clima.calcular_promedio_semanal()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°")


if __name__ == "__main__":
    main()
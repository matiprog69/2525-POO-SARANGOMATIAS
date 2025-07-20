# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas diarias para 7 días:")
    for i in range(1, 8):
        temp = float(input(f"Día {i}: "))
        temperaturas.append(temp)
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    # Entrada de datos
    temperaturas = ingresar_temperaturas()

    # Cálculo del promedio
    promedio_semanal = calcular_promedio(temperaturas)

    # Mostrar resultado
    print(f"\nEl promedio semanal de temperaturas es: {promedio_semanal:.2f}°")


if __name__ == "__main__":
    main()
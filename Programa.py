# Programa para calcular el área y perímetro de un rectángulo
# El usuario ingresa la base y la altura, y el programa muestra los resultados.
# Se utilizan diferentes tipos de datos: float para medidas, string para mensajes y boolean para validación.

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura


def calcular_perimetro_rectangulo(base: float, altura: float) -> float:
    """Calcula el perímetro de un rectángulo dado su base y altura."""
    return 2 * (base + altura)


def es_valido_numero(valor: str) -> bool:
    """Verifica si el valor ingresado puede convertirse a float positivo."""
    try:
        numero = float(valor)
        return numero > 0
    except ValueError:
        return False


def main():
    print("Calculadora de área y perímetro de un rectángulo")

    # Solicitar base al usuario
    base_input = input("Ingrese la base del rectángulo (número positivo): ")
    while not es_valido_numero(base_input):
        print("Error: Debe ingresar un número positivo válido.")
        base_input = input("Ingrese la base del rectángulo (número positivo): ")
    base = float(base_input)

    # Solicitar altura al usuario
    altura_input = input("Ingrese la altura del rectángulo (número positivo): ")
    while not es_valido_numero(altura_input):
        print("Error: Debe ingresar un número positivo válido.")
        altura_input = input("Ingrese la altura del rectángulo (número positivo): ")
    altura = float(altura_input)

    # Calcular área y perímetro
    area = calcular_area_rectangulo(base, altura)
    perimetro = calcular_perimetro_rectangulo(base, altura)

    # Mostrar resultados
    print(f"\nResultados para un rectángulo de base {base} y altura {altura}:")
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")


if __name__ == "__main__":
    main()

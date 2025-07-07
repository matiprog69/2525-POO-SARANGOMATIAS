# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        # Encapsulación: atributos privados
        self.__nombre = nombre
        self.__edad = edad

    # Getters para acceder a atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def sonido(self):
        return "Sonido indefinido"

    # Método para mostrar información general
    def descripcion(self):
        return f"Animal: {self.__nombre}, Edad: {self.__edad}"

# Clase derivada: Perro hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza  # atributo privado específico de Perro

    def get_raza(self):
        return self.__raza

    # Sobrescritura del método sonido (polimorfismo)
    def sonido(self):
        return "Guau"

    # Sobrescritura del método descripcion para incluir raza
    def descripcion(self):
        return f"Perro: {self.get_nombre()}, Edad: {self.get_edad()}, Raza: {self.__raza}"

# Clase derivada: Gato hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.__color = color  # atributo privado específico de Gato

    def get_color(self):
        return self.__color

    # Sobrescritura del método sonido (polimorfismo)
    def sonido(self):
        return "Miau"

    # Sobrescritura del método descripcion para incluir color
    def descripcion(self):
        return f"Gato: {self.get_nombre()}, Edad: {self.get_edad()}, Color: {self.__color}"

# Función que demuestra polimorfismo
def imprimir_sonido(animal):
    print(f"{animal.descripcion()} -> Sonido: {animal.sonido()}")

# Creación de instancias y demostración
if __name__ == "__main__":
    animal_domestico = Animal("AnimalDoméstico", 5)
    perro = Perro("Max", 3, "Labrador")
    gato = Gato("Luna", 2, "Blanco")

    # Acceso a atributos encapsulados mediante getters
    print("Accediendo a atributos encapsulados:")
    print(f"Animal: {animal_domestico.get_nombre()}, Edad: {animal_domestico.get_edad()}")
    print(f"Perro: {perro.get_nombre()}, Edad: {perro.get_edad()}, Raza: {perro.get_raza()}")
    print(f"Gato: {gato.get_nombre()}, Edad: {gato.get_edad()}, Color: {gato.get_color()}")
    print()

    # Demostración de polimorfismo con métodos sobrescritos
    print("Demostración de polimorfismo:")
    imprimir_sonido(animal_domestico)
    imprimir_sonido(perro)
    imprimir_sonido(gato)
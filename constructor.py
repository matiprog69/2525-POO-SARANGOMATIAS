class Persona:
    """
    Clase que representa a una persona con nombre y edad.
    """

    def __init__(self, nombre, edad):
        """
        Constructor: se llama automáticamente al crear un objeto Persona.
        Inicializa los atributos 'nombre' y 'edad'.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años.")

    def __del__(self):
        """
        Destructor: se llama cuando el objeto es eliminado.
        Aquí se muestra un mensaje indicando que la persona fue eliminada.
        """
        print(f"Persona eliminada: {self.nombre},{self.edad} años")

    def mostrar_informacion(self):
        """
        Metodo para mostrar la información de la persona.
        """
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años")

# Uso de la clase
def main():
    persona1 = Persona("Ana", 30)  # Constructor se ejecuta aquí
    persona1.mostrar_informacion()

    persona2 = Persona("Luis", 25)
    persona2.mostrar_informacion()

    # Eliminamos explícitamente persona1 para activar el destructor
    del persona1

if __name__ == "__main__":
    main()
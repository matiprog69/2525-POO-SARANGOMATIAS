import os

def mostrar_codigo(ruta_script):
    """
    Abre y muestra el contenido del archivo en ruta_script.
    Usa rutas absolutas para evitar errores.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Se agrega encoding='utf-8' para evitar problemas con caracteres especiales
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """
    Muestra un menú con opciones para seleccionar scripts y ver sus códigos.
    """

    ruta_base = os.path.dirname(__file__)

    # Diccionario con las rutas a los scripts usando nombres amigables para el menú
    # Puedes agregar más opciones al menú solo añadiendo más pares clave: ruta
    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 2/2.1. Clases y Objetos/Ejemplo_Clase.py',
        '3': 'UNIDAD 3/3.1. Herencia y Polimorfismo/Ejemplo_Herencia.py',
    }

    while True:
        print("\n=== Menú Principal - Dashboard ===")
        # Se usa sorted() para mostrar las opciones ordenadas
        for key, valor in sorted(opciones.items()):
            print(f"{key} - {valor}")
        print("0 - Salir")

        # Se usa strip() para limpiar espacios en blanco
        eleccion = input("\nElige un script para ver su código o '0' para salir: ").strip()

        if eleccion == '0':
            print("Saliendo del Dashboard. ¡Hasta luego!")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

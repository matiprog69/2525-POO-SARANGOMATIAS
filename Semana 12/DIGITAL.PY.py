import json
from typing import Tuple, List, Dict, Set


class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self.info: Tuple[str, str] = (titulo, autor)
        self.categoria: str = categoria
        self.isbn: str = isbn
        self.disponible: bool = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.info[0]}' por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado})"

    def to_dict(self):
        return {
            "titulo": self.info[0],
            "autor": self.info[1],
            "categoria": self.categoria,
            "isbn": self.isbn,
            "disponible": self.disponible
        }

    @staticmethod
    def from_dict(data):
        libro = Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])
        libro.disponible = data["disponible"]
        return libro


class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.libros_prestados: List[str] = []  # Guardar ISBNs para evitar problemas al serializar

    def __str__(self):
        return f"Usuario {self.nombre} (ID: {self.id_usuario})"

    def listar_libros_prestados(self, biblioteca_libros: Dict[str, Libro]):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return "\n".join(str(biblioteca_libros[isbn]) for isbn in self.libros_prestados)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": self.libros_prestados
        }

    @staticmethod
    def from_dict(data):
        usuario = Usuario(data["nombre"], data["id_usuario"])
        usuario.libros_prestados = data["libros_prestados"]
        return usuario


class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios: Dict[str, Usuario] = {}
        self.ids_usuarios: Set[str] = set()

    def anadir_libro(self, libro: Libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn: str):
        if isbn in self.libros:
            libro = self.libros[isbn]
            if libro.disponible:
                self.libros.pop(isbn)
                print(f"Libro eliminado: {libro}")
                # También eliminar de libros prestados de usuarios si hubiera inconsistencia
                for usuario in self.usuarios.values():
                    if isbn in usuario.libros_prestados:
                        usuario.libros_prestados.remove(isbn)
            else:
                print("No se puede eliminar un libro prestado.")
        else:
            print("No se encontró libro con ese ISBN.")

    def registrar_usuario(self, usuario: Usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("El ID ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario: str):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios[id_usuario]
            if not usuario.libros_prestados:
                self.usuarios.pop(id_usuario)
                self.ids_usuarios.remove(id_usuario)
                print(f"Usuario dado de baja: {usuario}")
            else:
                print("El usuario tiene libros prestados. No se puede dar de baja.")
        else:
            print("No existe usuario con ese ID.")

    def prestar_libro(self, isbn: str, id_usuario: str):
        if isbn not in self.libros:
            print("Libro no disponible en la biblioteca.")
            return
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        if not libro.disponible:
            print("El libro está actualmente prestado.")
            return
        usuario.libros_prestados.append(isbn)
        libro.disponible = False
        print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn: str, id_usuario: str):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if isbn in usuario.libros_prestados:
            usuario.libros_prestados.remove(isbn)
            self.libros[isbn].disponible = True
            print(f"Libro '{self.libros[isbn].info[0]}' devuelto por {usuario.nombre}.")
        else:
            print("El usuario no tiene ese libro prestado.")

    def buscar_libros(self, titulo: str = None, autor: str = None, categoria: str = None) -> List[Libro]:
        resultados = []
        for libro in self.libros.values():
            if titulo and titulo.lower() not in libro.info[0].lower():
                continue
            if autor and autor.lower() not in libro.info[1].lower():
                continue
            if categoria and categoria.lower() != libro.categoria.lower():
                continue
            resultados.append(libro)
        return resultados

    def listar_libros_prestados_usuario(self, id_usuario: str):
        if id_usuario not in self.ids_usuarios:
            return "Usuario no registrado."
        usuario = self.usuarios[id_usuario]
        return usuario.listar_libros_prestados(self.libros)

    def guardar_en_json(self, archivo: str):
        data = {
            "libros": [libro.to_dict() for libro in self.libros.values()],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios.values()]
        }
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {archivo}")

    def cargar_desde_json(self, archivo: str):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.libros = {lib["isbn"]: Libro.from_dict(lib) for lib in data.get("libros", [])}
            self.usuarios = {usr["id_usuario"]: Usuario.from_dict(usr) for usr in data.get("usuarios", [])}
            self.ids_usuarios = set(self.usuarios.keys())
            print(f"Datos cargados desde {archivo}")
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}. Se iniciará con datos vacíos.")


def menu():
    biblioteca = Biblioteca()
    archivo_datos = "biblioteca_digital.json"
    biblioteca.cargar_desde_json(archivo_datos)

    while True:
        print("\n----- Menú Biblioteca -----")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados a un usuario")
        print("9. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.anadir_libro(libro)
        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == "7":
            titulo = input("Buscar por título (dejar en blanco para ignorar): ")
            autor = input("Buscar por autor (dejar en blanco para ignorar): ")
            categoria = input("Buscar por categoría (dejar en blanco para ignorar): ")
            resultados = biblioteca.buscar_libros(
                titulo if titulo else None,
                autor if autor else None,
                categoria if categoria else None
            )
            print("\nLibros encontrados:")
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros que coincidan con la búsqueda.")
        elif opcion == "8":
            id_usuario = input("ID del usuario para listar libros prestados: ")
            print(biblioteca.listar_libros_prestados_usuario(id_usuario))
        elif opcion == "9":
            biblioteca.guardar_en_json(archivo_datos)
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()

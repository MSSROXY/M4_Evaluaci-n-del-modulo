class Libro:
    def __init__(self, titulo, autor, anio, estado="disponible"):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__estado = estado

    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_anio(self): return self.__anio
    def get_estado(self): return self.__estado

    def set_titulo(self, t): self.__titulo = t
    def set_autor(self, a): self.__autor = a
    def set_anio(self, an): self.__anio = an
    def set_estado(self, e): self.__estado = e

    def __str__(self):
        return (f"Libro | {self.__titulo} | {self.__autor} | "
                f"{self.__anio} | {self.__estado}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, estado="disponible"):
        super().__init__(titulo, autor, anio, estado)
        self.__formato = formato

    def get_formato(self): return self.__formato
    def set_formato(self, f): self.__formato = f

    # --- Sobrescribe __str__ ---
    def __str__(self):
        return (f"LibroDigital | {self.get_titulo()} | {self.get_autor()} | "
                f"{self.get_anio()} | {self.get_estado()} | {self.__formato}")
        

class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo
        self.libros = []
        self.cargar_libros()


    def cargar_libros(self):
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    partes = linea.strip().split(" | ")
                    tipo = partes[0]

                    if tipo == "Libro":
                        _, titulo, autor, anio, estado = partes
                        self.libros.append(Libro(titulo, autor, anio, estado))

                    elif tipo == "LibroDigital":
                        _, titulo, autor, anio, estado, formato = partes
                        self.libros.append(LibroDigital(titulo, autor, anio, formato, estado))

        except FileNotFoundError:
            pass 


    def guardar_libros(self):
        with open(self.archivo, "w") as file:
            for libro in self.libros:
                file.write(str(libro) + "\n")


    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado.")

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower():
                self.libros.remove(libro)
                print("Libro eliminado.")
                return
        print("No se encontró el libro.")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros.")
            return
        for libro in self.libros:
            print(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None


    def marcar_prestado(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.get_estado() == "prestado":
                print("El libro ya está prestado.")
            else:
                libro.set_estado("prestado")
                print("Libro marcado como prestado.")
        else:
            print("No se encontró el libro.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.get_estado() == "disponible":
                print("Este libro no estaba prestado.")
            else:
                libro.set_estado("disponible")
                print("Libro devuelto.")
        else:
            print("No se encontró el libro.")        


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Gestor de Biblioteca ---")
        print("1. Agregar libro físico")
        print("2. Agregar libro digital")
        print("3. Eliminar libro")
        print("4. Ver todos los libros")
        print("5. Buscar libro")
        print("6. Marcar libro como prestado")
        print("7. Devolver libro")
        print("8. Salir\n")

        opcion = input("Elige una opción:")

        if opcion == "1":
            t = input("Título: ")
            a = input("Autor: ")
            an = input("Año: ")
            biblioteca.agregar_libro(Libro(t, a, an))

        elif opcion == "2":
            t = input("Título: ")
            a = input("Autor: ")
            an = input("Año: ")
            f = input("Formato (PDF, ePub, etc): ")
            biblioteca.agregar_libro(LibroDigital(t, a, an, f))

        elif opcion == "3":
            titulo = input("Título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)

        elif opcion == "4":
            biblioteca.listar_libros()

        elif opcion == "5":
            titulo = input("Título del libro a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            print(libro if libro else "No encontrado.")

        elif opcion == "6":
            biblioteca.marcar_prestado(input("Título: "))

        elif opcion == "7":
            biblioteca.devolver_libro(input("Título: "))

        elif opcion == "8":
            print("Guardando cambios...")
            biblioteca.guardar_libros()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


menu()

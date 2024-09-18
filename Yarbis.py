import random

class Benchmark:
    def __init__(self):
        self.alumnos = []  # Inicialización de la lista para almacenar la matriz de notas

    def Tamaño_Matriz(self):
        # Validación para obtener el número de filas (alumnos)
        while True:
            try:
                self.filas = int(input("Define el número de filas (alumnos) de tu tabla: "))
                if self.filas <= 0:
                    raise ValueError("El número de filas debe ser positivo.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor ingresa un número entero positivo.")

        # Validación para obtener el número de columnas (materias)
        while True:
            try:
                self.columnas = int(input("Define el número de columnas (materias) de tu tabla: "))
                if self.columnas <= 0:
                    raise ValueError("El número de columnas debe ser positivo.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor ingresa un número entero positivo.")

    def Crear_Matriz(self):
        # Creación de la matriz con notas aleatorias entre 0 y 100
        self.alumnos = [[random.randint(0, 100) for _ in range(self.columnas)] for _ in range(self.filas)]
        print(f"Matriz creada con {self.filas} alumnos y {self.columnas} materias.\n")

    def Asignar_Valor(self):
        # Validación del ID del alumno (se debe ingresar un número válido y dentro del rango)
        while True:
            try:
                alumno_id = int(input(f"Nº de alumno a buscar (entre 0 y {self.filas - 1}): "))
                if alumno_id < 0 or alumno_id >= self.filas:
                    raise ValueError(f"El número de alumno debe estar entre 0 y {self.filas - 1}.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor ingresa un número válido.")

        # Validación del ID de la materia (se debe ingresar un número válido y dentro del rango)
        while True:
            try:
                materia_id = int(input(f"Nº de la materia a buscar (entre 0 y {self.columnas - 1}): "))
                if materia_id < 0 or materia_id >= self.columnas:
                    raise ValueError(f"El número de la materia debe estar entre 0 y {self.columnas - 1}.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor ingresa un número válido.")

        self.Buscar_nota(alumno_id, materia_id)

    def Buscar_nota(self, alumno_id, materia_id):
        # Muestra la nota del alumno en la materia especificada
        nota = self.alumnos[alumno_id][materia_id]
        print(f"La nota del alumno {alumno_id} en la materia {materia_id} es: {nota}")

# Ejecución del programa
key = Benchmark()
key.Tamaño_Matriz()
key.Crear_Matriz()
key.Asignar_Valor()

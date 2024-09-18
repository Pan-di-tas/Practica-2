import random

class Benchmark:
    def __init__(self):
        self.alumnos = []  

    def Tamaño_Matriz(self):
        self.filas = int(input("Define el número de filas de tu tabla: "))
        self.columnas = int(input("Define el número de columnas de tu tabla: "))

    def Crear_Matriz(self):
        self.alumnos = [[random.randint(0, 100) for _ in range(self.columnas)] for _ in range(self.filas)]

    def Asignar_Valor(self):
        alumno_id = int(input("Nº de alumno a buscar: "))  
        materia_id = int(input("Nº de la materia a buscar: "))   
        self.Buscar_nota(alumno_id, materia_id)

    def Buscar_nota(self, alumno_id, materia_id):
        nota = self.alumnos[alumno_id][materia_id]
        print(f"La nota del alumno {alumno_id} en la materia {materia_id} es: {nota}")

key = Benchmark()
key.Tamaño_Matriz()
key.Crear_Matriz()
key.Asignar_Valor()

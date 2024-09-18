yarbis:
gestiona una matriz de notas de alumnos y materias. Utiliza la clase Benchmark, que permite:

Definir el tamaño de la matriz de alumnos y materias con validaciones.
Generar una matriz con notas aleatorias entre 0 y 100.
Buscar y mostrar la nota de un alumno en una materia específica.
Componentes Principales
__init__:

Inicializa la matriz vacía de alumnos.
Tamaño_Matriz:

Solicita el número de filas (alumnos) y columnas (materias), asegurando que sean enteros positivos. Valida la entrada con bucles y manejo de errores.
Crear_Matriz:

Crea una matriz de tamaño definido, asignando notas aleatorias a cada alumno en cada materia.
Asignar_Valor:

Solicita al usuario los IDs de alumno y materia a buscar, validando que estén dentro del rango.
Buscar_nota:

Muestra la nota del alumno seleccionado en la materia especificada.
Validaciones Clave
Asegura que los tamaños de la matriz sean números positivos.
Verifica que los índices de alumno y materia estén dentro del rango válido antes de buscar la nota.
Ejemplo de Ejecución
El usuario define el número de alumnos y materias.
El programa genera una matriz con notas aleatorias.
El usuario ingresa un alumno y materia para ver la nota correspondiente.
Este programa maneja errores y asegura que los datos ingresados sean válidos para evitar fallos durante la ejecución.

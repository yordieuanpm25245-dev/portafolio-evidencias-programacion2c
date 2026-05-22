# Sistema de control de asistencia escolar

# Lista con nombres de alumnos que asistieron
alumnos = ["Juan","María","Pedro","Ana","Luis",]

# Conjunto para eliminar nombres repetidos
asistencia_unica = set(alumnos)

# Diccionario con materias favoritas
materias_favoritas = {"Juan": "Matemáticas","María": "Español","Pedro": "Historia","Ana": "Ciencias","Luis": "Educación Física"}

# Mostrar alumnos registrados
print("Lista de alumnos registrados:")
print(alumnos)

# Mostrar asistencia sin repetidos
print("\nAlumnos que asistieron (sin repetir):")
print(asistencia_unica)

# Mostrar materias favoritas
print("\nMaterias favoritas de cada alumno:")
for alumno, materia in materias_favoritas.items():
    print(alumno, "->", materia)
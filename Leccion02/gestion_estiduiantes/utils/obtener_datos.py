from models.estudiante import Estudiante
def datos_insertar():
    nombre = input('Ingresa el nombre del estudiante: ').strip()
    edad = int(input('Ingresa la edad del estudiante: '))
    carrera = input('Ingresa la carrera del estudiante: ').strip()
    return Estudiante(id_estudiante=None,nombre=nombre, edad=edad, carrera=carrera)
def actualizar_datos():
    id_estudiante = int(input('Ingresa el id del estudiante: '))
    nueva_edad = int(input('Ingresa la edad actual del estudiante: '))
    nueva_carrera = input('Ingresa la carrera del estudiante: ').strip()
    return Estudiante(id_estudiante=id_estudiante, nombre=None, edad=nueva_edad, carrera=nueva_carrera)
def obtener_id():
    return int(input('Ingrese el id_alumno del alumno: '))
def buscar_nombre():
    return input('Ingrese el nombre del estudiante: ').strip() 



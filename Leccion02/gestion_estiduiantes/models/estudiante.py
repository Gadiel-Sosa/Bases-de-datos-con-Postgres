class Estudiante:
    def __init__(self, id_estudiante: None, nombre: None, edad: None, carrera: None):
        self.id_estudiante = id_estudiante 
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    def __str__(self):
        return f'{self.id_estudiante}: {self.nombre} - {self.edad} - {self.carrera}'
    
from database.conexion import conectar
from models.estudiante import Estudiante
class GestorEstudiante:
    def insertar_estudiante(self,estudiante:Estudiante):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO estudiantes(nombre, edad, carrera) VALUES(%s, %s, %s)'
                valores = (estudiante.nombre, estudiante.edad, estudiante.carrera)
                cursor.execute(sentencia, valores)
                registros = cursor.rowcount
                print(f'Se insertó {registros} registros')
                conexion.commit()
    def actualizar_estudiante(self,estudiante:Estudiante):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'UPDATE estudiantes SET edad = %s, carrera = %s WHERE id_estudiante = %s'
                valores = (estudiante.edad, estudiante.carrera, estudiante.id_estudiante)
                cursor.execute(sentencia, valores)
                registros = cursor.rowcount
                print(f'Se actualizaron {registros} registros')
                conexion.commit()
    def buscar_estudiante(self, nombre):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM estudiantes WHERE nombre LIKE %s '
                valores = (f'%{nombre}%',)
                cursor.execute(sentencia, valores)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
    def eliminar_estudiante(self, id_estudiante):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'DELETE FROM estudiantes WHERE id_estudiante = %s'
                valores = (id_estudiante,)
                cursor.execute(sentencia, valores)
                registros = cursor.rowcount
                print(f'Se han eliminado {registros} registros')
                conexion.commit()
    def mostrar_lista_estudiantes(self):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM estudiantes'
                cursor.execute(sentencia)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
    
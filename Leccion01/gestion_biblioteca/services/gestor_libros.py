from gestion_biblioteca.Database.conexion_db import conectar
from gestion_biblioteca.models.libro import Libro
class GestorLibros:
    def insertar_libro(self, libro:Libro):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO libros(titulo, autor, anio) VALUES(%s, %s, %s)'
                valores = (libro.titulo, libro.autor, libro.anio)
                cursor.execute(sentencia, valores)
            conexion.commit()
    def actualizar_libro(self, libro:Libro):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'UPDATE libros SET titulo = %s, autor = %s, anio = %s WHERE id_libro = %s'
                valores = (libro.titulo, libro.autor, libro.anio, libro.id_libro)
                cursor.execute(sentencia, valores)
                conexion.commit()
    def listar_libros(self):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM libros'
                cursor.execute(sentencia)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
    def eliminar_libro(self, id_libro):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'DELETE FROM libros WHERE id_libro = %s'
                valores = (id_libro,)
                cursor.execute(sentencia, valores)
                conexion.commit()
    def buscar_libro(self, nombre):
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM libros WHERE titulo LIKE %s'
                valores = (f'%{nombre}%',)
                cursor.execute(sentencia, valores)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)


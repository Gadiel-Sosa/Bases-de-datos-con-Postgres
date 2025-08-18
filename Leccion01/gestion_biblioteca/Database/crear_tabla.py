from gestion_biblioteca.Database.conexion_db import conectar
def crear_tabla():
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            sentencia = '''
            CREATE TABLE libros(
                id_libro SERIAL PRIMARY KEY,
                titulo VARCHAR(100),
                autor VARCHAR(100),
                anio INTEGER
            )'''
            cursor.execute(sentencia)

# Eliminar un registro de la bd
import psycopg
with psycopg.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    dbname = 'test_db'
) as conexion:
    with conexion.cursor() as cursor:
        query = 'DELETE FROM persona WHERE id_persona = %s'
        entrada = input('Ingresa el id_persona a eliminar: ')
        valor_eliminar = (int(entrada),)
        cursor.execute(query,valor_eliminar)
        registros_eliminados = cursor.rowcount
        print(f'Registros eliminados: {registros_eliminados}')

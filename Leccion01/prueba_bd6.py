# ACTUALIZAR UN REGISTRO EN LA DB
import psycopg # type: ignore
with psycopg.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    dbname = 'test_db'
) as conexion:
    with conexion.cursor() as cursor:
        sentencia ='UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
        sentencia2 = 'SELECT * FROM persona'
        entrada = input('Ingresa los valores a modificar y el id_persona a quien se modifica los datos (nombre, apellido, email, id): ')
        
        valores = entrada.split(',')
        valores[-1] = int(valores[-1])
        valores = tuple(valores)
        cursor.execute(sentencia,valores)
        total_registros = cursor.rowcount
        print(f'Total de registros modificados: {total_registros}\n')
        cursor.execute(sentencia2)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

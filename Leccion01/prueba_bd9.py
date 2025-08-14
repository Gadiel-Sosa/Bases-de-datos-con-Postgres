# Eliminar varios registros de la bd
# Cuando de quiere eliminar varios registros que el usuario pida se usan tuplas de tuplas
# o listas de tuplas
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
        n = int(input('Cuantos registros deseas elimina: '))
        registros = []
        for i in range(n):
            entrada = input('Ingresa el id_persona a eliminar: ')
            valor_eliminar = (int(entrada),)
            registros.append(valor_eliminar)
        print(registros)
        cursor.executemany(query,registros)
        registros_eliminados = cursor.rowcount
        print(f'Registros eliminados: {registros_eliminados}')

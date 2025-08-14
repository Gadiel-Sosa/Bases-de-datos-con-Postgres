import psycopg
with psycopg.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    dbname = 'test_db'
) as conexion:
    with conexion.cursor() as cursor:
        sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
        sentencia2 = 'SELECT * FROM persona'
        entrada = input('Ingresa los valores de (nombre, apellio, email): ')
        valores = tuple(entrada.split(','))
        cursor.execute(sentencia, valores)
        cursor.execute(sentencia2)
        total_registros = cursor.rowcount
        print(f'Registros insertados: {total_registros}')
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
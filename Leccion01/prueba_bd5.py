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
        n = int(input('Cuantos registros deseas añadir: '))
        registros = []
        for i in range(n):
            entrada = input('Ingresa los valores para (nombre, apellido, email): ')
            valores = tuple(entrada.split(',')) #('nombre', 'apellido', 'email')
            registros.append(valores)
        registros = tuple(registros)
        cursor.executemany(sentencia, registros)
        total_registros = cursor.rowcount
        print(f'Total registros: {total_registros}')
        cursor.execute(sentencia2)
        regis = cursor.fetchall()
        for regi in regis:
            print(regi)

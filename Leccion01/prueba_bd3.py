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
        valores = ('Miguel', 'Carmona', 'mcarmona@gmail.com')
        cursor.execute(sentencia, valores)
        cursor.execute(sentencia2)
        registros = cursor.fetchall()
        #conexion.commit()
        registros_insertados = cursor.rowcount
        print(f'Registros insertados: {registros_insertados}\n')
        for registro in registros:
            print(registro)
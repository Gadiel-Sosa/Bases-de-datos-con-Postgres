import psycopg
with psycopg.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    dbname = 'test_db'
) as conexion:
    with conexion.cursor() as cursor:
        entrada = input('Proporciona los id\'s a buscar (ej. 1,2,3): ')
        ids = tuple(entrada.split(','))
        sentencia = f"SELECT * FROM persona WHERE id_persona IN ({', '.join(['%s'] * len(ids))})"
        print(f'sentencia: {sentencia}')
        cursor.execute(sentencia, ids)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
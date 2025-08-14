import psycopg
with psycopg.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    dbname = 'test_db'
) as conexion:
    with conexion.cursor() as cursor:
        query = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
        query2 = 'SELECT * FROM persona'
        n = int(input('Cuantos registros deseas actualizar? '))
        registros = []
        for i in range(n):
            entrada = input('Ingresa los nuevos valores para (nombre, apellido, email, id_persona a aplicar los cambios): ')
            valores = entrada.split(',').strip()
            valores[-1] = int(valores[-1])
            valores = tuple(valores)
            registros.append(valores)
        cursor.executemany(query, registros)
        total_registros = cursor.rowcount
        print(f'Total registros actiualizados: {total_registros}')
        cursor.execute(query2)
        regis = cursor.fetchall()
        for reg in regis:
            print(reg)
        
            
            

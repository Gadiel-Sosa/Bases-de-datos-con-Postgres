import psycopg as bd
conexion = bd.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    dbname = 'test_db'
)
cursor = conexion.cursor()
conexion.autocommit = False
try:
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esperanza', 'mesperanza@gmail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()
    print('Transacción completada exitosamente')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error durante la transacción: {e}')
finally:
    conexion.close()
    cursor.close()
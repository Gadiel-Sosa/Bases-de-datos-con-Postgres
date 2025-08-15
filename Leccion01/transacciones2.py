import psycopg as db
conexion = db.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    dbname = 'test_db'
)
cursor = conexion.cursor()
conexion.autocommit = False
try:
    sentencia_insert = (
        'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    )
    valores_insert = ("Rocio", "Mijares", "rmijares@mail.com")
    cursor.execute(sentencia_insert, valores_insert)
    sentencia_update = (
        'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona =%s'
    )
    valores_update = ("Juan Carlos", "Juarez", "jcjuarez@mail.com", 4)
    cursor.execute(sentencia_update, valores_update)
    conexion.commit()
    print('Transacción completada exitosamente')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error durante la transacción: {e}')
finally:
    conexion.close()
    cursor.close()

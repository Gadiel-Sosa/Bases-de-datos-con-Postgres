import psycopg as db
def conectar():
    conexion = db.connect(
        user = 'postgres',
        password = 'admin',
        host = 'localhost',
        port = '5432',
        dbname = 'test_db'
        )
    return conexion

def obtener_cursor(conexion):
    cursor = conexion.cursor()
    return cursor
    
import psycopg as db
def conectar():
    return db.connect(
        user  = 'postgres',
        password = 'admin',
        host = 'localhost',
        port = '5432',
        dbname = 'escuela'
    )
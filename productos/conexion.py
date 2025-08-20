import logging as log
import psycopg as db
class Conexion:
    _DATABASE = 'test_db'
    _PORT = '5432'
    _HOST = 'localhost'
    _USER = 'postgres'
    _PASSWORD = 'admin'
    @classmethod
    def obtener_conexion(cls):
        return db.connect(
            dbname = cls._DATABASE,
            port = cls._PORT,
            user = cls._USER,
            password = cls._PASSWORD,
            host = cls._HOST
        )

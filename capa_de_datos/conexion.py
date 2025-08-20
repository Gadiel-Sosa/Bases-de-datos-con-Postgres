import psycopg as db
from logger_base import log
class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = 'localhost'
    _PORT = '5432'

    @classmethod
    def obtener_conexion(cls):
        return db.connect(
            host = cls._HOST,
            user = cls._USERNAME,
            dbname = cls._DATABASE,
            port = cls._PORT,
            password = cls._PASSWORD
        )
if __name__ == '__main__':
    with Conexion.obtener_conexion() as conexion:
        log.debug(f'Conexión abierta exitosamente:{conexion.info.dsn}')
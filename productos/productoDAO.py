from producto import Producto
from conexion import Conexion
from logging_base import log

class ProductoDAO:
    _SELECT = 'SELECT * FROM prodducto'
    _INSERT = 'INSERT INTO prodducto(nombre, categoria, precio) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE prodducto SET nombre = %s, categoria = %s, precio = %s WHERE id_producto = %s'
    _DELETE = 'DELETE FROM prodducto WHERE id_producto = %s'

    @classmethod
    def insertar(cls, prod):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (prod.nombre, prod.categoria, prod.precio)
                cursor.execute(cls._INSERT, valores)
                log.debug(f'Producto insertado: {prod}')
                return cursor.rowcount
    @classmethod
    def actualizar(cls, prod):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (prod.nombre, prod.categoria, prod.precio, prod.id_producto)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f'Se actualizó el producto: {prod}')
                return cursor.rowcount
    @classmethod
    def eliminar(cls, id_producto):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (id_producto,)
                cursor.execute(cls._DELETE, valores)
                log.debug(f'Producto eliminado: {id_producto}')
                return cursor.rowcount
    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                productos = []
                for registro in registros:
                    producto = Producto(registro[0], registro[1], registro[2], registro[3])
                    productos.append(producto)
                return productos

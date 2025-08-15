from database.conexion_db import conectar, obtener_cursor
from utils.obetener_datos_transacciones import datos_insert, datos_update, datos_bscar, datos_eliminar
from utils.menu import menu
from utils.trasnsacciones_usuario import ejecutar_transaccion
from utils.validacion_n import pedir_cantidad

def transacciones():
    conexion = conectar()
    cursor = obtener_cursor(conexion)
    conexion.autocommit = False 

    try:
        while True:
            menu()
            try:
                opcion = int(input('Selecciona una opción del menú: '))
                if opcion < 1 or opcion > 6:
                    print('Opción no válida, elige entre 1 y 6.')
                    continue
            except Exception as e:
                print('Debes ingresar un número.')
                continue
            if opcion == 1:
                sentencia_insert = (
                    'INSERT INTO producto(nombre, precio, stock) VALUES(%s, %s, %s)'
                )
                n = pedir_cantidad('Cuántos productos deseas insertar?: ')
                total = ejecutar_transaccion(cursor, sentencia_insert, datos_insert, n)
                print(f'Se han insertado {total} registros')
                conexion.commit()
            elif opcion == 2:
                sentencia_update = (
                    'UPDATE producto SET precio = %s, stock = %s WHERE id_producto = %s'
                )
                n = pedir_cantidad('Cuántos productos deseas actualizar?: ')
                total =  ejecutar_transaccion(cursor,sentencia_update,datos_update,n)
                print(f'Se han actualizado {total} registros')
                conexion.commit()
            elif opcion == 3:
                sentencia_buscar = (
                    'SELECT * FROM producto WHERE nombre LIKE %s'
                )
                nombre_buscar = datos_bscar()
                cursor.execute(sentencia_buscar, nombre_buscar)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro) 
                
            elif opcion == 4:
                sentencia_select = (
                    'SELECT * FROM producto'
                )
                cursor.execute(sentencia_select)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
            elif opcion == 5:
                sentencia_delete = (
                    'DELETE FROM producto WHERE id_producto = %s'
                )
                n = pedir_cantidad('Cuántos productos deseas eliminar?: ')
                total = ejecutar_transaccion(cursor,sentencia_delete, datos_eliminar, n)
                print(f'Se han borrado {total} registros')
                conexion.commit()
            elif opcion == 6:
                print('Saliendo del menú...')
                break
            else:
                print('Ocurrió un error inesperado, opción inválida.')
    except Exception as e:
        conexion.rollback()
        print(f'Ocurrió un error: {e}')
    finally:
        conexion.close()
        cursor.close()

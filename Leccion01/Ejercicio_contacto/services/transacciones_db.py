from database.conexion_db import conectar, obtener_cursor
from operadorest.obtener_datos_tras import obtener_contacto_insert, obtener_contacto_update, obtener_id_eliminar

def menu():
    conexion = conectar()
    cursor = obtener_cursor(conexion)
    conexion.autocommit = False

    try:
        while True:
            print("\n--- Menú ---")
            print("1. Insertar contactos")
            print("2. Actualizar contactos")
            print("3. Eliminar contactos")
            print("4. Mostrar todos los contactos")
            print("5. Salir")

            opcion = input('Selecciona una opción: ').strip()
            if opcion == '1':
                sentenci_insertar = (
                    'INSERT INTO contacto(nombre, telefono, email) VALUES(%s, %s, %s)'
                )
                n = int(input('Cuantos registros deseas insertar?: '))
                registros = []
                for i in range(n):
                    valores = obtener_contacto_insert()
                    registros.append(valores)
                cursor.executemany(sentenci_insertar, registros)
                total_registros = cursor.rowcount
                print(f'Se han insertado {total_registros} registros')
                conexion.commit()

            elif opcion == '2':
                sentencia_update = (
                    'UPDATE contacto SET telefono = %s, email = %s WHERE id_contacto = %s'
                )
                registros = []
                n = int(input('Cuántos registros deseas actualizar?: '))
                for i in range(n):
                    valores = obtener_contacto_update()  # Debe devolver (nombre, telefono, email, id_contacto)
                    registros.append(valores)
                cursor.executemany(sentencia_update, registros)
                total_registros = cursor.rowcount
                print(f'Se han actualizado {total_registros} registros')
                conexion.commit()
            elif opcion == '3':
                sentencia_delete = (
                    'DELETE FROM contacto WHERE id_contacto = %s'
                )
                n = int(input('Cuantos registros deseas eliminas?: '))
                registros = []
                for i in range(n):
                    valores = obtener_id_eliminar()
                    registros.append((valores,))
                cursor.executemany(sentencia_delete, registros)
                total_registros = cursor.rowcount
                print(f'Se han eliminado {total_registros} registros')
                conexion.commit()
            elif opcion == '4':
                sentencia_select = (
                    'SELECT * FROM contacto'
                )
                cursor.execute(sentencia_select)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
            elif opcion == '5':
                print('Saliendo del menú')
                break
            else:
                print('Seleccione una opción válida')
    except Exception as e:
        conexion.rollback()
        print(f'Ocurrio un error: {e}')
    finally:
        conexion.close()
        cursor.close()
if __name__ == '__main__':
    menu()






from menu import menu
from obtener_datos import pedir_nuevo_producto, pedir_actualizar_producto, pedir_eliminar_producto
from productoDAO import ProductoDAO
from producto import Producto

def estructura():
    dao = ProductoDAO()

    while True:
        menu()
        try:
            opcion = int(input('Escoge una opción: '))
        except ValueError as e:
            print("Debes ingresar un número válido.")
            continue 
        if opcion == 1:
            producton = pedir_nuevo_producto()
            dao.insertar(producton)
        elif opcion == 2:
            productos = dao.seleccionar()
            for p in productos:
                print(p)
        elif opcion == 3:
            proda = pedir_actualizar_producto()
            dao.actualizar(proda)
        elif opcion == 4:
            id_eliminar= pedir_eliminar_producto()
            dao.eliminar(id_eliminar)
        elif opcion == 5:
            print('saliendo...')
            break
        else: 
            print('Opción no válida')

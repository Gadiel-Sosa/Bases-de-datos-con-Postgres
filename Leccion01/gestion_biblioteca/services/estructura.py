from gestion_biblioteca.Database.crear_tabla import crear_tabla
from gestion_biblioteca.utils.pedir_datos import datos_insert, datos_actualizar, pedir_id_libro,pedir_nombre
from gestion_biblioteca.utils.menu import menu
from gestion_biblioteca.services.gestor_libros import GestorLibros

def estructura():
    gestor = GestorLibros()
    #crear_tabla()
    while True:
        menu()
        try:
            opcion = int(input('Selecciona una opción: '))
        except Exception as e:
            print(f'Selecciona una opción válida: {e}')
        
        if opcion == 1:
            libro = datos_insert()
            gestor.insertar_libro(libro)
            print("Libro agregado exitosamente.")
        elif opcion == 2:
            gestor.listar_libros()
            
        elif opcion == 3:
            libro = datos_actualizar()
            gestor.actualizar_libro(libro)
            print("Libro actualizado exitosamente.")
        elif opcion == 4:
            id_libro =  pedir_id_libro()
            gestor.eliminar_libro(id_libro)
            print("Libro eliminado exitosamente.")
        elif opcion == 5:
            nombre = pedir_nombre()
            gestor.buscar_libro(nombre)
        elif opcion == 6:
            print('Saliendo del sistema...')
            break
        else:
            print('opción no válida')
if __name__ == '__main__':
    estructura()


        



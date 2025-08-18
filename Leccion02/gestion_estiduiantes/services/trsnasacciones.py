from models.estudiante import Estudiante
from utils.menu import menu
from utils.obtener_datos import datos_insertar, actualizar_datos, obtener_id, buscar_nombre
from database.gestor_estudiante import GestorEstudiante

def transacciones():
    gestor = GestorEstudiante()
    while True:
        menu()
        try:
            opcion = int(input('Selecciona una opción: '))
        except ValueError as e:
            print(f'Selecciona una opción válida: {e}')
        
        if opcion == 1:
            estudiante = datos_insertar()
            gestor.insertar_estudiante(estudiante)
            print('Estudiante agregado exitosamente')
        elif opcion == 2:
            gestor.mostrar_lista_estudiantes()
        elif opcion == 3:
            estudiante = actualizar_datos()
            gestor.actualizar_estudiante(estudiante)
            print('Estudiante actualizado correctamente')
        elif opcion == 4:
            nombre = buscar_nombre()
            gestor.buscar_estudiante(nombre)
        elif opcion == 5:
            id_estudiante = obtener_id()
            gestor.eliminar_estudiante(id_estudiante)
            print('Se ha eliminado al estudiante exitosamente')
        elif opcion == 6:
            print('Saliendo del menú...')
            break
        else:
            print('Ocurrió un error')
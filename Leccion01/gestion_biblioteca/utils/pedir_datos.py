from gestion_biblioteca.models.libro import Libro

def datos_insert():
    titulo = input('Ingrese el título del libro: ').strip()
    autor = input('Ingrese el autor del libro: ').strip()
    anio =  int(input('Ingrese el año de publicación: '))
    id_libro = None
    return Libro(id_libro,titulo, autor, anio)
def datos_actualizar():
    id_libro = int(input('Ingresa el Id del libro: '))
    nuevo_titulo = input('Ingresa el nuevo título del libro: ').strip()
    nuevo_autor = input('Ingresa el nuevo autor del libro: ').strip()
    nuevo_anio = int(input('Ingresa el nuevo año de publicación: '))
    return Libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_anio) 
def pedir_id_libro():
    return int(input('ID libro: '))
def pedir_nombre():
    return input('Ingresa el nombre del libro: ').strip()


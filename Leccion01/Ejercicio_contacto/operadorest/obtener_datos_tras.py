def obtener_contacto_insert():
    nombre = input('Nombre ').strip()
    telefono = input('Teléfono: ').strip()
    email = input('Email:  ').strip()
    return (nombre, telefono, email)
def obtener_contacto_update():
    id_contacto = int(input('ID del contacto a actualizar: '))
    nuevo_telefono = input('Nuevo_teléfono: ').strip()
    nuevo_email = input('Nuevo email: ').strip()
    return (nuevo_telefono, nuevo_email, id_contacto)
def obtener_id_eliminar():
    id_contacto = int(input('Id del contacto a eliminar: '))
    return (id_contacto)
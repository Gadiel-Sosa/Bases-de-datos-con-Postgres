from producto import Producto
def pedir_nuevo_producto():
    nombre = input('Ingresa el nombre del producto: ').strip()
    categoria = input('Ingresa la categpría del producto: ').strip()
    precio = float(input('Ingresa el precio del producto: '))
    return Producto(id_producto=None, nombre=nombre, categoria=categoria, precio=precio)
def pedir_actualizar_producto():
    id_producto = int(input('Ingres el Id del producto a actualizar: '))
    nombre = input('Nuevo nombre: ').strip()
    categoria = input('Nueva categoría: ').strip()
    precio = float(input('Nuevo precio: '))
    return Producto(id_producto=id_producto, nombre=nombre, categoria=categoria, precio=precio)
def pedir_eliminar_producto():
    id_producto = int(input('Ingresa el id del producto a eliminar: '))
    return id_producto

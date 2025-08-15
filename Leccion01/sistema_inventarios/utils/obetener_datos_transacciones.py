def datos_insert():
    nombre = input('Ingresa el nombre del producto: ').strip()
    precio = float(input('Ingresa el precio del producto: '))
    stock = int(input('Ingresa el stock del producto: '))
    return (nombre, precio, stock)
def datos_update():
    id_producto = int(input('Ingresa el id del producto a actualizar: '))
    nuevo_precio = float(input('Ingresa el nuevo precio para el producto: '))
    nuevo_stock = int(input('Ingresa el nuevo stock del producto: '))
    return (nuevo_precio, nuevo_stock, id_producto)
def datos_eliminar():
    id_producto = int(input('Ingresa el id_produto a eliminar: '))
    return (id_producto,)
def datos_bscar():
    nombre = input('Ingresa el nombre del producto a buscar: ').strip()
    return (f'%{nombre}%',)
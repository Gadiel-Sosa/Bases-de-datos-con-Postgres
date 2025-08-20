class Producto:
    def __init__(self, id_producto:None, nombre:None, categoria:None, precio:None):
        self._id_producto = id_producto
        self._nombre = nombre 
        self._categoria = categoria
        self._precio = precio
    def __str__(self):
        return f'''Id producto: {self._id_producto}, Nombre: {self._nombre},
        Categoría: {self._categoria}, Precio: {self._precio}'''
    @property
    def id_producto(self):
        return self._id_producto
    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property 
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio 
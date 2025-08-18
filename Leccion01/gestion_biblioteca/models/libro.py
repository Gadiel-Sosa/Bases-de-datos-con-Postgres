class Libro:
    def __init__(self, id_libro,titulo, autor, anio):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    def __str__(self):
        return f'{self.id_libro}: {self.titulo} - {self.autor} ({self.anio})'
    
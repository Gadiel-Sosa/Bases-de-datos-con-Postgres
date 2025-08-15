def pedir_cantidad(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            if n <= 0:
                print('Ingresa un número mayor que cero.')
                continue
            return n
        except ValueError:
            print('Debes ingresar un número entero válido.')

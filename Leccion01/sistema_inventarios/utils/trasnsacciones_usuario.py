def ejecutar_transaccion(cursor, sentencia, obtener_datos, cantidad):
    registros = []
    for _ in range(cantidad):
        registros.append(obtener_datos())
    cursor.executemany(sentencia, registros)
    return cursor.rowcount

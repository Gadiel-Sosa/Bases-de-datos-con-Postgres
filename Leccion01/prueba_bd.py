#import psycopg2 # type: ignore
# Esta es la forma básica de conectarse a la BD de postgresql, pero existe una mejor 
# sintaxis con el uso de with como se usó en el manejo de archivos.

#conexion = psycopg2.connect(
#    user = 'postgres',
#    password = 'admin',
#    host = '127.0.0.1',
#    port = '5432',
#    database = 'test_db'
#
#)
#cursor = conexion.cursor()
#sentencia = 'SELECT * FROM persona'
#cursor.execute(sentencia)
#registros = cursor.fetchall()
#print(registros)
#cursor.close()
#conexion.close()

# Actualmente las versiones más recientes de postgres ya no nececitan un try except
# Importamos la librería psycopg, que nos permite conectarnos y trabajar con bases de datos PostgreSQL
import psycopg 

# Abrimos una conexión a la base de datos usando un "context manager" (with)
# Esto asegura que la conexión se cierre automáticamente al salir del bloque
with psycopg.connect(
    user = 'postgres',    # Usuario de PostgreSQL
    password = 'admin',   # Contraseña del usuario
    host = 'localhost',   # Dirección del servidor de la base de datos (localhost = computadora local)
    port = '5432',        # Puerto en el que PostgreSQL escucha (por defecto 5432)
    dbname = 'test_db'    # Nombre de la base de datos a la que nos conectamos
) as conexion:
    
    # Creamos un "cursor" para ejecutar sentencias SQL en la base de datos
    # El cursor actúa como un intermediario entre el programa y la base de datos
    with conexion.cursor() as cursor:
        
        # Definimos la sentencia SQL que queremos ejecutar
        sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
        id_persona = input('Proporciona el valor id_persona: ')
        
        # Ejecutamos la sentencia usando el cursor
        cursor.execute(sentencia,(id_persona,))
        
        # fetchall() recupera **todas** las filas que resultan de la consulta
        #fetchone() regresa solo un registro
        # Devuelve una lista de tuplas, donde cada tupla representa una fila de la tabla
        registro = cursor.fetchone()
        
        # Imprimimos el resultado de la consulta
        print(registro)

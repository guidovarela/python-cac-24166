
from db import conexionMySQL


# consultas -> CRUD

# Read -> SELECT
def obtener_productos():
    # conexion
    conexion = conexionMySQL()
    # consulta db
    with conexion.cursor() as cursor:
        # Read a single record
        query = "SELECT * FROM productos ORDER BY precio"
        # query2=f"SELECT * FROM productos where id = {id}"
        cursor.execute(query)
    # procesar los resultados -> fetch
        result = cursor.fetchall()
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result
    
# Create - insert
def cargar_nuevo_producto(nombre, descripcion, precio):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, descripcion, precio))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
# Update -> 1) 
def obtener_prod_por_id(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query="SELECT * FROM productos WHERE id = %s"
        cursor.execute(query, (id))
        prod = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return prod
# update -> 2)
def actualizar_prod(nombre, descripcion, precio, id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",(nombre, descripcion, precio, id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

# borrar -> delete
def eliminar_prod(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

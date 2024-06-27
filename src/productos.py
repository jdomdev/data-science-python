# productos.py

# Función de lectura de fichero existente 'productos.txt'
# para guardarlos en diccionarios y devolverlos al flujo
def leer_fichero(file_path):
    productos = []
    with open(file_path, encoding="utf8") as f:
        for linea in f:
            id_, nombre, precio, cantidad = linea.strip().split(';')
            producto = {
                "id": int(id_),
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

# Función que recorre la lista devuelta de diccionarios y los imprime por pantalla
def mostrar_productos(productos):
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: €{producto['precio']}, Cantidad: {producto['cantidad']}")
# Función que escribe en fichero la lista de diccionarios de productos
def escribir_fichero(productos, file_path):
    with open(file_path, 'w', encoding="utf8") as f:
        for producto in productos:
            linea = f"{producto['id']};{producto['nombre']};{producto['precio']};{producto['cantidad']}\n"
            f.write(linea)

# Leer productos del fichero de entrada
productos = leer_fichero('files/productos.txt')

# Mostrar los productos por terminal
mostrar_productos(productos)

# Escribir productos en el fichero de salida
escribir_fichero(productos, 'files/productos_salida.txt')

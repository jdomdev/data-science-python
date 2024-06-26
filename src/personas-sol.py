# Importamos del módulo 'io' la función 'open'
from io import open

# Creamos una variable 'fichero' a la que le asignamos el resultado de abrir 'personas.txt'
# en modo lectura con una codificación 'utf8'
fichero = open("files/personas.txt", "r",  encoding='utf-8') 
# Creamos la variable 'lineas' a la que asignamos el resultado de aplicar a la 
# variable 'fichero' la función 'readlines()' -> lista de líneas 
lineas = fichero.readlines()
# Cerramos el flujo que da acceso al 'fichero' que hemos leido
fichero.close()

# Inicializamos una lista vacía -> 'personas'
personas = []
# Inicializamos un bucle 'for' en el que recorremos la lista de líneas(var lineas)
for linea in lineas:
    # Inicializamos la var 'campos' en donde guardamos el la lista de datos
    # generados al aplicar la función 'split()' a la var linea del bucle for.
    # Aplicamos salto de línea(\n) cuando se encuentra un espacio al final de la var linea
    campos = linea.replace("\n", "").split(";")
    # Inicializamos el diccionario 'persona' en el que vamos introduciendo, por clave,
    # los índices de la lista 'campos[]'.
    persona = {'id': campos[0], 'nombre': campos[1], 'apellido': campos[2], 'nacimiento': campos[3]}
    # Se añade el diccionario recién creado a la lista 'personas'.
    personas.append(persona)
# Recorremos la lista 'personas' para mostrar su contenido de diccionarios. 
for p in personas:
    print(f"(id={p['id']}) {p['nombre']} {p['apellido']} => {p['nacimiento']}")
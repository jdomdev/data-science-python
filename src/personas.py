# personas.py

# Definimos el nombre del archivo de entrada
filename = "files/personas.txt"

# Inicializamos una lista vacía para almacenar los diccionarios
personas = []

# Leemos el archivo y transformamos cada línea en un diccionario
with open(filename, encoding="utf8") as file:
    for line in file:
        # Eliminamos los espacios en blanco alrededor de la línea y la separamos por ";"
        datos = line.strip().split(';')
        # Creamos un diccionario con los campos correspondientes
        persona = {
            "id": int(datos[0]),
            "nombre": datos[1],
            "apellido": datos[2],
            "nacimiento": datos[3]
        }
        # Añadimos el diccionario a la lista de personas
        personas.append(persona)

# Recorremos la lista de diccionarios y mostramos sus campos de forma amigable
for persona in personas:
    print(f"ID: {persona['id']}")
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellido']}")
    print(f"Fecha de Nacimiento: {persona['nacimiento']}")
    print("-" * 20)

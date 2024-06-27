# suma.py

# Función que crea fichero en ubicación indicada 
# y escribe las sumas de a con n, teniendo n un rango desde a hasta b
def generar_suma(a, b):
    with open(f"files/suma-{a}-{b}.txt", "w", encoding="utf8") as f:
        for n in range(a, b + 1):
            resultado = a + n
            f.write(f"{a} + {n} = {resultado}\n")

# Guardamos en variables los inputs del usuario
a = int(input("Introduce un número entero entre 1 y 10 para a: "))
b = int(input("Introduce un número entero entre 1 y 10 para b: "))

# Llamamos a la función 'generar_suma()'
generar_suma(a, b)

def generar_tabla_verdad(num_bits):
    tabla_verdad = []
    for i in range(2 ** num_bits):
        fila = []
        for j in range(num_bits):
            fila.append((i // (2 ** j)) % 2)
        tabla_verdad.append(fila)
    return tabla_verdad

def obtener_ecuacion(fila):
    pass

# Pedimos la cantidad de bits
num_bits = int(input("Introduce la cantidad de bits para representar en la tabla de verdad: "))

# Generamos la tabla de verdad
tabla_verdad = generar_tabla_verdad(num_bits)

# Pedimos la salida sepa rada por comas
salida = input("Ingrese la salida de la tabla se parada por comas ").split(",")
print(salida)

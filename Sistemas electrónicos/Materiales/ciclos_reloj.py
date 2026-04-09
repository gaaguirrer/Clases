import random # Importamos la librería random para generar poder generar los voltajes aleatoriamente
import time # La librería time nos servirá para simular el paso del tiempo del ciclo de reloj

# Definir los valores mínimos y máximos de los voltajes
voltage_low_min = 0
voltage_low_max = 2.5
voltage_high_min = 2.5
voltage_high_max = 5

# Definir el número de ciclos de reloj a simular
num_clock_cycles = 100

# Generar una lista de valores aleatorios de voltaje para cada ciclo de reloj
voltage_values = []

#Generar aleatoriamente los voltajes para graficar los ciclos
for i in range(num_clock_cycles):
    voltage_values.append(random.uniform(0,5))

# Imprimir los valores de voltaje generados
# print("Valores de voltaje generados:")
# print(voltage_values)

print("\n")
# Simular los ciclos de reloj y dibujar la gráfica
for i in range(num_clock_cycles):
    # Definir el valor de voltaje para cada ciclo de reloj
    voltage = voltage_values[i]

    # Dibujar la gráfica usando "_." para representar voltaje bajo y "|" para representar voltaje alto
    if voltage_low_min <= voltage < voltage_low_max:
        print("_", end='')
    else:
        print("|", end='')

    # Esperar un segundo antes de continuar con el siguiente ciclo de reloj
    #time.sleep(1)             
print("\n")
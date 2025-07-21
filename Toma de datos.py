import serial
import matplotlib.pyplot as plt
import csv

#Estipular puerto de ESP32
puerto_serial = 'COM4'
baud_rate = 115200

# Nombre del archivo CSV y de la grafica
Nombre = input(f"Color (# de muestreo): ")
nombre_archivo_csv = f'PWM {Nombre} 60 Hz.csv'
nombre_archivo_imagen = f'PWM {Nombre} 60 Hz.png'

# Listas para almacenar las lecturas y los tiempos
lecturas = []
tiempos = []

# Conectar al puerto
try:
    ser = serial.Serial(puerto_serial, baud_rate, timeout=1)
    print(f"Conectado a {puerto_serial}")
except serial.SerialException:
    print("No es posible abrir el puerto")
    exit()

# Leer datos desde el puerto
try:
    while True:

        raw = ser.readline().decode('utf-8', errors='replace').strip()
        datos = raw.strip().split(",")
        print(f"Datos recibidos: {datos}") # Mostrar los datos recibidos

        if len(datos) == 2:
            tiempo = int(datos[0].strip())
            valor = int(datos[1].strip())
            # Agregar los valores a las listas
            lecturas.append(valor)
            tiempos.append(tiempo)
            print(f"Tiempo = {tiempo} ms  →  Intensidad = {valor}")

        # Estipular cantidad de lecturas
        if len(lecturas) >= 400:
            print("Lectura completa")
            break
    inicio = tiempos[0] + 100
    for i in range(len(tiempos)):
        tiempos[i] -= inicio
        print(f"Tiempo: {tiempos[i]} ms, Intensidad: {lecturas[i]}")

finally:
    ser.close()

if len(lecturas) > 100:
    lecturas = lecturas[100:]
    tiempos = tiempos[100:]

# Guardar los datos en un archivo CSV
try:
    with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['Tiempo (ms)', 'Intensidad Luminosa (ADC)'])
        for i in range(len(lecturas)):
            writer.writerow([tiempos[i], lecturas[i]])
    print(f"Datos guardados en '{nombre_archivo_csv}'")
except IOError:
    print(f"No se pudo guardar el archivo '{nombre_archivo_csv}'.")

# Graficar los datos
plt.figure(figsize=(10, 5))
plt.plot(tiempos, lecturas, linestyle='-', marker='o', color='green')
plt.title("Oscilaciones de luz detectadas por el fototransistor")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Intensidad luminosa")
plt.grid(True)
plt.tight_layout()

# Guardar la imagen de la gráfica
try:
    plt.savefig(nombre_archivo_imagen, dpi=300)
    print(f"Imagen guardada como '{nombre_archivo_imagen}'")
except Exception as e:
    print(f"Error al guardar la imagen: {e}")

# Mostrar la gráfica
plt.show()

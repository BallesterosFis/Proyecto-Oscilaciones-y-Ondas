import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Inicializar la lista de magnitudes
acumulado_magnitudes = np.zeros(150, dtype=float)  # Inicializar un arreglo para las magnitudes acumuladas
n_archivos = 5  # Número de archivos
Nombre = input("Color: ")

# Leer y procesar los archivos CSV
for i in range(1, n_archivos + 1):
    archivo = f'PWM {Nombre} ({i}) 60 Hz.csv'
    data = pd.read_csv(archivo)

    tiempo = data['Tiempo (ms)']
    intensidad = data['Intensidad Luminosa (ADC)']

    # Calcular la FFT de la intensidad
    fft_intensidad = np.fft.fft(intensidad)

    # Calcular las frecuencias correspondientes
    frecuencias = np.fft.fftfreq(len(tiempo), tiempo[1] - tiempo[0])

    # Solo tomar la mitad positiva de las frecuencias (por simetría)
    fft_intensidad = fft_intensidad[:len(frecuencias)//2]
    frecuencias = frecuencias[:len(frecuencias)//2]*1000

    # Magnitud de la FFT (para ver la amplitud)
    magnitud = np.abs(fft_intensidad)

    # Acumular las magnitudes de todas las iteraciones
    acumulado_magnitudes += magnitud

frecuencias = frecuencias
promedio_magnitudes = acumulado_magnitudes / n_archivos

# Graficar la FFT promedio
plt.figure(figsize=(10, 6))
plt.plot(frecuencias, promedio_magnitudes)
plt.title(f'Transformada Rápida de Fourier (FFT) {Nombre} Promediada')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)

plt.savefig(f'FFT {Nombre}.png')
plt.show()

# Guardar los resultados en un archivo CSV
resultado_fft = pd.DataFrame({
    'Frecuencia (Hz)': frecuencias,
    'Magnitud': promedio_magnitudes
})

resultado_fft.to_csv(f'FFT {Nombre}.csv', index=False)

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(Fs, Fo, amp, muestras, fase, color):
    Ts = 1.0 / Fs
    t = np.arange(0, muestras) * Ts
    sinusoidal_signal = amp * np.sin(2 * np.pi * Fo * t + fase)
    plt.plot(t, sinusoidal_signal, label=f'Frecuencia = {Fo} Hz', color=color)

# Ejemplos de uso de las funciones
Fs = 1000  # Frecuencia de muestreo en Hz
amp = 1.0  # Amplitud de la señal
muestras = 50
fase = 0  # Fase solo para la sinusoidal

# Frecuencia 0.1*Fs
Fo1 = 0.49 * Fs
color1 = 'b'  # Color para la primera señal
sinusoidal(Fs, Fo1, amp, muestras, fase, color1)

# Frecuencia 1.1*Fs
Fo2 = 0.51 * Fs
color2 = 'r'  # Color para la segunda señal
sinusoidal(Fs, Fo2, amp, muestras, fase, color2)

plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señales Sinusoidales')
plt.grid(True)
plt.legend()
plt.show()
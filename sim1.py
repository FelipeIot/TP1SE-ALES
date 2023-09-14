import numpy as np
import matplotlib.pyplot as plt

def cuadrada(Fs, Fo, amp, muestras):
    T = 1.0 / Fo
    Ts = 1.0 / Fs
    t = np.arange(0, T, Ts)
    cuadrada_signal = amp * (np.sign(np.sin(2 * np.pi * Fo * t)))
    plt.plot(t, cuadrada_signal)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Señal Cuadrada')
    plt.grid(True)
    plt.show()

def triangular(Fs, Fo, amp, muestras):
    T = 1.0 / Fo
    Ts = 1.0 / Fs
    t = np.arange(0, T, Ts)
    triangular_signal = amp * (2 * np.abs((t * Fo) - np.floor(0.5 + (t * Fo))))
    plt.plot(t, triangular_signal)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Señal Triangular')
    plt.grid(True)
    plt.show()

def sinusoidal(Fs, Fo, amp, muestras,fase):
    Ts = 1.0 / Fs
    t = np.arange(0, muestras) * Ts
    sinusoidal_signal = amp * np.sin(2 * np.pi * Fo * t+ fase)
    plt.plot(t, sinusoidal_signal)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Señal Sinusoidal')
    plt.grid(True)
    plt.show()

# Ejemplos de uso de las funciones
Fs = 1000  # Frecuencia de muestreo en Hz
Fo = 10    # Frecuencia de la señal en Hz
amp = 1.0  # Amplitud de la señal
muestras = 1000
fase=0 #fase solo para la sinusoidal  

cuadrada(Fs, Fo, amp, muestras)
triangular(Fs, Fo, amp, muestras)
sinusoidal(Fs, Fo, amp, muestras,fase)

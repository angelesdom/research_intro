import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq,ifft,fftshift
from scipy import signal
###################TIME/MOMENTUM DOMAIN########################
p0 = 2
A = np.sqrt(1/(2*p0))
t = np.linspace(-5,5,10000)
y = np.zeros_like(t)
y[(t > -2)*(t<2)] = A
sample_signal = signal.square(2 * np.pi * 5 * t)

#################Frequency/Position Domain#####################
def plot_magnitude_spectrum(signal,title,f_ratio=1):
    fft_val = fft(signal)
    magnitude_spectrum = np.abs(fft_val)
    num_frequncy_bins = int(len(t) * f_ratio)
    plt.plot(t[:num_frequncy_bins],magnitude_spectrum[:num_frequncy_bins],label = title)
    plt.show()

plot_magnitude_spectrum(sample_signal,"square wave",.01)

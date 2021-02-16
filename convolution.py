import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq,ifft,fftshift
t = np.linspace(-5,5,100)
f_cos = [np.cos(i) for i in t]
g_sin = [np.sin(i) for i in t]

plt.subplot(2,1,1)
plt.plot(t,f_cos)
plt.ylabel('height')
plt.xlabel('time(t)')
plt.plot(t,g_sin)

plt.subplot(2,1,2)
f_fft = abs(fft(f_cos))
g_fft = abs(fft(g_sin))
convolution = f_fft*g_fft
t_con = np.linspace(0,2,len(convolution))
plt.plot(t_con,convolution)
plt.title('convolution of f & g')
plt.xlabel('t')
plt.ylabel('convolution (units^2)?')
plt.show()
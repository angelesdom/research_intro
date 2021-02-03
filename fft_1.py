import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq,ifft,fftshift
###################TIME/MOMENTUM DOMAIN########################
p0 = 2
A = np.sqrt(1/(2*p0)) #Amplitude of square wave
t = np.linspace(-p0,p0,4096) 
y = np.zeros_like(t)
y[(t>-p0)*(t<p0)] =A  #ploting over one period
plt.plot(t,y,label="Momentum Function")


#################Frequency/Position Domain#####################
fft_val = fft(abs(y),axis=-1)

plt.plot(t,fft_val,label = "Computed FFT")
print(fft_val)
##############Calculated FFT by Hand########################

x = np.linspace(-p0-p0,p0*2,4096)
y = [((np.sqrt(1/(np.pi*p0)))*np.sin(p0*t))/t for t in x]


plt.plot(x,y,label = "Theoretical FFT")
plt.legend()
plt.xlim([-3,3])
plt.ylim([-1,1])
plt.title('p0 = 2')
plt.show()

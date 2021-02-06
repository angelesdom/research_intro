import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd

#Change the parameters of two sine waves, the first wave will always have a phase shift of 0, second is up to user
def pearson_cross_correlation(Amplitude,omega,phi=0):
    phi = phi*(np.pi/180)
    t = np.linspace(0,5,100)
    signal_1 = Amplitude*np.sin(omega*t)
    signal_2 = Amplitude*np.sin(omega*t - phi)
    
    #this is for me to look at my data
    signals = {'Sig1':signal_1,'Sig2':signal_2}
    data_values = pd.DataFrame(data=signals)
    data_values.to_csv('output.csv')

    #########calculate mean#########
    n = len(signal_1)
    x_bar = (1/n)*sum(signal_1)
    y_bar = (1/n)*sum(signal_2)
    ###############################

    numerator = 0
    x_denom,y_denom = 0,0

    #######for loops summations####   
    for i in range(len(signal_1)):
        numerator += ((signal_1[i]-x_bar)*(signal_2[i]-y_bar))
    for x in signal_1:
        x_denom += ((x-x_bar)**2)
    for x in signal_2:
        y_denom += ((x-y_bar)**2)
    ##############################
    r = (numerator)/((np.sqrt(x_denom))*(np.sqrt(y_denom)))
    ###########plot###############
    plt.plot(t,signal_1,label=r'$\phi$ shift 0')
    plt.plot(t,signal_2,label=r'$\phi$ shift {:.2}'.format(phi))
    plt.title(r"r = {:.2f}, $\omega$ =  {:.2f}, amplitude {:.2f}, $\phi$ = {:.2f}".format(r,omega,Amplitude,phi))
    plt.ylabel("Amplitude")
    plt.xlabel("Time (t)")
    plt.grid()
    plt.legend()
    plt.show()
    ##############################
pearson_cross_correlation(2,2,20)

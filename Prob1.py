from matplotlib import pyplot as plot
import numpy as np

def y(n):
    if n<9:
        y = n**2-7;
        return y;
    elif n>=10:
        y = (n-10)**2-7;
        return y

nrange = np.arange(0,100)
valReturnedY = [y(n) for n in nrange]
    
plot.stem(nrange,valReturnedY)
plot.show
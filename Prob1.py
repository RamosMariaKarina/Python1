from matplotlib import pyplot as plot
import numpy as np

def y(n):
    if n<9:
       a=(n**2)-7
       return a
    elif n>=10:
       a=y(n-10)
       return a
        

nrange = np.arange(0,100)
valReturnedY = [y(n) for n in nrange]
    
plot.stem(nrange,valReturnedY)
plot.show
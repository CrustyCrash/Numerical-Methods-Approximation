import scipy.integrate as integrate
import numpy as np

a = 0 
b = 1

def f(x):
    y = 2+2*x+x**2+np.sin(2*np.pi*x)+np.cos(2*np.pi*x/0.5)
    return y

print(integrate.quad(f,a,b))
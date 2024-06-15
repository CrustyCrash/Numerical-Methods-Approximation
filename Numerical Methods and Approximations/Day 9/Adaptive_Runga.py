import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -2*y

def rk4(f,t,y,h):
    # perform a single step of RK4 method

    k1 = h*f(t,y)
    k2 = h*f(t+0.5*h, y+0.5*k1)
    k3 = h*f(t+0.5*h, y+0.5*k2)
    k4 = h*f(t+h, y+k3)
    return y + k1/6 + k2/3 + k3/3 + k4/6

def adaptive_rk4(f,x0,y0,tf,h0,tol):
    #Adaptive stepsize control for RK4 method
    #tf : final time
    x = x0
    y = y0
    h = h0
    X = [x]
    ys = [y]
    while x < tf:
        y1 = rk4(f,x,y,h)
        y2 = rk4(f,x,y,h/2)
        y2 = rk4(f,x+h/2,y2,h/2)
        error = (y2 - y1)/10.0

        if error < tol:
            x += h
            y = y1
            X.append(x)
            ys.append(y)
        else:
            h *= 0.5
            return np.array(X), np.array(ys)
        
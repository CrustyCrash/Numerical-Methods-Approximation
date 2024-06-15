import numpy as np

def f(x):
    return 2 + 2*x + x**2 + np.sin(2*np.pi*x) + np.cos(2*np.pi*x/0.5)

def simpson_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    area = h/3 * (y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2]))
    
    return area

a = 0
b = 1.5
n = 10000  # number of intervals (must be even)

area = simpson_rule(a, b, n)

print("Approximated area under the curve is: ", area)
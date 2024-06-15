import numpy as np

def f(x):
    return 2 + 2*x + x**2 + np.sin(2*np.pi*x) + np.cos(2*np.pi*x/0.5)

a = 0
b = 1.5
n = 10000  # number of intervals

h = (b-a)/n
x = np.linspace(a, b, n+1)
y = f(x)

area = h/2 * (y[0] + y[-1] + 2 * sum(y[1:-1]))

print("Approximated area under the curve is: ", area)


from scipy.integrate import quad

def f(x):
    return 2 + 2*x + x**2 + np.sin(2*np.pi*x) + np.cos(2*np.pi*x/0.5)

a = 0
b = 1.5

exact_area, _ = quad(f, a, b)

print("Exact area under the curve is: ", exact_area)
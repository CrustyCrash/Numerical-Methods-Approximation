def f(x,y,h):
    return y + h*(x**3 + y)

h = 0.02
x = 0
y = 1

while x <= 0.12:
    k1 = f(x,y,h)
    print("X = ", x, "Y = ", k1 )
    x = x + h
    y = k1

    ## x**2 + y**2 y(x) = 1, h = 0.1
from math import cos, sin


def f(x):
    z = sin(x * 5) + cos(x * 2)
    return z


def bisection(a, b):
    print("Checking the roots of the equations")
    for i in range(0, 35):
        if f(a)*f(b) < 0:
            xi = (a + b) / 2
            if round(f(xi), 4) == 0:
                print("Roots of given equation is ", xi)
                break
            elif f(xi) * f(a) < 0:
                print("Shifting value of b")
                b = xi
            elif f(xi) * f(b) < 0:
                print("Shifting value of a")
                a = xi
        else:
            print("Roots does not exist between a=", a, "b=", b)
            break


bisection(-0.6, -0.5)
bisection(-0.3, -0.2)
bisection(0.1, 0.9)

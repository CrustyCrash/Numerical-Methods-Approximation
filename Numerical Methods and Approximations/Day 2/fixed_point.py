from math import cos


def f(x):
    return cos(x)


def fixedPoint(x):
    for i in range(0, 25):
        res = f(x)
        error = res - x
        if abs(error) < 0.001:
            break
        print(i, "x = ", x, "cos(x) = ", res, "error = ", error)
        x = res


fixedPoint(0.1)

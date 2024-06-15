# f(x,y) = x^2 + y^2
def f(x,y):
    return x**2 + y**2

# a and b are chosen to keep x and y constant
# since for every value of k, x and y are constant
x = 0
y = 2
a = 0
b = 2
h = 0.1
# store the values of k
res = []

# for the first value of k no variation needs to be done for x and y
# for 2nd and third value, x + h/2, y + k/2
for i in range(0,3):
    k = h*f(a,b)
    a = x + h/2
    b = y + k/2
    res.append(k)

k = h * f(x+h, y+res[-1])
res.append(k)

res[1] = 2* res[1]
res[2] = 2* res[2]

res = sum(res)
res = 2 + res/6 
print(res)
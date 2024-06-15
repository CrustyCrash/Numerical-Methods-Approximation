import matplotlib.pyplot as plt
def f(C):
    return C

C = 3

x_new = []
y_new = []

for x in range(-50,50):
    y = C
    x_new.append(x)
    y_new.append(y)


plt.plot(x_new, y_new)


plt.title('Graph of given function is y = C')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
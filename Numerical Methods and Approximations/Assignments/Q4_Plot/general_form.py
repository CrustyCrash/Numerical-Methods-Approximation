import matplotlib.pyplot as plt

x_new = []
y_new = []

for x in range(-50 , 50):
    y = 6 - 2*x / 3
    x_new.append(x)
    y_new.append(y)

plt.plot(x_new, y_new)

plt.title('Graph for y = 6 - 2*x /3')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
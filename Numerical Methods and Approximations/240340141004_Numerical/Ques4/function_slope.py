import matplotlib.pyplot as plt
def f(x,C):
    return x+ C

C = 3

x_new = []
y_new = []

for x in range(-100 , 100):
    y = x + C
    x_new.append(x)
    y_new.append(y)
    
plt.plot(x_new, y_new)

plt.title('Graph of the  equaton y = x + C')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
    
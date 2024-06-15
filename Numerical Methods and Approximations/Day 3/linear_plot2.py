import matplotlib.pyplot as plt
x = []
y = []
a = 0
for i in range (-50, 50):
    x.append(i*0.5)
    y.append(6*(x[a]-2) + 3)
    a += 1
    plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
x = []
y = []
for i in range (-50, 50):
    x.append(i*0.22)
    y.append(30 - 2 * i**2) 
    plt.plot(x, y)
plt.show()

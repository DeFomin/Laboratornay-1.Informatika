import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 50)
y = -(x-50)**2 + 2500
plt.plot(x,y)

x_1 = np.linspace(0, 100, 50)
y_1 = -(x_1-50)**2 + 2200
plt.plot(x_1, y_1)

x_2 = np.linspace(0, 100, 50)
y_2 = -(x_2-50)**2 + 1900
plt.plot(x_2, y_2)

x_3 = np.linspace(0, 100, 50)
y_3 = -(x_3-50)**2 + 1600
plt.plot(x_3, y_3)

x_4 = np.linspace(0, 100, 50)
y_4 = -(x_4-50)**2 + 1300
plt.plot(x_4, y_4)

x_5 = np.linspace(0, 100, 50)
y_5 = -(x_5-50)**2 + 1000
plt.plot(x_5, y_5)

x_6 = np.linspace(0, 100, 50)
y_6 = -(x_6-50)**2 + 700
plt.plot(x_6, y_6)

plt.fill_between(x, y, color='red')
plt.fill_between(x_1, y_1, color='orange')
plt.fill_between(x_2, y_2, color='green')
plt.fill_between(x_3, y_3, color='blue')
plt.fill_between(x_4, y_4, color='purple')
plt.fill_between(x_5, y_5, color='pink')
plt.fill_between(x_6, y_6, color='white')

plt.ylim(0, 2500)
plt.show()

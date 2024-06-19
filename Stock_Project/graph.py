# adding graphing to the project
import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4]
y_axis = [9000, 1075, 11223, 11223]
y_axis1 = [6730, 1424, 23456, 10293]
plt.plot(x_axis, y_axis, y_axis1)
plt.title("Stock Price over time")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()

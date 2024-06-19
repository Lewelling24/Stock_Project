# adding graphing to the project
import matplotlib.pyplot as plt

x_axis = [1, 2, 3]
y_axis = [9000, 1075, 11223]
y_axis1 = [9000, 1075, 11223]
plt.plot(x_axis, y_axis, y_axis1)
plt.title("Stock Price over time")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()

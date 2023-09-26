# importing the modules
import numpy as np
import matplotlib.pyplot as plt
 
# data to be plotted
x = np.array([1,2,6])
y = np.array([3,10,12])
 
# plotting
plt.title("Line diagram")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y, color ="red",marker="o")
plt.show()

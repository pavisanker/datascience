# importing the modules
import numpy as np
import matplotlib.pyplot as plt
 
# data to be plotted
x = np.array([1,2,3,4])
y = np.array([10,20,30,40])
 
# plotting
plt.title("Line diagram")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y, color ="red",linestyle="dotted",marker="o",mfc="green")
plt.grid()
plt.show()

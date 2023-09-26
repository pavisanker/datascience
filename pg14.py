# importing the modules
import numpy as np
import matplotlib.pyplot as plt
 
# data to be plotted
x = np.array([1,3,6,18])
y = np.array([6,8,12,20])
 
# plotting
plt.title("Line diagram")
plt.xlabel("x axis ")
plt.ylabel("y axis")
plt.plot(x, y, color ="red",linestyle="dotted",marker="o",mfc="green",mec="green")
plt.show()

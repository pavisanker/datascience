# importing the modules
import numpy as np
import matplotlib.pyplot as plt
 
# data to be plotted
x = np.array([1,2,6,8])
y = np.array([3,0,2,20])
 
# plotting
plt.title("Line Diagram")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y, color ="green")
plt.show()

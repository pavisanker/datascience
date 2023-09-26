# importing the modules
import numpy as np
import matplotlib.pyplot as plt
 
# data to be plotted
x = np.array([12,14,16,18,20])
y = np.array([100,200,250,400,300])
 
# plotting
plt.title("Score/Person")
plt.xlabel("Person")
plt.ylabel("Score")
plt.plot(x, y, color ="red")
plt.show()

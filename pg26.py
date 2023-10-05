import matplotlib.pyplot as plt
import numpy as np
 
x=np.array([5,7,8,6,2,17])
y=np.array([99,86,87,76,64,51])

z = np.array([1,2,3,4,5,6])
colors = np.random.rand(6) 

plt.scatter(x, y, s=z*100,c=colors)
plt.show()


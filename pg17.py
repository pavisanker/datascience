import numpy as np
import matplotlib.pyplot as plt
 
x = np.array([1,2,3,4])
y = np.array([10,20,30,40])

a=np.array([2,6,8])
b=np.array([5,8,10])

plt.plot(x, y, color ="red",label="Line 1")
plt.plot(a,b,color="green",label="Line 2")
plt.plot(x, np.sin(x), label = "curve 1")
plt.plot(a, np.cos(a), label = "curve 2")
plt.legend()
plt.show()

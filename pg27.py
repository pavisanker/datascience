import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data_1 = np.random.normal(100, 20, 200)
data_2 = np.random.normal(80, 30, 200)
data = [data_1, data_2]

fig = plt.figure(figsize =(10, 7))

plt.boxplot(data)

plt.show()

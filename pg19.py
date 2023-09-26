import numpy as np
import matplotlib.pyplot as plt

data = {'Java':22.2, 'Python':17, 'PHP':8.8,'C++':6.5}
courses = list(data.keys())
values = list(data.values())

plt.bar(courses, values, color ='red',width = 0.4)

plt.xlabel("Programming Language")
plt.ylabel("Popularity")
plt.title("Language vs Polpularity")
plt.show()


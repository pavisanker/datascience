import numpy as np
import matplotlib.pyplot as plt
 
data = {'Maths':30, 'Physics':40, 'Chemistry':15,'Biology':25}
courses = list(data.keys())
values = list(data.values())

plt.bar(courses, values, color ='maroon',width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

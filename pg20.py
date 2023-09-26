import matplotlib.pyplot as plt

y=['Java','Python','PHP','C++']
 
x=[22.2,17,8.8,6.5]
plt.barh(y, x)

plt.ylabel("pen sold")

plt.xlabel("price")
plt.title("Horizontal bar graph")
plt.show()

import numpy as np
print("Enter matrix elements:")
x=input("Enter x = ")
y=input("Enter y = ")
a=input("Enter a = ")
b=input("Enter b = ")

n_array = np.array([[int (x),int (y)], [int (a),int (b)]])
print("Matrix is:")
print(n_array)
  
tra = n_array.transpose()
  
print("\nTranspose of given 2X2 matrix:")
print(tra)

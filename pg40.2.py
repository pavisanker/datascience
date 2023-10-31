import numpy as np
import pandas as pv
import csv

dataset=pv.read_csv("data_salary.csv")

x=dataset.iloc[:-1 ,:].values

print(dataset)
print(dataset.shape)
print(dataset.head(5))
print(dataset.tail())
print(x)


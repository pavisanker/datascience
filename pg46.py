
import pandas as pd
import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
dataset=pd.read_csv("data_study_mark.csv")
x=dataset.iloc[:,:-1].values

y=dataset.iloc[:,-1].values


model=LinearRegression()
model.fit(x,y)


Age=int(input("Enter the age :"))
Hours=int(input("Enter the study hours :"))
Internet=int(input("Enter the hours of internet usage :"))

Marks=[[Age,Hours,Internet]]
result=model.predict(Marks)
predicted_marks = min(result[0], 100)

print("Predicted marks:", predicted_marks)

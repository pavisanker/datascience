import numpy as np    
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('data_area_price.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values 


regressor = LinearRegression()
regressor.fit(x, y)

area =float(input("Enter area:")) 

price=[[area]]
predicted_price = regressor.predict(price)

intercept = regressor.intercept_
coefficients = regressor.coef_

print("Predicted price:", predicted_price)
print("Intercept:", intercept)
print("Coefficients:", coefficients)





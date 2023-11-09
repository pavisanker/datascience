import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv('data_height.csv')
print(dataset.shape)
print(dataset.head(5))
x = dataset[['Age', 'Weight']].values
y = dataset['Height'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)


print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))

Age=int(input("Enter age :"))
Weight=int(input("Enter the weight :"))
Height=[[Age,Weight]]
result=clf.predict(Height)
print(result)



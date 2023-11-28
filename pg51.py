from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC

iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

model = SVC(kernel='linear', random_state=0)  
model.fit(x_train, y_train)  
y_pred = model.predict(x_test)  

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

SL = float(input("Enter the sepal length: "))
SW = float(input("Enter the sepal width: "))
PL = float(input("Enter the petal length: "))
PW = float(input("Enter the petal width: "))

sample = [[SL, SW, PL, PW]]

pred = model.predict(sample)
pred_v = [iris.target_names[p] for p in pred]
print(pred_v)


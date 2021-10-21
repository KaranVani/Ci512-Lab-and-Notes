from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
np.random.seed(55)


## This reads all the data from our iris.data file, which consists of 4 features (numbers) 1 label (what type of plant)
data = pd.read_csv("iris.data", skiprows=0)
print(data)

## this specifies how many neighbors you will use for your testing
clf = KNeighborsClassifier(n_neighbors=1)

## Columns 1-4 are features and column 5 is a label

## X is taking ALL data from the rows, and columns 0-3 (1,2,3,4)
X = data.values[:, 0:3]
Y = data.values[:,4]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4)
print(X_train)
print('Test')
print(X_test)
clf = clf.fit(X_train, Y_train)
Y_prediction = clf.predict(X_test)
print("Test data")
print(X_test)
print("This is my prediction for 20% test data")
print(Y_prediction)
print("This is the true/actual labels")
print(Y_test)
print("Train/test accuracy:",accuracy_score(Y_test,Y_prediction))

############# Cross validation

from sklearn.model_selection import ShuffleSplit
cv = ShuffleSplit(n_splits=5, test_size=0.4)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(clf, X, Y, cv=cv)
print()
print("Cross fold validation accuracy scores:",scores)
print("Cross fold validation accuracy mean:",scores.mean())

print('My Prediction')
print(Y_prediction)
print('True Lable')
print(Y_test)
precision = precision_score(Y_test, Y_prediction, average="macro")
print(precision)
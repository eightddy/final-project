import sys
#import matplotlib.pyplot as plt
import itertools
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('train/train.csv')
X = dataset.iloc[:, 0:1573].values
# print "X: ", X.shape, X
y = dataset.iloc[:, 1573:1574].values
# print "y: ", y.shape, y
y = y.reshape(y.shape[0],)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X, y, random_state = 42, test_size=0.4)
from sklearn.metrics import classification_report, confusion_matrix
# import the KNeighborsClassifer class from sklearn
from sklearn.neighbors import KNeighborsClassifier
# import metrics model to check the accuracy
from sklearn import metrics
# import SVM
from sklearn.svm import SVC
# import the Naive_Bayes class from sklearn
from sklearn.naive_bayes import GaussianNB
# import the RandomForest
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

from sklearn.linear_model import LogisticRegression

def classifier(classType):
    if (classType == "SVM"):
        clf = SVC(gamma='auto', verbose=True)
    elif (classType == "KNN"):
        clf = KNeighborsClassifier(n_neighbors = 10, weights = 'distance')
    elif (classType == "DT"):
        clf = tree.DecisionTreeClassifier()
    elif (classType == "NB"):
        clf = GaussianNB()
    h = clf.fit(train_x, train_y)
    print h

    pred = clf.predict(test_x)

    print("Val Score: ", clf.score(test_x, test_y))
    print classification_report(test_y, pred)
    print confusion_matrix(test_y, pred)

# classifier("KNN")
# classifier("SVM")
# sys.exit()

# -----------------------------------------------------------------------------------------------------
# KNN
clf = KNeighborsClassifier(n_neighbors = 10, weights = 'distance')
h = clf.fit(train_x, train_y)
print h
pred = clf.predict(test_x)
print("Val Score: ", clf.score(test_x, test_y))
print classification_report(test_y, pred)
print test_y, pred
# sys.exit()
print confusion_matrix(test_y, pred)

# -----------------------------------------------------------------------------------------------------
# Naive Bayes
clf = GaussianNB()
h = clf.fit(train_x, train_y)
print h
pred = clf.predict(test_x)
print("Val Score: ", clf.score(test_x, test_y))
print classification_report(test_y, pred)
print confusion_matrix(test_y, pred)

# -----------------------------------------------------------------------------------------------------
# SVM
clf = SVC(gamma='auto')
h = clf.fit(train_x, train_y)
print h
pred = clf.predict(test_x)
print("Val Score: ", clf.score(test_x, test_y))
print classification_report(test_y, pred)
print confusion_matrix(test_y, pred)
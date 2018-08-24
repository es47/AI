# -*- coding: cp950 -*-
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import os
import sys

# 讀入資料

pathProg = 'C:\Users\user\Downloads'
os.chdir(pathProg)

if os.getcwd() != pathProg:
    print "EEROR: the file path incorrect."
    sys.exit()

file = pd.read_csv(pathProg + '\TraData.csv',sep= ',', header= None)

X = file.values[1:, 0:11]
print X
Y = file.values[1:,12]
print Y

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

clf_gini.predict([[4, 4, 3, 3]])

y_pred = clf_gini.predict(X_test)
print y_pred

print "Accuracy is ", accuracy_score(y_test,y_pred)*100

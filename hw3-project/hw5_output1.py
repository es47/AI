import numpy as np
import pandas as pd
import csv
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

df = pd.read_csv('TraData.csv')

X = df.loc[:,['adx','spaceType','spaceId','spaceCat','adType','ip','os','deviceType','publisherId','dclkVerticals','campaignId','advertiserId']]
y = df.click

labelencoder = LabelEncoder()
X.adx = labelencoder.fit_transform(X.adx)
X.spaceType = labelencoder.fit_transform(X.spaceType)
X.spaceId = labelencoder.fit_transform(X.spaceId)
X.spaceCat = labelencoder.fit_transform(X.spaceCat)
X.adType = labelencoder.fit_transform(X.adType)
X.ip = labelencoder.fit_transform(X.ip)
X.os = labelencoder.fit_transform(X.os)
X.deviceType = labelencoder.fit_transform(X.deviceType)
X.publisherId = labelencoder.fit_transform(X.publisherId)
X.dclkVerticals = labelencoder.fit_transform(X.dclkVerticals)
X.campaignId = labelencoder.fit_transform(X.campaignId)
X.advertiserId = labelencoder.fit_transform(X.advertiserId)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
fmeasure = 2*(precision*recall/(precision+recall))

print"accuracy score  = ",accuracy
print"precision score = ",precision
print"recall score    = ",recall
print"fmeasure score  = ",fmeasure

df = pd.read_csv('input.csv')

X = df.loc[:,['adx','spaceType','spaceId','spaceCat','adType','ip','os','deviceType','publisherId','dclkVerticals','campaignId','advertiserId']]

labelencoder = LabelEncoder()
X.adx = labelencoder.fit_transform(X.adx)
X.spaceType = labelencoder.fit_transform(X.spaceType)
X.spaceId = labelencoder.fit_transform(X.spaceId)
X.spaceCat = labelencoder.fit_transform(X.spaceCat)
X.adType = labelencoder.fit_transform(X.adType)
X.ip = labelencoder.fit_transform(X.ip)
X.os = labelencoder.fit_transform(X.os)
X.deviceType = labelencoder.fit_transform(X.deviceType)
X.publisherId = labelencoder.fit_transform(X.publisherId)
X.dclkVerticals = labelencoder.fit_transform(X.dclkVerticals)
X.campaignId = labelencoder.fit_transform(X.campaignId)
X.advertiserId = labelencoder.fit_transform(X.advertiserId)

y_pred = clf.predict(X)

save = pd.DataFrame(y_pred)  
save.to_csv('output3.csv', index=False)  


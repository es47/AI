# -*- coding: cp950 -*-
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import preprocessing
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

# 讀入資料

ad = pd.read_csv('TraData.csv', usecols=[0])
ad = np.asarray(ad)
st = pd.read_csv('TraData.csv', usecols=[1])
st = np.asarray(st)
sid = pd.read_csv('TraData.csv', usecols=[2])
sid = np.asarray(sid)
sc = pd.read_csv('TraData.csv', usecols=[3])
sc = np.asarray(sc)
at = pd.read_csv('TraData.csv', usecols=[4])
at = np.asarray(at)
ip = pd.read_csv('TraData.csv', usecols=[5])
ip = np.asarray(ip)
os = pd.read_csv('TraData.csv', usecols=[6])
os = np.asarray(os)
dt = pd.read_csv('TraData.csv', usecols=[7])
dt = np.asarray(dt)
pid = pd.read_csv('TraData.csv', usecols=[8])
pid = np.asarray(pid)
dv = pd.read_csv('TraData.csv', usecols=[9], dtype = {"dclkVerticals": str})
dv = np.asarray(dv)
cid = pd.read_csv('TraData.csv', usecols=[10])
cid = np.asarray(cid)
aid = pd.read_csv('TraData.csv', usecols=[11])
aid = np.asarray(aid)
cl = pd.read_csv('TraData.csv', usecols=[12], dtype = {"click": int})
cl = np.asarray(cl)

number = preprocessing.LabelEncoder()

ad = number.fit_transform(ad)
ad = np.nan_to_num(ad)
st = number.fit_transform(st)
st = np.nan_to_num(st)
sid = number.fit_transform(sid)
sid = np.nan_to_num(sid)
sc = number.fit_transform(sc)
sc = np.nan_to_num(sc)
at = number.fit_transform(at)
at = np.nan_to_num(at)
ip = number.fit_transform(ip)
ip = np.nan_to_num(ip)
os = number.fit_transform(os)
os = np.nan_to_num(os)
dt = number.fit_transform(dt)
dt = np.nan_to_num(dt)
pid = number.fit_transform(pid)
pid = np.nan_to_num(pid)
dv = number.fit_transform(dv)
dv = np.nan_to_num(dv)
cid = number.fit_transform(cid)
cid = np.nan_to_num(cid)
aid = number.fit_transform(aid)
aid = np.nan_to_num(aid)
cl = number.fit_transform(cl)
cl = np.nan_to_num(cl)

ad = ad[:, np.newaxis]
st = st[:, np.newaxis]
sid = sid[:, np.newaxis]
sc = sc[:, np.newaxis]
at = at[:, np.newaxis]
ip = ip[:, np.newaxis]
os = os[:, np.newaxis]
dt = dt[:, np.newaxis]
pid = pid[:, np.newaxis]
dv = dv[:, np.newaxis]
cid = cid[:, np.newaxis]
aid = aid[:, np.newaxis]
cl = cl[:, np.newaxis]

data = np.hstack((ad, st, sid, sc, at, ip, os, dt, pid, dv, cid, aid))
target = cl.astype('int')

# 切分訓練與測試資料
train_X, test_X, train_y, test_y = train_test_split(data, target, train_size = 0.1, random_state = 42)

# 建立分類器
clf = tree.DecisionTreeClassifier(random_state = 42)
data_clf = clf.fit(train_X, train_y)

# 預測
test_y_predicted = data_clf.predict(test_X)

# 績效
accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print "accuracy : ", accuracy
precision = metrics.precision_score(test_y, test_y_predicted, average='macro')
print "precision : ", precision
recall = metrics.recall_score(test_y, test_y_predicted, average='macro')
print "recall : ", recall
f_measure = 2 * (precision * recall / (precision + recall))
print "f_measure : ", f_measure

output = {'click' : test_y_predicted}
output = DataFrame(output)
output.to_csv('output.csv', sep=',', index = 0)

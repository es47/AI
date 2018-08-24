import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

ADdata = pd.read_csv('TraData.csv', sep= ',', header= 0)
Testdata = pd.read_csv('input.csv', sep= ',', header= 0)

le_0 = preprocessing.LabelEncoder()
le_1 = preprocessing.LabelEncoder()
le_2 = preprocessing.LabelEncoder()
le_3 = preprocessing.LabelEncoder()
le_4 = preprocessing.LabelEncoder()
le_5 = preprocessing.LabelEncoder()
le_6 = preprocessing.LabelEncoder()
le_7 = preprocessing.LabelEncoder()
le_8 = preprocessing.LabelEncoder()
le_9 = preprocessing.LabelEncoder()

adtmp = pd.concat([ADdata['adx'],Testdata['adx']],axis=0)
sttmp = pd.concat([ADdata['spaceType'],Testdata['spaceType']],axis=0)
sitmp = pd.concat([ADdata['spaceId'],Testdata['spaceId']],axis=0)
sctmp = pd.concat([ADdata['spaceCat'],Testdata['spaceCat']],axis=0)
attmp = pd.concat([ADdata['adType'],Testdata['adType']],axis=0)
iptmp = pd.concat([ADdata['ip'],Testdata['ip']],axis=0)
ostmp = pd.concat([ADdata['os'],Testdata['os']],axis=0)
dttmp = pd.concat([ADdata['deviceType'],Testdata['deviceType']],axis=0)
pitmp = pd.concat([ADdata['publisherId'],Testdata['publisherId']],axis=0)
dvtmp = pd.concat([ADdata['dclkVerticals'],Testdata['dclkVerticals']],axis=0)

le_0.fit(adtmp)
le_1.fit(sttmp)
le_2.fit(sitmp)
le_3.fit(sctmp.astype(str))
le_4.fit(attmp)
le_5.fit(iptmp)
le_6.fit(ostmp)
le_7.fit(dttmp)
le_8.fit(pitmp)
le_9.fit(dvtmp.astype(str))


ad = le_0.transform(ADdata['adx'])
st = le_1.transform(ADdata['spaceType'])
si = le_2.transform(ADdata['spaceId'])
sc = le_3.transform(ADdata['spaceCat'].astype(str))
at = le_4.transform(ADdata['adType'])
ip = le_5.transform(ADdata['ip'])
os = le_6.transform(ADdata['os'])
dt = le_7.transform(ADdata['deviceType'])
pi = le_8.transform(ADdata['publisherId'])
dv = le_9.transform(ADdata['dclkVerticals'].astype(str))

ad = ad[:,np.newaxis]
st = st[:,np.newaxis]
si = si[:,np.newaxis]
sc = sc[:,np.newaxis]
at = at[:,np.newaxis]
ip = ip[:,np.newaxis]
os = os[:,np.newaxis]
dt = dt[:,np.newaxis]
pi = pi[:,np.newaxis]
dv = dv[:,np.newaxis]

feature = ADdata.values[:,10:11]
target = ADdata.values[:,12]
target = target.astype('int')

feature = np.hstack((ad,st,si,sc,at,ip,os,dt,pi,dv,feature))

#x meas feature, y means target

#x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size = 0.1, random_state = 42)
#clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 42) 
#clf_entropy.fit(x_train, y_train)
#clf_entropy.fit(feature, target)

clf_entropy = RandomForestClassifier(criterion = "entropy", random_state = 100, n_estimators = 300)
clf_entropy.fit(feature, target)

"""
y_pred_en = clf_entropy.predict(x_test)
print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)
print ("F-measure is ", f1_score(y_test, y_pred_en, average='macro') )
"""

adin = le_0.transform(Testdata['adx'])
stin = le_1.transform(Testdata['spaceType'])
siin = le_2.transform(Testdata['spaceId'])
scin = le_3.transform(Testdata['spaceCat'].astype(str))
atin = le_4.transform(Testdata['adType'])
ipin = le_5.transform(Testdata['ip'])
osin = le_6.transform(Testdata['os'])
dtin = le_7.transform(Testdata['deviceType'])
piin = le_8.transform(Testdata['publisherId'])
dvin = le_9.transform(Testdata['dclkVerticals'].astype(str))

adin = adin[:,np.newaxis]
stin = stin[:,np.newaxis]
siin = siin[:,np.newaxis]
scin = scin[:,np.newaxis]
atin = atin[:,np.newaxis]
ipin = ipin[:,np.newaxis]
osin = osin[:,np.newaxis]
dtin = dtin[:,np.newaxis]
piin = piin[:,np.newaxis]
dvin = dvin[:,np.newaxis]

feature_test = Testdata.values[:,10:11]
feature_test = np.hstack((adin,stin,siin,scin,atin,ipin,osin,dtin,piin,dvin,feature_test))
target_pred = clf_entropy.predict(feature_test)
np.savetxt("output.csv", target_pred, fmt='%d')



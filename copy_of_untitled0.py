# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xPP9cUu_EU0uRdLBWgAtseRAKlCtkFk2
"""

! pip install kaggle

from google.colab import drive
drive.mount('/content/drive')

! mkdir ~/.kaggle

import numpy as np #
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from keras.utils.np_utils import to_categorical
from sklearn.utils import class_weight
import warnings
warnings.filterwarnings('ignore')

from zipfile import ZipFile

train_df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/mitbih_train.csv", header = None)
test_df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/mitbih_test.csv", header = None)

train_df[187].value_counts()

per_class = train_df[187].value_counts()
plt.figure(figsize=(10,8))
my_circle=plt.Circle( (0,0), 0.7, color='white')
plt.pie(per_class, labels=['normal beat','unknown Beats','Ventricular ectopic beats','Supraventricular ectopic beats','Fusion Beats'], colors=['tab:blue','tab:orange','tab:purple','tab:olive','tab:green'],autopct='%1.1f%%')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

from sklearn.utils import resample
df_1=train_df[train_df[187]==1]
df_2=train_df[train_df[187]==2]
df_3=train_df[train_df[187]==3]
df_4=train_df[train_df[187]==4]
df_0=(train_df[train_df[187]==0]).sample(n=20000,random_state=42)

df_1_upsample=resample(df_1,replace=True,n_samples=20000,random_state=123)
df_2_upsample=resample(df_2,replace=True,n_samples=20000,random_state=124)
df_3_upsample=resample(df_3,replace=True,n_samples=20000,random_state=125)
df_4_upsample=resample(df_4,replace=True,n_samples=20000,random_state=126)

train_df=pd.concat([df_0,df_1_upsample,df_2_upsample,df_3_upsample,df_4_upsample])

# representation of classes % wise
per_class = train_df[187].value_counts()
plt.figure(figsize=(20,10))
my_circle=plt.Circle( (0,0), 0.7, color='white')
plt.pie(per_class, labels=['normal beat','unknown Beats','Ventricular ectopic beats','Supraventricular ectopic beats','Fusion Beats'], colors=['tab:blue','tab:orange','tab:purple','tab:olive','tab:green'],autopct='%1.1f%%')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

target_train=train_df[187]
target_test=test_df[187]
y_train=to_categorical(target_train)
y_test=to_categorical(target_test)

X_train=train_df.iloc[:,:186].values
X_test=test_df.iloc[:,:186].values
#for i in range(len(X_train)):
#    X_train[i,:186]= add_gaussian_noise(X_train[i,:186])
X_train = X_train.reshape(len(X_train), X_train.shape[1],1)
X_test = X_test.reshape(len(X_test), X_test.shape[1],1)

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

encoder = preprocessing.LabelEncoder()
encoder.fit(target_train)
Y_train = encoder.transform(target_train)
encoder.fit(target_test)
Y_test = encoder.transform(target_test)

nsamples, nx, ny = X_train.shape
train_dataset = X_train.reshape((nsamples,nx*ny))
nsamples, nx, ny = X_test.shape
test_dataset = X_test.reshape((nsamples,nx*ny))

accu = []
prec = []
recc = []
f1   = []
models =[]

ytest = Y_test

dtree_model = DecisionTreeClassifier(max_depth = 100).fit(train_dataset, Y_train)
dt_pred = dtree_model.predict(test_dataset)
  
# creating a confusion matrix
#cm = confusion_matrix(Y_test, dtree_predictions)


accuracy_score(Y_test, dt_pred)#, normalize=False)

print('Accuracy Score : ' + str(accuracy_score(ytest, dt_pred)))
print('Precision Score : ' + str(precision_score(ytest,dt_pred,average='macro')))
print('Recall Score : ' + str(recall_score(ytest,dt_pred,average='macro')))
print('F1 Score : ' + str(f1_score(ytest,dt_pred,average='macro')))

# Classifier Confusion matrix

print('Confusion Matrix : \n' + str(confusion_matrix(ytest,dt_pred)))


accu.append(accuracy_score(ytest, dt_pred))
prec.append(precision_score(ytest,dt_pred,average='macro'))
recc.append(recall_score(ytest,dt_pred,average='macro'))
f1.append(f1_score(ytest,dt_pred,average='macro'))
models.append("Decision Tree" )
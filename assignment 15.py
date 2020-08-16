#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


dataset=pd.read_csv(r"C:\Users\Simran\Desktop\Industrial Training\datasets\breast_cancer.csv")


# In[4]:


dataset.shape


# In[5]:


dataset.head()


# In[6]:


dataset.isnull().sum()


# In[7]:


dataset['clump_thickness'].fillna(dataset['clump_thickness'].mean(), inplace=True)


# In[8]:


dataset['cell_size_uniformity'].fillna(dataset['cell_size_uniformity'].mean(), inplace=True)


# In[9]:


dataset['bare_nuclei']=dataset.fillna(dataset['bare_nuclei'].mode())


# In[10]:


dataset['bland_chromatin'].fillna(dataset['bland_chromatin'].mean(), inplace=True)

dataset['normal_nucleoli'].fillna(dataset['normal_nucleoli'].mean(), inplace=True)


# In[11]:


dataset.isnull().sum()


# In[12]:


from sklearn.preprocessing import LabelEncoder
lr=LabelEncoder()
dataset['class']=lr.fit_transform(dataset['class'])
dataset['doctor_name']=lr.fit_transform(dataset['doctor_name'])


# In[13]:


dataset.head()


# In[14]:


dataset.describe()


# In[15]:


c=dataset.corr()


# In[16]:


cm=c['class']


# In[17]:


cm


# no need of patient_id and doctor name
# also since cell_size_uniformity and cell_shape_uniformity have almost similar values we will use only one of them
# similarly in marginal_adhesion and single_ep_cell_size  too we will use only one.
# 

# In[18]:


dataset.drop(['patient_id','doctor_name','cell_shape_uniformity','marginal_adhesion'],axis=1,inplace=True)


# In[19]:


dataset.head()


# In[20]:


X=dataset.iloc[:,0:7].values


# In[21]:


y=dataset.iloc[:,7].values


# In[22]:


from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
sc = StandardScaler()

x=sc.fit_transform(X)


# In[23]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)


# In[24]:


log=LogisticRegression()


# In[25]:


log.fit(x_train,y_train)


# In[26]:


y_pred=log.predict(x_test)


# In[27]:


accuracy_score(y_pred,y_test)


# In[28]:


log.score(x_train,y_train)


# In[29]:


confusion_matrix(y_pred,y_test)


# In[30]:


from sklearn.naive_bayes import GaussianNB
nvclassifier = GaussianNB()
nvclassifier.fit(x_train, y_train)


# In[31]:


y_pred = nvclassifier.predict(x_test)
print(y_pred)


# In[32]:


accuracy_score(y_pred,y_test)


# In[33]:


nvclassifier.score(x_train,y_train)


# In[34]:


confusion_matrix(y_pred,y_test)


# In[ ]:


#Accuracy(logistic regression):0.96428 
#Accuracy(Naive_bayes) :0.95714


# In[ ]:





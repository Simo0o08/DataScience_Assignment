#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


diabetes=pd.read_csv(r"C:\Users\Simran\Desktop\Industrial Training\datasets\diabetes.csv")
diabetes


# In[5]:


diabetes.head()


# In[6]:


diabetes.shape


# In[7]:


diabetes.describe()


# In[8]:


diabetes.isnull().sum()


# In[9]:


x=diabetes.iloc[:,:-1]
x


# In[10]:


y=diabetes.iloc[:,8:9]
y


# In[11]:


import seaborn as sns
sns.set(style="darkgrid")
#titanic = sns.load_dataset("titanic")
ax = sns.countplot(y="Outcome",data=diabetes)


# In[12]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10))
sns.heatmap(diabetes.corr().abs(),  annot=True)
plt.show()


# In[13]:


#here blood pressure and skin thickness are almost non linear with Outcome


# In[14]:


fig, axs = plt.subplots(ncols=3, nrows=3, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in diabetes.items():
    sns.distplot(v, ax=axs[index],kde_kws={'bw': 0.1}) # for some prob write kde
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
plt.show()


# In[15]:


import seaborn as sns
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=4, nrows=3, figsize=(20, 10))
index = 0
axs = axs.flatten() # to flaten to 1d
for k,v in diabetes.items():
    sns.boxplot(y=v, data=diabetes, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.1, h_pad=5.0)
plt.show()


# In[ ]:





# In[16]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x1=diabetes.iloc[:,0:-1].values
y1=diabetes.iloc[:,-1:]
x=sc.fit_transform(x1)
y=sc.fit_transform(y1)


# In[21]:


x=pd.DataFrame(x)
x


# In[22]:


y=pd.DataFrame(y)
y


# In[24]:


y=diabetes.iloc[:,-1]
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)


# In[25]:


log=LogisticRegression()


# In[26]:


log.fit(x_train,y_train)


# In[27]:


y_pred=log.predict(x_test)


# In[28]:


from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
accuracy_score(y_pred,y_test)


# In[29]:


log.score(x_train,y_train)


# In[30]:


confusion_matrix(y_pred,y_test)


# In[ ]:





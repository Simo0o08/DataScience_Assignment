#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


houseprice=pd.read_csv(r"C:\Users\Simran\Desktop\Industrial Training\datasets\houseprice.csv")
houseprice.head()


# In[3]:


houseprice.shape


# In[4]:


houseprice.isnull().sum()


# In[5]:


#here in prediction id and date has no use
#as zipcode is provided there is no need of latitude and longitude
houseprice=houseprice.drop(['id','date','lat','long'],axis=1)
houseprice.head()


# In[6]:


houseprice.describe()


# In[7]:


#difference between mean and std in sqft_living,sqft_above,sqft_lot15 is more so drop that column
houseprice=houseprice.drop(['sqft_living','sqft_above','sqft_lot15'],axis=1)
houseprice.head()


# In[ ]:





# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=5, nrows=4, figsize=(15, 20))
index = 0
axs = axs.flatten() # to flaten to 1d
for k,v in houseprice.items():
    sns.boxplot(y=v, data=houseprice, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.5, w_pad=0.1, h_pad=5.0)
plt.show()


# In[10]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x1=houseprice.iloc[:,1:].values
y1=houseprice.iloc[:,0:1].values
x=sc.fit_transform(x1)
y=sc.fit_transform(y1)


# In[11]:


x=pd.DataFrame(x)
x


# In[12]:


y=pd.DataFrame(y)
y


# In[13]:


plt.figure(figsize=(20, 10))
sns.heatmap(houseprice.corr().abs(),  annot=True)
plt.show()


# In[14]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=0)


# In[15]:


lr=LinearRegression()
lr.fit(X_train,y_train)


# In[16]:


y_pred=lr.predict(X_test)


# In[17]:


from sklearn.metrics import r2_score, mean_squared_error
r2_score(y_test,y_pred)


# In[18]:


lr.score(x,y)


# In[19]:


mean_squared_error(y_test,y_pred)


# In[20]:


#polynomial regression


# In[21]:


from sklearn.preprocessing import PolynomialFeatures


# In[22]:


poly_reg=PolynomialFeatures(degree=3)
x_poly_train=poly_reg.fit_transform(X_train)


# In[23]:


poly_reg=PolynomialFeatures(degree=3)
x_poly_test=poly_reg.fit_transform(X_test)


# In[24]:


ro_2=LinearRegression()
ro_2.fit(x_poly_train,y_train)


# In[25]:


y_pred_poly=ro_2.predict(x_poly_test)


# In[26]:


r2_score(y_pred_poly,y_test)


# In[27]:


ro_2.score(x_poly_train,y_train)


# In[ ]:





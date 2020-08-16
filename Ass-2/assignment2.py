#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create a python module with 2 fun
#1st sum of all the odd no
#2nd square of no from 1 to 50
#call the above function from another file using import
import os


# In[2]:


os.chdir(r"C:\Users\Simran\Desktop\Python")


# In[3]:


import mod


# In[4]:


mod.sum()


# In[5]:


mod.sq()


# In[6]:


#calculate the summation of 2 numbers using lambda function

sum = lambda a,b:a+b


# In[7]:


sum(17,42)


# In[12]:


#write a program to take number from user and reverse it
Number = eval(input("Enter a number"))
Reverse = 0.
while(Number > 0):
    Reminder = Number %10.
    Reverse = (Reverse *10) + Reminder
    Number = Number //10.
print("\nReverse of entered number is = %d" %Reverse)


# In[ ]:





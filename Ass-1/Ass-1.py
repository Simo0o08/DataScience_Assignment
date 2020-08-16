#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creat a python program to find the prime no bw 1 to 50
for num in range(1,51):
    if num>1:
        for i in range(2,num):
            if(num%i == 0):
                break
        else:
            print(num, end=" ")


# In[2]:


# find a factorial of any user given number 
n = eval(input("Enter a number"))
fact =1
for i in range(1,n+1):
    fact = fact * i
print("The factorial of",n,"is",fact)


# In[3]:


#find whether the number is even or odd
n = eval(input("Enter a number"))
if(n%2==0):
    print(n, "is even")
else:
    print(n,"is odd")


# In[4]:


#creat a python program to find the sum of all even number from 1 to 50
i=1
sum=0
while i<=50:
    if i%2==0:
        sum=sum+i
    i=i+1
print('Sum of even numbers',sum)


# In[1]:


def sum():
    i=1
    sum=0
    while i<=50:
        if i%2!=0:
            sum=sum+i
        i=i+1
    print('Sum of even numbers',sum)


# In[2]:


sum()


# In[6]:


#create a python program to a below series   0 1 1 2 3 5 8 13....upto 20 term
n1=0
n2=1
count = 0
while count<=20:
    print(n1,end=" ")
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count = count + 1


# In[ ]:





# In[ ]:





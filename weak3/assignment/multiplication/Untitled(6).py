#!/usr/bin/env python
# coding: utf-8

# In[14]:


#printing the multiplication table of a given number based on the number given by the user
number=int(input("please enter the number you want to find the multiplication"))
for iter in range(10):
    print(iter+1,"*",number,"=",(iter+1)*number)


#!/usr/bin/env python
# coding: utf-8

# In[7]:


#doing array opertation using python
size=int(input("enter the size of the array"))
list=[]
for si in range(size):
    data=input("data want ot store in the file")
    list.append(data)
#making the copy of the list to other list
#list slicint
copy=list[:]
#adding one more element to the list copy
data=int(input("enter the element want to add in copy of the list"))
copy.append(data)
print(list,"  ",copy)


# In[21]:


#using numpy funtion
import numpy as np
size=int(input("enter size of the array"))
arr=np.empty(size,dtype=int)
for i in range(size):
    arr[i]=int(input("enter elements of array"))
#copy elements of arr to anotherarray
newarr=np.copy(arr)
#adding new element to the array
print(arr)
np.append(newarr,4)


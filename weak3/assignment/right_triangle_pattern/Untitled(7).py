#!/usr/bin/env python
# coding: utf-8

# In[16]:


#printing the pattern of number in right angle format in python
rows=int(input("please enter the number of rows you want to print the right angle triangle"))
#loop for row
for row in range(rows+1):
    #loop for printing cols
    for col in range(1,row+1):
        print(col,end=" ")
    print()


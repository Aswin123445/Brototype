#!/usr/bin/env python
# coding: utf-8

# In[12]:


#using switch case printing days according to the number user as provide
number=int(input("enter the number you want to find the day"))
match number:
    case 1 : 
        print("the day is sunday")
    case 2 :
        print("the day is monday")
    case 3 :
        print("the day is tuesday")
    case 4 :
        print("the day is wedsdey")
    case 5 :
        print("the day is thursday")
    case 6 :
        print("the day is friday")
    case 7 :
        print("the day is saturday")
    case _:
        print("output invalid number")


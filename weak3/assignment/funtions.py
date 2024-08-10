#!/usr/bin/env python
# coding: utf-8

# In[4]:


#fibonci series
number=int(input("enter the limit of the fibnoci series"))
def fibonci(number):
    #funtion to create a fibnoci series
    a,b=0,1
    while a<number:
        print(a, end=' ')
        a,b=b,a+b
    print()
fibonci(number)


# In[5]:


#default argument values 
#allow to define funtion with default values
def defaultArgument(name,gender="male"):
    print("name is"+name)
    print("gender is"+gender)
defaultArgument("aswin")


# In[2]:


#keyword funtions
#these are the funtions in python were we can use variable name to initalize values to it instead of using 
#postional method
def keywordArgument(name, gender="female"):
    print("my name is "+name+gender)
print(keywordArgument(name="madhu"))
print(keywordArgument(name="aswin"))


# In[4]:


#arbitary argument list in python
#arbitary argument is used when we don't know the number of arguments passed
#add funtion was doing some repative task with it 
#arbitary argurments used *argument_name for it
def arbitary_funtion(*output):
    for count in output:
        print(count)
arbitary_funtion(1,2,3,4,5)
#this funtion will print numbers according to the number of argumentw instead of declaring funtion definition inside the funtion 


# In[ ]:





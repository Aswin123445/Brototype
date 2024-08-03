#!/usr/bin/env python
# coding: utf-8

# In[9]:


#pass or failed after inputing data
mark=float(input("please enter your mark"))
if mark<50:
    print("student is failed in the exam")
else:
    print("student passed in the exam")


# In[10]:


#grade optained after student input the mark of the student
mark=float(input("please enter your mark"))
if mark<50:
    print("failed in the exam")
elif mark<=59:
    print("passed the exam with grade E")
elif mark<=69:
    print("passed the exam with D")
elif mark<=79:
    print("passed the exam with C")
elif mark<=89:
    print("passed the exam with B")
elif mark<=100:
    print("passed the exam with A")


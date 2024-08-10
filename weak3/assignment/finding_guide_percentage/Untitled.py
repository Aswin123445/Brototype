#!/usr/bin/env python
# coding: utf-8

# In[7]:


#finding the total percentage of mark 
mark_written=int(input("please enter the mark you scored in the writtern text"))
mark_particles=int(input("please enter the mark you optained in the particle section"))
mark_assignments=int(input("please enter the mark you got for the assignments"))
def percentage(written,particles,assignment):
    percentage=((written*70/100)+(particles*20/100)+(assignment*10/100))
    return percentage
print("percentage got for the student is",percentage(mark_written,mark_particles,mark_assignments))


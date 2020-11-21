#!/usr/bin/env python
# coding: utf-8

def PrintTriangle(x):
    start = 0
    for i in range(x,0,-1):
        blankCount = ( 2 * i - 3)
        starCount = (2 * i - 1)
        print(start * " ",end='')
        if(start == 0):
            print('*' * starCount)
        elif(blankCount <= 0):
            print('*')
        else:
            print('*' + blankCount * " " + '*')
        start = start + 1 


# In[112]:


PrintTriangle(5)

input("Program Ended")


# In[ ]:





# In[ ]:





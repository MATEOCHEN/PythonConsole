#!/usr/bin/env python
# coding: utf-8

# In[41]:


import random

def SortRandomNumber(randomCount):
    randomList = []

    for i in range(randomCount):
        randomList.append(random.randint(1,49))

    randomList.sort()
    print(randomList)


# In[43]:


SortRandomNumber(6)


# In[ ]:

input("Program End")



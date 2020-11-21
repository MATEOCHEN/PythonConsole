#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random

def FindOdds(randomList,result):
    if len(randomList) == 0:
        return result
    if randomList[0] % 2 == 1:
        result.append(randomList[0])
        
    return FindOdds(randomList[1:],result)

def FindEvens(randomList,result):
    if len(randomList) == 0:
        return result
    if randomList[0] % 2 == 0:
        result.append(randomList[0])
        
    return FindOdds(randomList[1:],result)

def SortRandomNumber(randomCount):
    randomList = []

    for i in range(randomCount):
        randomList.append(random.randint(1,100))

    print("Current List:",randomList)
    sortedList = sorted(randomList, reverse = False)
    print("Sorted List Aesc:",sortedList)
    reversedList = sorted(randomList, reverse = True)
    print("Sorted List Desc:",reversedList)
    print("Get Even Value",FindEvens(randomList,[]))
    print("Get Odds Value",FindOdds(randomList,[]))
    newList = [x+1 for x in sortedList]
    print("All Plus one",newList)


# In[32]:


SortRandomNumber(10)
input("Program End")

# In[ ]:





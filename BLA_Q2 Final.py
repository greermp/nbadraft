#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv


# In[3]:


def findFixedTeam(probs,remainingProbs,restProb):
    for i in range(11):
        nonzeros = [j for j, e in enumerate(probs) if e!=0]
        team=min(nonzeros)
        remainingProbs[i][team]=remainingProbs[i][team] + restProb
        probs[team] = 0.
    return remainingProbs

remainingProbs   = [[0. for x in range(16)] for y in range(11)]
# remainingProbs


# In[4]:


#Setting Draft Lottery Probabilities

initialProbs = [.114, .113, .112, .111, .099, .089, .079, .069, .059, .049, .039, .029, .019, .009, .006, .004]
secondProbs = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
thirdProbs = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
fourthProbs = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
fifthProbs = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]


# In[5]:


for i in range(16):
    firstRemoved = initialProbs[:i]+[0.]+initialProbs[i+1:]
    totalProb = sum(firstRemoved)
    conditionalProbs = [initialProbs[i]*x/totalProb for x in firstRemoved]
    secondProbs = [x + y for x,y in zip(secondProbs,conditionalProbs)]

print(secondProbs)
secondProbsSave = secondProbs


# In[6]:


for i in range(16):
    firstRemoved = initialProbs[:i]+[0.]+initialProbs[i+1:]
    totalProb = sum(firstRemoved)
    conditionalProbs = [initialProbs[i]*x/totalProb for x in firstRemoved]
    secondProbs = [x + y for x,y in zip(secondProbs,conditionalProbs)]

    for j in range(16):
        if i != j:
            secondRemoved = firstRemoved[:j]+[0.]+firstRemoved[j+1:]
            totalProb = sum(secondRemoved)
            conditionalProbs2 = [conditionalProbs[j]*x/totalProb for x in secondRemoved]
            thirdProbs = [x + y for x,y in zip(thirdProbs,conditionalProbs2)]

print(thirdProbs)
thirdProbsSave = thirdProbs


# In[7]:


for i in range(16):
    firstRemoved = initialProbs[:i]+[0.]+initialProbs[i+1:]
    totalProb = sum(firstRemoved)
    conditionalProbs = [initialProbs[i]*x/totalProb for x in firstRemoved]
    secondProbs = [x + y for x,y in zip(secondProbs,conditionalProbs)]

    for j in range(16):
            if i != j:
                secondRemoved = firstRemoved[:j]+[0.]+firstRemoved[j+1:]
                totalProb = sum(secondRemoved)
                conditionalProbs2 = [conditionalProbs[j]*x/totalProb for x in secondRemoved]
                thirdProbs = [x + y for x,y in zip(thirdProbs,conditionalProbs2)]


                for k in range(16):
                    if i != k:
                        thirdRemoved = secondRemoved[:k]+[0.]+secondRemoved[k+1:]
                        totalProb = sum(thirdRemoved)
                        conditionalProbs3 = [conditionalProbs2[k]*x/totalProb for x in thirdRemoved]
                        fourthProbs = [x + y for x,y in zip(fourthProbs,conditionalProbs3)]

print(fourthProbs)
fourthProbsSave = fourthProbs


# In[8]:


#problem cell
for i in range(16):
    firstRemoved = initialProbs[:i]+[0.]+initialProbs[i+1:]
    totalProb = sum(firstRemoved)
    conditionalProbs = [initialProbs[i]*x/totalProb for x in firstRemoved]
    secondProbs = [x + y for x,y in zip(secondProbs,conditionalProbs)]

    for j in range(16):
            if i != j:
                secondRemoved = firstRemoved[:j]+[0.]+firstRemoved[j+1:]
                totalProb = sum(secondRemoved)
                conditionalProbs2 = [conditionalProbs[j]*x/totalProb for x in secondRemoved]
                thirdProbs = [x + y for x,y in zip(thirdProbs,conditionalProbs2)]


                for k in range(16):
                    if i != k:
                        thirdRemoved = secondRemoved[:k]+[0.]+secondRemoved[k+1:]
                        totalProb = sum(thirdRemoved)
                        conditionalProbs3 = [conditionalProbs2[k]*x/totalProb for x in thirdRemoved]
                        fourthProbs = [x + y for x,y in zip(fourthProbs,conditionalProbs3)]
                        
                        
                        for l in range(16):
                            if i != l:
                                fourthRemoved = thirdRemoved[:l]+[0.]+thirdRemoved[l+1:]
                                totalProb = sum(fourthRemoved)
                                conditionalProbs4 = [conditionalProbs3[l]*x/totalProb for x in fourthRemoved]
                                fifthProbs = [x + y for x,y in zip(fifthProbs, conditionalProbs4)]
                                
                                for m in range(16):
                                    if (i != m) and (j != m) and (k != m) and (l != m):
                                        restProb = conditionalProbs4[m]
                                        #print(i,j,k,l,m,restProb)
                                        fifthRemoved = fourthRemoved[:m]+[0.]+fourthRemoved[m+1:]
                                        remainingProbs = findFixedTeam(fifthRemoved,remainingProbs,restProb)


# In[9]:


print(fifthProbs)
fifthProbsSave = fifthProbs


# In[10]:


for x in remainingProbs:
    print (x)


# In[11]:


#for m in range(16):
 #   if (i != m) and (j != m) and (k != m) and (l != m):
  #      restProb = conditionalProbs4[m]
   #     fifthRemoved = fourthRemoved[:m]+[0.]+fourthRemoved[m+1:]
    #    remainingProbs = findFixedTeam(fifthRemoved,remainingProbs,restProb)


# In[ ]:


# secondProbs


# In[12]:


teams= list(range(1,17))
teams


# In[14]:


remainingProbs[10]


# In[17]:


dict = {'Team Number': teams,
        'first': initialProbs,
        'second': secondProbsSave,
        'third': thirdProbsSave,
        'fourth': fourthProbsSave, 
        'fifth': fifthProbsSave, 
        'sixth': remainingProbs[0], 
        'seventh':remainingProbs[1], 
        'eighth':remainingProbs[2], 
        'ninth':remainingProbs[3], 
        'tenth':remainingProbs[4], 
        'eleventh':remainingProbs[5], 
        'twelfth':remainingProbs[6], 
        'thirteenth':remainingProbs[7], 
        'fourteenth':remainingProbs[8], 
        'fifteenth':remainingProbs[9], 
        'sixteenth':remainingProbs[10]}

df=pd.DataFrame(dict)
# df.reset_index(drop=True, inplace=True)
df=df.round(3)
df.to_csv('GFY.csv', index=False)


# In[ ]:





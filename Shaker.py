# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:00:04 2020

@author: simon880502
"""


from numpy import arange
from numpy.random import shuffle

def Find_Min(L):
    min_num=L[0]
    for i in range(len(L)):
        if min_num>L[i]:
            min_num=L[i]
    return min_num

def Find_Max(L):
    max_num=L[0]
    for i in range(len(L)):
        if max_num<L[i]:
            max_num=L[i]
    return max_num

def rand(c,k):
    if c<k:
        return 0 
    temp = arange(1,c)
    shuffle(temp)
    return list(temp[:k])

Rand_list=rand(100,10)  #  Combination(10,5)
print("Before Sort",Rand_list,'\n\n')
Max_id=Rand_list.index(Find_Max(Rand_list))
Min_id=Rand_list.index(Find_Min(Rand_list))
n=len(Rand_list)
Rand_list[-1],Rand_list[Max_id]=Rand_list[Max_id],Rand_list[-1]
Rand_list[0],Rand_list[Min_id]=Rand_list[Min_id],Rand_list[0]
i=1

while(True):
    if (i==n-i-1)or(i==n-i):
        break
    Max_id=Rand_list.index(Find_Max(Rand_list[i:n-i]))
    Min_id=Rand_list.index(Find_Min(Rand_list[i:n-i]))
    Rand_list[n-i-1],Rand_list[Max_id]=Rand_list[Max_id],Rand_list[n-i-1]
    Rand_list[i],Rand_list[Min_id]=Rand_list[Min_id],Rand_list[i]
    i+=1
print(Rand_list)




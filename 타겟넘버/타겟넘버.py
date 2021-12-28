#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://programmers.co.kr/learn/courses/30/lessons/43165


# In[ ]:


def solution(numbers, target):
    super=[0]
    for i in numbers:
        sub=[]
        for j in super:
            sub.append(j+i)
            sub.append(j-i)
        super=sub
    return super.count(target)


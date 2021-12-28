#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://programmers.co.kr/learn/courses/30/lessons/64065


# In[12]:


def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = sorted(s, key = len)
    for element in s:
        num_in_element = element.split(',')
        for num in num_in_element:
            num = int(num)
            if num not in answer:
                answer.append(num)
    return answer 


# In[13]:


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")


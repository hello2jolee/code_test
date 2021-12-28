#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3


# In[2]:


def solution(s):
    answer = 10000
    
    for slice in range(1, len(s)//2+2):
        res = ''
        count = 1
        temp = s[:slice]
        
        for i in range(slice, len(s) + slice, slice):
            if temp == s[i:i+slice]:
                count += 1
            else:
                if count == 1:
                    res += temp
                else:
                    res += str(count) + temp
                temp = s[i:i+slice]
                count = 1
                
        answer = min(answer, len(res))
    return answer 


# In[3]:


S = 'aabbaccc'

print(solution(S))


# In[ ]:





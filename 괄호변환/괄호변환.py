#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://programmers.co.kr/learn/courses/30/lessons/60058


# In[2]:


def parse(str):
    correct = True
    left = 0
    right = 0
    mystack = []
    
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            mystack.append('(')
        else:
            right += 1
            if len(mystack) == 0:
                correct = False
            else :
                mystack.pop()
        
        if left == right:
            return i + 1, correct
    
    return 0, False
    
def solution(p):
    if len(p) == 0:
        return p
    pos, correct = parse(p)
    u = p[:pos]
    v = p[pos:]
    
    if correct:
        return u + solution(v)
    
    answer = '(' + solution(v) + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer +='('
        
    return answer


# In[4]:


solution('(()())()')


# In[5]:


solution(')(')


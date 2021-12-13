#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://programmers.co.kr/learn/courses/30/lessons/42888


# In[4]:


def solution(record):
    answer=[]
    userDB = dict()
    actions=[]
    
    for event in record:
        info=event.split()
        action, userid=info[0], info[1]
        if action in ("Enter", "Change"):
            nickname=info[2]
            userDB[userid]=nickname
        actions.append((action, userid))
    
    for actionInfo in actions:
        action, userid = actionInfo[0], actionInfo[1]
        if action=='Enter':
            answer.append(f'{userDB[userid]}님이 들어왔습니다.')
        elif action=='Leave':
            answer.append(f'{userDB[userid]}님이 나갔습니다.')
    
    return answer


# In[5]:


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])


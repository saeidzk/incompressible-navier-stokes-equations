#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[7]:


class initial_condition():
    def __init__(self):
        pass
    
    def matrix_initialization(NX, NY, zero_initialization, intial_value):
        
        if zero_initialization == True:
            
            m_prev = np.zeros([NX,NY], dtype = np.longdouble)
           
            
        else:
            m_prev = np.full([NX,NY], intial_value,dtype = np.longdouble)
            
        m_tent = np.zeros([NX,NY], dtype = np.longdouble)
        m_next = np.zeros([NX,NY], dtype = np.longdouble)
           
            
            
        
        return [m_prev, m_tent, m_next]


# In[8]:


k, k1, k2 = initial_condition.matrix_initialization(41, 41, False, 293)


# In[9]:


k


# In[10]:


k1


# In[ ]:





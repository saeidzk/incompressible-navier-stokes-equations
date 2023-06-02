#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


'Defining discritization schemes'


class discretization_schemes():
    
    


#------------------------------------------------#
    def central_difference_x(f, DX):
            diff = np.zeros_like(f, dtype = np.longdouble)
            diff[1:-1, 1:-1] = (
                f[1:-1, 2:  ]
                -
                f[1:-1, 0:-2]
            ) / (
                2 * DX
            )
            return diff
#------------------------------------------------#
#------------------------------------------------#
    def central_difference_y(f, DY):
        diff = np.zeros_like(f, dtype = np.longdouble)
        diff[1:-1, 1:-1] = (
                f[2:  , 1:-1]
                -
                f[0:-2, 1:-1]
            ) / (
                2 * DY
            )
        
        return diff
#------------------------------------------------#
#------------------------------------------------#    
    def upwind_x(f, DX):
    
        diff = np.zeros_like(f, dtype = np.longdouble)
        diff[1:-1, 1:-1] = (
                
                f[1:-1, 1: -1 ]
                -
                f[1:-1,  : -2]
            ) / (
                DX
            )
            
        return diff
#------------------------------------------------#
    def upwind_y(f, DY):
    
        diff = np.zeros_like(f, dtype = np.longdouble)
        diff[1:-1, 1:-1] = (
                
                f[1:-1, 1: -1 ]
                -
                f[: -2, 1:-1]
            ) / (
                DY
            )
            
        return diff
#------------------------------------------------#
#------------------------------------------------#    
    def laplace(f, DX):
        diff = np.zeros_like(f, dtype = np.longdouble)
        diff[1:-1, 1:-1] = (
                f[1:-1, 0:-2]
                +
                f[0:-2, 1:-1]
                -
                4
                *
                f[1:-1, 1:-1]
                +
                f[1:-1, 2:  ]
                +
                f[2:  , 1:-1]
            ) / (
                DX**2
            )
        return diff
#------------------------------------------------#


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


class boundary_update():
    def __init__(self):
        pass
    
    def velocity_boundary_x(u_tent):
        u_tent[0, :] = 0.0 
        u_tent[:, 0] = 0.0
        u_tent[:, -1] = 0.0
        u_tent[-1, :] = 10.0
        
        return u_tent
        
    def velocity_boundary_y(v_tent):
        v_tent[0, :] = 0.0
        v_tent[:, 0] = 0.0
        v_tent[:, -1] = 0.0
        v_tent[-1, :] = 0.0
        
        return v_tent
    
    def pressure_boundary(p_next):
        p_next[:, -1] = p_next[:, -2]
        p_next[0,  :] = p_next[1,  :]
        p_next[:,  0] = p_next[:,  1]
        p_next[-1, :] = 0 #0.0
        
        return p_next
    
    def temperature_boundary(T_next):
        
        
        
        T_next[0,:] = 398
        T_next[:,0] =  T_next[:,1]
        T_next[:,-1] = T_next[:,-2]
        T_next[-1, :] =   T_next[-2, :] 
        
        
        
        return T_next
        


# In[ ]:


class boundary_update_lid_driven_cavity():
    def __init__(self):
        pass
    
    def velocity_boundary_x(u_tent):
        u_tent[0, :] = 0.0 
        u_tent[:, 0] = 0.0
        u_tent[:, -1] = 0.0
        u_tent[-1, :] = 10.0
        
        return u_tent
        
    def velocity_boundary_y(v_tent):
        v_tent[0, :] = 0.0
        v_tent[:, 0] = 0.0
        v_tent[:, -1] = 0.0
        v_tent[-1, :] = 0.0
        
        return v_tent
    
    def pressure_boundary(p_next):
        p_next[:, -1] = p_next[:, -2]
        p_next[0,  :] = p_next[1,  :]
        p_next[:,  0] = p_next[:,  1]
        p_next[-1, :] = 0 #0.0
        
        return p_next
    
    def temperature_boundary(T_next):
        
        
        
        T_next[0,:] = 398
        T_next[:,0] =  T_next[:,1]
        T_next[:,-1] = T_next[:,-2]
        T_next[-1, :] =   T_next[-2, :] 
        
        
        
        return T_next
        


# In[3]:


class boundary_update_rayleigh_benard():
    def __init__(self):
        pass
    
    def velocity_boundary_x(u_next):
        u_next[:, -1] = 0
        u_next[0,  :] = 0
        u_next[:,  0] = 0
        u_next[-1, :] = 0
        
        return u_next
        
    def velocity_boundary_y(v_next):
        v_next[:, -1] = 0
        v_next[0,  :] = 0
        v_next[:,  0] = 0
        v_next[-1, :] = 0
        
        return v_next
    
    def pressure_boundary(p_next):
        p_next[:, -1] = p_next[:, -2]
        p_next[0,  :] = p_next[1,  :]
        p_next[:,  0] = p_next[:,  1]
        p_next[-1, :] = p_next[-2, :]
        
        return p_next
    
    def temperature_boundary(T_next):
        
        
        
        #T_next[0,:] = 1.2
        T_next[0,16:26] = 4
        T_next[:,0] =  0
        T_next[:,-1] = 0
        T_next[-1, :] =   T_next[-2, :] 
        
        
        
        return T_next
        


# In[4]:


class boundary_update_nondimensionalized_rayleigh_benard():
    def __init__(self):
        pass
    
    def velocity_boundary_x(u_next):
        u_next[:, -1] = u_next[:, -2]
        u_next[0,  :] = u_next[1,  :]
        u_next[:,  0] = u_next[:,  1]
        u_next[-1, :] = u_next[-2, :]
        
        return u_next
        
    def velocity_boundary_y(v_next):
        v_next[:, -1] = v_next[:, -2]
        v_next[0,  :] = v_next[1,  :]
        v_next[:,  0] = v_next[:,  1]
        v_next[-1, :] = v_next[-2, :]
        
        return v_next
    
    def pressure_boundary(p_next):
        p_next[:, -1] = p_next[:, -2]
        p_next[0,  :] = p_next[1,  :]
        p_next[:,  0] = p_next[:,  1]
        p_next[-1, :] = p_next[-2, :]
        
        return p_next
    
    def temperature_boundary(T_next):
        
        
        
        #T_next[0,:] = 1.2
        T_next[0,16:26] = 1.2
        T_next[:,0] =  0
        T_next[:,-1] = 0
        T_next[-1, :] =   T_next[-2, :] 
        
        
        
        return T_next
        


# #Rayleigh_benard
# 
# class boundary_update():
#     def __init__(self):
#         pass
#     
#     def velocity_boundary_x(u_tent):
#         u_tent[0, :] = 0.0 #bottom
#         u_tent[:, 0] = 0.0
#         u_tent[:, -1] = 0.0
#         u_tent[-1, :] = 0.0 
#         
#         return u_tent
#         
#     def velocity_boundary_y(v_tent):
#         v_tent[0, :] = 0.0
#         v_tent[:, 0] = 0.0
#         v_tent[:, -1] = 0.0
#         v_tent[-1, :] = 0.0
#         
#         return v_tent
#     
#     def pressure_boundary(p_next):
#         p_next[:, -1] = p_next[:, -2]
#         p_next[0,  :] = p_next[1,  :]
#         p_next[:,  0] = p_next[:,  1]
#         p_next[-1, :] = 0.0
#         
#         return p_next
#     
#     def temperature_boundary(T_next):
#         
#         T_next[0, :] = 10 #bottom
#         T_next[:, 0] = 0
#         T_next[:, -1] = 0
#         T_next[-1, :] = 0
#         
#         
#         
#         return T_next
#         

# In[5]:


#c = np.zeros([369,369])


# In[6]:


#c


# In[7]:


#mu = 0
#sigma = 0.1
#line = np.linspace(0,369,369)
#c[0] = 5* np.sin(line/118) #np.exp( - (line-20)**2)
#np.shape(c[0])
#np.shape(line)


# In[ ]:





# In[8]:


#plt.plot(line, c[0])


# In[9]:


#np.shape(c[0])


# In[10]:


#c[0]


# In[11]:


#c = np.zeros([41,41])


# In[12]:


#boundary_update.temperature_boundary(c)


# In[13]:


#c[0]


# In[ ]:





# In[ ]:





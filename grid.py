#!/usr/bin/env python
# coding: utf-8

# In[15]:


import concurrent.futures
from abc import abstractmethod
import matplotlib.pyplot as plt
import numpy as np


# In[16]:


def mesh(NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y):
    pass


class mesh_grid():
    
    def __init__(self):
        pass
#------------------------------------------------#
    @abstractmethod
    def mesh(NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y):
#------------------------------------------------#
        DX = 2/(NX -1) #element length in x direction
        DY = 2/(NY -1) #element length in y direction
        element_length = DX
#------------------------------------------------#
        x = np.linspace(0, DOMAIN_SIZE_X, NX) #range in xdirection
        y = np.linspace(0, DOMAIN_SIZE_Y, NY) #range in ydirection
        X, Y = np.meshgrid(x,y) #X, Y are 2d arrays containing same range again and again
#------------------------------------------------#
        #Parallelizing "mesh_grid" Using "futures3"      
        with concurrent.futures.ProcessPoolExecutor() as executor: 
            executor.map(mesh(NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y), (x, y))
#------------------------------------------------#
        plot_mesh.mesh_plot(X,Y)
    
        return [X, Y, DX, DY]



# In[14]:


class plot_mesh():
    def __init__(self):
        pass
    
    def mesh_plot(X, Y):
        
        from matplotlib.pyplot import figure
        #Plotting the mesh
        print('\nOUTPUT: Plotting the mesh in two dimension')
        figure(figsize=(6, 5), dpi=80)
        plt.plot(X, Y, color = 'g', marker='o',markersize = 4, linestyle='-')
        plt.plot(np.transpose(X), np.transpose(Y), color = 'g', linestyle='-')
        plt.xlabel('xdirection', fontsize = 12)
        plt.ylabel('ydirection', fontsize = 12)
        plt.title('Discritized domain in 2d', fontsize = 12)
        plt.show()
        
        return None






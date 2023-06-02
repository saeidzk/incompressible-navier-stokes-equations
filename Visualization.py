#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import numpy as np


# In[2]:


class Visual():
    
    def __init__():
        pass
    
    def visualize_vector_plot(X, Y, u_next, v_next, streamplot):
        
        #------------------------------------------------#
        plt.figure(1)
        plt.xlim((0, 1))
        plt.ylim((0, 0.5))
        #------------------------------------------------#
    
        if streamplot == True: 
            z1 = plt.streamplot(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], v_next[::2, ::2], color="black")
        else:
            z1 = plt.quiver(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], v_next[::2, ::2], color="black")
    
   
        #plt.show()
    
        return z1
    
    def visualize_contour_plot(X, Y, u_next):
    
        #------------------------------------------------#
        #plt.figure()
        plt.xlim((0, 1))
        plt.ylim((0, 0.5))
        #------------------------------------------------#
        plt.contourf(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], cmap="viridis")
        plt.colorbar()
        #------------------------------------------------#
        
        return None
    
    def visualize_Spin_up_plot(Spin_up,N_ITERATIONS, xlim_pos, xlim_neg, ylim_pos, ylim_neg):
        
        Spin_up = np.array(Spin_up)
        np.shape(Spin_up)
        
        #plt.ylabel('Error')
        #plt.xlabel('Timesteps')
        plt.plot(np.linspace(0,N_ITERATIONS,N_ITERATIONS),Spin_up)
        plt.xlim(xlim_neg, xlim_pos)
        plt.ylim(ylim_neg, ylim_pos)
        plt.ylabel('Spin_up w.r.t time')
        plt.xlabel('iterations')
        plt.show()
        
        return None
    
    

    
    def animation(solution, TIME_STEP_LENGTH, X, Y):
        
        import matplotlib.animation as animation
        get_ipython().run_line_magic('matplotlib', 'notebook')
        fig = plt.figure(figsize=(6.1,5),facecolor='w')
        images=[]
        lev=np.linspace(-1,1,50)
        i=0
        t=0
        
        for sol in solution:
            if i%50==0: # plots contour each 50 time steps
                im=plt.contourf(X,Y,solution[i,:,:], levels=lev,vmax=1.0,vmin=-1.0)
                images.append(im.collections)
            i+=1
            t += TIME_STEP_LENGTH

        cbar = plt.colorbar()
        plt.title('Contour')
        #plt.clim(-1,1)
        cbar.set_ticks(np.linspace(-1,1,50))

        ani = animation.ArtistAnimation (fig, images, interval=35, blit= True, repeat_delay=50)

        plt.show()
        
        return None
    


# In[ ]:





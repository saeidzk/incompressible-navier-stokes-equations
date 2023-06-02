#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import abstractmethod
from test import test_code


# In[1]:


class Navier_stokes_variables():
    def __init__():
        pass
    

    #he following function decides variables like element length, domain size,
    #time_step_length etc. When 'input_variables(N='TRUE')', we get default values,
    #on the contrary when N = 'False' we get to define our own parameters
    def input_variables(NX, NY, DOMAIN_SIZE_X, N_ITERATIONS, N_PRESSURE_POISSON_ITERATIONS, TIME_STEP_LENGTH, STABILITY_SAFETY_FACTOR, KINEMATIC_VISCOSITY, DENSITY):
        
        
        DOMAIN_SIZE_Y = 0.5 * float(DOMAIN_SIZE_X)
        
        input_return_list = [NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y, N_ITERATIONS, N_PRESSURE_POISSON_ITERATIONS, TIME_STEP_LENGTH, STABILITY_SAFETY_FACTOR, KINEMATIC_VISCOSITY, DENSITY]
        test_code.test_input(input_return_list)

        
        return input_return_list
        
            


# In[ ]:





# In[ ]:





# In[ ]:





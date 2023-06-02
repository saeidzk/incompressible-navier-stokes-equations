#!/usr/bin/env python
# coding: utf-8

# In[4]:


from abc import abstractmethod
import numpy as np
import dask
from dask import delayed


# In[5]:


class test_code():
    
    def __init__():
        pass
    
    def test_input(input_return_list: list):
        
        
                for x in input_return_list:
                    if type(x) == str:
                        raise valueError('Only integers are allowed')
                        print('The vairable is an ineteger: ', x)
                        c = None
                        break;
                        
                        
                    elif input_return_list[0] < 10 or input_return_list[1] < 10:
                        raise ValueError('Increase number of nodes: NX or NY > 10')
                        c = None
                        break;
                        
                    elif input_return_list[6] > 0.001:
                        raise ValueError('Reduce timestep length, otherwise stability is not assured')
                        c = None
                        break;
                        
                        
                    else:
                        c = input_return_list
                    
                
                return c
            


# In[1]:


class test_stability():
    
    @dask.delayed
    def __init__():
        pass
    
    def test_initial_timestep_value(DX, TIME_STEP_LENGTH, KINEMATIC_VISCOSITY, STABILITY_SAFETY_FACTOR):
        
        maximum_possible_time_step_length = dask.delayed((0.5 * DX**2 / KINEMATIC_VISCOSITY))
        
        while TIME_STEP_LENGTH > STABILITY_SAFETY_FACTOR * maximum_possible_time_step_length:
            raise RuntimeError("Stability is not guarenteed: modifying timestep value")
            TIME_STEP_LENGTH = TIME_STEP_LENGTH/2
            
        return TIME_STEP_LENGTH
    
    def test_CFL_number_calculation(u_next, v_next, DX, DY, TIME_STEP_LENGTH):
        
        CFL_X = dask.delayed(np.mean(u_next) * (TIME_STEP_LENGTH/DX))
        CFL_Y = dask.delayed(np.mean(v_next) * (TIME_STEP_LENGTH/DY))
        
        
        if CFL_X < 1 and CFL_Y < 1:
            pass
        
        else:
            print("Stability not guarenteed: modify timestep value")
            #raise RuntimeError("Stability not guarenteed: modify timestep value")
            
            while CFL_X > 1 or CFL_Y > 1:
                TIME_STEP_LENGTH = CFL_X * DX * (1/np.max(u_next))
                CFL_X = np.mean(u_next) * (TIME_STEP_LENGTH/DX)
                CFL_Y = np.mean(v_next) * (TIME_STEP_LENGTH/DY)
            
        return TIME_STEP_LENGTH
    
    def test_pressure_poisson_convergence(p_prev, p_next):
        
        if np.mean(p_next - p_prev) < 0.00001:
            raise RuntimeError("Stability not guarenteed: Error in pressure convergence")
            
        else:
            pass
        
        return None
        
        
    


# In[ ]:





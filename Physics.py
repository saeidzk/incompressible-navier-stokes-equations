#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from boundary_conditions import boundary_update
from test import test_stability
import dask
from dask import delayed


# In[1]:


class homogenous_advection:
    
    @dask.delayed
    def advection_temperature(T, u, v, d_T__d_x, d_T__d_y, laplace_T,KINEMATIC_VISCOSITY, TIME_STEP_LENGTH):
        
        T_next = dask.delayed((T + TIME_STEP_LENGTH * 
                  (
                      - 
                      (
                          u * d_T__d_x 
                          + 
                          v * d_T__d_y
                      )
                      + 
                      KINEMATIC_VISCOSITY * laplace_T
                  )
                 ))
        return T_next
    
    # 000019
    @dask.delayed
    def advection_velocity_prediction_horizontal(u, v, d_u__d_x, d_u__d_y, laplace__u,  KINEMATIC_VISCOSITY, TIME_STEP_LENGTH ):
    
        u_half = dask.delayed((u + TIME_STEP_LENGTH * 
                  (
                      -
                      (
                          u * d_u__d_x
                          +
                          v * d_u__d_y
                      
                      )
                      +
                    KINEMATIC_VISCOSITY * laplace__u
                )
            ))
    
        return u_half
    
    @dask.delayed
    def advection_velocity_prediction_vertical(v, u, d_v__d_x, d_v__d_y, laplace__v,  KINEMATIC_VISCOSITY, TIME_STEP_LENGTH ):

        v_half = dask.delayed((v + TIME_STEP_LENGTH * 
                  (
                      -
                      (
                          u * d_v__d_x
                          +
                          v * d_v__d_y
                      
                      )
                      +
                    KINEMATIC_VISCOSITY * laplace__v
                )
            ))
    
        return v_half
    



# In[2]:


class pressure_poisson:
    
    @dask.delayed
    def pressure_solver(p, DX, rhs, N_PRESSURE_POISSON_ITERATIONS):
        
        
        for _ in range(N_PRESSURE_POISSON_ITERATIONS):
            
            p_next = dask.delayed(np.zeros_like(p))
            p_next[1:-1, 1:-1] = 1/4 * (
                +
                p[1:-1, 0:-2]
                +
                p[0:-2, 1:-1]
                +
                p[1:-1, 2:  ]
                +
                p[2:  , 1:-1]
                -
                DX**2
                *
                rhs[1:-1, 1:-1]
            )
            
            
            # Pressure Boundary Conditions: Homogeneous Neumann Boundary
            # Conditions everywhere except for the top, where it is a
            # homogeneous Dirichlet BC
           # if N_PRESSURE_POISSON_ITERATIONS + 1 > N_PRESSURE_POISSON_ITERATIONS:
            #    test_stability.test_pressure_poisson_convergence(p, p_next)
                
            
            p = p_next
            
        return p_next
    
    
    


# In[8]:


class advection_velocity_correction:
    
    @dask.delayed
    def advection_velocity(u_half, d_p__d_x, DENSITY, TIME_STEP_LENGTH):
        
        u_next = dask.delayed((
            u_half
            -
            TIME_STEP_LENGTH / DENSITY
            *
            d_p__d_x
        ))
        
        return u_next


# In[ ]:





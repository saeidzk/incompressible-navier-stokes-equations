#!/usr/bin/env python
# coding: utf-8

# In[1]:


from input_Navier import Navier_stokes_variables
from grid import *
from difference_equation import discretization_schemes
from tqdm import tqdm
from boundary_conditions import boundary_update_rayleigh_benard 
from Physics import *
from initial_conditions import *
from test import *
from Visualization import *
from matplotlib import pyplot as plt


# # Parameter and solution scheme setup

# In[2]:


class setup_parameters:
    
    def __init__(self):
        pass
#------------------------------------------------#
    
    def call_inputvars():
        
        
        return Navier_stokes_variables.input_variables(NX = 41, NY = 41, DOMAIN_SIZE_X = 1.0, N_ITERATIONS = 1000, N_PRESSURE_POISSON_ITERATIONS = 50, TIME_STEP_LENGTH = 0.0001, STABILITY_SAFETY_FACTOR = 0.5, KINEMATIC_VISCOSITY =  0.000025, DENSITY = 1.00)
#------------------------------------------------#    
    def call_mesh_grid(NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y):
        
        return mesh_grid.mesh(NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y)
#------------------------------------------------#    
    def call_discretization_schemes(central_difference = True, upwind = False):
        
        if central_difference == True:
            
            first_order_discrete_space_x = discretization_schemes.central_difference_x #option: upwind
            first_order_discrete_space_y = discretization_schemes.central_difference_y #option: upwind
            
            
        else:
            if upwind == True:
                
                first_order_discrete_space_x = discretization_schemes.upwind_x #option: upwind
                first_order_discrete_space_y = discretization_schemes.upwind_y #option: upwind
                
                
        second_order_discrete_space_x = discretization_schemes.laplace
        second_order_discrete_space_y = discretization_schemes.laplace
                
        
        dscheme = [first_order_discrete_space_x, first_order_discrete_space_y, second_order_discrete_space_x,second_order_discrete_space_y  ]
        return dscheme
#------------------------------------------------#        


# In[3]:


#Parameters

NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y, N_ITERATIONS, N_PRESSURE_POISSON_ITERATIONS, TIME_STEP_LENGTH, STABILITY_SAFETY_FACTOR, KINEMATIC_VISCOSITY , DENSITY = setup_parameters.call_inputvars()
Spin_up = []
Error = []

u_solution_time = []
v_solution_time = []
p_solution_time = []
T_solution_time = []

beta = 0.0034

reynolds_number = 1000000 #10/KINEMATIC_VISCOSITY
prandtl_number = 0.7 #KINEMATIC_VISCOSITY/beta

alpha = np.sqrt(prandtl_number/reynolds_number)
gama = 1/(np.sqrt(reynolds_number * prandtl_number))
sigma = np.sqrt(KINEMATIC_VISCOSITY)

print('reynolds_number:', reynolds_number)
print('prandtl_number:', prandtl_number)
print('alpha:',alpha)
print('gama: ',gama)
print('sigma:',sigma)

#grid
X, Y, DX, DY = setup_parameters.call_mesh_grid(NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y)


# In[ ]:





# In[4]:


#Inital_conditions
#check out initial_conditions file
# if zero_intialization == False, then define initial_value for matrix formation
    
u_prev, u_tent, u_next = initial_condition.matrix_initialization(NX, NY, zero_initialization = False, intial_value = 0.0)
v_prev, v_tent, v_next = initial_condition.matrix_initialization(NX, NY, zero_initialization = False, intial_value = 0.0)
p_prev, p_tent, p_next = initial_condition.matrix_initialization(NX, NY, zero_initialization = False, intial_value = 0.0)
if beta > 0:
    T, T_tent, T_next = initial_condition.matrix_initialization(NX, NY, zero_initialization = False, intial_value = 0.0)
else:
    pass


# In[ ]:





# # Solution loop

# In[5]:


if __name__ == '__main__':
    
#------------------------------------------------#

    
    
#------------------------------------------------#
    #selecting up discretization schemes
    
    dscheme = setup_parameters.call_discretization_schemes()
    first_order_discrete_space_x = dscheme[0] 
    first_order_discrete_space_y = dscheme[1] 
    second_order_discrete_space_x = dscheme[2]
    second_order_discrete_space_y =dscheme[3]
#------------------------------------------------#  



    for _ in tqdm(range(N_ITERATIONS)):

        #Generating derivative terms for homogenous advection calculation
        
        d_u_prev__d_x = first_order_discrete_space_x(u_prev, DX)
        d_u_prev__d_y = first_order_discrete_space_y(u_prev, DX)
        d_v_prev__d_x = first_order_discrete_space_x(v_prev, DY)
        d_v_prev__d_y = first_order_discrete_space_y(v_prev, DY)
        laplace__u_prev = second_order_discrete_space_x(u_prev, DX)
        laplace__v_prev = second_order_discrete_space_y(v_prev, DY)
        
        if beta > 0:
            
            #d_T__d_x = first_order_discrete_space_x(T,DX)
            #d_T__d_y = first_order_discrete_space_y(T,DY)
            laplace_T = second_order_discrete_space_x(T, DX)
            d_T__d_x = discretization_schemes.central_difference_x(T,DX) #discretization_schemes.upwind_x(T,DX)
            d_T__d_y = discretization_schemes.central_difference_y(T,DY) #discretization_schemes.upwind_y(T,DY)
            
        else:
            pass
        
#------------------------------------------------#
        # Perform a tentative step by solving the momentum equation without the
        # pressure gradient
        
            
        #TIME_STEP_LENGTH = test_stability.test_initial_timestep_value(DX,TIME_STEP_LENGTH, KINEMATIC_VISCOSITY, STABILITY_SAFETY_FACTOR)        
        u_tent =homogenous_advection.advection_velocity_prediction_horizontal(u_prev, v_prev, d_u_prev__d_x,  d_u_prev__d_y, laplace__u_prev, KINEMATIC_VISCOSITY, TIME_STEP_LENGTH)
        v_tent =homogenous_advection.advection_velocity_prediction_vertical(v_prev, u_prev, d_v_prev__d_x,  d_v_prev__d_y, laplace__v_prev, KINEMATIC_VISCOSITY, TIME_STEP_LENGTH)  
        
#------------------------------------------------#
        # Velocity Boundary Conditions: Homogeneous Dirichlet BC everywhere
        # except for the horizontal velocity at the top, which is prescribed
        
        u_tent = boundary_update_rayleigh_benard.velocity_boundary_x(u_tent)
        v_tent = boundary_update_rayleigh_benard.velocity_boundary_y(v_tent)
        
        if beta > 0:
            T_next = boundary_update_rayleigh_benard.temperature_boundary(T_next)
        else:
            pass
         

#------------------------------------------------#
        d_u_tent__d_x = first_order_discrete_space_x(u_tent, DX)
        d_v_tent__d_y = first_order_discrete_space_y(v_tent, DY)
#------------------------------------------------#
#------------------------------------------------#
#------------------------------------------------#
        # Compute a pressure correction by solving the pressure-poisson equation
    
        rhs = (DENSITY / TIME_STEP_LENGTH *(d_u_tent__d_x + d_v_tent__d_y))
        p_next = pressure_poisson.pressure_solver(p_prev, DX, rhs, N_PRESSURE_POISSON_ITERATIONS)
        p_next = boundary_update_rayleigh_benard.pressure_boundary(p_next)
#------------------------------------------------#
        #Generating derivative terms for velocity correction calculation

        d_p_next__d_x = first_order_discrete_space_x(p_next, DX)
        d_p_next__d_y = first_order_discrete_space_y(p_next, DY)
#------------------------------------------------#
#------------------------------------------------#
#------------------------------------------------#
        # Correct the velocities such that the fluid stays incompressible
    
        if beta > 0:
            T_next = homogenous_advection.advection_temperature(T, u_prev, v_prev, d_T__d_x, d_T__d_y, laplace_T, 1, TIME_STEP_LENGTH )
        else:
            pass
        
        if beta > 0:
            bouancy =  beta * (T_next)
             
        else:
            bouancy = 0
        
        
        u_next = advection_velocity_correction.advection_velocity(u_tent, d_p_next__d_x, DENSITY, TIME_STEP_LENGTH  ) 
        v_next = advection_velocity_correction.advection_velocity(v_tent, d_p_next__d_y, DENSITY, TIME_STEP_LENGTH  )     + bouancy  * TIME_STEP_LENGTH#'Add temperature part'
#------------------------------------------------#
        # Velocity Boundary Conditions: Homogeneous Dirichlet BC everywhere
        # except for the horizontal velocity at the top, which is prescribed
        
        u_next = boundary_update_rayleigh_benard.velocity_boundary_x(u_next)
        v_next = boundary_update_rayleigh_benard.velocity_boundary_y(v_next)
        
        if beta > 0:
            T_next = boundary_update_rayleigh_benard.temperature_boundary(T_next)
        else:
            pass
#------------------------------------------------#
        Spin_up.append((np.mean(u_next) - np.mean(u_prev))/np.mean(u_prev))
        Error.append((np.sqrt(np.sum((u_next - u_prev)**2))/ (NX * NY)))
#------------------------------------------------#
        # Advance in time
    
        u_prev = u_next
        v_prev = v_next
        p_prev = p_next
        if beta > 0:
            T = T_next
        else:
            pass
        
        u_solution_time.append(u_next)
        v_solution_time.append(v_next)
        p_solution_time.append(p_next)
        
        if beta > 0:
            T_solution_time.append(T_next)
            
        else:
            pass
        
        

#------------------------------------------------#

        # Modifying timestep based on CFL number
    
        TIME_STEP_LENGTH = test_stability.test_CFL_number_calculation(u_next, v_next, DX, DY, TIME_STEP_LENGTH) 


# # Plot solution and error

# In[6]:


u_solution_time = np.array(v_solution_time)
v_solution_time = np.array(v_solution_time)
p_solution_time = np.array(v_solution_time)
T_solution_time = np.array(v_solution_time)


# In[8]:


#Plotting the contour
Visual.visualize_contour_plot(X, Y, v_next)
Visual.visualize_vector_plot(X, Y, u_next, v_next, True)
Visual.visualize_vector_plot(X, Y, u_next, v_next, False)


# In[ ]:





# In[ ]:


Visual.visualize_Spin_up_plot(Spin_up,N_ITERATIONS, xlim_pos = N_ITERATIONS, xlim_neg = 1, ylim_pos =  0.05 , ylim_neg =  -0.05)


# In[ ]:


#animate
Visual.animation(v_prev, TIME_STEP_LENGTH, X, Y)
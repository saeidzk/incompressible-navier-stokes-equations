#!/usr/bin/env python
# coding: utf-8

# In[1]:


from input_Navier import Navier_stokes_variables
from grid import *
from difference_equation import discretization_schemes
from tqdm import tqdm
from boundary_conditions import boundary_update
from Physics import *


# Welcome to the solver
#     
#     1. Define necessary constants for setting up discritization and difference equation constants.
#        For more information, check the 'input_Navier.ipynb' file.
#        
#     2. Setting up discritization and mesh.
#     
#     3. Set up solution matrices. Intially containing zeros. 
#     
#     4. Enter stability criteria
#     
#     5. Update loop and BC/IC conditions
#     
#     6. plot    
#     

# In[2]:


if __name__ == '__main__':
    
    
    
    #1
    KINEMATIC_VISCOSITY = 0.1
    DENSITY = 1.0
    NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y, N_ITERATIONS, N_PRESSURE_POISSON_ITERATIONS, TIME_STEP_LENGTH, STABILITY_SAFETY_FACTOR = Navier_stokes_variables.input_variables(1)


# In[3]:


#2
X, Y, DX, DY = mesh_grid.mesh(NX, NY, DOMAIN_SIZE_X, DOMAIN_SIZE_Y)


# In[4]:


'Defining solution matrices'

#3
#------------------------------------------------#
u_prev = np.zeros((NY,NX))#___U0 Initially everything is zero
u_tent = np.zeros((NY,NX))#___U1/2
u_next = np.zeros((NY,NX))#___U1
#------------------------------------------------#
#------------------------------------------------#
v_prev = np.zeros((NY,NX))
v_tent = np.zeros((NY,NX))
v_next = np.zeros((NY,NX))
#------------------------------------------------#
#------------------------------------------------#
p_prev = np.zeros((NY,NX))
p_tent = np.zeros((NY,NX))
p_next = np.zeros((NY,NX))
#------------------------------------------------#
#------------------------------------------------#
#'Introduce temperature distribution at t =0 level'
#'It should be differentiable up to some high order'
#T = np.zeros((NY,NX))
#x = np.linspace(0, len(X), NX)
#T[0, :] = np.exp(- (x -20)**2 )
#------------------------------------------------#
#------------------------------------------------#
#plt.plot(x,T[0, :])
#plt.show()


# In[5]:


'Checking stability condition'


#4
#------------------------------------------------#
maximum_possible_time_step_length = (
        0.5 * DX**2 / KINEMATIC_VISCOSITY
    )
if TIME_STEP_LENGTH > STABILITY_SAFETY_FACTOR * maximum_possible_time_step_length:
    raise RuntimeError("Stability is not guarenteed")
#------------------------------------------------#


# In[7]:


'Main loop for iteration'



#5
for _ in tqdm(range(N_ITERATIONS)):
#------------------------------------------------#
        #Generating derivative terms for homogenous advection calculation
    
        d_u_prev__d_x = discretization_schemes.central_difference_x(u_prev, DX)
        d_u_prev__d_y = discretization_schemes.central_difference_y(u_prev, DX)
        d_v_prev__d_x = discretization_schemes.central_difference_x(v_prev, DY)
        d_v_prev__d_y = discretization_schemes.central_difference_y(v_prev, DY)
        laplace__u_prev = discretization_schemes.laplace(u_prev, DX)
        laplace__v_prev = discretization_schemes.laplace(v_prev, DY)
#------------------------------------------------#
        # Perform a tentative step by solving the momentum equation without the
        # pressure gradient
        'Do changes in temperature part'
        #T_prev = 10 + discretization_schemes.central_difference_x(T_prev, DX) + discretization_schemes.central_difference_x(T_prev, DT)
        u_tent =homogenous_advection.advection_velocity_prediction_horizontal(u_prev, v_prev, d_u_prev__d_x,  d_u_prev__d_y, laplace__u_prev, KINEMATIC_VISCOSITY, TIME_STEP_LENGTH)
        v_tent =homogenous_advection.advection_velocity_prediction_vertical(v_prev, u_prev, d_v_prev__d_x,  d_v_prev__d_y, laplace__v_prev, KINEMATIC_VISCOSITY, TIME_STEP_LENGTH)     
#------------------------------------------------#
        # Velocity Boundary Conditions: Homogeneous Dirichlet BC everywhere
        # except for the horizontal velocity at the top, which is prescribed
        'Define boundary conditions for temperature'
        u_tent = boundary_update.velocity_boundary_x(u_tent)
        v_tent = boundary_update.velocity_boundary_y(v_tent)
#------------------------------------------------#
        d_u_tent__d_x = discretization_schemes.central_difference_x(u_tent, DX)
        d_v_tent__d_y = discretization_schemes.central_difference_y(v_tent, DY)
#------------------------------------------------#
        # Compute a pressure correction by solving the pressure-poisson equation
    
    
        rhs = (
            DENSITY / TIME_STEP_LENGTH
            *
            (
                d_u_tent__d_x
                +
                d_v_tent__d_y
            )
        )
        
        p_next = pressure_poisson.pressure_solver(p_prev, DX, rhs, N_PRESSURE_POISSON_ITERATIONS)
#------------------------------------------------#
        #Generating derivative terms for velocity correction calculation

        d_p_next__d_x = discretization_schemes.central_difference_x(p_next, DX)
        d_p_next__d_y = discretization_schemes.central_difference_y(p_next, DY)
#------------------------------------------------#
        # Correct the velocities such that the fluid stays incompressible
    
        u_next = advection_velocity_correction.advection_velocity(u_tent, d_p_next__d_x, DENSITY, TIME_STEP_LENGTH  )
        'Add temperature term to the vertical velocity directly'
        v_next = advection_velocity_correction.advection_velocity(v_tent, d_p_next__d_y, DENSITY, TIME_STEP_LENGTH  )       #'Add temperature part'
#------------------------------------------------#
        # Velocity Boundary Conditions: Homogeneous Dirichlet BC everywhere
        # except for the horizontal velocity at the top, which is prescribed
        
        u_next = boundary_update.velocity_boundary_x(u_next)
        v_next = boundary_update.velocity_boundary_y(v_next)
#------------------------------------------------#
        # Advance in time
    
        u_prev = u_next
        v_prev = v_next
        p_prev = p_next
#------------------------------------------------#


# In[8]:


'Plotting the contour'

#6
#------------------------------------------------#
#plt.style.use("white_background")
plt.figure()
plt.contourf(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], cmap="plasma")
plt.colorbar(ticks=np.linspace(-10, 10, 20))
#------------------------------------------------#
plt.quiver(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], v_next[::2, ::2], color="black")
plt.streamplot(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], v_next[::2, ::2], color="black")
plt.xlim((0, 1))
plt.ylim((0, 0.5))
plt.show()
#------------------------------------------------#


# In[ ]:





# In[ ]:





# In[ ]:





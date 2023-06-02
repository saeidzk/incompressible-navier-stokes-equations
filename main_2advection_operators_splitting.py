import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import Analytical
import anim

def twoD_linear_advection(Ny, Nz, Ly, Lz, V, W, tend, dt):    
   
    y = np.linspace(0,Ly,Ny)
    z = np.linspace(0,Lz,Nz)
    dy = y[1]-y[0]
    dz = z[1]-z[0]

    Y,Z = np.meshgrid(y,z)

    #u0 = lambda y,z: np.cos(omega0*y) * np.sin(omega0*z)
    u0 = lambda y,z: np.exp(y/(2*V) + z/(2*W))


    #plt.contourf(Y,Z,u0(Y,Z))

    #plt.show()


    t=0
    cfly=V*dt/dy
    cflz=W*dt/dz


    u = np.zeros([Ny,Nz])
    u [:, :]=u0 (Y, Z)

    #*********************** Boundary conditions *********************
    #n=np.linspace(0,Ly+2*dy,Ny+2)
    #m=np.linspace(0,Lz+2*dz,Nz+2)
    ######################### Left side wall #########################

    l = np.exp(-t+z/(2*W))
    u [: , 0] = l

    ######################### Right side wall ########################

    r = np.exp(-t+Ly/(2*V)+z/(2*W))
    u [: , -1] = r

    ########################### Lower wall ###########################

    L = np.exp(-t+y/(2*V)) 
    u [0 , :] = L

    ########################### Upper wall ###########################

    U = np.exp(-t+y/(2*V)+Lz/(2*W))
    u [-1 , :] = U

    solution = []
    solution.append(u)

    # while loop for progrecing in time
    while t < tend:

        u_old = solution [-1] # using the last row of solution for calculating new time step
        u_new_12 = u_old.copy ()
        u_new = u_old.copy ()
        u_new_12 [1 : -1, 1 : -1] = u_old [1 : -1, 1 : -1] - cfly * (u_old [1 : -1, 1 : -1] - u_old [1 : -1, : -2])
        u_new [1 : -1, 1 : -1] = u_new_12 [1 : -1, 1 : -1] - cflz * (u_new_12 [1 : -1, 1 : -1] - u_new_12 [ : -2, 1 : -1])

        # set boundary conditions for new time step
        # Left side wall
        l = np.exp(-t+z/(2*W)) 
        u_new [: , 0] = l

        # Right side wall
        r = np.exp(-t+Ly/(2*V)+z/(2*W))
        u_new [: , -1] = r

        # Lower wall
        L = np.exp(-t+y/(2*V)) 
        u_new [0 , :] = L

        # Upper wall
        U = np.exp(-t+y/(2*V)+Lz/(2*W))
        u_new [-1 , :] = U

        solution.append(u_new)

        t += dt


    #------------Ploting the solution as animation-----------------
    #anim.my_animation(solution,dt,Y,Z)
    #--------------Ploting the error as animation-----------------
    #anim.my_animation(error,dt,Y,Z)
    return solution
#twoD_linear_advection(30,30,1,1,1,1,5,0.001)


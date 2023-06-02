import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from anim import Anim

def analytical_solution (Ny, Nz, Ly, Lz, V, W, tend, dt):

    y = np.linspace(0,Ly,Ny)
    z = np.linspace(0,Lz,Nz)

    Y,Z = np.meshgrid(y,z)


    t=0

    u0 = np.exp(-t + Y/(2*V) + Z/(2*W))

    u = np.zeros([Ny,Nz])



    solution = []
    solution.append(u0)

    # while loop for progrecing in time
    while t < tend:

        u = np.exp(-t + Y/(2*V) + Z/(2*W))

        solution.append(u)

        t += dt

    #------------Ploting the solution as animation-----------------
    #Anim().my_animation(solution,dt,Y,Z)
    #--------------------------------------------------------------
    return solution

#analytical_solution (30,30,1,1,1,1,5,0.001)





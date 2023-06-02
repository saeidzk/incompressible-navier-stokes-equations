import Analytical
import numpy as np
import matplotlib.pyplot as plt
import main_2advection_operators_splitting
import dask
from dask import delayed

class Eror:
    
    @dask.delayed
    def error_func (Ny_start, Nz_start, Ny_end, Nz_end, Ly, Lz, step,
                    V, W, tend, dt):

        """ This function calculate the error in center point of the box for velocity
            for different numbers of mesh and plot the error aganst mesh number
        The input arguments for the function are:
        Ny_start = The first number of mesh in y direction
        Nz_start = The first number of mesh in z direction
        Ny_end   = The last number of mesh in y direction
        Nz_end   = The last number of mesh in z direction
        Ly       = y direction length
        Lz       = z direction length
        step     = Number of sampling
        For Example for (Ny_start=20,Nz_start=20,Ny_end=100,Nz_end=100,1,1,step=10): it calculates the error of velocity for
            10 different numbers of mesh 20*20, 30*30, 40*40, 50*50, 60*60, 70*70, 80*80
            , 90*90, 100*100
        """
        y_mesh_list = dask.delayed(list(range(Ny_start, Ny_end+step,step)))
        z_mesh_list = dask.delayed(list(range(Nz_start, Nz_end+step,step)))
        i = 0
        error = []
        mesh = []
        for n in y_mesh_list:
            print (i)
            m = z_mesh_list [i]
            print (n*m)
            sol_ana = dask.delayed(np.array(Analytical.analytical_solution 
                            (n,m,Ly=Ly,Lz=Lz,V=V,W=W,tend=tend,dt=dt)))
            
            sol_num = dask.delayed(np.array(main_2advection_operators_splitting.twoD_linear_advection
                            (n,m,Ly=Ly,Lz=Lz,V=V,W=W,tend=tend,dt=dt)))

            subt = (np.abs (sol_ana[70,:,:]-sol_num[70,:,:]))**2
            print (np.shape(subt))
            err = np.sqrt((np.sum(subt)))/(n*m)

            i += 1
            error.append(err)
            mesh.append(n*m)
        return error, mesh


    er, mesh= error_func (50,50,300,300,Ly=1,Lz=1,step=30,V=1,W=1,tend=0.075,dt=0.001)
    
    error = np.array(er)
    mesh = np.array(mesh)
    ##------------------Fitting a first order line to the data--------------
    coefficients = np.polyfit(np.log10(mesh), np.log10(error), 1)
    slope, intercept = coefficients
    def fitted_function (mesh, intercept, slope):
        return 10**(intercept) * mesh**(slope)
    
    x_values =  np.linspace(mesh.min(), mesh.max())
    y_fitted = fitted_function(x_values, intercept, slope)
    #--------------------Plot the scatter plot and the fitted function
    plt.figure(figsize=(7,4.5))
    plt.scatter(mesh,error)
    plt.plot(x_values,y_fitted, 'r')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(['Error', 'First order fit'])
    plt.xlabel('log (Number of mesh)')
    plt.ylabel('log (Error)')
    plt.title ('2D Linear Advection Numerical vs Analytical solution error', fontsize =12)
    
    plt.grid(linestyle='dotted')
    plt.savefig('Error.png',dpi=300)
    plt.show()
    
    print (mesh)
    print (error)    


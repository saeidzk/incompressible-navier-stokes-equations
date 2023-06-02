For running Lid driven cavity and Rayleigh benard convection solve lid_driven_cavity.py and rayleigh_benard.py.

1. Open simulation.py for setting up input parameters and discritization schemes:
    a) call_inputvars: number of nodes, number of iterations, 
                       pressure_poisson_iterations, TIME_STEP_LENGTH, 
                       KINEMATIC_VISCOSITY, DENSITY
                       
    b) call_mesh_grid: Prints grid, and returns element length
    
    c) call_discritization_schemes: shift between central_difference and upwind
    
2.  #Parameters: beta = 0.0, temperature dependence is off
                 beta -> [0,1]

3.  Solution loop: 

    a) #Intial conditions: u, v, P matrices are intialized with zeros. using the
                               function matrix_intialization. By defining
                               zero_intialization = False, and passing a value
                               to intial_value = value, we can intialize matrices
                               with non_zero matrices.
                               
    b) #Selecting up discretization schemes: calls the call_discritization_schemes
    
    c) Boundary_update: Contains three functions: velocity_boundary_x(u_tent),
                        velocity_boundary_y(v_tent),  pressure_boundary(p_next),
                        temperature_boundary(T_next).
                        
                       
                        
    d) #modify timestep based on CFL number: If the CFL number is greater than 1
                        in x or y direction then timestep is recalculated.
                        
                        
4.  Test:

    a) time_step_length > 0.001 (Check under def test_input(input_return_list: list))
    b) cfl_x < 1 and cfl_y <1 (check test_CFL_number_calculation) 

from input_Navier import Navier_stokes_variables

def test_for_CICD():
    NX = 20
    NY = 20
    DOMAIN_SIZE_X = 0
    N_ITERATIONS = 0
    N_PRESSURE_POISSON_ITERATIONS = 0
    TIME_STEP_LENGTH = 0
    STABILITY_SAFETY_FACTOR = 0
    KINEMATIC_VISCOSITY = 0
    DENSITY = 0
    y = Navier_stokes_variables.input_variables(NX, NY, DOMAIN_SIZE_X, N_ITERATIONS, N_PRESSURE_POISSON_ITERATIONS, TIME_STEP_LENGTH, STABILITY_SAFETY_FACTOR, KINEMATIC_VISCOSITY, DENSITY)

    all(isinstance(x, int) for x in y)

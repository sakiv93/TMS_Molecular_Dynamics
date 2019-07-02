def LJ_potential(r, sigma, epsilon):
    """Compute the potential energy
    
    Parameter:
    ----------
    r:       point of evaluation at distance `r` away from the atom
    sigma:   length scale parameter
    epsilon: scaling parameter for energy
    
    Returns: potential energy
    """
    D=sigma/r
    return  4*epsilon*(D**12-D**6)


def LJ_force(r, sigma, epsilon):
    """Compute the interatomic force
    
    Parameter:
    ----------
    r:       point of evaluation at distance `r` away from the atom
    sigma:   length scale parameter
    epsilon: scaling parameter for energy
    
    Returns: force value
    """  
    D=sigma/r 
    return  24*(epsilon/sigma)*(2*D**13-D**7)
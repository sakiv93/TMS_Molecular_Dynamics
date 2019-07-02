import matplotlib.pyplot as plt
import numpy as np


from ex2 import LJ_potential,LJ_force


def do_time_integration_step(time_step, y_old, dydt):
    """ Perform an explicit Euler time integration step

    Parameters
    ----------
    time_step: time difference between two steps (float)
    dydt :     the 1D numpy array dy/dt = [dy1/dt, dy2/dt]
    y_old :    1D numpy.ndarrayvector with values from previous time step
    """
    y_new = y_old+time_step*(dydt)
    return y_new


def vector_of_derivatives(y, sigma, epsilon, mass):
    """ Creates a numpy array with the two ODE varialbes y1 and y2

    Parameters
    ----------
    y :  the 1D numpy.ndarray [y1, y2] 
    sigma, epsilon : the LJ parameter
    mass :      atom's mass
    """
    dydt = np.array([(24*epsilon/mass*sigma)*(2*(sigma/y[1])**13-(sigma/y[1])**7),y[-1]]) 
    #print(dydt) 
    return dydt


# Here are some reasonable parameters and initial values
time_step = 1e-17  # s
total_time = 4e-12
sigma=3.40510e-10
kb=1.3806488e-23
epsilon=120*kb
mass=39.948*1.66054e-27
y_init = np.array([0., 1.3 * sigma])

# Do the time integration in a loop and store the results in a list
all_times = np.arange(0, total_time+time_step, time_step)

y = [y_init]
#print(y)
for time in all_times[1:]:
    y_new=do_time_integration_step(time_step, y[-1], vector_of_derivatives(y[-1], sigma, epsilon, mass))
    y.append(y_new)

y = np.array(y)  # convert from list to ndarray
#print(len(all_times))
#print(y)
position=y[:,1]

# plot the results
fig,ax=plt.subplots()
ax.plot(all_times,y[:,1])
ax.set_ylim(-5e-10,5e-10)
plt.show()

#ax.axhline(r0)

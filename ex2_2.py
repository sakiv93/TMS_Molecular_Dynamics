
import numpy as np 
import matplotlib.pyplot as plt 
from time import sleep


from ex2_1 import LJ_potential,LJ_force
def do_time_integration_step(time_step,old_position,old_velocity,old_acceleration):
    ##Do explicit euler time integartion step and return the updated positions and velocities
    new_velocity=old_velocity+old_acceleration*time_step
    new_position=old_position+old_velocity*time_step+0.5*old_acceleration*time_step**2
    return new_position,new_velocity

def get_acceleration(position,sigma,epsilon,mass):
    #this only works for 2 atoms!!!!!
    assert position.size==2  #This function works only for 2 atoms
    distance=position[1]-position[0]
    force0=LJ_force(-distance,sigma,epsilon)
    force1=LJ_force(+distance,sigma,epsilon)
    acceleration=np.array([force0/mass,force1/mass])
    #print(force0,force1)
    #exit(0)
    return acceleration





time_step = 1e-15  # s
total_time = 4e-12
sigma=3.40510e-10
kb=1.3806488e-23
epsilon=120*kb
emu=1.66054e-27
mass=4.0026*emu
r0=(2**(1/6))*sigma  #equilibrium distance
n_steps=int(total_time/time_step)
time_step=(total_time/n_steps)  #adjust time step such that n_steps+time_step is exactly total_time 

#initial position of all atoms
position=np.array([0.,1.3*sigma])
velocity=np.array([0.,0.])

#create a list for all time steps
positions=[position]
velocities=[velocity]
times=[0]

plt.ion()
fig,(ax0,ax1)=plt.subplots(ncols=2,figsize=(9,4))
fig.canvas.draw()

for n_step in range(n_steps):
    old_position=positions[-1]
    old_velocity=velocities[-1]

    #apply boundary conditiond
    old_position[0]=0
    old_velocity[0]=0

    old_acceleration=get_acceleration(old_position,sigma,epsilon,mass)
    new_position,new_velocity=do_time_integration_step(time_step,old_position,old_velocity,old_acceleration)

    positions.append(new_position)
    velocities.append(new_velocity)
    times.append((n_step+1)*time_step)
    if n_step%15==0:
        ax0.clear()
        ax0.plot(positions[-1],[0,0],lw=0,marker='o',c='C0')
        ax0.set(xlim=(-2*r0,2*r0))

        ax1.clear()
        ax1.plot(times,positions,c='C3')
        ax1.axhline(r0,ls='--')
        ax1.set(xlim=(0,total_time))
        #re-render the figure to give the GUI the chance to update
        fig.canvas.flush_events() 
        sleep(0.001)

#make sure that the last plot is kept


# fig,ax=plt.subplots(figsize=(9,5))
# ax.plot(times,positions)
plt.ioff()
plt.show()


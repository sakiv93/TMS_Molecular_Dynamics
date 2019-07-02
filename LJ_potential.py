import numpy as np 
import matplotlib.pyplot as plt 


# Leonard jones potential function definition
def LJ_Potential(sigma,fixed_atom,surrounding_atom,depth):
    distance=surrounding_atom-fixed_atom
    distance_sigma=distance/sigma
    LJP=4*depth*distance_sigma**(-6)*(distance_sigma**(-6)-1)
    return LJP

# Force function definition
def LJ_Force(sigma,fixed_atom,surrounding_atom,depth):
    distance=surrounding_atom-fixed_atom
    distance_sigma=distance/sigma
    LJF=24*(depth/distance)*distance_sigma**(-6)*((2*distance_sigma**(-6))-1)
    return LJF

#input parameters
sigma=0.34e-9                               #m
depth=1.6                                   #kilojoules per mole  #Depth of potential well
fixed_atom=0
surrounding_atom=sigma*np.linspace(0.01,6,100)


#Potential function call
potentials=LJ_Potential(sigma,fixed_atom,surrounding_atom,depth)

#Force function call
forces=LJ_Force(sigma,fixed_atom,surrounding_atom,depth)



fig, ax = plt.subplots(ncols=2,figsize=(15,5))
ax[0].plot(surrounding_atom/1e-9,potentials)
ax[0].set_ylim(-3*depth, 3*depth)
ax[0].set_xlabel('position of atom (nm)')
ax[0].set_ylabel('LJ Potential $\phi$')
ax[1].plot(surrounding_atom/1e-9,forces)
ax[1].set_ylim(-3*depth/sigma, 3*depth/sigma)
ax[1].set_xlabel('position of atom (nm)',fontsize='large')
ax[1].set_ylabel('Force')
#print(potentials)
#print(forces)

#Use this style for setting limits labels etc.,
#ax.set(ylim=(),
#       xlabel='',
#       ylabels='')
ax[0].grid(True)
ax[0].plot(sigma/1e-9,0,marker='*',color='0')
plt.show()






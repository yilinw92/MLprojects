import matplotlib
import numpy as np
import matplotlib.cm as cm
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the seed to be reproductive
np.random.seed(8675309)

# rcParams: rc settings in python for controlling matplotlibrc configuration file
# Change the direction of ticks towards out
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

#Create grid and multivariate normal
delta = 0.1                     # define step length
x = np.arange(-5.0, 5.0, delta) # define the interval range for x
y = np.arange(-5.0, 5.0, delta) # define the interval range for y
X, Y = np.meshgrid(x, y)        # create grid

# Resize the size of X
pos = np.empty(X.shape + (2,))  
pos[:, :, 0] = X; pos[:, :, 1] = Y

Z = multivariate_normal( [1.0,1.0], [[2, -1], [-1, 1]])

# Plot the contours of 2D Gaussian PDF
plt.figure()
CS = plt.contour(X, Y, Z.pdf(pos), 6,
                 linewidths = np.arange(.5, 4, .5),
                 colors = ('r','green','blue',(1, 1, 0),'#afeeee','0.5')
                 )
plt.clabel(CS, fontsize = 9, inline = 1)
plt.title('Contour of 2D Gaussian PDF')
CB = plt.colorbar(CS, shrink=0.8, extend='both')

# Plot the surface.
# Make a 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, 
                Z.pdf(pos), 
                cmap = cm.coolwarm, 
                linewidth = 0)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
cset = ax.contour(X, Y, 
                  Z.pdf(pos), 
                  zdir = 'x', 
                  offset = -5, 
                  cmap = cm.coolwarm)
cset = ax.contour(X, Y, 
                  Z.pdf(pos),
                  zdir = 'y', 
                  offset = 5, 
                  cmap = cm.coolwarm)
plt.title('Surface Plot of 2D Gaussian PDF')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
plt.show()
import matplotlib
import numpy as np
import matplotlib.cm as cm
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

# Set required value to parameters
mean1 = [0.0,0.0]
cov1 = [[1,0.1],[0.1,1]]
mean2 = [1.0,1.0]
cov2 = [[1.0,-0.1],[-0.1,1.0]]

# Initialize the matrix and predefine the size of the input dataset
syntheticData21 = np.zeros((100,2))
syntheticData22 = np.zeros((100,2))

# Set the seed to be reproductive
np.random.seed(8675309)

# Generate 100 random data points 
for ii in range(0,100):
    syntheticData21[ii,:] = np.random.multivariate_normal(mean1,cov1,size=(1,))
    syntheticData22[ii,:] = np.random.multivariate_normal(mean2,cov2,size=(1,))

# Scatter Plot of two datasets  
fig2, ax2 = plt.subplots()
sc21= ax2.scatter(syntheticData21[:,0], 
                  syntheticData21[:,1], 
                  marker='o', 
                  color='blue',
                  s=5)
sc22=ax2.scatter(syntheticData22[:,0], 
                 syntheticData22[:,1], 
                 marker='o', 
                 color='orange',
                 s=5)
# Plot the mixture centers as Xs
ax2.scatter( 1, 1, marker='x', color='orange',s=50)

ax2.scatter( 0, 0, marker='x', color='blue',s=50)
plt.axis('equal')
plt.legend((sc21, sc22),
           ('Class 1', 'Class 2'),
           scatterpoints=1,
           loc='upper right',
           ncol=3,
           fontsize=8)
plt.title('Scatter plot of 200 observations from two different 2D Normal Distribution')
plt.show()
import matplotlib
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

# Set required values to parameters
mean4 =[2.0,5.0]
cov4 = [[1,0.-0.1],[-0.1,1]]

# Initialize and predefine the input data
syntheticData41 = np.zeros((10,2))

# Generate 10 random 2D data points 
for ii in range(0,10):
    syntheticData41[ii,:] = np.random.multivariate_normal(mean4,cov4,size=(1,))

# Calculate sample mean and sample variance
sample_mean4 = np.mean(syntheticData41, axis = 0)
sample_cov4 = np.var(syntheticData41, axis = 0)

# Initialize dataset
syntheticData41_standardize = np.zeros((10,2))

# Standardize input data
for i in range(0,2):
    syntheticData41_standardize[:,i] = (syntheticData41[:,i] - np.ones((1,10))*sample_mean4[i])/sample_cov4[i]
    
# Scatter Plot of original data
fig41, ax41 = plt.subplots()
sc41= ax41.scatter(syntheticData41[:,0], 
                  syntheticData41[:,1], 
                  marker='o', 
                  color='blue',
                  s = 10)
ax41.scatter( 2, 5, marker='x', color='blue')

ax41.set_xlim(0, 5)
ax41.set_ylim(2, 8)
plt.title('Scatter Plot of Original Data X')
plt.show()

# Scatter Plot of the standardized data
fig42, ax42 = plt.subplots()
sc42=ax42.scatter(syntheticData41_standardize[:,0], 
                 syntheticData41_standardize[:,1], 
                 marker='o', 
                 color='orange',
                 s = 20)
ax42.scatter( 0, 0, marker='x', color='orange')

ax42.set_xlim(-2, 3)
ax42.set_ylim(-2, 2)
plt.title('Scatter Plot of Standardized Data X')
plt.show()
import matplotlib
import numpy as np
import matplotlib.cm as cm
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

# Initialize and predefine the size of input datas
syntheticData31 = np.zeros((100,1))
syntheticData32 = np.zeros((100,1))
syntheticData33 = np.zeros((100,1))

# Set the seed to be reproductive
np.random.seed(8675309)

# Generate 100 random data points
for ii in range(0,100):
    syntheticData31[ii] = np.random.uniform(-5,5,1)
    syntheticData32[ii] = 0.1*syntheticData31[ii,:]**3 + 3
    syntheticData33[ii] = syntheticData32[ii] + np.random.standard_normal(1)
    
# Scatter Plot of the Ground-true data compared with the noisy data
fig3, ax3 = plt.subplots()
sc31= ax3.scatter(syntheticData31, 
                  syntheticData32, 
                  marker='o', 
                  color='blue',
                  s = 5)
sc32=ax3.scatter(syntheticData31, 
                 syntheticData33, 
                 marker='o', 
                 color='orange',s = 5)
plt.legend((sc31, sc32),
           ('Ground-true','Observed'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
ax3.set_xlim(-5, 5)
ax3.set_ylim(-16.5, 16.5)
plt.title('Scatter plot of 100 noisy and 100 ground-truth overvations')

plt.show()
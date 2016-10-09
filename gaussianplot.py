
import math          # to calculate sqrt
import matplotlib.pyplot as plt   # to plot graph
import matplotlib.mlab as mlab      # to use the already defined normalized gaussian function 
import numpy as np   # to define values of x to be plotted

mu = 30  
variance = 12
sigma = math.sqrt(variance)
x = np.linspace(-200,200,1000)     # 1000 values of x are plotted from x=-200 to x=200 )

plt.plot(x,mlab.normpdf(x,mu,sigma))    # predefined  normal function
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x|'+str(mu)+','+str(sigma)+')')     # f(x| mean, standard deviation)
plt.show()





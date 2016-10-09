#!/usr/bin/python
# to use the mathematical constant e
import math

# to assign values to the abscissa of the plot 
import numpy as np

#to plot the distribution      
import matplotlib.pyplot as plt 

# lambda = average number of events in a fixed time 
l = int(input('enter average no. of events in a fixed time interval - l for the distr. f(k,l) : '))

# range of x values for which P(x) is calculated  - which is 0 to 20 (21 values) here
x = np.linspace(0,20,21)     
y = []

# iterated k+1 times to include integers in the interval [0,k]
i=0
while (i<21):
	# P(x) = e^(-l).(l^x)/x!                      
	a = (math.exp(-l)*(l**i))/math.factorial(i)   
	y.append(a)
	i += 1

plt.plot(x,y)
plt.title('Poisson distribution P{'+str(l)+'} (x ) :') 
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

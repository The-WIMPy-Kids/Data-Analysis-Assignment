import numpy as np
import matplotlib.pyplot as plt
import math

#import data from the file,store it in a 2d array
data = np.genfromtxt('recoilenergydata_EP219.csv' , delimiter = ',');

#create array for energy and number of events.
energy = []
number = []
num_of_pts = len(data)
signal=[]
likel=[]
l=0
#store the energy and number of events in two different lists
for i in range(num_of_pts):
	energy.append(float(data[i][0]))
	number.append(float(data[i][1]))

#create a list of background events only using the formula for only background events
bgnumber = []
for i in range (0,40):
	n = 1000 * np.exp((-1) * (i+0.5) / 10 )
	bgnumber.append(n)

#Find the log-likelihood for different values of sigma
sigma = np.linspace(0,1,1000)
for s in sigma:
#Generate the signal only using the formula for only signal
	l = 0
	signal = [0,0,0,0,0]
	for i in range (5,25):
		if i < 15:
			n = s * 20 * (i + 0.5 - 5)
		else :
			n = s * 20 * (25 - i - 0.5)
		signal.append(n)
	for i in range(25,40):
		n=0
		signal.append(n)

#Calculate the log likelihood function for histograms.
	for i in range(0,40):
		d = number[i]
		t = signal[i]
		b = bgnumber[i]
		l = l + (d* np.log(b+t) - (b + t))
	likel.append(l)

#Block to find the maximum log likelihood and the sigma for which log l is max.
l=likel[0]
nmax = 0
for i in range(len(likel)):
	if(l<likel[i]):
		l = likel[i]
		nmax = i

#Block to find the 1-sigma interval for value of sigma.
lower=0
upper=0
for i in range(len(likel)):
	if(likel[i] > likel[nmax] -0.5) :
 		lower = i
		break
for i in range(177,1000):
	if(likel[i] < likel[nmax] -0.5):
		upper = i
		break
#Output and plots
print(sigma[nmax])
print(likel[nmax])
print(sigma[lower])
print(sigma[upper])
plt.plot(sigma,likel)
plt.xlabel(r"$\sigma$")
plt.ylabel('log(L)')
plt.text(0.6,50750, r"Maximum at $\sigma = $ 0.176")
plt.show()



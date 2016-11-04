import numpy as np
import matplotlib.pyplot as plt
import math

#import data from the file,store it in a 2d array
data = np.genfromtxt('recoilenergydata_EP219.csv' , delimiter = ',');

#create array for energy and number of events.
energy = []
number = []
num_of_pts = len(data)
sigma = 0.01

#store the energy and number of events in two different lists
for i in range(num_of_pts):
	energy.append(float(data[i][0]))
	number.append(float(data[i][1]))

#Plot histogram of the data
plt.hist(range(0,40) , weights = number , bins =40)
plt.title('Histogram of recoil energy data')
plt.xlabel('Recoil Energy (KeV)')
plt.ylabel('Number of events')

#create a list of background events only using the formula for only background events
bgnumber = []
for i in range (0,40):
	n = 1000 * np.exp((-1) * (i+0.5) / 10 )
	bgnumber.append(n)

#Generate the signal only using the formula for only signal
signal = [0,0,0,0,0]
for i in range (5,25):
	if i < 15:
		n = sigma * 20 * (i + 0.5 - 5)
	else :
		n = sigma * 20 * (25 - i - 0.5)
	signal.append(n)
for i in range(25,40):
	n=0
	signal.append(n)

#Net number of events for signal + background 
total = []

for i in range(0,40):
	n = bgnumber[i] + signal[i]
	total.append(n)
	
#plot the data
plt.hist(range(0,40) , weights = total , bins =40)
plt.title('Histogram of recoil energy data assuming background and signal')
plt.xlabel('Recoil Energy (KeV)')
plt.ylabel('Number of events')
plt.text(30,900, r"$\sigma = $"+str(sigma) + "fb")
plt.show()




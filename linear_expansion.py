import numpy as np
import matplotlib.pyplot as plt
#import data from the file and store it in data
#data is an array whose each element is 2-array
data = np.genfromtxt('linearexpansion.csv', delimiter = ',')
#create array for temperature and length
temp = []
length = []
for point in range(len(data)):
    temp.append(float(data[point][0]))
    length.append(float(data[point][1]))
plt.figure(1)
plt.title("Scatter plot of lengths vs temperature")
plt.plot(temp, length, 'ro')
plt.xlabel("Temperature ("+r"$^0C$)")
plt.ylabel("Length (mm)")
plt.show()

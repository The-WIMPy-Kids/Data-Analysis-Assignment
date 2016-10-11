#This uses the iterative method.
#For the analytical method checkout the analytical branch
import numpy as np
import matplotlib.pyplot as plt
#import data from the file and store it in data
#data is an array whose each element is 2-array
data = np.genfromtxt('linearexpansion.csv', delimiter = ',')
#create array for temperature and length
temps = []
lengths = []
num_of_data_pts = len(data)
for point in range(num_of_data_pts):
    temps.append(float(data[point][0]))
    lengths.append(float(data[point][1]))
#Finding the maximum and minimum values of length:
#This will help in defining a range for m and c
#Length = m(temp) + c
#We know in general that length increases with temperature.
#So, the max_index is most likely to be lying among the last 1/3rd indices.
#Similarly, the min_index is most likely to be among the first 1/3rd indices.
#Even if they don't, we still get a very good estimate for m because m won't be among the extreme values. We just need a  good range to search in.

#Considering the last 1/3rd indices:
max_index = int((num_of_data_pts*2)/3)
for l in range(int((num_of_data_pts*2)/3),num_of_data_pts):
#(num_of_data_pts*2)/3 will always be an integer(due to truncation), so we are safe.
    if lengths[l] > lengths[max_index]:
        max_index = l
#Considering the first 1/3rd indices:
min_index = 0
for l in range(int(num_of_data_pts/3)):
    if lengths[l] < lengths[min_index]:
        min_index = l
#max_index and min_index now store the indices of the max and min lengths respectively.
#Line joining point with minimum slope
max_slope = (lengths[max_index] - lengths[min_index])/(temps[max_index] - temps[min_index])
#min_slope will be zero. We know that length increases with temperature.

#line joing max and min points will have the least(including sign) intercept.
#for y = mx +c passing through (x1, y1) and (x2, y2), c = (x2y1-x1y2)/(x2-x1)
min_c = (temps[max_index]*lengths[min_index] - temps[min_index]*lengths[max_index])/(temps[max_index] - temps[min_index])
#max_c will correspond to the y co-ordinate of the maximum point.
max_c = lengths[max_index]
M = np.linspace(0, max_slope, 250)
C = np.linspace(min_c, max_c, 250)
m_best = 0.0
c_best = 0.0
#Initialising Least Square distance (LSq)to the worst possible condition
LSq = num_of_data_pts*((lengths[max_index] - min_c)**2)
i = 0
for m in M:
    for c in C:
        lsq = 0.0
        for l in range(num_of_data_pts):
            lsq = lsq + ((lengths[l] - (m*temps[l] + c))**2)
        if lsq < LSq:
            m_best = m
            c_best = c
            LSq = lsq

plt.figure(1)
plt.title("Scatter plot of lengths vs temperature")
plt.plot(temps, lengths, 'ro')
plt.xlabel("Temperature ("+r"$^0C$)")
plt.ylabel("Length (mm)")
bbox_props1 =  dict(boxstyle = "square, pad=0.4", fc = "w", ec = 'k', lw = 1)
plt.text(0.75, 1250, "slope : "+str(m_best)+" and intercept : "+str(c_best), size = 14, bbox = bbox_props1)
plt.plot([0, 10], [c_best, (m_best*10 + c_best)], color = 'g', linewidth = 2.0)
bbox_props2 =  dict(boxstyle = "square, pad=0.4", fc = "w", ec = 'k', lw = 1)
plt.text(3.5, 950, "At 15"+r"$^oC$, length = "+str(15*m_best + c_best)+"mm", size = 14, bbox = bbox_props2)
print("Linear extrapolation upto 15"+r"$^oC$ gives an expected length of "+str(15*m_best + c_best)+"mm")
#Linear extrapolation upto 15$^oC$ gives an expected length of 1336.96991312mm
plt.show()

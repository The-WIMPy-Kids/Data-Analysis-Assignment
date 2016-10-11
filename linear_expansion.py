import numpy as np
import matplotlib.pyplot as plt
import math
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
'''
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
'''
temp_sum = 0.0
for temp in temps:
    temp_sum = temp_sum + temp
length_sum = 0.0
for length in lengths:
    length_sum = length_sum + length
mean_temp = temp_sum/num_of_data_pts
mean_length = length_sum/num_of_data_pts
#Summation temp_i*length_i:
sum_ti_li = 0.0
#Summation (temp_i)^2:
sum_ti2 = 0.0
for i in range(num_of_data_pts):
    sum_ti_li = sum_ti_li + temps[i]*lengths[i]
    sum_ti2 = sum_ti2 + (temps[i]**2)
#The derivation of the following two formulae for m_best and c_best can be found in the report
m_best = (sum_ti_li - mean_temp*length_sum)/(sum_ti2 - num_of_data_pts*(mean_temp**2))
c_best = mean_length - m_best*mean_temp
#Making the scatter plot with the best-fit line
plt.figure(1)
plt.title("Scatter plot of lengths vs temperature")
plt.plot(temps, lengths, 'ro')
plt.xlabel("Temperature ("+r"$^0C$)")
plt.ylabel("Length (mm)")
#Text_box with m_best and c_best values
bbox_props1 =  dict(boxstyle = "square, pad=0.4", fc = "w", ec = 'k', lw = 1)
plt.text(0.20, 1275, "slope : "+str(m_best)+r"$\frac{mm}{^0C}$"+" and intercept : "+str(c_best)+r"$mm$", size = 10, bbox = bbox_props1)
#Plot the best-fit line
plt.plot([0, 10], [c_best, (m_best*10 + c_best)], color = 'g', linewidth = 2.0)
#Text_box with extrapolated length
bbox_props2 =  dict(boxstyle = "square, pad=0.4", fc = "w", ec = 'k', lw = 1)
plt.text(3.5, 950, "At 15"+r"$^0C$"+", length = "+str(15*m_best + c_best)+"mm", size = 12, bbox = bbox_props2)
print("Linear extrapolation upto 15"+"ºC"+" gives an expected length of "+str(15*m_best + c_best)+"mm")
print("m_best is "+str(m_best))
print("c_best is "+str(c_best))
#Linear extrapolation upto 15ºC gives an expected length of 1337.0421541416586
#Calculate single measurement error of lis:
sigma_li2 = 0.0
t_ext = 15 #degree Celsius
#First we technically calculate sum of squares of deviations from sample mean
for length in lengths:
    sigma_li2 = sigma_li2 + ((length - mean_length)**2)
sigma_li2 = sigma_li2/(num_of_data_pts-2)
#These formulae have been explained in the report
sigma2_y_ext = sigma_li2*((1.0/num_of_data_pts)+((mean_temp**2)+(t_ext**2))/(sum_ti2 - num_of_data_pts*(mean_temp**2)))
sigma_y_ext = math.sqrt(sigma2_y_ext)
sigma_li = math.sqrt(sigma_li2)
print("Error in li is " + str(sigma_li)+" mm"+"\n")
print("Error in Length at 15ºC is "+str(sigma_y_ext)+" mm")
plt.show()

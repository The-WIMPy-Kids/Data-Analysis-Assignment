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
#Choose the extrapolated temperature
t_ext = 15 #degree Celsius
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
plt.text(3.5, 950, "At "+str(t_ext)+r"$^0C$"+", length = "+str(t_ext*m_best + c_best)+" mm", size = 12, bbox = bbox_props2)
print("The estimate of the co-efficient of linear expansion is "+str(m_best)+"mm/ºC")
print("y - intercept of the best fit  "+str(c_best))
print("Linear extrapolation upto "+str(t_ext)+"ºC"+" gives an expected length of "+str(t_ext*m_best + c_best)+" mm")
#Linear extrapolation upto 15ºC gives an expected length of 1337.0421541416586
#Calculate the error in extrapolated value
sum_of_squares = 0.0
for i in range(num_of_data_pts):
    sum_of_squares = sum_of_squares + (lengths[i] - (m_best*temps[i] + c_best))**2
sigma_yi = math.sqrt(sum_of_squares/(num_of_data_pts-2))
print("Error in Length at "+str(t_ext)+"ºC is "+str(sigma_yi)+" mm")
plt.show()

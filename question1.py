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
m_sigma = []
c_sigma = []
#Block to find the minimum square distance , which is same as minimising chi_squared as we assume the standard deviation for all readings to be same.
for m in M:
    for c in C:
        lsq = 0.0
        for l in range(num_of_data_pts):
            lsq = lsq + ((lengths[l] - (m*temps[l] + c))**2)
	
        if lsq < LSq:
            m_best = m
            c_best = c
            LSq = lsq
print(LSq)
#Generate a small set of m and c values around m_best and c_best for estimating the 1-sigma ellipse.
M = np.linspace(m_best-10 , m_best+10 ,501)
C = np.linspace(c_best-20 , c_best+20 ,501) 

#Block to find those values of m and c for which the chi_squared is less than (chi_squared_min + 2).
#The standard deviation for each reading is estimated by (1/(N-2) * (Least_distance_squared)).So the required values of m and c are those for which chi_squared < (N/N-2)* (Least_distance_squared)
m_least = m_best + 10
m_great = m_best - 10
c_least = c_best + 20
c_great = c_best - 20
for m in M:
	if(m > m_best):
		m_best = m
		break
for m in M:
	for c in C:
		lsq = 0.0
		for l in range(num_of_data_pts):
			lsq = lsq + ((lengths[l] - (m*temps[l] +c))**2)
		if (lsq < ((num_of_data_pts) * LSq / (num_of_data_pts - 2))) :
			m_sigma.append(m)
			c_sigma.append(c)
#Find limits for m with c=c_best and c with m=m_best.
			if (m==m_best):
				if(c_least > c):
					c_least = c
			if (m==m_best):
				if(c_great < c):				
					c_great = c
			if (c==c_best):
				if(m_least > m):
					m_least = m
			if (c==c_best):
				if(m_great < m):
					m_great = m

#Output and Plots			
print(m_least,m_great)
print(c_least,c_great)
plt.figure()
plt.plot(m_sigma , c_sigma ,"o")
plt.plot(m_best , c_best , "ro")
plt.xlabel('m')
plt.ylabel('c')
plt.title('1- $\sigma $ ellipse in the m-c space')
plt.text(23,1000, r"$m_0$ = 22.93 , $c_0$ = 993.04")

#Block for 2-sigma ellipse.
M = np.linspace(m_best-20 , m_best+20,500)
C = np.linspace(c_best-25 , c_best+25,500)
for m in M:
	for c in C:
		lsq = 0.0
		for l in range(num_of_data_pts):
			lsq = lsq + ((lengths[l] - (m*temps[l] +c))**2)
		if (lsq < ((num_of_data_pts + 6) * LSq / (num_of_data_pts - 2))) :
			m_sigma.append(m)
			c_sigma.append(c)
plt.figure()
plt.plot(m_sigma , c_sigma ,"o")
plt.plot(m_best , c_best , "ro")
plt.xlabel('m')
plt.ylabel('c')
plt.title('2- $\sigma $ ellipse in the m-c space')
plt.text(23,1010, r"$m_0$ = 22.93 , $c_0$ = 993.04")
plt.show()

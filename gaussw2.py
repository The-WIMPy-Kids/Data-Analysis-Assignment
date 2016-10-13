#import matplotlib separately to configure ticks
import matplotlib as mpl
#for the sqrt fn import math
import math as math
#Inorder to plot
import matplotlib.pyplot as plt
#to use arange
import numpy as np
#for colourmap
import matplotlib.cm as cm
#to use the bivariate_normal function
import matplotlib.mlab as mlab

mpl.rcParams['xtick.direction'] = 'out'
#the ticks appearing above the label points now point outwards
mpl.rcParams['ytick.direction'] = 'out'

#Question 1a)
#Feed in the different parameters of the Gaussian
mu_x = 0.0
mu_y = 0.0
sigma_sqr_x = 9.0
sigma_sqr_y = 6.0
sigma_xy = -2.0
sigma_x = math.sqrt(sigma_sqr_x)
sigma_y = math.sqrt(sigma_sqr_y)
#small number inorder to get a smooth contour
delta = 0.025
#Define the range for x and y
x = np.arange(-7, 7, delta)
y = np.arange(-6.0, 6.0, delta)
#normal function takes only lists as input, so convert tuple to list
X0, Y0 = np.meshgrid(x, y)
Z0 = mlab.bivariate_normal(X0, Y0, sigma_x, sigma_y, mu_x, mu_y, sigma_xy)

plt.figure(1)
#Number of levels of a Contour
N = 10
cont = plt.contour(X0, Y0, Z0, N)
#Need to introduce inline labelling
plt.clabel(cont, inline = 5, fontsize = 8)
plt.title('Contour plot of the given Gaussian')
#Mark the mu_x, mu_y point on the plane
plt.plot(mu_x, mu_y, 'bo')
plt.vlines(mu_x, -6.0, mu_y, 'g', 'dashed')
plt.hlines(mu_y, -7.0, mu_x, 'g', 'dashed')
plt.xlabel(r"$\mu_x =$"+str(mu_x)+" and "+r"$\mu_y =$"+str(mu_y))
#define attributes of the text box
#Square box with a padding of 0.2 around the text
#White face colour and black edge colour with linewidth = 1
bbox_props1 =  dict(boxstyle = "square, pad=0.2", fc = "w", ec = 'k', lw = 1)
plt.text(3.8, 5.4, r"$\sigma^2_x=$"+str(sigma_sqr_x)+", "+r"$\sigma^2_y =$"+str(sigma_sqr_y)+", "+r"$\sigma_{xy} =$"+str(sigma_xy), ha="center", va="center", size = 14, bbox = bbox_props1)

#Question 1b)
#2D random number generator
plt.figure(figsize=(12, 9))
X1 = []
Y1 = []
num_of_pts = 50000
for i in range(num_of_pts):
    #use Numpy's multivariate_normal function
    x = np.random.multivariate_normal([0, 0], [[9, -2],[-2, 6]])
    X1.append(x[0])
    Y1.append(x[1])
#X, Y contain the X and Y co-ordinates of the randomly generated points.

#Question 1c)
num_of_bins2D = 250
#plot the 2D histogram with colour scheme inferno
plt.hist2d(X1, Y1, num_of_bins2D,cmap='inferno')
plt.colorbar()
plt.title('2D Histogram of Gaussian distributed random numbers')
bbox_props2 = dict(boxstyle = "square, pad=0.2", fc="w", ec="b", lw = 1)
plt.text(0,9,"No. of bins: "+r"$n_x$"+"= "+r"$n_y$"+"="+str(num_of_bins2D)+"; Number of points = "+str(num_of_pts), ha="center", va="center", size = 12, bbox = bbox_props2)

#Question 1d)
#Construct and Plot Z
Z1 =[]
#For calculating the mean value and standard deviation
Z_sum = 0.0
Z_sqr_sum = 0.0
for i in range(num_of_pts):
    Z1.append((1/50.0)*(6*(X1[i]**2)+4*X1[i]*Y1[i]+9*(Y1[i]**2)))
    Z_sum = Z_sum + Z1[i]
    Z_sqr_sum = Z_sqr_sum + (Z1[i]**2)
#Now calculate mean and std deviation from above values
mean_Z = Z_sum/num_of_pts
std_dev_Z = math.sqrt((Z_sqr_sum/num_of_pts)-(mean_Z**2))
plt.figure(3)
num_of_bins1D = 50
#Plot the histogram
plt.hist(Z1, num_of_bins1D, color = 'g')
plt.title("Histogram of "+r"$z=\frac{6x^2+4xy+9y^2}{50}$", size ='large')
plt.xlabel('No. of bins = '+str(num_of_bins1D))
plt.ylabel('Frequency')
#Mean and Standard deviation will be printed in a text box
bbox_props3 = dict(boxstyle = "square, pad=0.3", fc="w", ec="k", lw = 1)
plt.text(14,11000,r"$\mu_z=$"+str(mean_Z)+", "+r"$\sigma_z=$"+str(std_dev_Z), ha="center", va="center", size = 14, bbox = bbox_props3)
plt.show()

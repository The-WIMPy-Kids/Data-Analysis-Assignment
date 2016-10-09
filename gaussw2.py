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

#Feed in the different parameters of the Gaussian
#Define the range for x and y
mu_x = 0.0
mu_y = 0.0
sigma_sqr_x = 9.0
sigma_sqr_y = 6.0
sigma_xy = -2.0
sigma_x = math.sqrt(sigma_sqr_x)
sigma_y = math.sqrt(sigma_sqr_y)
#small number inorder to get a smooth contour
delta = 0.025
x = np.arange(-7, 7, delta)
y = np.arange(-6.0, 6.0, delta)
#normal function takes only lists as input, so convert tuple to list
X, Y = np.meshgrid(x, y)
Z = mlab.bivariate_normal(X, Y, sigma_x, sigma_y, mu_x, mu_y, sigma_xy)

plt.figure(1)
#Number of levels of a Contour
N = 10
cont = plt.contour(X, Y, Z, N)
plt.clabel(cont, inline = 5, fontsize = 8)
plt.title('Contour plot of the given Gaussian')
plt.plot(mu_x, mu_y, 'bo')
plt.vlines(mu_x, -6.0, mu_y, 'g', 'dashed')
plt.hlines(mu_y, -7.0, mu_x, 'g', 'dashed')
plt.xlabel(r"$\mu_x =$"+str(mu_x)+" and "+r"$\mu_y =$"+str(mu_y))
#define attributes of the text box
#Square box with a padding of 0.2 around the text
#White face colour and black edge colour with linewidth = 1
bbox_props1 =  dict(boxstyle = "square, pad=0.2", fc = "w", ec = 'k', lw = 1)
plt.text(3.8, 5.4, r"$\sigma^2_x=$"+str(sigma_sqr_x)+", "+r"$\sigma^2_y =$"+str(sigma_sqr_y)+", "+r"$\sigma_{xy} =$"+str(sigma_xy), ha="center", va="center", size = 14, bbox = bbox_props1)

plt.figure(2)
#2D random number generator
X = []
Y = []
num_of_pts = 50000
for i in range(num_of_pts):
    x = np.random.multivariate_normal([0, 0], [[9, -2],[-2, 6]])
    X.append(5*x[0])
    Y.append(5*x[1])
num_of_bins = 250
plt.hist2d(X, Y, num_of_bins,cmap='inferno')
plt.colorbar()
plt.title('2D Histogram of Gaussian distributed random numbers')
bbox_props2 = dict(boxstyle = "square, pad=0.2", fc="w", ec="b", lw = 1)
plt.text(0,45,"No. of bins: "+r"$n_x$"+"= "+r"$n_y$"+"="+str(num_of_bins)+"; Number of points = "+str(num_of_pts), ha="center", va="center", size = 12, bbox = bbox_props2)
plt.show()

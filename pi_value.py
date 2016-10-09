# for square root and actual pi value
import math         
# for generating random numbers(points)
import random 
# for making plots            
import matplotlib.pyplot as plt              
# function evaluates distance of point from (1,1) and returns true or false
def numincirc(x, y):    
	if (math.sqrt( (x-1)**2 + (y-1)**2)<= 1):   
		return True
	else:
		return False

 
 # creating and writing a file to record the 500 obtained values of meanpi
f = open('meanpifile9.txt','a')     
meanpi = []
# 500 experiments
num_of_exp=500
N=2000
j=0
while (j<num_of_exp):                      

	i=0
# counter to count the number of points inside Incircle
	circnum = 0                 
	while (i<N):
	# assigning a random decimal numbers between 0 and 2 to x coordinate of point               
		x = random.random()*2
		# similarly, for the y coord.         
		y = random.random()*2           
		point = numincirc(x, y)
		if (point==True):
			circnum += 1
		i += 1

#probability(point in circle = Area(Circle)/Area(Square)) = pi/4. => circnum/N = pi/4 => pi = 4*(circnum/N)
	pi = 4*(circnum/float(N))         
	meanpi.append(pi)
	# writing the value of pi to the text file 
	f.write('%f' % pi)           
	f.write(' ')
	
	j += 1

# error in measurement = sigma(meanpi) = sqrt [(p*(1-p)/N] where p= pi(actual)/4
a = math.pi*(4-math.pi)/16

# mperror => mean pi error           
mperror = math.sqrt(a/N)        

print ('The error in measurement is : ', mperror)

f.close()

# histogram with : mean pi values, no.of bins, type and width of each bar - is plotted
plt.hist(meanpi, 50, histtype='bar', rwidth=1)     

plt.xlabel('mean values of pi')      
plt.ylabel('frequency') 
plt.legend()
plt.title('Distribution of mean values of pi')
plt.show()

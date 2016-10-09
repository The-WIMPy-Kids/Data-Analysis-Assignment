import math 
import numpy as np
import matplotlib.pyplot as plt

#defining a function to calculate factorial
def f(i):
	j=1
	k=1
	while(j<=i):
		k=k*j
		j=j+1
	return k
# defining a function to calculate nCr
def nCr(n, r):                    
	return f(n)/(f(r)*f(n-r))
# n is obtained
n = int(input('enter the number of trials : '))
# p is entered
p = float(input('enter probability of success: ')) 

# x is an integer from 0 to n including both - a total of n+1 values
x = np.linspace(0,n,n+1) 
y = []

# assigning B{n,p}(x) of each x to y
i=0
while (i<n+1):
	y.append(nCr(n,i)*(p**i)*((1-p)**(n-i)))  
	i += 1 

plt.plot(x,y)

plt.title('B{'+str(n)+','+str(p)+'} (x)')
plt.xlabel('x')
plt.ylabel('B(x)')
plt.show() 





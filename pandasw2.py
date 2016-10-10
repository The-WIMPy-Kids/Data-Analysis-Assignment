#Question2
#Estimating the mean, assigning the error and calculating typical fluctuation about mean.
import math
#import data from given file
input = open('pandas.txt', 'r')
#Create an array to store panda weights
pandas = []
#Given 100 pandas, yet the code is general so can use any input file containing any number of pandas
#Number of pandas:
panda_num = 0
for weight in input:
    #Need to convert string to float:
    pandas.append(float(weight))
    #panda counter:
    panda_num = panda_num + 1
#Sum of weights:
weight_sum = 0.0
#Sum of squares of weights:
weight_sqr_sum = 0.0
for panda in pandas:
  weight_sum = weight_sum + panda
  weight_sqr_sum = weight_sqr_sum + (panda**2)

mean_weight = weight_sum/panda_num
#sum of squares of deviations:
sum_dev_sqr = 0.0
#sum of magnitudes of deviations:
dev_mag_sum = 0.0
for i in range(panda_num):
    sum_dev_sqr = sum_dev_sqr + ((pandas[i]-mean_weight)**2)
    dev_mag_sum = dev_mag_sum +abs(pandas[i]-mean_weight)
error_assigned = math.sqrt((1.0/(panda_num-1))*sum_dev_sqr)
#fluctuation about mean:
fluctuation = dev_mag_sum/panda_num
#create an output file to store acquired data
panda_out = open('panda_output.txt', 'w')
print("Mean weight is " + str(mean_weight)+"\n")
panda_out.write("Mean weight is " + str(mean_weight)+"\n")
print("Error assigned is " + str(error_assigned)+"\n")
panda_out.write("Error assigned is " + str(error_assigned))
print("Typical fluctuation about mean is " + str(fluctuation)+"\n")
panda_out.write("Typical fluctuation about mean is " + str(fluctuation))

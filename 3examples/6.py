# import modules
import numpy as np
import matplotlib.pyplot as plt
# create an array of random numbers
a = np.random.random(100)
#function to calculate mean and std
def calculateMeanAndStd(x):
	info = []
	info.append(np.mean(x))
	info.append(np.std(x))
	return info
#print mean and std dev
info = calculateMeanAndStd(a)
# mean,stdev lines in line graph
mean = [info[0] for x in range(101)]
stdev = [info[1] for x in range(101)]
# create line graph of data with
# blue dashes for points, blue squares for mean 
# green tiangles for stdev
plt.plot(a,'b--',mean,'bs',stdev,'g^')
#write text in plot
plt.text(0.5,info[0]+0.02,r'Mean')
plt.text(0.3,info[1]+0.02,r'Stdev')
# show line graph
plt.show()

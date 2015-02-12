# import modules
import numpy as np
import matplotlib.pyplot as plt
# Open a file and read floats
a = np.fromfile("data", dtype=int, count=-1, sep='')
# create a generator for intervals
g = [14*x for x in range(8)]
g[-1] += 2
#create a histogram
plt.hist(a,bins=g)
plt.xlabel('Interval')
plt.ylabel('Count')
#disply histogram
plt.show()
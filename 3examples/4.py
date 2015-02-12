# import modules
import numpy as np
import matplotlib.pyplot as plt
#array with 100 uniform random values
a = np.random.randint(1,101,100)
#create a line graph
plt.plot(a)
# Open a file
f = open("data", "wb")
#write array to file
f.write(a)
# Close opend file
f.close()
#disply histogram
plt.show()

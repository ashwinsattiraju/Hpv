# import modules
import numpy as np
import matplotlib.pyplot as plt
#array with 8000 random values
a = np.random.random(8000)
#reshape array into 20x20x20
np.reshape(a,(20,20,20))
#create a histogram
plt.hist(a,20)
#disply histogram
plt.show()
# import modules
import numpy as np
import matplotlib.pyplot as plt
#array with 8000 random values
a = np.random.random(8000)
#reshape array into 20x20x20
a = np.reshape(a,(20,20,20))
#compute average of slices 
avg_x = np.mean(a, axis=0)
avg_y = np.mean(a, axis=1)
avg_z = np.mean(a, axis=2)
# save images
plt.imshow(avg_x)
plt.savefig('xAvg.png')
plt.imshow(avg_y)
plt.savefig('yAvg.png')
plt.imshow(avg_z)
plt.savefig('zAvg.png')
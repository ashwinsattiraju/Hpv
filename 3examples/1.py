#import numpy module
import numpy
# crearw an array from 1 to 100
A = numpy.array(range(1,101))
#create a box plot
plt.boxplot(A)
#disply boxplot
plt.show()
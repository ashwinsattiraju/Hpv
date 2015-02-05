from netCDF4 import Dataset


def ndims():
 rootgrp = Dataset('tos_O1_2001-2002.nc','r')
 dims = rootgrp.dimensions
 dimlen = len(dims)
 print (str(dimlen))


ndims()

from netCDF4 import Dataset


def ndims():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	dimlen = len(dims)
 	print("No. of Dimensions: " + str(dimlen))

def get_global_dim_names():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	print ("Global dimensions name: ")
	for gnames in dims:
		print gnames

def get_global_dim_lens():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	print ("Global dimensions length: ")
	for gnames in dims:
		print ( str(dims) + ":")

		




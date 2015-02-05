from netCDF4 import Dataset

#return the number of dimensions 
def ndims():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	dimlen = len(dims)
 	print("No. of Dimensions: " + str(dimlen))

#names of the dimensions 
def get_global_dim_names():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	print ("Global dimensions name: ")
	for gnames in dims:
		print gnames

# lengths of the dimensions
def get_global_dim_lens():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	print ("Global dimensions length: ")
	for gnames in dims:
		print ( str(gnames) + " : " + str(len(dims[gnames])) )

#number of variables 
def nvars():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	vars = rootgrp.variables
	varlen = len(vars)
	print ("No. of Variables: "+ str(varlen))

#names of  variable
def get_var_names():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	for var in vars:
		print var
	

#dimensions of the input variable 'var' 
def get_var_dim_lens():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'lon'
	j = 0 
	for i in vars[var].ncattrs():
		j = j + 1
	print ("Dimensions of " + var + " : " + str(j))

#names of the dimensions for the variable 'var' 
def get_var_dim_names():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'tos'
	j = 0 
	for i in vars[var].ncattrs():
		print i


#number of grid points that have the variable 'var' defined
def get_num_of_points():
	rootgrp = Dataset('tos_O1_2001-2002.nc','r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'lon'
	print vars[var][:]

get_num_of_points()
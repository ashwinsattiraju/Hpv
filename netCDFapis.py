from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

#return the number of dimensions 
def ndims(fileName):
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	dimlen = len(dims)
 	print("No. of Dimensions: " + str(dimlen))

#names of the dimensions 
def get_global_dim_names():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	print ("Global dimensions name: ")
	for gnames in dims:
		print gnames

# lengths of the dimensions
def get_global_dim_lens():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	print ("Global dimensions length: ")
	for gnames in dims:
		print ( str(gnames) + " : " + str(len(dims[gnames])) )

#number of variables 
def nvars():
	rootgrp = Dataset(fileName,'r')
	vars = rootgrp.variables
	varlen = len(vars)
	print ("No. of Variables: "+ str(varlen))

#names of  variable
def get_var_names():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	for var in vars:
		print var
	

#dimensions of the input variable 'var' 
def get_var_dim_lens():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'lon'
	j = 0 
	for i in vars[var].ncattrs():
		j = j + 1
	print ("Dimensions of " + var + " : " + str(j))

#names of the dimensions for the variable 'var' 
def get_var_dim_names():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'tos'
	j = 0 
	for i in vars[var].ncattrs():
		print i


#number of grid points that have the variable 'var' defined
def get_num_of_points():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'lat'
	numPoint = vars[var].shape
	total = 1
	for i in numPoint:
		total *= (i+1)
	print "Number of Grid points: " , total
		
# return the number of cells that have the variable 'var' defined
def get_num_of_Cells():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'tos'
	numCells = vars[var].shape
	total = 1
	for i in numCells:
		total *= i
	print "Number of Cells : " , total

#  return the data array for the variable 'var'
def get_data():
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'tos'
	data_array = np.array(vars[var][:])
	print data_array

# plot the histogram of the variable 'var'
def plot_histogram(): 
	rootgrp = Dataset(fileName,'r')
	dims = rootgrp.dimensions
	vars = rootgrp.variables
	var = 'lon'

	data_array = np.array(vars[var][:])

	# For Tos variable give range as (270,310) - kelvin unit
	if var == 'tos':
		y , x= np.histogram(data_array,bins=50, range = (270,310))
	else:
		 y , x= np.histogram(data_array,bins=50, range = None)

	width = 0.9 * (x[1] - x[0])
	center = (x[:-1] + x[1:]) /2

	plt.bar(center, y, align='center', width=width)
	plt.show()


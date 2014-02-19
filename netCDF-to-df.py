# Convert netCDF4 4-dimensional temperature data to 2-dimensional stacked dataframe
# By: Matt Bartos

# This script is intended for use with CMIP3 and CMIP5 climate projection data. In this example, maximum daily temperature data is converted from a 4-dimensional netCDF dataset (where each temperature entry is indexed by 3 other variables: lat, lon and time) to a 2-dimensional pandas dataframe (where each temperature entry is indexed by a single integer, corresponding to a tuple of lat, lon and time).

import numpy as np
import pandas as pd
import netCDF4
	
# Import netcdf dataset

f_max = netCDF4.Dataset('Extraction_tasmax.nc', 'r')

# Separate projection scenarios into a list of 3-dimensional panels. Each object in lst_tasmax represents a different projection scenario (0-53).

lst_tasmax = []

def pop_tasmax(k,v):
	for i in range(k,v):
		lst_tasmax.append(pd.Panel(f_max.variables['tasmax'][i][:], items=f_max.variables['time'][:], major_axis=f_max.variables['lat'], minor_axis=f_max.variables['lon'][:]))
return lst_tasmax

pop_tasmax(0,3)

# Convert 3-dimensional panels to 2-dimensional dataframes

df_lst_tasmax = []

def df_tasmax(k,v):
	for i in range(k,v):
		df_lst_tasmax.append(lst_tasmax[i].to_frame())
return df_lst_tasmax

df_tasmax(0,3)

# Stack dataframe to create hierarchical index

stack_lst_tasmax = []

def stack_tasmax(k,v):
	for i in range(k,v):
		stack_lst_tasmax.append(df_lst_tasmax[i].stack())
return stack_lst_tasmax

stack_tasmax(0,3)

# Flatten hierarchical index, indexing each temperature reading to a single integer. Define column names, allowing merge and concatenation operations.

flat_lst_tasmax = []

def flatten_tasmax(k,v):
	for i in range(k,v):
		flat_lst_tasmax.append(stack_lst_tasmax[i].reset_index())
		flat_lst_tasmax[i].columns = ['lat', 'lon', 'time', 'tmax%s' % (i)]
return flat_lst_tasmax

flatten_tasmax(0,3)

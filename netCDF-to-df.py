# Convert netCDF4 to stacked dataframe
# By: Matt Bartos

import numpy as np
import pandas as pd
import netCDF4
	
#Import netcdf dataset

f_max = netCDF4.Dataset('Extraction_tasmax.nc', 'r')
f_min = netCDF4.Dataset('Extraction_tasmin.nc', 'r')

#netcdf -> 3-d panel -> stacked dataframe
#tasmax

lst_tasmax = []
lst_tasmin = []

def pop_tasmax(v):
	for i in range(0,v):
		lst_tasmax.append(pd.Panel(f_max.variables['tasmax'][i][:], items=f_max.variables['time'][:], major_axis=f_max.variables['lat'], minor_axis=f_max.variables['lon'][:]))
return lst_tasmax

pop_tasmax(3)
		
print lst_tasmax

df_lst_tasmax = []
df_lst_tasmin = []

def df_tasmax(v):
	for i in range(0,v):
		df_lst_tasmax.append(lst_tasmax[i].to_frame())
return df_lst_tasmax

df_tasmax(3)

stack_lst_tasmax = []
stack_lst_tasmin = []

def stack_tasmax(v):
	for i in range(0,v):
		stack_lst_tasmax.append(df_lst_tasmax[i].stack())
return stack_lst_tasmax

stack_tasmax(3)

flat_lst_tasmax = []
flat_lst_tasmin = []

def flatten_tasmax(v):
	for i in range(0,v):
		flat_lst_tasmax.append(stack_lst_tasmax[i].reset_index())
		flat_lst_tasmax[i].columns = ['lat', 'lon', 'time', 'tmax%s' % (i)]
return flat_lst_tasmax

flatten_tasmax(3)

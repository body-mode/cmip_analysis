# Convert netCDF4 4-dimensional temperature data to 2-dimensional stacked dataframe
# By: Matt Bartos

# This script is intended for use with CMIP5 climate projection data. In this example, maximum daily temperature data is converted from a 4-dimensional netCDF dataset (where each temperature entry is indexed by 3 other variables: latitude, longitude and time) to a 2-dimensional pandas dataframe (where each temperature entry is indexed by a single integer, corresponding to a tuple of latitude, longitude and time). The 2-dimensional dataframe for each scenario is then stored in an hdf5 file. From here, the ensemble average for each projection scenario is calculated.

import numpy as np
import pandas as pd
import netCDF4
	
# Import netcdf dataset

f_max = netCDF4.Dataset('Extraction_tasmax.nc', 'r')

# Separate projection scenarios into a list of 3-dimensional panels. Each object in lst_tasmax represents a different projection scenario (0-53).

lst_tasmax = []

def pop_tasmax(k,v):
	for i in range(k,v):
		lst_tasmax.append(pd.Panel(f_max.variables['tasmax'][i][:], items=f_max.variables['time'][:], major_axis=f_max.variables['latitude'], minor_axis=f_max.variables['longitude'][:]))
return lst_tasmax

pop_tasmax(0,133)

# Convert 3-dimensional panels to 2-dimensional dataframes

df_lst_tasmax = []

def df_tasmax(k,v):
	for i in range(k,v):
		df_lst_tasmax.append(lst_tasmax[i].to_frame())
return df_lst_tasmax

df_tasmax(0,133)

# Stack dataframe to create hierarchical index

stack_lst_tasmax = []

def stack_tasmax(k,v):
	for i in range(k,v):
		stack_lst_tasmax.append(df_lst_tasmax[i].stack())
return stack_lst_tasmax

stack_tasmax(0,133)

# Flatten hierarchical index, indexing each temperature reading to a single integer. Define column names, allowing merge and concatenation operations.

flat_lst_tasmax = []

def flatten_tasmax(k,v):
	for i in range(k,v):
		flat_lst_tasmax.append(stack_lst_tasmax[i].reset_index())
		flat_lst_tasmax[i].columns = ['latitude', 'longitude', 'time', 'tmax%s' % (i)]
return flat_lst_tasmax

flatten_tasmax(0,133)

# Store results in hdf5

store1 = pd.HDFStore('store1.h5')

for i in range(len(flat_lst_tasmax)):
	store1['flat_lst_tasmax_%s' % (i)] = flat_lst_tasmax[i]
	
# Merge rcp scenarios into rcp 2.6, 4.5 and 8.5 bins and store as hdf5

dflist26 = [store1['flat_lst_tasmax_2'],store1['flat_lst_tasmax_8'],store1['flat_lst_tasmax_9'],store1['flat_lst_tasmax_10'],store1['flat_lst_tasmax_11'],store1['flat_lst_tasmax_12'],store1['flat_lst_tasmax_23'],store1['flat_lst_tasmax_24'],store1['flat_lst_tasmax_35'],store1['flat_lst_tasmax_36'],store1['flat_lst_tasmax_37'],store1['flat_lst_tasmax_38'],store1['flat_lst_tasmax_39'],store1['flat_lst_tasmax_40'],store1['flat_lst_tasmax_41'],store1['flat_lst_tasmax_42'],store1['flat_lst_tasmax_43'],store1['flat_lst_tasmax_44'],store1['flat_lst_tasmax_65'],store1['flat_lst_tasmax_68'],store1['flat_lst_tasmax_72'],store1['flat_lst_tasmax_78'],store1['flat_lst_tasmax_79'],store1['flat_lst_tasmax_80'],store1['flat_lst_tasmax_90'],store1['flat_lst_tasmax_94'],store1['flat_lst_tasmax_98'],store1['flat_lst_tasmax_102'],store1['flat_lst_tasmax_103'],store1['flat_lst_tasmax_104'],store1['flat_lst_tasmax_112'],store1['flat_lst_tasmax_113'],store1['flat_lst_tasmax_114'],store1['flat_lst_tasmax_121'],store1['flat_lst_tasmax_126'],store1['flat_lst_tasmax_130']]

dflist45 = [store1['flat_lst_tasmax_0'],store1['flat_lst_tasmax_3'],store1['flat_lst_tasmax_6'],store1['flat_lst_tasmax_13'],store1['flat_lst_tasmax_14'],store1['flat_lst_tasmax_15'],store1['flat_lst_tasmax_16'],store1['flat_lst_tasmax_17'],store1['flat_lst_tasmax_25'],store1['flat_lst_tasmax_26'],store1['flat_lst_tasmax_31'],store1['flat_lst_tasmax_33'],store1['flat_lst_tasmax_45'],store1['flat_lst_tasmax_46'],store1['flat_lst_tasmax_47'],store1['flat_lst_tasmax_48'],store1['flat_lst_tasmax_49'],store1['flat_lst_tasmax_50'],store1['flat_lst_tasmax_51'],store1['flat_lst_tasmax_52'],store1['flat_lst_tasmax_53'],store1['flat_lst_tasmax_54'],store1['flat_lst_tasmax_69'],store1['flat_lst_tasmax_73'],store1['flat_lst_tasmax_76'],store1['flat_lst_tasmax_81'],store1['flat_lst_tasmax_82'],store1['flat_lst_tasmax_83'],store1['flat_lst_tasmax_84'],store1['flat_lst_tasmax_91'],store1['flat_lst_tasmax_95'],store1['flat_lst_tasmax_99'],store1['flat_lst_tasmax_105'],store1['flat_lst_tasmax_106'],store1['flat_lst_tasmax_107'],store1['flat_lst_tasmax_115'],store1['flat_lst_tasmax_116'],store1['flat_lst_tasmax_117'],store1['flat_lst_tasmax_122'],store1['flat_lst_tasmax_123'],store1['flat_lst_tasmax_124'],store1['flat_lst_tasmax_127'],store1['flat_lst_tasmax_131']]

dflist85 = [store1['flat_lst_tasmax_1'],store1['flat_lst_tasmax_5'],store1['flat_lst_tasmax_7'],store1['flat_lst_tasmax_18'],store1['flat_lst_tasmax_19'],store1['flat_lst_tasmax_20'],store1['flat_lst_tasmax_21'],store1['flat_lst_tasmax_22'],store1['flat_lst_tasmax_29'],store1['flat_lst_tasmax_30'],store1['flat_lst_tasmax_32'],store1['flat_lst_tasmax_34'],store1['flat_lst_tasmax_55'],store1['flat_lst_tasmax_56'],store1['flat_lst_tasmax_57'],store1['flat_lst_tasmax_58'],store1['flat_lst_tasmax_59'],store1['flat_lst_tasmax_60'],store1['flat_lst_tasmax_61'],store1['flat_lst_tasmax_62'],store1['flat_lst_tasmax_63'],store1['flat_lst_tasmax_64'],store1['flat_lst_tasmax_67'],store1['flat_lst_tasmax_71'],store1['flat_lst_tasmax_75'],store1['flat_lst_tasmax_77'],store1['flat_lst_tasmax_86'],store1['flat_lst_tasmax_87'],store1['flat_lst_tasmax_88'],store1['flat_lst_tasmax_89'],store1['flat_lst_tasmax_93'],store1['flat_lst_tasmax_97'],store1['flat_lst_tasmax_101'],store1['flat_lst_tasmax_109'],store1['flat_lst_tasmax_110'],store1['flat_lst_tasmax_111'],store1['flat_lst_tasmax_118'],store1['flat_lst_tasmax_119'],store1['flat_lst_tasmax_120'],store1['flat_lst_tasmax_125'],store1['flat_lst_tasmax_129'],store1['flat_lst_tasmax_133']]

def rcp_merge(dflist):
	merge_rcp = dflist[0]
	for idx in range(len(dflist))[1:]:
		merge_rcp = pd.merge(merge_rcp, dflist[idx])
	return merge_rcp
		
rcp26 = rcp_merge(dflist26)
rcp45 = rcp_merge(dflist45)
rcp85 = rcp_merge(dflist85)

rcp26['avg'] = rcp26[[elem for elem in rcp26.columns if elem[1] == 'm']].mean(axis=1)
rcp45['avg'] = rcp45[[elem for elem in rcp45.columns if elem[1] == 'm']].mean(axis=1)
rcp85['avg'] = rcp85[[elem for elem in rcp85.columns if elem[1] == 'm']].mean(axis=1)
 
rcp26_avg = rcp26[['latitude', 'longitude', 'time', 'avg']]
rcp45_avg = rcp45[['latitude', 'longitude', 'time', 'avg']]
rcp85_avg = rcp85[['latitude', 'longitude', 'time', 'avg']]

rcp26_1 = pd.HDFStore('rcp26_1.h5')
rcp45_1 = pd.HDFStore('rcp45_1.h5')
rcp85_1 = pd.HDFStore('rcp85_1.h5')

rcp26_1['rcp26_avg'] = rcp26_avg
rcp45_1['rcp45_avg'] = rcp45_avg
rcp85_1['rcp85_avg'] = rcp85_avg
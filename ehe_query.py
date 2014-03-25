#1. Store phx/la entries for particular historical year in HDF5 file.

import numpy as np
import pandas as pd
import netCDF4
from datetime import date

f_max = netCDF4.Dataset('gridded_obs.daily.Tmax.1960.nc', 'r')

pan = pd.Panel(f_max.variables['Tmax'][:], items=f_max.variables['time'], major_axis=f_max.variables['latitude'][:], minor_axis=f_max.variables['longitude'][:])

df = pan.to_frame()

df_stack = df.stack()

df_flat=df_stack.reset_index()

df_flat.columns=['latitude', 'longitude', 'time', 'tmax']

la_latlon = [
(33.4375, -117.6875),
(33.4375, -117.5625),
(33.4375, -117.4375),
(33.4375, -117.3125),
(33.4375, -117.1875),
(33.4375, -117.0625),
(33.4375, -116.9375),
(33.4375, -116.8125),
(33.5625, -117.9375),
(33.5625, -117.8125),
(33.5625, -117.6875),
(33.5625, -117.5625),
(33.5625, -117.4375),
(33.5625, -117.3125),
(33.5625, -117.1875),
(33.5625, -117.0625),
(33.5625, -116.9375),
(33.5625, -116.8125),
(33.6875, -118.4375),
(33.6875, -118.3125),
(33.6875, -118.0625),
(33.6875, -117.9375),
(33.6875, -117.8125),
(33.6875, -117.6875),
(33.6875, -117.5625),
(33.6875, -117.4375),
(33.6875, -117.3125),
(33.6875, -117.1875),
(33.6875, -117.0625),
(33.6875, -116.9375),
(33.6875, -116.8125),
(33.8125, -118.4375),
(33.8125, -118.3125),
(33.8125, -118.1875),
(33.8125, -118.0625),
(33.8125, -117.9375),
(33.8125, -117.8125),
(33.8125, -117.6875),
(33.8125, -117.5625),
(33.8125, -117.4375),
(33.8125, -117.3125),
(33.8125, -117.1875),
(33.8125, -117.0625),
(33.8125, -116.9375),
(33.8125, -116.8125),
(33.9375, -118.4375),
(33.9375, -118.3125),
(33.9375, -118.1875),
(33.9375, -118.0625),
(33.9375, -117.9375),
(33.9375, -117.8125),
(33.9375, -117.6875),
(33.9375, -117.5625),
(33.9375, -117.4375),
(33.9375, -117.3125),
(33.9375, -117.1875),
(33.9375, -117.0625),
(33.9375, -116.9375),
(33.9375, -116.8125),
(34.0625, -119.0625),
(34.0625, -118.9375),
(34.0625, -118.8125),
(34.0625, -118.6875),
(34.0625, -118.5625),
(34.0625, -118.4375),
(34.0625, -118.3125),
(34.0625, -118.1875),
(34.0625, -118.0625),
(34.0625, -117.9375),
(34.0625, -117.8125),
(34.0625, -117.6875),
(34.0625, -117.5625),
(34.0625, -117.4375),
(34.0625, -117.3125),
(34.0625, -117.1875),
(34.0625, -117.0625),
(34.0625, -116.9375),
(34.0625, -116.8125),
(34.1875, -119.0625),
(34.1875, -118.9375),
(34.1875, -118.8125),
(34.1875, -118.6875),
(34.1875, -118.5625),
(34.1875, -118.4375),
(34.1875, -118.0625),
(34.1875, -117.8125),
(34.1875, -117.6875),
(34.1875, -117.5625),
(34.1875, -117.4375),
(34.1875, -117.3125),
(34.1875, -117.1875),
(34.1875, -117.0625),
(34.1875, -116.9375),
(34.1875, -116.8125),
(34.3125, -119.0625),
(34.3125, -118.9375),
(34.3125, -118.8125),
(34.3125, -118.6875),
(34.3125, -118.5625),
(34.3125, -118.4375),
(34.3125, -118.3125),
(34.3125, -118.1875),
(34.3125, -118.0625),
(34.3125, -117.9375),
(34.3125, -117.8125),
(34.3125, -117.6875),
(34.3125, -117.5625),
(34.3125, -117.4375),
(34.3125, -117.3125),
(34.3125, -117.1875),
(34.3125, -117.0625),
(34.3125, -116.9375),
(34.3125, -116.8125),
(34.4375, -119.0625),
(34.4375, -118.9375),
(34.4375, -118.8125),
(34.4375, -118.6875),
(34.4375, -118.5625),
(34.4375, -118.4375),
(34.4375, -118.3125),
(34.4375, -118.1875),
(34.4375, -118.0625),
(34.4375, -117.9375),
(34.4375, -117.8125),
(34.4375, -117.6875),
(34.4375, -117.5625),
(34.4375, -117.4375),
(34.4375, -117.3125),
(34.4375, -117.1875),
(34.4375, -117.0625),
(34.4375, -116.9375),
(34.4375, -116.8125),
(34.5625, -119.0625),
(34.5625, -118.9375),
(34.5625, -118.8125),
(34.5625, -118.6875),
(34.5625, -118.5625),
(34.5625, -118.4375),
(34.5625, -118.3125),
(34.5625, -118.1875),
(34.5625, -118.0625),
(34.5625, -117.9375),
(34.5625, -117.8125),
(34.5625, -117.6875),
(34.5625, -117.5625),
(34.5625, -117.4375),
(34.5625, -117.3125),
(34.5625, -117.1875),
(34.5625, -117.0625),
(34.5625, -116.9375),
(34.5625, -116.8125),
(34.6875, -119.0625),
(34.6875, -118.9375),
(34.6875, -118.8125),
(34.6875, -118.6875),
(34.6875, -118.5625),
(34.6875, -118.4375),
(34.6875, -118.3125),
(34.6875, -118.1875),
(34.6875, -118.0625),
(34.6875, -117.9375),
(34.6875, -117.8125),
(34.6875, -117.6875),
(34.6875, -117.5625),
(34.6875, -117.4375),
(34.6875, -117.3125),
(34.6875, -117.1875),
(34.6875, -117.0625),
(34.6875, -116.9375),
(34.6875, -116.8125),
(34.8125, -119.0625),
(34.8125, -118.9375),
(34.8125, -118.8125),
(34.8125, -118.6875),
(34.8125, -118.5625),
(34.8125, -118.4375),
(34.8125, -118.3125),
(34.8125, -118.1875),
(34.8125, -118.0625),
(34.8125, -117.9375),
(34.8125, -117.8125),
(34.8125, -117.6875),
(34.8125, -117.5625),
(34.8125, -117.4375),
(34.8125, -117.3125),
(34.8125, -117.1875),
(34.8125, -117.0625),
(34.8125, -116.9375),
(34.8125, -116.8125),
(34.9375, -119.0625),
(34.9375, -118.9375),
(34.9375, -118.8125),
(34.9375, -118.6875),
(34.9375, -118.5625),
(34.9375, -118.4375),
(34.9375, -118.3125),
(34.9375, -118.1875),
(34.9375, -118.0625),
(34.9375, -117.9375),
(34.9375, -117.8125),
(34.9375, -117.6875),
(34.9375, -117.5625),
(34.9375, -117.4375),
(34.9375, -117.3125),
(34.9375, -117.1875),
(34.9375, -117.0625),
(34.9375, -116.9375),
(34.9375, -116.8125)]

phx_latlon = [
(32.4375, -113.3125),
(32.4375, -113.1875),
(32.4375, -113.0625),
(32.4375, -112.9375),
(32.4375, -112.8125),
(32.4375, -112.6875),
(32.4375, -112.5625),
(32.4375, -112.4375),
(32.4375, -112.3125),
(32.4375, -112.1875),
(32.4375, -112.0625),
(32.4375, -111.9375),
(32.4375, -111.8125),
(32.4375, -111.6875),
(32.4375, -111.5625),
(32.4375, -111.4375),
(32.4375, -111.3125),
(32.4375, -111.1875),
(32.4375, -111.0625),
(32.5625, -113.3125),
(32.5625, -113.1875),
(32.5625, -113.0625),
(32.5625, -112.9375),
(32.5625, -112.8125),
(32.5625, -112.6875),
(32.5625, -112.5625),
(32.5625, -112.4375),
(32.5625, -112.3125),
(32.5625, -112.1875),
(32.5625, -112.0625),
(32.5625, -111.9375),
(32.5625, -111.8125),
(32.5625, -111.6875),
(32.5625, -111.5625),
(32.5625, -111.4375),
(32.5625, -111.3125),
(32.5625, -111.1875),
(32.5625, -111.0625),
(32.6875, -113.3125),
(32.6875, -113.1875),
(32.6875, -113.0625),
(32.6875, -112.9375),
(32.6875, -112.8125),
(32.6875, -112.6875),
(32.6875, -112.5625),
(32.6875, -112.4375),
(32.6875, -112.3125),
(32.6875, -112.1875),
(32.6875, -112.0625),
(32.6875, -111.9375),
(32.6875, -111.8125),
(32.6875, -111.6875),
(32.6875, -111.5625),
(32.6875, -111.4375),
(32.6875, -111.3125),
(32.6875, -111.1875),
(32.6875, -111.0625),
(32.8125, -113.3125),
(32.8125, -113.1875),
(32.8125, -113.0625),
(32.8125, -112.9375),
(32.8125, -112.8125),
(32.8125, -112.6875),
(32.8125, -112.5625),
(32.8125, -112.4375),
(32.8125, -112.3125),
(32.8125, -112.1875),
(32.8125, -112.0625),
(32.8125, -111.9375),
(32.8125, -111.8125),
(32.8125, -111.6875),
(32.8125, -111.5625),
(32.8125, -111.4375),
(32.8125, -111.3125),
(32.8125, -111.1875),
(32.8125, -111.0625),
(32.9375, -113.3125),
(32.9375, -113.1875),
(32.9375, -113.0625),
(32.9375, -112.9375),
(32.9375, -112.8125),
(32.9375, -112.6875),
(32.9375, -112.5625),
(32.9375, -112.4375),
(32.9375, -112.3125),
(32.9375, -112.1875),
(32.9375, -112.0625),
(32.9375, -111.9375),
(32.9375, -111.8125),
(32.9375, -111.6875),
(32.9375, -111.5625),
(32.9375, -111.4375),
(32.9375, -111.3125),
(32.9375, -111.1875),
(32.9375, -111.0625),
(33.0625, -113.3125),
(33.0625, -113.1875),
(33.0625, -113.0625),
(33.0625, -112.9375),
(33.0625, -112.8125),
(33.0625, -112.6875),
(33.0625, -112.5625),
(33.0625, -112.4375),
(33.0625, -112.3125),
(33.0625, -112.1875),
(33.0625, -112.0625),
(33.0625, -111.9375),
(33.0625, -111.8125),
(33.0625, -111.6875),
(33.0625, -111.5625),
(33.0625, -111.4375),
(33.0625, -111.3125),
(33.0625, -111.1875),
(33.0625, -111.0625),
(33.1875, -113.3125),
(33.1875, -113.1875),
(33.1875, -113.0625),
(33.1875, -112.9375),
(33.1875, -112.8125),
(33.1875, -112.6875),
(33.1875, -112.5625),
(33.1875, -112.4375),
(33.1875, -112.3125),
(33.1875, -112.1875),
(33.1875, -112.0625),
(33.1875, -111.9375),
(33.1875, -111.8125),
(33.1875, -111.6875),
(33.1875, -111.5625),
(33.1875, -111.4375),
(33.1875, -111.3125),
(33.1875, -111.1875),
(33.1875, -111.0625),
(33.3125, -113.3125),
(33.3125, -113.1875),
(33.3125, -113.0625),
(33.3125, -112.9375),
(33.3125, -112.8125),
(33.3125, -112.6875),
(33.3125, -112.5625),
(33.3125, -112.4375),
(33.3125, -112.3125),
(33.3125, -112.1875),
(33.3125, -112.0625),
(33.3125, -111.9375),
(33.3125, -111.8125),
(33.3125, -111.6875),
(33.3125, -111.5625),
(33.3125, -111.4375),
(33.3125, -111.3125),
(33.3125, -111.1875),
(33.3125, -111.0625),
(33.4375, -113.3125),
(33.4375, -113.1875),
(33.4375, -113.0625),
(33.4375, -112.9375),
(33.4375, -112.8125),
(33.4375, -112.6875),
(33.4375, -112.5625),
(33.4375, -112.4375),
(33.4375, -112.3125),
(33.4375, -112.1875),
(33.4375, -112.0625),
(33.4375, -111.9375),
(33.4375, -111.8125),
(33.4375, -111.6875),
(33.4375, -111.5625),
(33.4375, -111.4375),
(33.4375, -111.3125),
(33.4375, -111.1875),
(33.4375, -111.0625),
(33.5625, -113.3125),
(33.5625, -113.1875),
(33.5625, -113.0625),
(33.5625, -112.9375),
(33.5625, -112.8125),
(33.5625, -112.6875),
(33.5625, -112.5625),
(33.5625, -112.4375),
(33.5625, -112.3125),
(33.5625, -112.1875),
(33.5625, -112.0625),
(33.5625, -111.9375),
(33.5625, -111.8125),
(33.5625, -111.6875),
(33.5625, -111.5625),
(33.5625, -111.4375),
(33.5625, -111.3125),
(33.5625, -111.1875),
(33.5625, -111.0625),
(33.6875, -113.3125),
(33.6875, -113.1875),
(33.6875, -113.0625),
(33.6875, -112.9375),
(33.6875, -112.8125),
(33.6875, -112.6875),
(33.6875, -112.5625),
(33.6875, -112.4375),
(33.6875, -112.3125),
(33.6875, -112.1875),
(33.6875, -112.0625),
(33.6875, -111.9375),
(33.6875, -111.8125),
(33.6875, -111.6875),
(33.6875, -111.5625),
(33.6875, -111.4375),
(33.6875, -111.3125),
(33.6875, -111.1875),
(33.6875, -111.0625),
(33.8125, -113.3125),
(33.8125, -113.1875),
(33.8125, -113.0625),
(33.8125, -112.9375),
(33.8125, -112.8125),
(33.8125, -112.6875),
(33.8125, -112.5625),
(33.8125, -112.4375),
(33.8125, -112.3125),
(33.8125, -112.1875),
(33.8125, -112.0625),
(33.8125, -111.9375),
(33.8125, -111.8125),
(33.8125, -111.6875),
(33.8125, -111.5625),
(33.8125, -111.4375),
(33.8125, -111.3125),
(33.8125, -111.1875),
(33.8125, -111.0625),
(33.9375, -113.3125),
(33.9375, -113.1875),
(33.9375, -113.0625),
(33.9375, -112.9375),
(33.9375, -112.8125),
(33.9375, -112.6875),
(33.9375, -112.5625),
(33.9375, -112.4375),
(33.9375, -112.3125),
(33.9375, -112.1875),
(33.9375, -112.0625),
(33.9375, -111.9375),
(33.9375, -111.8125),
(33.9375, -111.6875),
(33.9375, -111.5625),
(33.9375, -111.4375),
(33.9375, -111.3125),
(33.9375, -111.1875),
(33.9375, -111.0625),
(34.0625, -113.3125),
(34.0625, -113.1875),
(34.0625, -113.0625),
(34.0625, -112.9375),
(34.0625, -112.8125),
(34.0625, -112.6875),
(34.0625, -112.5625),
(34.0625, -112.4375),
(34.0625, -112.3125),
(34.0625, -112.1875),
(34.0625, -112.0625),
(34.0625, -111.9375),
(34.0625, -111.8125),
(34.0625, -111.6875),
(34.0625, -111.5625),
(34.0625, -111.4375),
(34.0625, -111.3125),
(34.0625, -111.1875),
(34.0625, -111.0625)]

la_df = pd.DataFrame()
phx_df = pd.DataFrame()

for i in la_latlon:
	la_df = la_df.append(df_flat.ix[df_flat['latitude']==i[0]][df_flat['longitude']==i[1]])

for i in phx_latlon:
	phx_df = phx_df.append(df_flat.ix[df_flat['latitude']==i[0]][df_flat['longitude']==i[1]])

la_hist = pd.HDFStore('la_hist.h5')
phx_hist = pd.HDFStore('phx_hist.h5')

la_hist['la_1960'] = la_df
phx_hist['phx_1960'] = phx_df

#2. Append all entries to single df.

la_record = pd.DataFrame()
phx_record = pd.DataFrame()

record = range(1960, 1991)

for i in record:
	la_year = 'la_' + '%s' % (i)
	la_record = la_record.append(la_hist[la_year])

la_record = la_record.reset_index()

for i in record:
	phx_year = 'phx_' + '%s' % (i)
	phx_record = phx_record.append(phx_hist[phx_year])

phx_record = phx_record.reset_index()

#3. Convert time to datetime.

la_record['date'] = [date.fromordinal(int(711858 + i)) for i in la_record.time]
phx_record['date'] = [date.fromordinal(int(711858 + i)) for i in phx_record.time]

#4. Convert longitude format.

la_record['longitude'] = la_record['longitude'] + 360
phx_record['longitude'] = phx_record['longitude'] + 360

#5. Select summer months (June through August).

la_summer_idx = []
phx_summer_idx = []

for i, row in la_record.iterrows():
	if 6 <= row['date'].month <= 8:
		la_summer_idx.append(i)

for i, row in phx_record.iterrows():
	if 6 <= row['date'].month <= 8:
		phx_summer_idx.append(i)
		
la_summer = la_record.ix[la_summer_idx]
phx_summer = phx_record.ix[phx_summer_idx]

#6. Calculate 97.5th and 81st historical percentiles.

la_T1 = la_summer.groupby(['latitude', 'longitude']).quantile(0.975)
la_T2 = la_summer.groupby(['latitude', 'longitude']).quantile(0.81)

del la_T1['index']
del la_T1['time']
del la_T1['latitude']
del la_T1['longitude']
la_T1 = la_T1.reset_index()

del la_T2['index']
del la_T2['time']
del la_T2['latitude']
del la_T2['longitude']
la_T2 = la_T2.reset_index()

phx_T1 = phx_summer.groupby(['latitude', 'longitude']).quantile(0.975)
phx_T2 = phx_summer.groupby(['latitude', 'longitude']).quantile(0.81)

del phx_T1['index']
del phx_T1['time']
del phx_T1['latitude']
del phx_T1['longitude']
phx_T1 = phx_T1.reset_index()

del phx_T2['index']
del phx_T2['time']
del phx_T2['latitude']
del phx_T2['longitude']
phx_T2 = phx_T2.reset_index()

#7. Store percentiles

la_T1.to_csv('la_T1.csv')
la_T2.to_csv('la_T2.csv')

phx_T1.to_csv('phx_T1.csv')
phx_T2.to_csv('phx_T2.csv')

#8. Join percentile df with projection df.

import numpy as np
import pandas as pd
import netCDF4
from datetime import date

la_T1 = pd.read_csv('la_T1.csv')
la_T2 = pd.read_csv('la_T2.csv')
phx_T1 = pd.read_csv('phx_T1.csv')
phx_T2 = pd.read_csv('phx_T2.csv')

la_T1['latlon'] = la_T1[['latitude', 'longitude']].apply(tuple, axis=1)
la_T2['latlon'] = la_T2[['latitude', 'longitude']].apply(tuple, axis=1)
del la_T1['latitude']
del la_T1['longitude']
del la_T1['Unnamed: 0']
del la_T2['latitude']
del la_T2['longitude']
del la_T2['Unnamed: 0']
la_T1['t1'] = la_T1['tmax']
del la_T1['tmax']
la_T2['t2'] = la_T2['tmax']
del la_T2['tmax']

phx_T1['latlon'] = phx_T1[['latitude', 'longitude']].apply(tuple, axis=1)
phx_T2['latlon'] = phx_T2[['latitude', 'longitude']].apply(tuple, axis=1)

#9. Prepare projections

store2 = pd.HDFStore('store2.h5')

gfdl_esm2g_26 = store2['flat_lst_tasmax_68']
gfdl_esm2g_26['tmax'] = gfdl_esm2g_26['tmax68']
del gfdl_esm2g_26['tmax68']

gfdl_esm2g_26['latlon'] = gfdl_esm2g_26[['latitude', 'longitude']].apply(tuple, axis=1)

gfdl_esm2g_26 = pd.merge(gfdl_esm2g_26, la_T1, on='latlon')
gfdl_esm2g_26 = pd.merge(gfdl_esm2g_26, la_T2, on='latlon')


gfdl_esm2g_45 = store2['flat_lst_tasmax_69']
gfdl_esm2g_45['tmax'] = gfdl_esm2g_45['tmax69']
del gfdl_esm2g_45['tmax69']

gfdl_esm2g_45['latlon'] = gfdl_esm2g_45[['latitude', 'longitude']].apply(tuple, axis=1)

gfdl_esm2g_45 = pd.merge(gfdl_esm2g_45, la_T1, on='latlon')
gfdl_esm2g_45 = pd.merge(gfdl_esm2g_45, la_T2, on='latlon')

gfdl_esm2g_60 = store2['flat_lst_tasmax_70']
gfdl_esm2g_60['tmax'] = gfdl_esm2g_60['tmax70']
del gfdl_esm2g_60['tmax70']

gfdl_esm2g_60['latlon'] = gfdl_esm2g_60[['latitude', 'longitude']].apply(tuple, axis=1)

gfdl_esm2g_60 = pd.merge(gfdl_esm2g_60, la_T1, on='latlon')
gfdl_esm2g_60 = pd.merge(gfdl_esm2g_60, la_T2, on='latlon')

gfdl_esm2g_85 = store2['flat_lst_tasmax_71']
gfdl_esm2g_85['tmax'] = gfdl_esm2g_85['tmax71']
del gfdl_esm2g_85['tmax71']

gfdl_esm2g_85['latlon'] = gfdl_esm2g_85[['latitude', 'longitude']].apply(tuple, axis=1)

gfdl_esm2g_85 = pd.merge(gfdl_esm2g_85, la_T1, on='latlon')
gfdl_esm2g_85 = pd.merge(gfdl_esm2g_85, la_T2, on='latlon')

#10. Query projections for extreme heat events

crit = []

def sel(rcp):
	for i in range(len(rcp.index)):
		if rcp['tmax'].ix[i] > rcp['t1'].ix[i]:
			if rcp['tmax'].ix[i+1] > rcp['t1'].ix[i+1]:
				if rcp['tmax'].ix[i+2] > rcp['t1'].ix[i+2]:
					crit.extend([rcp.index[i]])
					cumsum = 0.0
					ct = 0
					for index, rows in rcp[i:].iterrows():				
						cumsum += rows['tmax']
						ct = ct + 1
						mov_avg = cumsum/float(ct)
						if mov_avg > rcp['t1'].ix[i]:
							if rows['tmax'] > rows['t2']:
								if ct>1:
									crit.extend([index])
									#print ct
									continue
								else:
									continue
							else:
								i = index
								break
						else:
							i = index
							break
				else:
					continue
			else:
				continue
		else:
			continue
			

sel(gfdl_esm2g_26)

EHE_gfdl_esm2g_26 = gfdl_esm2g_26.ix[sorted(set(crit))]
EHE_gfdl_esm2g_26.to_csv('EHE_gfdl_esm2g_26.csv')

sel(gfdl_esm2g_45)

EHE_gfdl_esm2g_45 = gfdl_esm2g_45.ix[sorted(set(crit))]
EHE_gfdl_esm2g_45.to_csv('EHE_gfdl_esm2g_45.csv')

sel(gfdl_esm2g_60)

EHE_gfdl_esm2g_60 = gfdl_esm2g_60.ix[sorted(set(crit))]
EHE_gfdl_esm2g_60.to_csv('EHE_gfdl_esm2g_60_2.csv')

sel(gfdl_esm2g_85)

EHE_gfdl_esm2g_85 = gfdl_esm2g_85.ix[sorted(set(crit))]
EHE_gfdl_esm2g_85.to_csv('EHE_gfdl_esm2g_85.csv')
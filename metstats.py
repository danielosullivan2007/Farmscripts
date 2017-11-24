# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:36:55 2017

@author: eardo
"""

from directories import farmdirs
import pandas as pd
import datetime

met=pd.read_pickle(farmdirs['pickels'] + 'met.p')
INPs= pd.read_pickle(farmdirs['pickels']+'INPs.p')
wind =pd.read_pickle(farmdirs['pickels']+'wind.p')
dt = INPs.loc[:,'start_datetime':'end_datetime']
dt['timedelta']=dt.end_datetime - dt.start_datetime
dt.drop('end_datetime', inplace =True, axis =1)
dt = dt.drop_duplicates(subset = 'start_datetime')
dt['end']=dt.start_datetime+dt.timedelta
dt.drop('timedelta', axis =1, inplace =True)
dt.rename(columns ={'start_datetime':'start'}, inplace =True)
dt.reset_index(inplace=True, drop=True)


# =============================================================================
# rain_cumul = met['Rainfall Total since 0900']
# met['hourly_rain'] = rain_cumul.diff()
# 
# for i in range(len(met)):
#     if met.index[i].time() == datetime.time(10, 0):
#         met['hourly_rain'][i] = 0
# 
# sun_cumul = met['Radiation Total since 0900']
# met['hourly_radiation'] = sun_cumul.diff()
# 
# for i in range(len(met)):
#     if met.index[i].time() == datetime.time(10, 0):
#         met['hourly_radiation'][i] = 0
# 
# for i in range(len(met['hourly_radiation'])):
#     if met['hourly_radiation'][i]<0:
#         met['hourly_radiation'][i]=0
#     
# cols = list(met)
# met_sampling =pd.DataFrame(columns=cols)
# for i in range(len(dt)):
#     mask = (met.index > dt['start'][i]) & (met.index <= dt['end'][i]) 
#     if met.loc[mask].empty:
#         continue
#     else: 
#         met_sampling = met_sampling.append(met.loc[mask])
#         
# met_sampling.drop(cols[0:5],axis =1, inplace =True)
# =============================================================================

wind_cols=list(wind)
wind_sampling =pd.DataFrame(columns=wind_cols)
for i in range(len(dt)):
    mask = (wind.index > dt['start'][i]) & (wind.index <= dt['end'][i]) 
    if wind.loc[mask].empty:
        continue
    else: 
        wind_sampling = wind_sampling.append(wind.loc[mask])


stats=wind_sampling.describe()




